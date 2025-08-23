# FFHS-DUA Algorithmen und Datenstrukturen

Eine Python-Implementierung grundlegender Datenstrukturen basierend auf dem Lehrbuch "Algorithms, 4th Edition" von Robert Sedgewick und Kevin Wayne, angepasst für den akademischen Gebrauch an der Fernfachhochschule Schweiz (FFHS) im Studiengang Data and Analytics (DUA).

## Projektübersicht

Dieses Projekt implementiert die wichtigsten Datenstrukturen aus dem ersten Teil des Algorithms-Lehrbuchs in Python. Alle Implementierungen folgen den Prinzipien des Buches, sind aber an die Python-Sprache und moderne Programmierkonzepte angepasst.

### Implementierte Datenstrukturen

#### Fundamentals (Grundlagen)

- **Stack (Stapel)**: Drei verschiedene Implementierungen
  - `Stack`: Verkettete Liste mit dynamischer Größe
  - `FixedCapacityStack`: Festes Array mit vorgegebener Kapazität
  - `ResizingArrayStack`: Dynamisches Array mit automatischer Größenanpassung
- **Queue (Warteschlange)**: FIFO-Datenstruktur
- **Bag (Sammlung)**: Ungeordnete Sammlung von Elementen

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

### Installation

```bash
# Repository klonen
git clone <repository-url>
cd ffhs-dua

# Abhängigkeiten installieren (mit uv)
uv sync

# Oder mit pip
pip install -e .
```

## Entwicklung

### Tests ausführen

```bash
# Alle Tests
pytest tests/

# Spezifische Testdatei
pytest tests/test_stack.py

# Spezifische Testklasse
pytest tests/test_stack.py::TestStack

# Mit Ausgabe der Testergebnisse
pytest tests/ -v
```

### Code-Qualität

#### Linting und Formatierung

```bash
# Code formatieren
ruff format

# Linting überprüfen
ruff check

# Automatische Fehlerbehebung
ruff check --fix
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
from algs4.fundamentals.stack import Stack

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
from algs4.fundamentals.queue import Queue

# Neue Queue erstellen
queue = Queue[str]()

# Elemente hinzufügen
queue.enqueue("Erstes")
queue.enqueue("Zweites")
queue.enqueue("Drittes")

# Element aus der Queue nehmen (FIFO)
first_element = queue.dequeue()  # Gibt "Erstes" zurück
```

### Beispiel: Sierpinski-Dreieck verwenden

```python
from pva1.sierpinski import sierpinski, zeichne_sierpinski_progression

# Einzelnes Sierpinski-Dreieck zeichnen
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
sierpinski(0, 0, 3, max_iterations=5)
plt.axis('equal')
plt.show()

# Progression der ersten 5 Iterationen
zeichne_sierpinski_progression()
```

## Projektstruktur

```text
ffhs-dua/
├── algs4/                     # Hauptpaket
│   ├── __init__.py
│   ├── fundamentals/          # Grundlegende Datenstrukturen
│   │   ├── __init__.py
│   │   ├── stack.py          # Stack-Implementierungen
│   │   ├── queue.py          # Queue-Implementierungen
│   │   └── bag.py            # Bag-Implementierung
│   └── errors/               # Benutzerdefinierte Exceptions
│       ├── __init__.py
│       └── errors.py
├── pva1/                     # Praktische Vertiefungsaufgaben 1
│   ├── __init__.py
│   ├── sierpinski.py         # Sierpinski-Dreieck Implementation
│   ├── sierpinski.adoc       # Sierpinski-Dokumentation
│   └── grundlagen.ipynb      # Grundlagen-Jupyter-Notebook
├── tests/                    # Testsuiten
│   ├── __init__.py
│   ├── test_stack.py
│   ├── test_queue.py
│   └── test_bag.py
├── docs/                     # Dokumentation
│   ├── test_stack_documentation.adoc
│   ├── test_queue_documentation.adoc
│   └── test_bag_documentation.adoc
├── pyproject.toml           # Projektkonfiguration
├── uv.lock                  # Dependency-Lock-Datei
├── README.md                # Diese Datei
└── CLAUDE.md               # Entwicklungsrichtlinien
```

## Besonderheiten

### Deutsche Dokumentation

Alle Docstrings, Kommentare und Fehlermeldungen sind auf Deutsch verfasst, um dem akademischen Kontext der FFHS zu entsprechen.

### Typsicherheit

Das Projekt macht extensiven Gebrauch von Python's Type-Hints und generischen Typen für maximale Typsicherheit.

### Akademischer Fokus

Die Implementierungen folgen den Lehrbuchkonzepten und sind für Lernzwecke optimiert, nicht unbedingt für Produktionsumgebungen.

### Multiple Implementierungen

Jede Datenstruktur wird in mehreren Varianten implementiert, um verschiedene Algorithmuskonzepte zu demonstrieren (verkettete Listen vs. Arrays, feste vs. dynamische Größe).

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