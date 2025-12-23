"""
ConTeXt-Dokumentationssystem - Konverter-Module
===============================================

Dieses Paket enthält alle Module zur Konvertierung von Markdown-Dateien
in ConTeXt-Format für die automatische Dokumentationserstellung.

Module:
    markdown_parser: Parst Markdown-Dateien und extrahiert Struktur
    context_generator: Generiert ConTeXt-Code aus geparsten Inhalten
    utils: Hilfsfunktionen für Konvertierung und Verarbeitung
    config: Konfigurationsmanagement

Hauptklassen:
    MarkdownConverter: Hauptklasse für Markdown → ConTeXt Konvertierung
    ConTeXtGenerator: Generiert finale ConTeXt-Dokumente
    BuildConfig: Konfigurationsmanagement
"""

from .config import BuildConfig, load_config
from .context_generator import ConTeXtGenerator
from .markdown_parser import MarkdownParser
from .utils import setup_logging, validate_environment


# Hauptklasse für einfache Verwendung
class MarkdownConverter:
    """
    Hauptklasse für die Konvertierung von Markdown zu ConTeXt.

    Diese Klasse kombiniert alle Konvertierungsschritte in einer
    einfach zu verwendenden Schnittstelle.
    """

    def __init__(self, config: BuildConfig):
        """
        Initialize the MarkdownConverter with a build configuration.
        
        Parameters:
            config (BuildConfig): Configuration used to initialize the converter and to configure the internal MarkdownParser and ConTeXtGenerator.
        """
        self.config = config
        self.parser = MarkdownParser(config)
        self.generator = ConTeXtGenerator(config)

    def convert_file(self, markdown_path, force_rebuild=False):
        """
        Convert a single Markdown file into a ConTeXt file.
        
        Parameters:
            markdown_path (str or Path): Path to the Markdown file to convert.
            force_rebuild (bool): If True, recreate the output even if it already exists.
        
        Returns:
            str or None: Path to the generated ConTeXt file, or `None` if conversion failed.
        """
        try:
            # Markdown parsen
            document = self.parser.parse_file(markdown_path)
            if not document:
                return None

            # ConTeXt generieren
            context_path = self.generator.generate_file(document, force_rebuild)
            return context_path

        except Exception as e:
            print(f"Fehler bei Konvertierung von {markdown_path}: {e}")
            return None

    def convert_directory(self, directory_path, pattern="*.md", force_rebuild=False):
        """
        Convert all Markdown files in a directory to ConTeXt files.
        
        Parameters:
            directory_path (str | pathlib.Path): Path to the directory containing Markdown files.
            pattern (str): Glob pattern to select Markdown files (default: "*.md").
            force_rebuild (bool): If True, regenerate ConTeXt files even when up-to-date.
        
        Returns:
            list[str]: Paths of the generated ConTeXt files.
        """
        from pathlib import Path

        directory = Path(directory_path)
        markdown_files = list(directory.glob(pattern))
        context_files = []

        for md_file in markdown_files:
            ctx_file = self.convert_file(md_file, force_rebuild)
            if ctx_file:
                context_files.append(ctx_file)

        return context_files


__all__ = [
    "MarkdownConverter",
    "ConTeXtGenerator",
    "MarkdownParser",
    "BuildConfig",
    "load_config",
    "setup_logging",
    "validate_environment",
]