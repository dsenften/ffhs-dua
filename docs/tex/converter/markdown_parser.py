"""
Markdown-Parser für ConTeXt-Konvertierung
=========================================

Dieses Modul parst Markdown-Dateien und extrahiert die Struktur
für die Konvertierung zu ConTeXt.
"""

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class MarkdownElement:
    """Basis-Klasse für Markdown-Elemente."""

    type: str
    content: str
    level: int = 0
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass
class MarkdownDocument:
    """Repräsentiert ein gepartes Markdown-Dokument."""

    title: str
    elements: list[MarkdownElement] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    source_path: Path | None = None


class MarkdownParser:
    """
    Parser für Markdown-Dateien mit Fokus auf ConTeXt-Konvertierung.

    Unterstützt:
    - Überschriften (# ## ### ####)
    - Code-Blöcke (``` und ~~~)
    - Inline-Code (`code`)
    - Listen (- * +)
    - Nummerierte Listen (1. 2. 3.)
    - Links [text](url)
    - Bilder ![alt](src)
    - Tabellen
    - Mathematische Formeln ($..$ und $$..$$)
    - Metadata (YAML Front Matter)
    """

    def __init__(self, config):
        """
        Initialisiert den Parser.

        Args:
            config: Build-Konfiguration
        """
        self.config = config
        self.logger = logging.getLogger(__name__)

        # Regex-Pattern für verschiedene Markdown-Elemente
        self.patterns = {
            "heading": re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE),
            "code_block": re.compile(
                r"^```(\w+)?\n(.*?)^```$", re.MULTILINE | re.DOTALL
            ),
            "inline_code": re.compile(r"`([^`]+)`"),
            "link": re.compile(r"\[([^\]]+)\]\(([^)]+)\)"),
            "image": re.compile(r"!\[([^\]]*)\]\(([^)]+)\)"),
            "list_item": re.compile(r"^[\s]*[-*+]\s+(.+)$", re.MULTILINE),
            "numbered_list": re.compile(r"^[\s]*\d+\.\s+(.+)$", re.MULTILINE),
            "table_row": re.compile(r"^\|(.+)\|$", re.MULTILINE),
            "math_inline": re.compile(r"\$([^$]+)\$"),
            "math_block": re.compile(r"^\$\$\n(.*?)\n\$\$$", re.MULTILINE | re.DOTALL),
            "yaml_frontmatter": re.compile(r"^---\n(.*?)\n---\n", re.DOTALL),
        }

    def parse_file(self, file_path: Path) -> MarkdownDocument | None:
        """
        Parst eine Markdown-Datei.

        Args:
            file_path: Pfad zur Markdown-Datei

        Returns:
            MarkdownDocument oder None bei Fehler
        """
        try:
            self.logger.info(f"Parse Markdown-Datei: {file_path}")

            # Datei lesen
            content = file_path.read_text(encoding="utf-8")

            # Dokument erstellen
            document = MarkdownDocument(
                title=self._extract_title(content, file_path), source_path=file_path
            )

            # Metadata extrahieren
            content, metadata = self._extract_metadata(content)
            document.metadata = metadata

            # Elemente parsen
            document.elements = self._parse_elements(content)

            self.logger.info(f"Erfolgreich geparst: {len(document.elements)} Elemente")
            return document

        except Exception as e:
            self.logger.error(f"Fehler beim Parsen von {file_path}: {e}")
            return None

    def _extract_title(self, content: str, file_path: Path) -> str:
        """Extrahiert den Titel aus dem Dokument."""
        # Erste H1-Überschrift suchen
        match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if match:
            return match.group(1).strip()

        # Fallback: Dateiname ohne Erweiterung
        return file_path.stem.replace("_", " ").replace("-", " ").title()

    def _extract_metadata(self, content: str) -> tuple[str, dict[str, Any]]:
        """Extrahiert YAML Front Matter."""
        metadata = {}

        match = self.patterns["yaml_frontmatter"].match(content)
        if match:
            yaml_content = match.group(1)
            # Einfaches YAML-Parsing (für komplexere Fälle PyYAML verwenden)
            for line in yaml_content.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    metadata[key.strip()] = value.strip()

            # YAML Front Matter aus Content entfernen
            content = content[match.end() :]

        return content, metadata

    def _parse_elements(self, content: str) -> list[MarkdownElement]:
        """Parst alle Elemente aus dem Content."""
        elements = []
        lines = content.split("\n")
        i = 0

        while i < len(lines):
            line = lines[i].rstrip()

            # Leerzeilen überspringen
            if not line:
                i += 1
                continue

            # Überschriften
            if line.startswith("#"):
                element = self._parse_heading(line)
                if element:
                    elements.append(element)
                i += 1
                continue

            # Code-Blöcke
            if line.startswith("```"):
                element, consumed_lines = self._parse_code_block(lines[i:])
                if element:
                    elements.append(element)
                i += consumed_lines
                continue

            # Listen
            if re.match(r"^[\s]*[-*+]\s+", line):
                element, consumed_lines = self._parse_list(lines[i:])
                if element:
                    elements.append(element)
                i += consumed_lines
                continue

            # Nummerierte Listen
            if re.match(r"^[\s]*\d+\.\s+", line):
                element, consumed_lines = self._parse_numbered_list(lines[i:])
                if element:
                    elements.append(element)
                i += consumed_lines
                continue

            # Tabellen
            if line.startswith("|"):
                element, consumed_lines = self._parse_table(lines[i:])
                if element:
                    elements.append(element)
                i += consumed_lines
                continue

            # Mathematische Blöcke
            if line.startswith("$$"):
                element, consumed_lines = self._parse_math_block(lines[i:])
                if element:
                    elements.append(element)
                i += consumed_lines
                continue

            # Normaler Absatz
            element, consumed_lines = self._parse_paragraph(lines[i:])
            if element:
                elements.append(element)
            i += consumed_lines

        return elements

    def _parse_heading(self, line: str) -> MarkdownElement | None:
        """Parst eine Überschrift."""
        match = self.patterns["heading"].match(line)
        if match:
            level = len(match.group(1))
            content = match.group(2).strip()
            return MarkdownElement(type="heading", content=content, level=level)
        return None

    def _parse_code_block(self, lines: list[str]) -> tuple[MarkdownElement | None, int]:
        """Parst einen Code-Block."""
        if not lines[0].startswith("```"):
            return None, 1

        # Sprache extrahieren
        first_line = lines[0][3:].strip()
        language = first_line if first_line else "text"

        # Code-Inhalt sammeln
        code_lines = []
        i = 1
        while i < len(lines):
            if lines[i].startswith("```"):
                break
            code_lines.append(lines[i])
            i += 1

        if i >= len(lines):
            # Kein schließendes ``` gefunden
            return None, 1

        element = MarkdownElement(
            type="code_block",
            content="\n".join(code_lines),
            attributes={"language": language},
        )

        return element, i + 1

    def _parse_list(self, lines: list[str]) -> tuple[MarkdownElement | None, int]:
        """Parst eine ungeordnete Liste."""
        # Implementation folgt...
        return None, 1

    def _parse_numbered_list(
        self, lines: list[str]
    ) -> tuple[MarkdownElement | None, int]:
        """Parst eine nummerierte Liste."""
        # Implementation folgt...
        return None, 1

    def _parse_table(self, lines: list[str]) -> tuple[MarkdownElement | None, int]:
        """Parst eine Tabelle."""
        # Implementation folgt...
        return None, 1

    def _parse_math_block(self, lines: list[str]) -> tuple[MarkdownElement | None, int]:
        """Parst einen mathematischen Block."""
        # Implementation folgt...
        return None, 1

    def _parse_paragraph(self, lines: list[str]) -> tuple[MarkdownElement | None, int]:
        """Parst einen normalen Absatz."""
        paragraph_lines = []
        i = 0

        while i < len(lines):
            line = lines[i].rstrip()

            # Absatz endet bei Leerzeile oder speziellem Element
            if (
                not line
                or line.startswith("#")
                or line.startswith("```")
                or line.startswith("|")
                or re.match(r"^[\s]*[-*+]\s+", line)
                or re.match(r"^[\s]*\d+\.\s+", line)
            ):
                break

            paragraph_lines.append(line)
            i += 1

        if paragraph_lines:
            content = " ".join(paragraph_lines)
            # Inline-Elemente verarbeiten
            content = self._process_inline_elements(content)

            element = MarkdownElement(type="paragraph", content=content)
            return element, i

        return None, 1

    def _process_inline_elements(self, content: str) -> str:
        """Verarbeitet Inline-Elemente wie Links, Code, etc."""
        # Links verarbeiten
        content = self.patterns["link"].sub(r"\\goto{\1}[url(\2)]", content)

        # Inline-Code verarbeiten
        content = self.patterns["inline_code"].sub(r"\\type{\1}", content)

        # Bilder verarbeiten
        content = self.patterns["image"].sub(
            r"\\placefigure[]{\1}{\\externalfigure[\2]}", content
        )

        # Inline-Mathematik verarbeiten
        content = self.patterns["math_inline"].sub(r"\\mathematics{\1}", content)

        return content
