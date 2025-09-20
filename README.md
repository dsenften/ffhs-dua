# FFHS-DUA: Algorithmen und Datenstrukturen

Eine umfassende Python-Implementierung grundlegender Algorithmen und Datenstrukturen basierend auf dem Lehrbuch "Algorithms, 4th Edition" von Robert Sedgewick und Kevin Wayne.

Dieses Projekt wurde für den akademischen Gebrauch an der Fernfachhochschule Schweiz (FFHS) entwickelt und bietet eine vollständige, gut dokumentierte und getestete Sammlung von Algorithmen und Datenstrukturen.

## Projektübersicht

### Ziele

* **Bildung**: Bereitstellung klarer, verständlicher Implementierungen für Lernzwecke
* **Qualität**: Hochwertige, gut getestete und dokumentierte Code-Basis
* **Praxis**: Anwendbare Implementierungen für reale Probleme
* **Standards**: Einhaltung moderner Python-Entwicklungsstandards

### Prinzipien

* **Deutsche Dokumentation**: Alle Dokumentation und Kommentare auf Deutsch
* **Type Hints**: Vollständige Typisierung für bessere Code-Qualität
* **Umfassende Tests**: Hohe Testabdeckung mit pytest
* **Clean Code**: Lesbare, wartbare Implementierungen

## Module

### Fundamentals (Grundlagen)

Das `fundamentals`-Modul enthält die grundlegenden Datenstrukturen:

#### Datenstrukturen
* **Stack**: Last-In-First-Out (LIFO) Stapel in drei Implementierungen
  - `Stack`: Verkettete Liste mit dynamischer Grösse
  - `FixedCapacityStack`: Festes Array mit vorgegebener Kapazität
  - `ResizingArrayStack`: Dynamisches Array mit automatischer Grössenanpassung
* **Queue**: First-In-First-Out (FIFO) Warteschlange
* **Bag**: Ungeordnete Sammlung von Elementen
* **Union-Find**: Datenstruktur für dynamische Konnektivität in vier Implementierungen
  - `UF`: Optimierte Version mit Weighted Quick Union by Rank und Path Compression
  - `QuickUnionUF`: Einfache Quick Union Implementation
  - `WeightedQuickUnionUF`: Weighted Quick Union by Size
  - `QuickFindUF`: Quick Find Implementation mit konstanter Find-Zeit

### Sorting (Sortieralgorithmen)

Das `sorting`-Modul enthält verschiedene Sortieralgorithmen:

#### Algorithmen
* **Quick Sort**: Effizienter Divide-and-Conquer-Algorithmus
* **Shell Sort**: Erweiterte Insertion-Sort-Variante

Alle Implementierungen unterstützen generische Typen und folgen den Python-Konventionen für Container-Klassen.

## Installation und Setup

### Voraussetzungen

- Python 3.13.1 oder höher
- uv Package Manager (empfohlen) oder pip

### Schnellstart

```bash
# Repository klonen
git clone <repository-url>
cd ffhs-dua

# Virtuelle Umgebung erstellen
python3 -m venv .venv
source .venv/bin/activate

# Abhängigkeiten installieren
pip install -e .
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
python3 -m pytest tests/ -v

# Tests mit Coverage-Report
python3 -m pytest tests/ --cov=src.algs4 --cov-report=html

# Spezifische Test-Kategorien
python3 -m pytest -m unit          # Nur Unit-Tests
python3 -m pytest -m integration   # Nur Integration-Tests
python3 -m pytest -m "not slow"    # Ohne langsame Tests

# Spezifische Testdatei
python3 -m pytest tests/test_fundamentals/test_bag.py

# Mit detaillierter Ausgabe
python3 -m pytest -v
```

### Code-Qualität und Formatierung

```bash
# Code automatisch formatieren
ruff format

# Linting überprüfen
ruff check

# Automatische Fehlerbehebung
ruff check --fix

# Type-Checking mit mypy
mypy src/

# Alle Qualitätschecks auf einmal
pre-commit run --all-files
```

### Performance-Tests

```bash
# Benchmark-Tests ausführen
python benchmarks/sorting_benchmarks.py

# Performance-Tests mit pytest-benchmark
python3 -m pytest tests/ --benchmark-only
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

### Beispiel: Sortieralgorithmen verwenden

```python
from src.algs4.sorting import Quick, Shell

# Quick Sort
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = Quick.sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 34, 64, 90]

# Shell Sort
words = ["zebra", "apple", "banana", "cherry"]
sorted_words = Shell.sort(words)
print(sorted_words)  # ['apple', 'banana', 'cherry', 'zebra']
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
# python3 -m pytest tests/test_fundamentals/test_stack.py::test_stack_push_pop

# 3. Implementierung schreiben
# 4. Test erneut ausführen (sollte erfolgreich sein)
```

## Projektstruktur

```text
ffhs-dua/
├── src/
│   └── algs4/
│       ├── fundamentals/          # Grundlegende Datenstrukturen
│       │   ├── stack.py           # Stack-Implementierungen
│       │   ├── queue.py           # Queue-Implementierung
│       │   ├── bag.py             # Bag-Implementierung
│       │   └── uf.py              # Union-Find-Implementierungen
│       ├── sorting/               # Sortieralgorithmen
│       │   ├── quick.py           # Quick Sort
│       │   └── shell.py           # Shell Sort
│       └── errors/                # Benutzerdefinierte Exceptions
├── tests/                         # Umfassende Test-Suite
│   ├── test_fundamentals/         # Tests für Grundlagen
│   └── test_sorting/              # Tests für Sortieralgorithmen
├── docs/                          # Dokumentation (AsciiDoc)
│   ├── api/                       # API-Dokumentation
│   └── tutorials/                 # Tutorials und Anleitungen
├── benchmarks/                    # Performance-Benchmarks
├── data/                          # Testdaten
│   ├── small/                     # Kleine Testdaten
│   ├── medium/                    # Mittlere Datensätze
│   └── large/                     # Grosse Datensätze
├── notebooks/                     # Jupyter Notebooks
│   └── pva1/                      # Praktische Vertiefungsaufgaben
├── pyproject.toml                 # Projektkonfiguration
├── README.md                      # Diese Datei
└── CLAUDE.md                      # Entwicklungsrichtlinien
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

Die Implementierungen folgen den Lehrbuchkonzepten aus "Algorithms, 4th Edition" und sind für Lernzwecke optimiert:

- Deutsche Dokumentation und Kommentare
- Schritt-für-Schritt Erklärungen
- Multiple Implementierungsvarianten für Vergleiche
- Comprehensive AsciiDoc-Dokumentation

## Beitragen

Dieses Projekt folgt akademischen Standards:

1. **Code-Stil**: Befolgen Sie die bestehenden Konventionen
2. **Dokumentation**: Alle neuen Features müssen dokumentiert werden
3. **Tests**: Neue Implementierungen benötigen umfassende Tests
4. **Type Hints**: Vollständige Typisierung ist erforderlich

### Commit-Nachrichten

Verwenden Sie konventionelle Commit-Nachrichten:

```text
feat: Neue Funktionalität hinzufügen
fix: Fehler beheben
docs: Dokumentation aktualisieren
test: Tests hinzufügen oder ändern
refactor: Code umstrukturieren
```

## Lizenz und Kontakt

### Autor
**Daniel Senften**
Email: daniel.senften@ffhs.ch

### Akademischer Kontext
Fernfachhochschule Schweiz (FFHS)
Studiengang: Informatik
Modul: Datenstrukturen und Algorithmen

### Basierend auf
"Algorithms, 4th Edition" von Robert Sedgewick und Kevin Wayne
Princeton University

## Weiterführende Ressourcen

### Externe Links
* https://algs4.cs.princeton.edu/[Algorithms 4th Edition Website]
* https://docs.python.org/3/[Python 3 Dokumentation]
* https://pytest.org/[pytest Dokumentation]

### Interne Verweise
* **Komplexitätsanalyse**: Detaillierte Performance-Analyse
* **Getting Started**: Ausführliche Einführung
* **API-Dokumentation**: Vollständige Referenz aller Module

---

_Diese Dokumentation wird kontinuierlich aktualisiert und erweitert._
