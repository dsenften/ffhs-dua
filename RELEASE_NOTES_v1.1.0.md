# Release Notes v1.1.0

## Übersicht
Veröffentlichung am: 2025-12-23

Diese Version bringt bedeutende Erweiterungen für String-Algorithmen (PVA 5), Verbesserungen an den Graphen-Algorithmen (PVA 4) und zahlreiche Dokumentations-Updates.

## 🚀 Neue Features

### PVA 5: String-Algorithmen
- **PatriciaTrie**: Implementierung der delete-Methode mit intelligentem Node-Merging
- **KMP (Knuth-Morris-Pratt)**: Vollständiger String-Suchalgorithmus mit DFA
- **Boyer-Moore**: Effiziente Rückwärtssuche mit Bad Character Rule
- **Rabin-Karp**: Rolling-Hash basierte Suche mit Las-Vegas-Verifikation
- **TrieST**: Standard Trie Symbol Table mit Präfix-Operationen
- **Complete Test Suite**: 282 Tests für alle String-Algorithmen (99%+ Coverage)

### PVA 4: Graphen-Algorithmen
- **Dijkstra-Algorithmus**: Kürzeste-Wege-Suche mit IndexMinPQ
- **Edge Weighted Graphs**: Ungerichtete und gerichtete Graphen mit Gewichten
- **Cycle Detection**: Zyklenerkennung in gewichteten Graphen
- **Backtracking-Algorithmen**: TSP und ähnliche Probleme
- **MST-Implementierungen**: Minimum Spanning Tree Algorithmen

### Dokumentationssystem
- **ConTeXt-Integration**: Vollständiges LaTeX-Dokumentationssystem
- **Automatisierte Build-Pipeline**: Markdown zu LaTeX Konvertierung
- **Strukturierte Kapitel**: Nach PVA-Modulen organisierte Dokumentation

## 📚 Verbesserungen

### Code-Qualität
- **Pre-commit Hooks**: Automatisiertes Linting und Formatierung
- **Git LFS Integration**: Effiziente Verwaltung grosser Datendateien
- **Enhanced Test Coverage**: Gesamtabdeckung >93%

### Dokumentation
- **Gruppenarbeit-Struktur**: Detaillierte Anleitungen für PVA 4
- **Musterlösungen**: Vollständige Beispiele und Lösungen
- **Buch-Referenz**: Tobias Häberlein Algorithmen als primäre Referenz

## 🐛 Bug Fixes
- **MyPy Konfiguration**: Korrekte Typ-Prüfung für Test-Module
- **Pre-commit Setup**: Robustere Konfiguration für Development-Workflow

## 🔧 Technische Änderungen

### Dependencies
- Python 3.13.1 als Minimum-Version
- Matplotlib >=3.10.5 für Visualisierungen
- PyYAML >=6.0.2 für Konfiguration

### Development
- Ruff >=0.12.10 für Linting und Formatierung
- Erweiterte pytest-Konfiguration mit Markern
- Git LFS für alle Datendateien unter `data/`

## 📊 Statistiken

| Kategorie | Vorher | Neu | Wachstum |
|-----------|--------|-----|----------|
| Gesamt Tests | ~500 | 786 | +57% |
| String-Algorithmen | 0 | 282 | +282 |
| Graphen-Algorithmen | ~50 | 78 | +56% |
| Code Coverage | ~85% | 93%+ | +8% |

## 🚨 Wichtige Hinweise

### Migration
- Python 3.13.1 wird jetzt benötigt (vorher 3.12+)
- Bestehende Installationen müssen mit `uv sync` aktualisiert werden

### Breaking Changes
- Keine breaking Changes in der öffentlichen API
- Interne Reorganisation der Dokumentationsstruktur

## 🙏 Danksagungen
Besonderer Dank an alle Studierenden die zur Erweiterung der String-Algorithmen und Graphen-Implementierungen beigetragen haben.

## 🔗 Nächste Schritte
- PVA 5: Weitere String-Algorithmus-Optimierungen
- Performance-Benchmarks für alle Algorithmen
- Interactive Jupyter Notebooks für Visualisierungen

---

**Installationsbefehl:**
```bash
pip install ffhs-dua==1.1.0
```

**Development Setup:**
```bash
git clone https://github.com/dsenften/ffhs-dua.git
cd ffhs-dua
uv sync
```
