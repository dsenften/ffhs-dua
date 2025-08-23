# CLAUDE.md

Diese Datei bietet Anleitungen für Claude Code (claude.ai/code) beim Arbeiten mit Code in diesem Repository.

## Projektübersicht

Dies ist eine Python-Implementierung grundlegender Datenstrukturen aus dem Lehrbuch "Algorithms, 4th Edition" (algs4), angepasst für den akademischen Gebrauch an der FFHS-DUA. Das Projekt enthält deutsche Dokumentation und umfassende Testsuiten.

## Entwicklungsbefehle

### Testen

- Alle Tests ausführen: `pytest tests/`
- Spezifische Testdatei ausführen: `pytest tests/test_stack.py`
- Spezifische Testklasse ausführen: `pytest tests/test_stack.py::TestStack`
- Spezifische Testmethode ausführen: `pytest tests/test_stack.py::TestStack::test_push_pop`

### Linting und Formatierung

- Code formatieren: `ruff format`
- Linting überprüfen: `ruff check`
- Linting-Probleme automatisch beheben: `ruff check --fix`

### Jupyter Notebooks

- Jupyter starten: `jupyter notebook` oder `jupyter lab`

## Architektur

### Projektstruktur

```text
algs4/
├── __init__.py
├── fundamentals/          # Grundlegende Datenstrukturen
│   ├── stack.py          # Stack-Implementierungen (3 Varianten)
│   ├── queue.py          # Queue-Implementierungen
│   └── bag.py            # Bag-Datenstruktur
└── errors/               # Benutzerdefinierte Fehlerklassen
    └── errors.py
pva1/                     # Praktische Vertiefungsaufgaben 1
├── __init__.py
├── sierpinski.py         # Sierpinski-Dreieck Fraktal-Implementierungen
├── sierpinski.adoc       # Sierpinski-Dokumentation
└── grundlagen.ipynb      # Grundlagen-Jupyter-Notebook
```

### Implementierungsmuster

#### Datenstruktur-Klassen

Jede grundlegende Datenstruktur folgt diesem Muster:

- Mehrere Implementierungsvarianten (z.B. verkettete Liste, festes Array, größenveränderliches Array)
- Generische Typisierung mit `TypeVar("T")`
- Deutsche Docstrings nach akademischen Konventionen
- Standardmethoden: `is_empty()`, `size()`, `__len__()`, `__iter__()`, `__repr__()`
- LIFO/FIFO-Verhalten je nach Bedarf

#### Stack-Implementierungen

1. **Stack**: Verkettete Liste-Implementierung mit dynamischer Größe
2. **FixedCapacityStack**: Feste Array-Größe-Implementierung
3. **ResizingArrayStack**: Dynamisches Array mit automatischer Größenanpassung

#### Fehlerbehandlung

- Benutzerdefinierte Exceptions in `algs4.errors.errors`
- Deutsche Fehlermeldungen (z.B. "Stack-Unterlauf")
- Ordnungsgemäße Type-Assertions für Sicherheit

#### Teststrategie

- Umfassende Testabdeckung für alle Implementierungen
- Deutsche Testmethodennamen und Docstrings
- Tests für Grenzfälle (leere Strukturen, Kapazitätsgrenzen)
- Typsicherheitstests mit verschiedenen generischen Typen
- Iterator- und String-Repräsentationstests

### Code-Konventionen

- Deutsche Dokumentation und Kommentare
- Type-Hints für alle öffentlichen Methoden
- Defensive Programmierung mit Assertions
- Konsistente Fehlerbehandlungsmuster
- Generische Typunterstützung durchgehend

## Abhängigkeiten

- Python >=3.13.1
- pytest für Tests
- ruff für Linting/Formatierung
- jupyter für Notebook-Entwicklung

## Testphilosophie

Tests sind auf Deutsch geschrieben und folgen akademischen Mustern. Jede Datenstruktur hat umfassende Testabdeckung einschließlich Grenzfälle, Typsicherheit und Verhaltenskorrektheit. Die Teststruktur spiegelt die Klassenhierarchie mit separaten Testklassen für jede Implementierungsvariante wider.