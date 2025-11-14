# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projektübersicht

Umfassende Python-Implementierung grundlegender Algorithmen und Datenstrukturen
für den akademischen Gebrauch an der Fernfachhochschule Schweiz (FFHS).
Das Projekt enthält deutsche Dokumentation, umfassende Testsuiten und ist nach
praktischen Vertiefungsaufgaben (PVA) strukturiert.

## Entwicklungsbefehle

### Package Management

Dieses Projekt verwendet `uv` als Package Manager:

- Abhängigkeiten installieren: `uv sync`
- Virtuelle Umgebung aktivieren: `source .venv/bin/activate` (wird von uv automatisch erstellt)

### Testen

- Alle Tests ausführen: `python3 -m pytest tests/ -v`
- Spezifische Testdatei: `python3 -m pytest tests/test_fundamentals/test_stack.py`
- Spezifische Testklasse: `python3 -m pytest tests/test_fundamentals/test_stack.py::TestStack`
- Spezifische Testmethode: `python3 -m pytest tests/test_fundamentals/test_stack.py::TestStack::test_push_pop`
- Tests mit Coverage: `python3 -m pytest tests/ --cov=src.algs4 --cov-report=html`
- Langsame Tests überspringen: `python3 -m pytest tests/ -v -m "not slow"`

### Linting und Formatierung

- Code formatieren: `ruff format`
- Linting überprüfen: `ruff check`
- Linting-Probleme automatisch beheben: `ruff check --fix`

### CLI-Nutzung

Sortieralgorithmen können direkt von der Kommandozeile ausgeführt werden:

```bash
# Quick Sort mit Daten aus stdin
cat data/sorting/tiny.txt | python3 -m src.algs4.pva_2_sorting.quick

# Mit --quiet Flag nur Zeitmessung anzeigen
cat data/sorting/1Kints.txt | python3 -m src.algs4.pva_2_sorting.quick --quiet
```

### Jupyter Notebooks

- Jupyter starten: `jupyter notebook` oder `jupyter lab`
- Notebooks befinden sich in `notebooks/pva1/` für Praktische Vertiefungsaufgaben 1

## Architektur

### Projektstruktur nach PVA-Modulen

```text
src/algs4/
├── pva_1_fundamentals/          # Praktische Vertiefungsaufgaben 1
│   ├── stack.py                 # Stack (3 Varianten: LinkedList, Fixed, Resizing)
│   ├── queue.py                 # Queue (LinkedList-basiert)
│   ├── bag.py                   # Bag (ungeordnete Sammlung)
│   └── uf.py                    # Union-Find (4 Varianten)
├── pva_2_sorting/               # Praktische Vertiefungsaufgaben 2
│   ├── quick.py                 # Quick Sort mit CLI
│   ├── merge.py                 # Merge Sort (stabil)
│   ├── heap.py                  # Heap Sort
│   └── shell.py                 # Shell Sort
├── pva_3_searching/             # Praktische Vertiefungsaufgaben 3
│   ├── bst.py                   # Binary Search Tree (BST)
│   ├── avl.py                   # AVL Tree (selbstbalancierend)
│   ├── red_black_bst.py         # Red-Black BST (links-lastiger Rot-Schwarz-Baum)
│   └── hashing.py               # Hash Tables
├── pva_4_graphs/                # Praktische Vertiefungsaufgaben 4
│   ├── directed_edge.py          # Gerichtete Kante mit Gewicht
│   ├── edge_weighted_digraph.py  # Gewichteter gerichteter Graph
│   ├── index_min_pq.py           # Indexed Min Priority Queue
│   └── dijkstra_sp.py            # Dijkstras Algorithmus
├── errors/
│   └── errors.py                # Benutzerdefinierte Exceptions
└── utils/
    └── timing.py                # Timing-Utilities

src/utils/
├── timing.py                    # @timeit Dekorator und Timing-Funktionen
└── README.md                    # Utils-Dokumentation

tests/
├── test_fundamentals/           # Tests für PVA-1
├── test_sorting/                # Tests für PVA-2
├── test_searching/              # Tests für PVA-3
├── test_graphs/                 # Tests für PVA-4
└── test_utils/                  # Tests für Utility-Module

data/                            # Thematisch organisierte Testdaten
├── fundamentals/                # Union-Find, Stacks, Queues
├── sorting/                     # Sortieralgorithmen (tiny.txt, 1Kints.txt, etc.)
├── graphs/                      # Graph-Algorithmen
├── strings/                     # String-Algorithmen, Texte
├── compression/                 # Binäre Dateien
├── small/                       # < 100KB
├── medium/                      # 100KB - 10MB
└── large/                       # > 10MB
```

### Implementierungsmuster

#### Datenstruktur-Klassen

Jede grundlegende Datenstruktur folgt diesem Muster:

- Mehrere Implementierungsvarianten zur Demonstration unterschiedlicher Trade-offs
- Generische Typisierung mit `TypeVar("T")`
- Deutsche Docstrings nach akademischen Konventionen
- Standardmethoden: `is_empty()`, `size()`, `__len__()`, `__iter__()`, `__repr__()`
- LIFO/FIFO-Verhalten je nach Datenstruktur

#### Stack-Implementierungen (pva_1_fundamentals/stack.py)

1. **Stack**: Verkettete Liste mit dynamischer Grösse (O(1) push/pop)
2. **FixedCapacityStack**: Feste Array-Grösse
3. **ResizingArrayStack**: Dynamisches Array mit amortisiert O(1) push/pop

#### Union-Find-Implementierungen (pva_1_fundamentals/uf.py)

1. **UF**: Optimierte Version mit Weighted Quick Union by Rank und Path Compression (O(α(n)))
2. **QuickUnionUF**: Einfache Quick Union (O(n) worst case)
3. **WeightedQuickUnionUF**: Weighted Quick Union by Size (O(log n))
4. **QuickFindUF**: Quick Find mit O(1) find, aber O(n) union

#### Sortieralgorithmen (pva_2_sorting/)

Alle Sortieralgorithmen haben:

- CLI-Interface mit `--quiet` Flag für Performance-Tests
- `sort(arr)` Klassenmethode für öffentliche API
- `is_sorted(arr)` zur Verifikation
- Zeitmessung mit `time.perf_counter()`

1. **Quick**: Hoare-Partitionierung, O(n log n) durchschnittlich
2. **Shell**: Knuth-Sequenz, O(n^(3/2)) worst case
3. **Heap**: Garantierte O(n log n) Performance
4. **Merge**: Stabile Sortierung, O(n log n) garantiert

#### Suchalgorithmen (pva_3_searching/)

Alle Symbol-Table-Implementierungen haben:

- Generische Typisierung mit `TypeVar` für Schlüssel und Werte
- Geordnete Operationen (min, max, floor, ceiling, rank, select)
- Iteration in sortierter Reihenfolge
- Deutsche Fehlerbehandlung

1. **BST**: Binary Search Tree (unbalanciert)
   - put, get, delete: O(log n) durchschnittlich, O(n) worst case
   - min, max, floor, ceiling, rank, select: O(log n) durchschnittlich
   - Hibbard Deletion für Knoten mit zwei Kindern
   - Level-Order und In-Order Traversierung
   - Visuelle Baumdarstellung mit `__str__()`

2. **AVL**: AVL Tree (selbstbalancierend)
   - put, get, delete: **O(log n) garantiert** (auch worst case!)
   - Automatische Balancierung durch Rotationen
   - Balance-Faktor wird für jeden Knoten gespeichert
   - Vier Rotations-Arten: Left, Right, Left-Right, Right-Left
   - Maximale Höhe: 1.44 * log₂(n + 2) (Fibonacci-Bäume)
   - Visuelle Darstellung zeigt Knotenhöhen: `A (h:2)`

3. **RedBlackBST**: Left-Leaning Red-Black BST (selbstbalancierend)
   - put, get, delete: **O(log n) garantiert** (auch worst case!)
   - Basiert auf 2-3 Bäumen (perfekte schwarze Balance)
   - Rot-Schwarz-Invarianten: Rote Kanten immer links, keine aufeinanderfolgenden roten Kanten
   - Drei Operationen: Linksrotation, Rechtsrotation, Farbwechsel
   - Maximale Höhe: 2 * log₂(n + 1) (doppelt so hoch wie perfekt balanciert)
   - Einfachere Implementierung als Standard Red-Black Trees
   - Visuelle Darstellung zeigt Knotenfarben: `A (R)` oder `A (B)`

#### Fehlerbehandlung

- Benutzerdefinierte Exceptions in `src.algs4.errors.errors`
- Deutsche Fehlermeldungen (z.B. "Stack-Unterlauf", "Index ist nicht zwischen 0 und n-1")
- Defensive Programmierung mit `assert` für Type-Safety
- Validierungsmethoden (z.B. `_validate(p)` in Union-Find)

#### Timing-Utilities (src/utils/timing.py)

```python
from src.utils.timing import timeit, enable_timing, measure_execution_time

# Dekorator-basierte Zeitmessung
enable_timing()  # Global aktivieren

@timeit
def my_algorithm():
    pass

# Einmalige Zeitmessung
result, exec_time = measure_execution_time(lambda: sorted([3, 1, 4, 2]))
```

### Code-Konventionen

- **Sprache**: Deutsche Dokumentation, Kommentare und Variablennamen
- **Type-Hints**: Für alle öffentlichen Methoden erforderlich
- **Docstrings**: Google-Style auf Deutsch mit Args/Returns/Raises
- **Defensive Programmierung**: Assertions für interne Invarianten
- **Generics**: `TypeVar("T")` für typensichere Container
- **Klassenmethoden**: `@classmethod` für stateless Algorithmen (z.B. Sort)

### Teststrategie

- **Namenskonventionen**: Deutsche Testmethodennamen (z.B. `test_push_pop`)
- **Testabdeckung**: Grenzfälle (leere Strukturen, volle Kapazität, einzelnes Element)
- **Typsicherheit**: Tests mit verschiedenen generischen Typen (int, str, float)
- **Assertions**: `assert` für erwartetes Verhalten, `pytest.raises` für Exceptions
- **Struktur**: Eine Testklasse pro Implementierungsvariante
- **Markers**: `@pytest.mark.slow` für Performance-Tests

## Abhängigkeiten

- Python >=3.13.1
- pytest für Tests (mit Coverage-Plugin)
- ruff für Linting/Formatierung
- jupyter für Notebook-Entwicklung
- matplotlib für Visualisierungen

Package Management erfolgt über `uv` (siehe pyproject.toml).
