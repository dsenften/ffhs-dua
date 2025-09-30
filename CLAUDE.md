# CLAUDE.md

Diese Datei enthält spezifische Richtlinien für die Arbeit mit Claude AI an diesem Projekt.

## Projektübersicht

Dies ist eine umfassende Python-Implementierung grundlegender Algorithmen und Datenstrukturen.
Das Projekt enthält deutsche Dokumentation und umfassende Testsuiten.

## Entwicklungsbefehle

### Testen

- Alle Tests ausführen: `python3 -m pytest tests/ -v`
- Spezifische Testdatei ausführen: `python3 -m pytest tests/test_fundamentals/test_stack.py`
- Spezifische Testklasse ausführen: `python3 -m pytest tests/test_fundamentals/test_stack.py::TestStack`
- Spezifische Testmethode ausführen: `python3 -m pytest tests/test_fundamentals/test_stack.py::TestStack::test_push_pop`
- Tests mit Coverage: `python3 -m pytest tests/ --cov=src.algs4 --cov-report=html`

### Linting und Formatierung

- Code formatieren: `ruff format`
- Linting überprüfen: `ruff check`
- Linting-Probleme automatisch beheben: `ruff check --fix`

### Jupyter Notebooks

- Jupyter starten: `jupyter notebook` oder `jupyter lab`

## Architektur

### Projektstruktur

```text
ffhs-dua/
├── src/
│   └── algs4/
│       ├── fundamentals/          # Grundlegende Datenstrukturen
│       │   ├── stack.py           # Stack-Implementierungen (3 Varianten)
│       │   ├── queue.py           # Queue-Implementierung
│       │   ├── bag.py             # Bag-Datenstruktur
│       │   └── uf.py              # Union-Find-Implementierungen (4 Varianten)
│       ├── sorting/               # Sortieralgorithmen
│       │   ├── quick.py           # Quick Sort
│       │   ├── shell.py           # Shell Sort
│       │   ├── heap.py            # Heap Sort
│       │   └── merge.py           # Merge Sort
│       └── errors/                # Benutzerdefinierte Fehlerklassen
│           └── errors.py
├── tests/                         # Umfassende Test-Suite
│   ├── test_fundamentals/         # Tests für Grundlagen
│   └── test_sorting/              # Tests für Sortieralgorithmen
├── docs/                          # AsciiDoc-Dokumentation
├── notebooks/                     # Jupyter Notebooks
│   └── pva1/                      # Praktische Vertiefungsaufgaben 1
│       ├── sierpinski.py          # Sierpinski-Dreieck Implementierung
│       ├── sierpinski.adoc        # Sierpinski-Dokumentation
│       └── grundlagen.ipynb       # Grundlagen-Notebook
├── benchmarks/                    # Performance-Benchmarks
│   └── sorting_benchmarks.py      # Sortieralgorithmus-Benchmarks
├── src/
│   ├── algs4/                     # Hauptalgorithmus-Package
│   └── utils/                     # Wiederverwendbare Hilfsfunktionen
│       ├── timing.py              # Timing-Utilities und @timeit Dekorator
│       └── README.md              # Utils-Dokumentation
└── data/                          # Testdaten (thematisch organisiert)
    ├── fundamentals/              # Union-Find, Stacks, Queues, Priority Queues
    ├── sorting/                   # Sortieralgorithmen und Integer-Arrays
    ├── graphs/                    # Graph-Algorithmen
    ├── strings/                   # String-Algorithmen, Texte
    ├── compression/               # Binäre Dateien und Kompression
    ├── small/                     # Kleine Testdaten (< 100KB)
    ├── medium/                    # Mittlere Datensätze (100KB - 10MB)
    ├── large/                     # Grosse Datensätze (> 10MB)
    └── misc/                      # CSV-Dateien und sonstige Daten
```

### Implementierungsmuster

#### Datenstruktur-Klassen

Jede grundlegende Datenstruktur folgt diesem Muster:

- Mehrere Implementierungsvarianten (z.B. verkettete Liste, festes Array, grössenveränderliches Array)
- Generische Typisierung mit `TypeVar("T")`
- Deutsche Docstrings nach akademischen Konventionen
- Standardmethoden: `is_empty()`, `size()`, `__len__()`, `__iter__()`, `__repr__()`
- LIFO/FIFO-Verhalten je nach Bedarf

#### Stack-Implementierungen

1. **Stack**: Verkettete Liste-Implementierung mit dynamischer Grösse
2. **FixedCapacityStack**: Feste Array-Grösse-Implementierung
3. **ResizingArrayStack**: Dynamisches Array mit automatischer Grössenanpassung

#### Union-Find-Implementierungen

1. **UF**: Optimierte Version mit Weighted Quick Union by Rank und Path Compression (O(α(n)))
2. **QuickUnionUF**: Einfache Quick Union Implementation (O(n) worst case)
3. **WeightedQuickUnionUF**: Weighted Quick Union by Size (O(log n))
4. **QuickFindUF**: Quick Find Implementation mit konstanter Find-Zeit (O(1) find, O(n) union)

#### Sortieralgorithmen

1. **Quick**: Quick Sort mit Hoare-Partitionierung
2. **Shell**: Shell Sort mit Knuth-Sequenz
3. **Heap**: Heap Sort mit garantierter O(n log n) Performance
4. **Merge**: Merge Sort mit stabiler Sortierung

#### Fehlerbehandlung

- Benutzerdefinierte Exceptions in `src.algs4.errors.errors`
- Deutsche Fehlermeldungen (z.B. "Stack-Unterlauf")
- Ordnungsgemässe Type-Assertions für Sicherheit

#### Teststrategie

- Umfassende Testabdeckung für alle Implementierungen
- Deutsche Testmethodennamen und Docstrings
- Tests für Grenzfälle (leere Strukturen, Kapazitätsgrenzen)
- Typsicherheitstests mit verschiedenen generischen Typen
- Iterator- und String-Repräsentationstests
- Separate Tests für Fundamentals und Sorting Module

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

Tests sind auf Deutsch geschrieben und folgen akademischen Mustern. Jede Datenstruktur hat umfassende Testabdeckung
einschliesslich Grenzfälle, Typsicherheit und Verhaltenskorrektheit. Die Teststruktur spiegelt die Klassenhierarchie
mit separaten Testklassen für jede Implementierungsvariante wider.
