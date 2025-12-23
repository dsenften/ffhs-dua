# ConTeXt-Dokumentationssystem für FFHS-DUA

Professionelles Dokumentationssystem zur automatischen Konvertierung von Markdown-Dateien in hochwertige PDF-Dokumente mit ConTeXt.

## 🎯 Überblick

Dieses System löst das Problem der professionellen Dokumentationserstellung für akademische Projekte. Es konvertiert automatisch alle Markdown-Dateien des FFHS-DUA Projekts in ein einheitliches, hochwertig formatiertes PDF-Dokument.

### ✨ Hauptfeatures

- **🔄 Automatische Markdown → ConTeXt Konvertierung**
- **🎨 Professionelle Typografie** mit FFHS-Corporate-Design
- **🌈 Syntax-Highlighting** für Python, Java, Shell, SQL, XML, JSON, YAML
- **📑 Automatisches Inhaltsverzeichnis** und Index-Generierung
- **🧮 Mathematische Formeln** und wissenschaftliche Notation
- **📊 Tabellen und Diagramme** mit automatischer Formatierung
- **🖼️ Bilder und Grafiken** mit intelligenter Skalierung
- **🧩 Modulare Template-Struktur** für einfache Anpassungen
- **⚙️ Konfigurierbare Build-Pipeline** mit YAML-Konfiguration

## 🚀 Schnellstart

### 1. Voraussetzungen installieren

**ConTeXt installieren:**

```bash
# macOS (mit Homebrew)
brew install --cask mactex
# oder nur ConTeXt:
brew install context

# Ubuntu/Debian
sudo apt-get install context

# Windows: ConTeXt Standalone herunterladen
# https://wiki.contextgarden.net/Installation
```

**Python-Abhängigkeiten:**

```bash
# Mit uv (empfohlen für dieses Projekt)
uv sync

# Oder mit pip
pip install pyyaml
```

### 2. Erste Verwendung

```bash
# 🎯 Komplette Dokumentation erstellen
python3 docs/tex/build.py

# 📚 Nur bestimmte Kapitel (PVA 1 und 5)
python3 docs/tex/build.py --chapters pva1 pva5

# 🔄 Nur Markdown → ConTeXt (kein PDF)
python3 docs/tex/build.py --convert-only

# 🐛 Mit ausführlicher Debug-Ausgabe
python3 docs/tex/build.py --debug
```

### 3. Ergebnis

Nach erfolgreichem Build finden Sie:
- **📕 PDF-Dokumentation**: `docs/tex/output/pdf/ffhs-dua-documentation.pdf`
- **📄 ConTeXt-Dateien**: `docs/tex/output/context/`
- **📋 Build-Log**: `docs/tex/output/build.log`

## 📁 Verzeichnisstruktur

```
docs/tex/
├── build.py                 # 🚀 Haupt-Build-Script
├── README.md                # 📖 Diese Dokumentation
├── config/
│   └── build.yaml           # ⚙️ Build-Konfiguration
├── templates/
│   ├── main.tex             # 📄 Haupt-ConTeXt-Template
│   ├── styles/              # 🎨 Style-Definitionen
│   │   ├── typography.tex   # ✍️ Schriftarten und Layout
│   │   ├── colors.tex       # 🌈 FFHS-Farbpalette
│   │   └── code.tex         # 💻 Code-Highlighting
│   └── components/          # 🧩 Wiederverwendbare Komponenten
│       ├── titlepage.tex    # 🏠 Professionelle Titelseite
│       ├── toc.tex          # 📑 Inhaltsverzeichnis
│       └── index.tex        # 📇 Stichwortverzeichnis
├── converter/               # 🔧 Python-Konverter-Module
│   ├── __init__.py          # 🎯 Hauptklassen und API
│   ├── markdown_parser.py   # 📝 Markdown-Parser
│   ├── context_generator.py # 📄 ConTeXt-Code-Generator
│   ├── config.py            # ⚙️ Konfigurationsmanagement
│   └── utils.py             # 🛠️ Hilfsfunktionen
├── examples/                # 💡 Beispiele und Demos
│   └── simple_build.py      # 🚀 Einfaches Build-Beispiel
├── assets/                  # 📦 Statische Assets
│   ├── logos/               # 🏢 FFHS-Logos und Grafiken
│   └── fonts/               # 🔤 Zusätzliche Schriftarten
└── output/                  # 📤 Generierte Dateien
    ├── context/             # 📄 Zwischenergebnisse (ConTeXt)
    ├── pdf/                 # 📕 Finale PDF-Ausgabe
    └── .cache/              # ⚡ Build-Cache für Performance
```

## Verwendung

### Schnellstart

```bash
# PDF-Dokumentation erstellen
python docs/tex/build.py

# Mit spezifischen Optionen
python docs/tex/build.py --config custom.yaml --output custom.pdf
```

### Erweiterte Verwendung

```bash
# Nur konvertieren (ohne PDF-Erstellung)
python docs/tex/build.py --convert-only

# Bestimmte Kapitel
python docs/tex/build.py --chapters "pva1,pva2,pva3"

# Debug-Modus
python docs/tex/build.py --debug --verbose
```

## Features

- ✅ Automatische Markdown → ConTeXt Konvertierung
- ✅ Professionelle Typografie und Layout
- ✅ Code-Syntax-Highlighting
- ✅ Automatisches Inhaltsverzeichnis
- ✅ Automatischer Index
- ✅ Mathematische Formeln (LaTeX-kompatibel)
- ✅ Bild- und Diagramm-Integration
- ✅ Hyperlinks und Querverweise
- ✅ Modulare Template-Struktur
- ✅ Konfigurierbare Styles
- ✅ Batch-Processing

## Anforderungen

- Python 3.8+
- ConTeXt (TeXLive oder Standalone)
- Pandoc (optional, für erweiterte Konvertierung)

## Installation

Siehe `docs/tex/INSTALL.md` für detaillierte Installationsanweisungen.
