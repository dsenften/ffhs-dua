#!/usr/bin/env python3
"""
Script zum Generieren von Coverage-Reports für ffhs-dua.

Dieses Script generiert Coverage-Reports in verschiedenen Formaten:
- Terminal-Report mit fehlenden Zeilen
- HTML-Report für interaktive Ansicht
- XML-Report für CI/CD-Integration

Verwendung:
    python3 scripts/generate_coverage.py [--html] [--xml] [--all]

Beispiele:
    # Nur Terminal-Report
    python3 scripts/generate_coverage.py

    # Terminal + HTML
    python3 scripts/generate_coverage.py --html

    # Alle Reports
    python3 scripts/generate_coverage.py --all
"""

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    """Hauptfunktion zum Generieren von Coverage-Reports."""
    parser = argparse.ArgumentParser(
        description="Coverage-Report Generator für ffhs-dua"
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Generiere HTML-Report",
    )
    parser.add_argument(
        "--xml",
        action="store_true",
        help="Generiere XML-Report",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generiere alle Reports (HTML + XML)",
    )

    args = parser.parse_args()

    # Stelle sicher, dass wir im Projekt-Root sind
    project_root = Path.cwd()
    if not (project_root / "pyproject.toml").exists():
        print("❌ Fehler: pyproject.toml nicht gefunden!")
        print("Bitte führe dieses Script aus dem Projekt-Root aus.")
        return 1

    print("=" * 60)
    print("Coverage-Report Generator für ffhs-dua")
    print("=" * 60)
    print()

    # Installiere Dependencies falls nötig
    print("📦 Überprüfe Dependencies...")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q", "pytest", "pytest-cov"],
        check=False,
    )
    print()

    # Baue pytest-Kommando
    pytest_cmd = [
        sys.executable,
        "-m",
        "pytest",
        "tests/",
        "--cov=src.algs4",
        "--cov-report=term-missing",
        "-q",
    ]

    if args.all or args.html:
        pytest_cmd.append("--cov-report=html")

    if args.all or args.xml:
        pytest_cmd.append("--cov-report=xml")

    # Führe pytest aus
    print("📊 Generiere Coverage-Reports...")
    print()

    result = subprocess.run(pytest_cmd, cwd=project_root)

    if result.returncode != 0:
        print()
        print("❌ Fehler beim Generieren der Coverage-Reports!")
        return 1

    print()
    print("=" * 60)
    print("✅ Coverage-Reports erfolgreich generiert!")
    print("=" * 60)
    print()

    # Zeige Pfade zu den generierten Reports
    if args.all or args.html:
        print("📄 HTML-Report:")
        print("  Pfad: htmlcov/index.html")
        print("  Öffnen mit: open htmlcov/index.html")
        print()

    if args.all or args.xml:
        print("📄 XML-Report:")
        print("  Pfad: coverage.xml")
        print()

    print("📊 Terminal-Report:")
    print("  Siehe oben für detaillierte Statistiken")
    print()

    # Zeige Coverage-Zusammenfassung
    print("=" * 60)
    print("Coverage-Zusammenfassung")
    print("=" * 60)
    subprocess.run(
        [sys.executable, "-m", "coverage", "report", "--skip-covered"],
        cwd=project_root,
        check=False,
    )

    print()
    print("✅ Fertig!")
    return 0


if __name__ == "__main__":
    sys.exit(main())

