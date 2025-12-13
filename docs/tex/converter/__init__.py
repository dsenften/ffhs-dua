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
        Initialisiert den Konverter.

        Args:
            config: Build-Konfiguration
        """
        self.config = config
        self.parser = MarkdownParser(config)
        self.generator = ConTeXtGenerator(config)

    def convert_file(self, markdown_path, force_rebuild=False):
        """
        Konvertiert eine einzelne Markdown-Datei zu ConTeXt.

        Args:
            markdown_path: Pfad zur Markdown-Datei
            force_rebuild: Datei auch bei vorhandener Ausgabe neu erstellen

        Returns:
            Pfad zur erstellten ConTeXt-Datei oder None bei Fehler
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
        Konvertiert alle Markdown-Dateien in einem Verzeichnis.

        Args:
            directory_path: Pfad zum Verzeichnis
            pattern: Datei-Pattern für Markdown-Dateien
            force_rebuild: Alle Dateien neu erstellen

        Returns:
            Liste der erstellten ConTeXt-Dateien
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
