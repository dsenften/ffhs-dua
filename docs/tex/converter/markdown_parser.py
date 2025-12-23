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
        Initialize the MarkdownParser with the given build configuration, set up a module logger, and prepare regex patterns used to identify Markdown elements.
        
        Parameters:
            config: Build configuration object used to customize parser behavior (kept as provided).
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
        Parse a Markdown file into a MarkdownDocument.
        
        Parameters:
            file_path (Path): Path to the Markdown file to read and parse.
        
        Returns:
            MarkdownDocument: Parsed document with title, metadata, elements, and source_path set, or `None` if an error occurred while reading or parsing.
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
        """
        Extracts the document title from the content, preferring the first H1 header and falling back to the file name.
        
        Parameters:
            content (str): Full markdown content to search for an H1 header.
            file_path (Path): Source file path used to derive a fallback title when no H1 is found.
        
        Returns:
            title (str): The H1 header text if present; otherwise the file name (underscores/dashes replaced with spaces and title-cased).
        """
        # Erste H1-Überschrift suchen
        match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if match:
            return match.group(1).strip()

        # Fallback: Dateiname ohne Erweiterung
        return file_path.stem.replace("_", " ").replace("-", " ").title()

    def _extract_metadata(self, content: str) -> tuple[str, dict[str, Any]]:
        """
        Extract YAML front matter from the given Markdown content and return the content with the front matter removed alongside the parsed metadata.
        
        Parameters:
            content (str): Markdown text that may begin with YAML front matter delimited by ---.
        
        Returns:
            tuple[str, dict[str, Any]]: A tuple where the first element is the content with the YAML front matter removed (or the original content if none found), and the second element is a metadata dictionary parsed from the front matter. Only lines containing a ':' are parsed into key/value pairs; keys and values are stripped of surrounding whitespace.
        """
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
        """
        Parse the Markdown content into a list of MarkdownElement objects.
        
        Scans the provided Markdown text, identifies element types (headings, code blocks, lists, numbered lists, tables, math blocks, and paragraphs), and returns the parsed elements in document order.
        
        Parameters:
            content (str): Full Markdown document content to parse.
        
        Returns:
            list[MarkdownElement]: Parsed Markdown elements in the order they appear in the content.
        """
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
        """
        Parse a Markdown heading line and produce a corresponding MarkdownElement.
        
        Parses a line that begins with one or more '#' characters, extracts the heading level (number of '#' characters) and the trimmed heading text.
        
        Parameters:
            line (str): A single line of Markdown to inspect for a heading.
        
        Returns:
            MarkdownElement | None: A MarkdownElement of type "heading" with `content` set to the heading text and `level` set to the heading level, or `None` if the line is not a heading.
        """
        match = self.patterns["heading"].match(line)
        if match:
            level = len(match.group(1))
            content = match.group(2).strip()
            return MarkdownElement(type="heading", content=content, level=level)
        return None

    def _parse_code_block(self, lines: list[str]) -> tuple[MarkdownElement | None, int]:
        """
        Parse a fenced code block starting at the first line of `lines`.
        
        Parameters:
            lines (list[str]): Consecutive document lines with the first line expected to begin with a triple backtick fence (```).
        
        Returns:
            tuple[MarkdownElement | None, int]: A tuple where the first element is a `MarkdownElement` of type `code_block` (with `content` set to the block's source and `attributes['language']` set to the fence language) or `None` if no valid closing fence was found; the second element is the number of lines consumed from `lines`.
        """
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
        """
        Parse an unordered (bulleted) list starting at the beginning of the provided lines.
        
        Parameters:
            lines (list[str]): Lines of the document with the current position at index 0.
        
        Returns:
            tuple[MarkdownElement | None, int]: A tuple where the first element is a MarkdownElement of type "list"
            representing the parsed unordered list (or `None` if no list was found), and the second element is the
            number of input lines consumed while parsing.
        """
        # Implementation folgt...
        return None, 1

    def _parse_numbered_list(
        self, lines: list[str]
    ) -> tuple[MarkdownElement | None, int]:
        """
        Parse an ordered (numbered) Markdown list starting at the first line.
        
        Parameters:
            lines (list[str]): Consecutive lines of the document starting at the current parsing position.
        
        Returns:
            tuple[MarkdownElement | None, int]: A tuple where the first element is a `MarkdownElement` of type "numbered_list" containing the list content and attributes when a numbered list is parsed, or `None` if no numbered list is present. The second element is the number of input lines consumed while attempting to parse the list (at least 1).
        """
        # Implementation folgt...
        return None, 1

    def _parse_table(self, lines: list[str]) -> tuple[MarkdownElement | None, int]:
        """
        Parse a Markdown table starting at the first line of `lines`.
        
        If a valid Markdown table (header row and separator row with pipes or pipe-less aligned columns) is present, returns a MarkdownElement of type "table" with the table content and attributes describing columns, and the number of lines consumed. If no table is found at the current position, returns (None, 1).
        
        Returns:
            tuple[MarkdownElement | None, int]: A tuple containing the parsed table element or `None` and the number of input lines consumed.
        """
        # Implementation folgt...
        return None, 1

    def _parse_math_block(self, lines: list[str]) -> tuple[MarkdownElement | None, int]:
        """
        Parse a block-level math element starting at the first line of `lines`.
        
        Attempts to consume a multi-line math block and produce a `MarkdownElement` of type "math" whose content is the math source (without surrounding delimiters). If no math block begins at the first line, returns `None` and `1` to indicate that one line was consumed.
        
        Parameters:
            lines (list[str]): Lines of text beginning at the candidate math block.
        
        Returns:
            tuple[MarkdownElement | None, int]: A tuple with the parsed `MarkdownElement` (or `None` if no math block was found) and the number of lines consumed from `lines`.
        """
        # Implementation folgt...
        return None, 1

    def _parse_paragraph(self, lines: list[str]) -> tuple[MarkdownElement | None, int]:
        """
        Parse a paragraph from the beginning of a list of Markdown lines.
        
        Parameters:
            lines (list[str]): Lines to parse starting at the current position.
        
        Returns:
            tuple[MarkdownElement | None, int]: A tuple where the first item is a `MarkdownElement` of type "paragraph" with inline elements already processed when a paragraph is found, or `None` if no paragraph starts at the first line; the second item is the number of lines consumed (or `1` when no paragraph is found).
        """
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
        """
        Convert inline Markdown constructs (links, inline code, images, inline math) into ConTeXt macro syntax.
        
        Parameters:
            content (str): Markdown text containing inline elements to be transformed.
        
        Returns:
            str: The input text with links converted to `\goto{text}[url(URL)]`, inline code to `\type{code}`, images to `\placefigure[]{caption}{\externalfigure[URL]}`, and inline math to `\mathematics{expr}`.
        """
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