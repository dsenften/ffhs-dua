#!/usr/bin/env python3
"""
Entwicklungsumgebung einrichten.
"""

import subprocess
import sys
from pathlib import Path


def run_command(command: str, description: str) -> bool:
    """Führt einen Befehl aus und gibt den Status zurück."""
    print(f"🔄 {description}...")
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ {description} erfolgreich")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Fehler bei {description}: {e}")
        return False


def main():
    """Hauptfunktion zum Einrichten der Entwicklungsumgebung."""
    print("🚀 Einrichtung der ALGS4 Entwicklungsumgebung")
    print("=" * 50)
    
    # Prüfe ob uv installiert ist
    try:
        subprocess.run(["uv", "--version"], check=True, capture_output=True)
        print("✅ uv ist bereits installiert")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ uv ist nicht installiert. Bitte installieren Sie uv zuerst:")
        print("   curl -LsSf https://astral.sh/uv/install.sh | sh")
        sys.exit(1)
    
    # Abhängigkeiten installieren
    if not run_command("uv sync --dev", "Abhängigkeiten installieren"):
        sys.exit(1)
    
    # Pre-commit hooks installieren
    if not run_command("uv run pre-commit install", "Pre-commit hooks installieren"):
        print("⚠️  Pre-commit hooks konnten nicht installiert werden")
    
    # Tests ausführen
    if not run_command("uv run pytest tests/ -v", "Tests ausführen"):
        print("⚠️  Einige Tests sind fehlgeschlagen")
    
    print("\n🎉 Entwicklungsumgebung erfolgreich eingerichtet!")
    print("\nNächste Schritte:")
    print("  - Starten Sie Jupyter Lab: uv run jupyter lab")
    print("  - Führen Sie Tests aus: uv run pytest")
    print("  - Formatieren Sie Code: uv run ruff format")
    print("  - Überprüfen Sie Code: uv run ruff check")


if __name__ == "__main__":
    main()
