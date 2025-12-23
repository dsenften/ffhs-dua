#!/usr/bin/env python3
"""
ConTeXt-Dokumentationssystem für FFHS-DUA
==========================================

Hauptscript zur automatischen Konvertierung von Markdown-Dateien
in eine professionelle ConTeXt-basierte PDF-Dokumentation.

Verwendung:
    python build.py [Optionen]

Beispiele:
    python build.py                           # Standard-Build
    python build.py --config custom.yaml     # Mit eigener Konfiguration
    python build.py --chapters "pva1,pva2"   # Nur bestimmte Kapitel
    python build.py --debug --verbose        # Debug-Modus
"""

import argparse
import logging
import sys
from pathlib import Path

# Lokale Imports
from converter import (
    ConTeXtGenerator,
    MarkdownConverter,
    load_config,
    setup_logging,
    validate_environment,
)


class DocumentationBuilder:
    """Hauptklasse für die Dokumentationserstellung."""

    def __init__(self, config_path: Path | None = None):
        """
        Create a DocumentationBuilder configured from the given configuration path and initialize its converters and logger.
        
        Parameters:
            config_path (Path | None): Optional path to the configuration file; if None, the default configuration location is used.
        """
        self.config = load_config(config_path)
        self.converter = MarkdownConverter(self.config)
        self.generator = ConTeXtGenerator(self.config)
        self.logger = logging.getLogger(__name__)

    def build_documentation(
        self,
        chapters: list[str] | None = None,
        convert_only: bool = False,
        force_rebuild: bool = False,
    ) -> bool:
        """
        Orchestrates conversion of Markdown sources to ConTeXt and optionally builds the final PDF.
        
        Performs environment validation, discovers and converts Markdown files (optionally restricted to specified chapters), generates the main ConTeXt document, and—unless disabled—builds the PDF output.
        
        Parameters:
            chapters (list[str] | None): Optional list of chapter names to process; if None, all configured Markdown files are processed.
            convert_only (bool): If True, only convert Markdown to ConTeXt and do not attempt to build the PDF.
            force_rebuild (bool): If True, force rebuilding of all files regardless of cached/previous outputs.
        
        Returns:
            bool: `True` if the requested workflow completed successfully, `False` on any failure.
        """
        try:
            self.logger.info("Starte Dokumentationserstellung...")

            # 1. Umgebung validieren
            if not validate_environment():
                return False

            # 2. Markdown-Dateien finden und konvertieren
            markdown_files = self._find_markdown_files(chapters)
            if not markdown_files:
                self.logger.error("Keine Markdown-Dateien gefunden")
                return False

            self.logger.info(f"Gefunden: {len(markdown_files)} Markdown-Dateien")

            # 3. Konvertierung durchführen
            context_files = []
            for md_file in markdown_files:
                self.logger.info(f"Konvertiere: {md_file}")
                ctx_file = self.converter.convert_file(md_file, force_rebuild)
                if ctx_file:
                    context_files.append(ctx_file)
                else:
                    self.logger.warning(f"Konvertierung fehlgeschlagen: {md_file}")

            if not context_files:
                self.logger.error("Keine ConTeXt-Dateien erstellt")
                return False

            # 4. Hauptdokument generieren
            main_document = self.generator.generate_main_document(context_files)
            if not main_document:
                self.logger.error("Hauptdokument-Generierung fehlgeschlagen")
                return False

            # 5. PDF erstellen (falls gewünscht)
            if not convert_only:
                pdf_path = self._build_pdf(main_document)
                if pdf_path:
                    self.logger.info(f"PDF erstellt: {pdf_path}")
                    return True
                else:
                    self.logger.error("PDF-Erstellung fehlgeschlagen")
                    return False

            self.logger.info("Konvertierung erfolgreich abgeschlossen")
            return True

        except Exception as e:
            self.logger.error(f"Fehler bei Dokumentationserstellung: {e}")
            return False

    def _find_markdown_files(self, chapters: list[str] | None = None) -> list[Path]:
        """
        Locate Markdown source files to process, either for specific chapters or for all configured directories.
        
        Parameters:
            chapters (list[str] | None): Optional list of chapter names to restrict discovery to; if omitted, files from all configured markdown directories are returned.
        
        Returns:
            list[Path]: A list of Paths to Markdown files. When `chapters` is provided, files are collected from each named chapter's configured file patterns (expanding glob patterns and including existing explicit file paths). When `chapters` is None, discovery uses the configured markdown directories and extensions.
        """
        from converter.utils import find_markdown_files

        if chapters:
            # Nur spezifische Kapitel
            files = []
            for chapter in chapters:
                if chapter in self.config.chapters:
                    chapter_config = self.config.chapters[chapter]
                    chapter_files = []
                    for file_pattern in chapter_config.get("files", []):
                        pattern_path = Path(file_pattern)
                        if "*" in str(pattern_path):
                            # Glob-Pattern
                            chapter_files.extend(Path.cwd().glob(str(pattern_path)))
                        else:
                            # Einzelne Datei
                            if pattern_path.exists():
                                chapter_files.append(pattern_path)
                    files.extend(chapter_files)
            return files
        else:
            # Alle Markdown-Dateien
            return find_markdown_files(
                self.config.markdown_dirs, self.config.markdown_extensions
            )

    def _build_pdf(self, main_document: Path) -> Path | None:
        """
        Builds a PDF from the provided ConTeXt main document.
        
        Runs the ConTeXt build using the configured output directory, optionally copies assets and cleans the PDF output directory beforehand, and ensures the final file uses the configured PDF output name when possible.
        
        Parameters:
            main_document (Path): Path to the generated ConTeXt main document to be compiled.
        
        Returns:
            Path | None: Path to the produced PDF file if the build succeeds and a PDF is found, `None` on failure.
        """
        from converter.utils import clean_output_directory, copy_assets, run_context

        try:
            # Assets kopieren
            if self.config.build_options.get("copy_assets", True):
                copy_assets(self.config.assets_dir, self.config.output_dir / "assets")

            # Ausgabeverzeichnis bereinigen (optional)
            if self.config.build_options.get("clean_before_build", False):
                clean_output_directory(self.config.output_dir / "pdf")

            # ConTeXt ausführen
            success, output = run_context(main_document, self.config.output_dir / "pdf")

            if success:
                # PDF-Datei finden
                pdf_name = self.config.pdf_output_name
                pdf_path = self.config.output_dir / "pdf" / pdf_name

                # Falls PDF mit anderem Namen erstellt wurde
                if not pdf_path.exists():
                    # Nach PDF-Dateien suchen
                    pdf_files = list((self.config.output_dir / "pdf").glob("*.pdf"))
                    if pdf_files:
                        pdf_path = pdf_files[0]
                        # Umbenennen falls nötig
                        if pdf_path.name != pdf_name:
                            new_path = pdf_path.parent / pdf_name
                            pdf_path.rename(new_path)
                            pdf_path = new_path

                return pdf_path if pdf_path.exists() else None
            else:
                self.logger.error(f"ConTeXt-Fehler: {output}")
                return None

        except Exception as e:
            self.logger.error(f"Fehler bei PDF-Erstellung: {e}")
            return None


def main():
    """
    Command-line entry point that parses CLI options, configures logging, and runs the documentation build.
    
    Parses arguments for configuration path, chapter selection, convert-only mode, force rebuild, output path, and verbosity/debug flags. Translates the chapters argument into a list when provided, sets the logging level based on debug/verbose flags, instantiates DocumentationBuilder with the given config, invokes its build_documentation method with the parsed options, and exits the process with status 0 on success or 1 on failure.
    """
    parser = argparse.ArgumentParser(
        description="ConTeXt-Dokumentationssystem für FFHS-DUA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "--config",
        "-c",
        type=Path,
        help="Pfad zur Konfigurationsdatei (Standard: config/build.yaml)",
    )

    parser.add_argument(
        "--chapters", help="Komma-getrennte Liste der Kapitel (z.B. 'pva1,pva2,pva3')"
    )

    parser.add_argument(
        "--convert-only",
        action="store_true",
        help="Nur konvertieren, keine PDF erstellen",
    )

    parser.add_argument(
        "--force-rebuild", action="store_true", help="Alle Dateien neu erstellen"
    )

    parser.add_argument("--output", "-o", type=Path, help="Ausgabepfad für PDF-Datei")

    parser.add_argument("--debug", action="store_true", help="Debug-Modus aktivieren")

    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Ausführliche Ausgabe"
    )

    args = parser.parse_args()

    # Logging konfigurieren
    log_level = (
        logging.DEBUG
        if args.debug
        else (logging.INFO if args.verbose else logging.WARNING)
    )
    setup_logging(log_level)

    # Kapitel-Liste verarbeiten
    chapters = None
    if args.chapters:
        chapters = [ch.strip() for ch in args.chapters.split(",")]

    # Builder erstellen und ausführen
    builder = DocumentationBuilder(args.config)
    success = builder.build_documentation(
        chapters=chapters,
        convert_only=args.convert_only,
        force_rebuild=args.force_rebuild,
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()