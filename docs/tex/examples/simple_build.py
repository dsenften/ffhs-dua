#!/usr/bin/env python3
"""
Einfaches Beispiel für die Verwendung des ConTeXt-Dokumentationssystems
=======================================================================

Dieses Script zeigt, wie das Dokumentationssystem verwendet wird,
um aus Markdown-Dateien eine professionelle PDF-Dokumentation zu erstellen.
"""

import sys
from pathlib import Path

from converter import (
    MarkdownConverter,
    load_config,
    setup_logging,
    validate_environment,
)
from converter.utils import format_file_size

# Pfad zum Converter-Modul hinzufügen
sys.path.insert(0, str(Path(__file__).parent.parent))


def main():
    """
    Orchestrates a simple ConTeXt documentation build and demonstrates single-file, directory, and full-project conversion workflows.
    
    Performs environment validation, loads configuration, initializes a MarkdownConverter, and runs three example scenarios:
    1. Convert a single README.md if present.
    2. Convert all Markdown files in a given directory (pva/pva5) if present.
    3. Discover all project Markdown files, convert them to ConTeXt, generate the main document, and attempt to build a PDF via the DocumentationBuilder.
    
    Returns:
        int: Exit code — `0` on successful completion, `1` if environment validation fails or an unrecoverable error occurs during the demo.
    """

    # Logging einrichten
    setup_logging()

    print("🚀 FFHS-DUA ConTeXt-Dokumentationssystem")
    print("=" * 50)

    # Umgebung validieren
    print("🔍 Validiere Umgebung...")
    if not validate_environment():
        print("❌ Umgebungsvalidierung fehlgeschlagen!")
        return 1
    print("✅ Umgebung OK")

    # Konfiguration laden
    print("📋 Lade Konfiguration...")
    config = load_config()
    print(f"✅ Konfiguration geladen: {config.document_title}")

    # Konverter initialisieren
    print("🔧 Initialisiere Konverter...")
    converter = MarkdownConverter(config)

    # Beispiel 1: Einzelne Datei konvertieren
    print("\n📄 Beispiel 1: Einzelne Datei konvertieren")
    readme_path = Path("README.md")
    if readme_path.exists():
        context_file = converter.convert_file(readme_path)
        if context_file:
            print(f"✅ Konvertiert: {readme_path} → {context_file}")
        else:
            print(f"❌ Fehler bei Konvertierung von {readme_path}")
    else:
        print("⚠️  README.md nicht gefunden")

    # Beispiel 2: Verzeichnis konvertieren
    print("\n📁 Beispiel 2: Verzeichnis konvertieren")
    pva5_dir = Path("pva/pva5")
    if pva5_dir.exists():
        context_files = converter.convert_directory(pva5_dir)
        print(f"✅ {len(context_files)} Dateien aus {pva5_dir} konvertiert")
        for ctx_file in context_files[:3]:  # Nur erste 3 anzeigen
            print(f"   → {ctx_file}")
        if len(context_files) > 3:
            print(f"   ... und {len(context_files) - 3} weitere")
    else:
        print("⚠️  pva/pva5 Verzeichnis nicht gefunden")

    # Beispiel 3: Vollständige Dokumentation erstellen
    print("\n📚 Beispiel 3: Vollständige Dokumentation")

    # Build-System verwenden
    from ..build import DocumentationBuilder

    builder = DocumentationBuilder(config)

    # Alle Markdown-Dateien finden
    markdown_files = builder._find_markdown_files()
    print(f"📄 {len(markdown_files)} Markdown-Dateien gefunden")

    # Zu ConTeXt konvertieren
    print("🔄 Konvertiere zu ConTeXt...")
    context_files = []
    for md_file in markdown_files:
        ctx_file = converter.convert_file(md_file)
        if ctx_file:
            context_files.append(ctx_file)

    print(f"✅ {len(context_files)} ConTeXt-Dateien erstellt")

    # Hauptdokument generieren
    print("📖 Generiere Hauptdokument...")
    main_doc = converter.generator.generate_main_document(context_files)
    if main_doc:
        print(f"✅ Hauptdokument: {main_doc}")

        # PDF erstellen
        print("🎯 Erstelle PDF...")
        pdf_path = builder._build_pdf(main_doc)
        if pdf_path:
            file_size = format_file_size(pdf_path.stat().st_size)
            print(f"🎉 PDF erfolgreich erstellt: {pdf_path} ({file_size})")
        else:
            print("❌ PDF-Erstellung fehlgeschlagen")
    else:
        print("❌ Hauptdokument-Generierung fehlgeschlagen")

    print("\n✨ Build-Prozess abgeschlossen!")
    return 0


def demo_advanced_features():
    """
    Demonstrates and prints examples of the converter's advanced features and configuration.
    
    Loads the project configuration, attempts to instantiate the DocumentationBuilder (returns early if not available), and prints:
    - the number of Markdown files selected for the "pva5" chapter,
    - the first five index terms and a count of remaining terms,
    - the ordered chapter structure with each chapter's title and file count.
    """

    print("\n🔬 Erweiterte Features")
    print("-" * 30)

    # Konfiguration laden
    config = load_config()

    # Spezifische Kapitel auswählen
    print("📑 Nur PVA 5 konvertieren...")
    try:
        from ..build import DocumentationBuilder

        builder = DocumentationBuilder(config)
    except ImportError:
        print("   ⚠️  DocumentationBuilder nicht verfügbar (Beispiel-Modus)")
        return
    pva5_files = builder._find_markdown_files(["pva5"])
    print(f"   → {len(pva5_files)} Dateien für PVA 5")

    # Index-Begriffe anzeigen
    print("📇 Index-Begriffe:")
    for term in config.index_terms[:5]:  # Nur erste 5
        print(f"   → {term}")
    print(f"   ... und {len(config.index_terms) - 5} weitere")

    # Kapitel-Konfiguration anzeigen
    print("📚 Kapitel-Struktur:")
    for chapter_id, chapter_config in config.chapters.items():
        order = chapter_config.get("order", 0)
        title = chapter_config.get("title", chapter_id)
        file_count = len(chapter_config.get("files", []))
        print(f"   {order}. {title} ({file_count} Dateien)")


if __name__ == "__main__":
    try:
        exit_code = main()

        # Erweiterte Features demonstrieren
        demo_advanced_features()

        sys.exit(exit_code)

    except KeyboardInterrupt:
        print("\n⚠️  Build-Prozess abgebrochen")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unerwarteter Fehler: {e}")
        sys.exit(1)