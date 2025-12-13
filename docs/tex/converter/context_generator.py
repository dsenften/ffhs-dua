"""
ConTeXt-Generator für Dokumentationssystem
==========================================

Dieses Modul generiert ConTeXt-Code aus geparsten Markdown-Dokumenten.
"""

import logging
from pathlib import Path

from .markdown_parser import MarkdownDocument, MarkdownElement


class ConTeXtGenerator:
    """
    Generator für ConTeXt-Code aus Markdown-Dokumenten.

    Konvertiert geparste Markdown-Elemente in entsprechende
    ConTeXt-Befehle und -Strukturen.
    """

    def __init__(self, config):
        """
        Initialisiert den Generator.

        Args:
            config: Build-Konfiguration
        """
        self.config = config
        self.logger = logging.getLogger(__name__)

        # ConTeXt-Befehle für verschiedene Elemente
        self.element_handlers = {
            "heading": self._generate_heading,
            "paragraph": self._generate_paragraph,
            "code_block": self._generate_code_block,
            "list": self._generate_list,
            "numbered_list": self._generate_numbered_list,
            "table": self._generate_table,
            "math_block": self._generate_math_block,
            "image": self._generate_image,
        }

    def generate_file(
        self, document: MarkdownDocument, force_rebuild: bool = False
    ) -> Path | None:
        """
        Generiert eine ConTeXt-Datei aus einem Markdown-Dokument.

        Args:
            document: Gepartes Markdown-Dokument
            force_rebuild: Datei auch bei vorhandener Ausgabe neu erstellen

        Returns:
            Pfad zur erstellten ConTeXt-Datei oder None bei Fehler
        """
        try:
            # Ausgabepfad bestimmen
            output_path = self._get_output_path(document)

            # Prüfen ob Rebuild nötig
            if not force_rebuild and output_path.exists():
                if output_path.stat().st_mtime > document.source_path.stat().st_mtime:
                    self.logger.info(f"ConTeXt-Datei ist aktuell: {output_path}")
                    return output_path

            self.logger.info(f"Generiere ConTeXt-Datei: {output_path}")

            # ConTeXt-Code generieren
            context_code = self._generate_document(document)

            # Datei schreiben
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(context_code, encoding="utf-8")

            self.logger.info(f"ConTeXt-Datei erstellt: {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(f"Fehler bei ConTeXt-Generierung: {e}")
            return None

    def generate_main_document(self, context_files: list[Path]) -> Path | None:
        """
        Generiert das Haupt-ConTeXt-Dokument aus mehreren Einzeldateien.

        Args:
            context_files: Liste der ConTeXt-Dateien

        Returns:
            Pfad zum Hauptdokument oder None bei Fehler
        """
        try:
            self.logger.info("Generiere Haupt-ConTeXt-Dokument")

            # Template laden
            template_path = Path(self.config.template_dir) / "main.tex"
            template_content = template_path.read_text(encoding="utf-8")

            # Content-Includes generieren
            includes = []
            for ctx_file in sorted(context_files):
                # Relativer Pfad zum Template-Verzeichnis
                rel_path = ctx_file.relative_to(
                    Path(self.config.output_dir) / "context"
                )
                includes.append(f"\\input {{{rel_path.as_posix()}}}")

            content_block = "\n".join(includes)

            # Template-Platzhalter ersetzen
            final_content = template_content.replace(
                "% CONTENT_PLACEHOLDER", content_block
            )

            # Hauptdokument schreiben
            main_path = Path(self.config.output_dir) / "context" / "main.tex"
            main_path.parent.mkdir(parents=True, exist_ok=True)
            main_path.write_text(final_content, encoding="utf-8")

            self.logger.info(f"Hauptdokument erstellt: {main_path}")
            return main_path

        except Exception as e:
            self.logger.error(f"Fehler bei Hauptdokument-Generierung: {e}")
            return None

    def _get_output_path(self, document: MarkdownDocument) -> Path:
        """Bestimmt den Ausgabepfad für eine ConTeXt-Datei."""
        # Relativer Pfad zur Projektroot
        rel_path = document.source_path.relative_to(Path.cwd())

        # .md durch .tex ersetzen
        tex_name = rel_path.with_suffix(".tex").name

        # In output/context/ Verzeichnis
        output_path = Path(self.config.output_dir) / "context" / tex_name
        return output_path

    def _generate_document(self, document: MarkdownDocument) -> str:
        """Generiert den kompletten ConTeXt-Code für ein Dokument."""
        lines = []

        # Dokument-Header
        lines.append(f"% Generiert aus: {document.source_path}")
        lines.append(f"% Titel: {document.title}")
        lines.append("")

        # Kapitel-Überschrift (falls nicht bereits vorhanden)
        if not any(
            elem.type == "heading" and elem.level == 1 for elem in document.elements
        ):
            lines.append(f"\\chapter{{{document.title}}}")
            lines.append("")

        # Alle Elemente verarbeiten
        for element in document.elements:
            context_code = self._generate_element(element)
            if context_code:
                lines.append(context_code)
                lines.append("")

        return "\n".join(lines)

    def _generate_element(self, element: MarkdownElement) -> str:
        """Generiert ConTeXt-Code für ein einzelnes Element."""
        handler = self.element_handlers.get(element.type)
        if handler:
            return handler(element)
        else:
            self.logger.warning(f"Unbekannter Element-Typ: {element.type}")
            return f"% Unbekanntes Element: {element.type}\n{element.content}"

    def _generate_heading(self, element: MarkdownElement) -> str:
        """Generiert ConTeXt-Code für Überschriften."""
        level_commands = {
            1: "chapter",
            2: "section",
            3: "subsection",
            4: "subsubsection",
            5: "subsubsubsection",
            6: "subsubsubsubsection",
        }

        command = level_commands.get(element.level, "subsubsubsubsection")
        return f"\\{command}{{{element.content}}}"

    def _generate_paragraph(self, element: MarkdownElement) -> str:
        """Generiert ConTeXt-Code für Absätze."""
        return element.content

    def _generate_code_block(self, element: MarkdownElement) -> str:
        """Generiert ConTeXt-Code für Code-Blöcke."""
        language = element.attributes.get("language", "text")

        # Sprach-spezifische Umgebungen
        if language in ["python", "java", "shell", "sql", "xml", "json", "yaml"]:
            return f"\\start{language}\n{element.content}\n\\stop{language}"
        else:
            return f"\\starttyping\n{element.content}\n\\stoptyping"

    def _generate_list(self, element: MarkdownElement) -> str:
        """Generiert ConTeXt-Code für ungeordnete Listen."""
        items = element.content.split("\n")
        lines = ["\\startitemize"]
        for item in items:
            if item.strip():
                lines.append(f"\\item {item.strip()}")
        lines.append("\\stopitemize")
        return "\n".join(lines)

    def _generate_numbered_list(self, element: MarkdownElement) -> str:
        """Generiert ConTeXt-Code für nummerierte Listen."""
        items = element.content.split("\n")
        lines = ["\\startenumerate"]
        for item in items:
            if item.strip():
                lines.append(f"\\item {item.strip()}")
        lines.append("\\stopenumerate")
        return "\n".join(lines)

    def _generate_table(self, element: MarkdownElement) -> str:
        """Generiert ConTeXt-Code für Tabellen."""
        # Vereinfachte Tabellen-Generierung
        lines = element.content.split("\n")
        table_lines = ["\\bTABLE"]

        for i, line in enumerate(lines):
            if "|" in line:
                cells = [cell.strip() for cell in line.split("|")[1:-1]]
                if i == 0:  # Header
                    table_lines.append("\\bTR")
                    for cell in cells:
                        table_lines.append(f"\\bTH {cell} \\eTH")
                    table_lines.append("\\eTR")
                elif not all(c in "-|: " for c in line):  # Nicht die Separator-Zeile
                    table_lines.append("\\bTR")
                    for cell in cells:
                        table_lines.append(f"\\bTD {cell} \\eTD")
                    table_lines.append("\\eTR")

        table_lines.append("\\eTABLE")
        return "\n".join(table_lines)

    def _generate_math_block(self, element: MarkdownElement) -> str:
        """Generiert ConTeXt-Code für mathematische Blöcke."""
        return f"\\startformula\n{element.content}\n\\stopformula"

    def _generate_image(self, element: MarkdownElement) -> str:
        """Generiert ConTeXt-Code für Bilder."""
        src = element.attributes.get("src", "")
        alt = element.attributes.get("alt", "")

        return f"\\placefigure[here][fig:{alt}]{{{alt}}}{{\\externalfigure[{src}][width=0.8\\textwidth]}}"
