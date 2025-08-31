# FFHS-DUA - Datenstrukturen und Algorithmen

Eine professionelle Python-Implementierung grundlegender Datenstrukturen und Algorithmen für das Modul
**Datenstrukturen und Algorithmen (DUA)** an der Fernfachhochschule Schweiz (FFHS).
Das Projekt ist optimiert für Test-Driven Development und moderne Softwareentwicklungspraktiken.

## Projektübersicht

Dieses Projekt implementiert die wichtigsten Datenstrukturen und Algorithmen basierend auf den folgenden Lehrbüchern.
Alle Implementierungen sind an die Python-Sprache und moderne Programmierkonzepte angepasst.

### Implementierte Datenstrukturen

#### Fundamentals (Grundlagen)

- **Stack (Stapel)**: Drei verschiedene Implementierungen
  - `Stack`: Verkettete Liste mit dynamischer Größe
  - `FixedCapacityStack`: Festes Array mit vorgegebener Kapazität
  - `ResizingArrayStack`: Dynamisches Array mit automatischer Größenanpassung
- **Queue (Warteschlange)**: FIFO-Datenstruktur
- **Bag (Sammlung)**: Ungeordnete Sammlung von Elementen
- **Union-Find (Disjoint-Set)**: Vier Implementierungen für dynamische Konnektivität
  - `UF`: Optimierte Version mit Weighted Quick Union by Rank und Path Compression
  - `QuickUnionUF`: Einfache Quick Union Implementation
  - `WeightedQuickUnionUF`: Weighted Quick Union by Size
  - `QuickFindUF`: Quick Find Implementation mit konstanter Find-Zeit

Alle Implementierungen unterstützen generische Typen und folgen den Python-Konventionen für Container-Klassen.

#### PVA1 (Praktische Vertiefungsaufgaben)

- **Sierpinski-Dreieck**: Fraktal-Implementation mit rekursiven und iterativen Algorithmen
  - Mathematisch korrekte Positionierung
  - Visualisierung der Iterationsschritte
  - Umfassende AsciiDoc-Dokumentation
- **Grundlagen-Notebook**: Interaktive Jupyter-Übungen

## Installation und Setup

### Voraussetzungen

- Python 3.13.1 oder höher
- uv Package Manager (empfohlen) oder pip

### Schnellstart

```bash
# Repository klonen
git clone <repository-url>
cd ffhs-dua

# Entwicklungsumgebung automatisch einrichten
python scripts/setup_dev.py

# Oder manuell:
uv sync --dev
uv run pre-commit install
```

### Manuelle Installation

```bash
# Nur Produktionsabhängigkeiten
uv sync

# Mit Entwicklungsabhängigkeiten
uv sync --dev

# Oder mit pip
pip install -e ".[dev]"
```

## Entwicklung

### Test-Driven Development

Dieses Projekt folgt TDD-Prinzipien. Schreiben Sie Tests vor der Implementierung:

```bash
# Alle Tests ausführen
uv run pytest

# Tests mit Coverage-Report
uv run pytest --cov=src/algs4 --cov-report=html

# Spezifische Test-Kategorien
uv run pytest -m unit          # Nur Unit-Tests
uv run pytest -m integration   # Nur Integration-Tests
uv run pytest -m "not slow"    # Ohne langsame Tests

# Spezifische Testdatei
uv run pytest tests/test_fundamentals/test_bag.py

# Mit detaillierter Ausgabe
uv run pytest -v
```

### Code-Qualität und Formatierung

```bash
# Code automatisch formatieren
uv run ruff format

# Linting überprüfen
uv run ruff check

# Automatische Fehlerbehebung
uv run ruff check --fix

# Type-Checking mit mypy
uv run mypy src/

# Alle Qualitätschecks auf einmal
uv run pre-commit run --all-files
```

### Performance-Tests

```bash
# Benchmark-Tests ausführen
uv run python benchmarks/sorting_benchmarks.py

# Performance-Tests mit pytest-benchmark
uv run pytest tests/ --benchmark-only
```

### Jupyter Notebooks

```bash
# Jupyter Lab starten
jupyter lab

# Jupyter Notebook starten
jupyter notebook
```

## Verwendung

### Beispiel: Stack verwenden

```python
from src.algs4.fundamentals.stack import Stack

# Neuen Stack erstellen
stack = Stack[int]()

# Elemente hinzufügen
stack.push(1)
stack.push(2)
stack.push(3)

# Element vom Stack nehmen (LIFO)
top_element = stack.pop()  # Gibt 3 zurück

# Oberstes Element betrachten ohne zu entfernen
peek_element = stack.peek()  # Gibt 2 zurück

# Stack-Status überprüfen
is_empty = stack.is_empty()  # False
size = stack.size()  # 2
```

### Beispiel: Queue verwenden

```python
from src.algs4.fundamentals.queue import Queue

# Neue Queue erstellen
queue = Queue[str]()

# Elemente hinzufügen
queue.enqueue("Erstes")
queue.enqueue("Zweites")
queue.enqueue("Drittes")

# Element aus der Queue nehmen (FIFO)
first_element = queue.dequeue()  # Gibt "Erstes" zurück
```

### Beispiel: Union-Find verwenden

```python
from src.algs4.fundamentals.uf import UF

# Erstelle Union-Find-Struktur für 10 Elemente
uf = UF(10)

# Verbinde verschiedene Elemente
uf.union(0, 1)
uf.union(2, 3)
uf.union(1, 2)  # Verbindet {0,1} mit {2,3}

# Prüfe Verbindungen
print(f"0 und 3 verbunden: {uf.connected(0, 3)}")  # True
print(f"Anzahl Komponenten: {uf.count()}")  # 7 (original 10 - 3 unions)
```

### Beispiel: Sierpinski-Dreieck verwenden

```python
from notebooks.pva1.sierpinski import sierpinski, zeichne_sierpinski_progression

# Einzelnes Sierpinski-Dreieck zeichnen
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
sierpinski(0, 0, 3, max_iterations=5)
plt.axis('equal')
plt.show()

# Progression der ersten 5 Iterationen
zeichne_sierpinski_progression()
```

### Beispiel: Test-Driven Development

```python
# 1. Test schreiben (tests/test_fundamentals/test_stack.py)
def test_stack_push_pop():
    stack = Stack[str]()
    stack.push("first")
    stack.push("second")
    assert stack.pop() == "second"
    assert stack.pop() == "first"
    assert stack.is_empty()

# 2. Test ausführen (sollte fehlschlagen)
# uv run pytest tests/test_fundamentals/test_stack.py::test_stack_push_pop

# 3. Implementierung schreiben
# 4. Test erneut ausführen (sollte erfolgreich sein)
```

## Projektstruktur

```text
ffhs-dua/
├── src/
│   └── algs4/                    # Hauptpaket
│       ├── __init__.py
│       ├── fundamentals/         # Grundlegende Datenstrukturen
│       │   ├── __init__.py
│       │   ├── bag.py            # Bag-Implementierung
│       │   ├── queue.py          # Queue-Implementierungen
│       │   ├── stack.py          # Stack-Implementierungen
│       │   └── uf.py             # Union-Find-Implementierungen
│       ├── sorting/              # Sortieralgorithmen
│       │   ├── __init__.py
│       │   └── shell.py          # Shell Sort
│       ├── searching/            # Suchalgorithmen
│       │   └── __init__.py
│       ├── graphs/               # Graph-Algorithmen
│       │   └── __init__.py
│       └── errors/               # Benutzerdefinierte Exceptions
│           ├── __init__.py
│           └── errors.py
├── tests/                        # Test-Struktur spiegelt src/
│   ├── __init__.py
│   ├── conftest.py               # Gemeinsame Test-Fixtures
│   ├── test_fundamentals/
│   │   ├── __init__.py
│   │   ├── test_bag.py
│   │   ├── test_queue.py
│   │   ├── test_stack.py
│   │   └── test_uf.py
│   ├── test_sorting/
│   │   └── __init__.py
│   └── fixtures/
│       └── sample_data.py        # Test-Daten
├── notebooks/                    # Jupyter Notebooks für Lehrzwecke
│   └── pva1/
│       ├── __init__.py
│       ├── grundlagen.ipynb      # Grundlagen-Notebook
│       ├── sierpinski.py         # Sierpinski-Implementierung
│       └── sierpinski.adoc       # Sierpinski-Dokumentation
├── docs/                         # Dokumentation
│   ├── api/                      # API-Dokumentation
│   ├── tutorials/                # Tutorials
│   ├── examples/                 # Beispiele
│   └── *.adoc                    # AsciiDoc-Dateien
├── benchmarks/                   # Performance-Messungen
│   ├── __init__.py
│   └── sorting_benchmarks.py
├── scripts/                      # Hilfsskripte
│   └── setup_dev.py              # Entwicklungsumgebung einrichten
├── data/                         # Testdaten
│   ├── small/                    # Kleine Testdaten
│   ├── medium/                   # Mittlere Datensätze
│   └── large/                    # Große Datensätze
├── .pre-commit-config.yaml       # Pre-commit Hooks
├── pyproject.toml                # Projektkonfiguration mit Testing
├── uv.lock                       # Dependency-Lock-Datei
├── README.md                     # Diese Datei
└── CLAUDE.md                     # Entwicklungsrichtlinien
```

## Besonderheiten

### Professionelle Entwicklungspraktiken

#### TDD-Ansatz

Das Projekt folgt TDD-Prinzipien mit umfassender Test-Abdeckung:

- **Unit-Tests**: Testen einzelne Funktionen und Klassen
- **Integration-Tests**: Testen das Zusammenspiel mehrerer Komponenten  
- **Performance-Tests**: Messen Laufzeiten und Speicherverbrauch
- **Fixtures**: Wiederverwendbare Test-Daten und -Objekte

#### Code-Qualität und Typsicherheit

- **Type Hints**: Vollständige Typisierung mit generischen Typen
- **Linting**: Automatische Code-Überprüfung mit Ruff
- **Formatierung**: Einheitlicher Code-Stil mit Ruff Format
- **Pre-commit Hooks**: Automatische Qualitätschecks vor jedem Commit

#### Akademischer Fokus

Die Implementierungen folgen den Lehrbuchkonzepten und sind für Lernzwecke optimiert:

- Deutsche Dokumentation und Kommentare
- Schritt-für-Schritt Erklärungen
- Multiple Implementierungsvarianten für Vergleiche
- Jupyter Notebooks für interaktives Lernen

## Beitragen

Dieses Projekt folgt akademischen Standards:

- Alle neuen Features müssen umfassend getestet werden
- Code muss den Ruff-Linting-Standards entsprechen
- Dokumentation muss auf Deutsch verfasst werden
- Implementierungen sollten den Algorithmen aus dem Lehrbuch folgen

## Lizenz

Dieses Projekt ist für akademische Zwecke an der FFHS entwickelt worden.

## Unterstützung

Bei Fragen oder Problemen wenden Sie sich an die Dozierenden des Moduls oder erstellen Sie ein Issue in diesem Repository.

## Literaturgrundlagen

Das Modul **Datenstrukturen und Algorithmen (DUA)** basiert auf folgenden Lehrbüchern:

1. **Praktische Algorithmik mit Python**  
   Tobias Häberlein  
   ISBN: 978-3-486-71390-9

2. **Grokking Algorithms**  
   Aditya Y. Bhargava  
   ISBN: 978-1-633-43853-8

3. **Grokking Data Structures**  
   Marcello La Rocca  
   ISBN: 978-1-633-43699-2

4. **Learning Algorithms**  
   George Heineman  
   ISBN: 978-1-492-09106-6

5. **Programmieren mit Python**  
   Tobias Häberlein  
   ISBN: 978-3-662-68677-5

## Zusätzliche Referenzen

- [Python Documentation](https://docs.python.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [Type Hints (PEP 484)](https://peps.python.org/pep-0484/)
