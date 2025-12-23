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
        Create a ConTeXtGenerator configured with the given build settings.
        
        Initializes generator state including the provided configuration, a module logger, and the mapping of Markdown element types to their ConTeXt handler methods.
        
        Parameters:
            config: Build/configuration object providing runtime settings used by the generator (for example: template and output directories).
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
        Generate a ConTeXt file from a parsed Markdown document.
        
        Parameters:
            document (MarkdownDocument): Parsed Markdown document to convert.
            force_rebuild (bool): If true, always regenerate the output even if an up-to-date file exists.
        
        Returns:
            Path | None: Path to the created ConTeXt file, or `None` if generation failed.
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
        Builds the main ConTeXt document by injecting \input includes for the given context files into the main template.
        
        Parameters:
            context_files (list[Path]): Ordered list of ConTeXt file paths to include; each file's path is made relative to the configured output_dir/context directory when generating the include statements.
        
        Returns:
            Path | None: Path to the written main.tex inside `output_dir/context` if successful, `None` if an error occurred.
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
        """
        Compute the output file path for a MarkdownDocument's ConTeXt (.tex) file.
        
        The path is derived from the document's source path relative to the project root, with the `.md` suffix replaced by `.tex`, and placed under the configured output directory's `context` subdirectory.
        
        Returns:
            Path: Path to the resulting `.tex` output file under `config.output_dir/context` corresponding to the given document.
        """
        # Relativer Pfad zur Projektroot
        rel_path = document.source_path.relative_to(Path.cwd())

        # .md durch .tex ersetzen
        tex_name = rel_path.with_suffix(".tex").name

        # In output/context/ Verzeichnis
        output_path = Path(self.config.output_dir) / "context" / tex_name
        return output_path

    def _generate_document(self, document: MarkdownDocument) -> str:
        """
        Builds the full ConTeXt source for the given MarkdownDocument.
        
        Parameters:
            document (MarkdownDocument): Parsed markdown document with attributes `source_path`, `title`, and a list of `elements` to render.
        
        Returns:
            context_source (str): Complete ConTeXt document as a single string. The result includes a header comment with source path and title, inserts a top-level \chapter{title} if the document has no level-1 heading, and contains the rendered ConTeXt blocks for each document element.
        """
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
        """
        Render a single parsed Markdown element into ConTeXt source.
        
        Looks up a handler by the element's type and returns the handler's ConTeXt output. If no handler exists, a warning is logged and a TeX comment indicating the unknown element type followed by the element's original content is returned.
        
        Parameters:
            element (MarkdownElement): The parsed Markdown element to render.
        
        Returns:
            str: ConTeXt source for the element; if the element type is unknown, a commented note with the element type and the element's content.
        """
        handler = self.element_handlers.get(element.type)
        if handler:
            return handler(element)
        else:
            self.logger.warning(f"Unbekannter Element-Typ: {element.type}")
            return f"% Unbekanntes Element: {element.type}\n{element.content}"

    def _generate_heading(self, element: MarkdownElement) -> str:
        """
        Map a Markdown heading element to the corresponding ConTeXt sectioning command and return the command wrapping the element's content.
        
        Parameters:
            element (MarkdownElement): A heading element with a numeric `level` (expected 1–6) and `content` string to be used as the heading text.
        
        Returns:
            str: A ConTeXt sectioning command containing the heading text (for example `\chapter{Title}`); for levels outside 1–6 the deepest available sectioning command is used.
        """
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
        """
        Generate ConTeXt code for a paragraph element.
        
        Returns:
            str: Paragraph text suitable for inclusion in the generated ConTeXt document.
        """
        return element.content

    def _generate_code_block(self, element: MarkdownElement) -> str:
        """
        Generate ConTeXt code for a Markdown code block element.
        
        This uses the element's `attributes["language"]` (defaults to "text") to select a language-specific ConTeXt environment for known languages; for unknown languages it wraps the content in a generic typing environment.
        
        Parameters:
        	element (MarkdownElement): Markdown element whose `content` is the code and whose `attributes` may contain a `language` key.
        
        Returns:
        	str: ConTeXt source that wraps the element content in the chosen environment (e.g. `\startpython ... \stoppython` or `\starttyping ... \stoptyping`).
        """
        language = element.attributes.get("language", "text")

        # Sprach-spezifische Umgebungen
        if language in ["python", "java", "shell", "sql", "xml", "json", "yaml"]:
            return f"\\start{language}\n{element.content}\n\\stop{language}"
        else:
            return f"\\starttyping\n{element.content}\n\\stoptyping"

    def _generate_list(self, element: MarkdownElement) -> str:
        """
        Render an unordered Markdown list element into a ConTeXt itemize environment.
        
        Parameters:
            element (MarkdownElement): Markdown element whose `content` contains list items separated by newline characters.
        
        Returns:
            str: ConTeXt code for an itemize environment where each non-empty line from `element.content` becomes an `\item`.
        """
        items = element.content.split("\n")
        lines = ["\\startitemize"]
        for item in items:
            if item.strip():
                lines.append(f"\\item {item.strip()}")
        lines.append("\\stopitemize")
        return "\n".join(lines)

    def _generate_numbered_list(self, element: MarkdownElement) -> str:
        """
        Generate ConTeXt code for a numbered (enumerate) list from the element's content.
        
        Takes the element's content, splits it by newline, and emits a ConTeXt \startenumerate...\stopenumerate block where each non-empty trimmed line becomes an `\item`.
        
        Returns:
            str: ConTeXt source for the numbered list.
        """
        items = element.content.split("\n")
        lines = ["\\startenumerate"]
        for item in items:
            if item.strip():
                lines.append(f"\\item {item.strip()}")
        lines.append("\\stopenumerate")
        return "\n".join(lines)

    def _generate_table(self, element: MarkdownElement) -> str:
        """
        Render a simplified Markdown-style table into ConTeXt TABLE markup.
        
        The function expects element.content to contain newline-separated rows where table rows use pipe-delimited cells (e.g., "| a | b | c |"). The first pipe-containing row is treated as the header; rows that consist only of pipe/colon/dash/space separators are ignored. Each header cell is rendered as a ConTeXt table header cell and each subsequent data row as a table data cell.
        
        Parameters:
            element (MarkdownElement): Element whose `content` is a Markdown-style table string.
        
        Returns:
            str: ConTeXt source for the table wrapped between "\bTABLE" and "\eTABLE".
        """
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
        """
        Render a ConTeXt formula block from a Markdown math element.
        
        Parameters:
            element (MarkdownElement): The math block element whose `content` holds the formula source.
        
        Returns:
            str: ConTeXt source string with the formula wrapped in a `\startformula` / `\stopformula` environment.
        """
        return f"\\startformula\n{element.content}\n\\stopformula"

    def _generate_image(self, element: MarkdownElement) -> str:
        """
        Render a ConTeXt figure placement for an image Markdown element.
        
        Parameters:
            element (MarkdownElement): Image element whose `attributes` should include
                `src` (image path) and `alt` (caption / identifier).
        
        Returns:
            str: ConTeXt code that places the image using `\placefigure` with the
            `alt` text as caption and `\externalfigure` referencing `src`.
        """
        src = element.attributes.get("src", "")
        alt = element.attributes.get("alt", "")

        return f"\\placefigure[here][fig:{alt}]{{{alt}}}{{\\externalfigure[{src}][width=0.8\\textwidth]}}"