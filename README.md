# FFHS-DUA: Algorithmen und Datenstrukturen

Eine umfassende Python-Implementierung grundlegender Algorithmen und
Datenstrukturen für den akademischen Gebrauch an der
Fernfachhochschule Schweiz (FFHS).

## ✨ Features

- **PVA 1 - Fundamentals**: Stack, Queue, Bag, Union-Find (4 Implementierungsvarianten)
- **PVA 2 - Sorting**: Quick Sort, Merge Sort, Heap Sort, Shell Sort (mit CLI-Interface)
- **PVA 3 - Searching**: Binary Search Tree (BST), AVL Tree, Red-Black BST (selbstbalancierend), Hash Tables
- **PVA 4 - Graphs**:
  - Gerichtete Graphen: Dijkstras Algorithmus, Gewichtete Digraphen, Zyklenerkennung
  - Ungerichtete Graphen: Gewichtete Graphen, Kanten-Verwaltung
  - Utilities: Indexed Min Priority Queue
- **PVA 5 - Strings**: Trie Symbol Table, Patricia-Trie (Pfadkompression), KMP String-Suche (Knuth-Morris-Pratt), Präfix-Operationen
- **Utils**: Timing-Utilities für Performance-Messungen (`@timeit` Dekorator)
- **Umfassende Tests**: Vollständige Test-Abdeckung mit pytest (625 Tests)
- **Deutsche Dokumentation**: AsciiDoc-basierte Dokumentation und Jupyter Notebooks

## 📦 Installation

### Voraussetzungen

- Python >=3.13.1
- uv (empfohlen) oder pip

### Mit uv (empfohlen)

```bash
# Repository klonen
git clone https://gitlab.com/talent-factory/ffhs/dua.git
cd ffhs-dua

# Abhängigkeiten installieren
uv sync

# Virtuelle Umgebung aktivieren
source .venv/bin/activate
```

### Mit pip

```bash
git clone https://gitlab.com/talent-factory/ffhs/dua.git
cd ffhs-dua

pip install -e .
```

## 🚀 Schnellstart

```bash
# Tests ausführen
python3 -m pytest tests/ -v

# Coverage-Report generieren
python3 scripts/generate_coverage.py --html

# Sortieralgorithmus ausprobieren
cat data/sorting/tiny.txt | python3 -m src.algs4.pva_2_sorting.quick

# Benchmarks ausführen
python3 -m benchmarks.sorting_benchmarks
```

## 💻 Verwendung

### Stack

```python
from src.algs4.pva_1_fundamentals import Stack

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # 2
```

### Sortieralgorithmen

```python
from src.algs4.pva_2_sorting import Quick, Merge, Heap, Shell

data = [3, 1, 4, 1, 5, 9, 2, 6]
Quick.sort(data)
print(data)  # [1, 1, 2, 3, 4, 5, 6, 9]
```

### Suchbäume

```python
from src.algs4.pva_3_searching import BST

bst = BST()
bst.put("A", 1)
bst.put("B", 2)
print(bst.get("A"))  # 1
```

### Graphen-Algorithmen

```python
from src.algs4.pva_4_graphs import EdgeWeightedDigraph, DijkstraSP, DirectedEdge

# Erstelle einen gewichteten Digraph
g = EdgeWeightedDigraph(8)
g.add_edge(DirectedEdge(0, 2, 0.26))
g.add_edge(DirectedEdge(0, 4, 0.38))
g.add_edge(DirectedEdge(2, 7, 0.34))

# Berechne kürzeste Pfade von Knoten 0
sp = DijkstraSP(g, 0)

# Überprüfe ob Pfad zu Knoten 7 existiert
if sp.has_path_to(7):
    print(f"Distanz: {sp.distTo[7]}")  # 0.6
    for edge in sp.path_to(7):
        print(edge)
```

### String-Algorithmen

#### Trie Symbol Table

```python
from src.algs4.pva_5_strings import TrieST

# Erstelle einen Trie Symbol Table
st = TrieST()
st.put("sea", 1)
st.put("sells", 2)
st.put("she", 3)
st.put("shells", 4)
st.put("shore", 5)

# Suche nach Schlüssel
print(st.get("sea"))  # 1

# Präfix-Suche
print(list(st.keys_with_prefix("sh")))  # ['she', 'shells', 'shore']

# Wildcard-Suche (. = beliebiges Zeichen)
print(list(st.keys_that_match(".he")))  # ['she']

# Längster Präfix
print(st.longest_prefix_of("shellsort"))  # 'shells'
```

#### KMP String-Suche (Knuth-Morris-Pratt)

```python
from src.algs4.pva_5_strings import KMP

# Erstelle KMP-Instanz mit Muster
kmp = KMP("NEEDLE")

# Suche Muster im Text
text = "HAYSTACK WITH NEEDLE IN IT"
position = kmp.search(text)
print(position)  # 14

# Finde alle Vorkommen
kmp_ab = KMP("ab")
for pos in kmp_ab.search_all("ababab"):
    print(pos)  # 0, 2, 4

# Zähle Vorkommen
kmp_the = KMP("the")
count = kmp_the.count("the quick brown fox jumps over the lazy dog")
print(count)  # 2

# CLI-Nutzung
# python3 -m src.algs4.pva_5_strings.kmp abracadabra "abacadabrabracabracadabra"
```

## 📖 Dokumentation

- 📚 **[Vollständige Dokumentation](docs/index.adoc)** - Umfassende Projektdokumentation
- 🎓 **[Erste Schritte](docs/tutorials/getting_started.adoc)** - Tutorial für Einsteiger
- ⚙️ **[Entwicklungsrichtlinien](CLAUDE.md)** - Für Entwickler und Beiträge

## 📚 Referenzen

Diese Implementierung basiert auf zwei Hauptquellen:

### Primäre Referenzen

- 📖 **[Algorithms, 4th Edition](https://algs4.cs.princeton.edu/)** - Robert Sedgewick & Kevin Wayne
  - Offizielles Lehrbuch und Java-Implementierung
  - Grundlage für die Algorithmen-Implementierungen

- 📘 **[Praktische Algorithmik mit Python](https://www.tobiashaeberlein.net/)** - Tobias Häberlein
  - Oldenbourg Verlag München, 2012
  - Verwendet im FFHS Moodle-Kurs und PVA-Übungen
  - Fokus auf praktische Python-Implementierungen

### Weitere Ressourcen

- 🐍 **[algs4-py (Xiao Kui)](https://github.com/shellfly/algs4-py)** - Python-Portierung
- 🎯 **[itu.algs4 (ITU Copenhagen)](https://github.com/itu-algorithms/itu.algs4)** - Alternative Python-Implementierung

## 🧪 Tests und Qualität

```bash
# Alle Tests ausführen
python3 -m pytest tests/ -v

# Tests mit Coverage
python3 -m pytest tests/ --cov=src.algs4 --cov-report=html

# Code-Qualität überprüfen
ruff check src/ tests/
mypy src/algs4

# Pre-Commit Hooks
pre-commit run --all-files
```

**Aktuelle Metriken:**

- ✅ 563 Tests (100% bestanden)
- ✅ 93%+ Code-Coverage (Trie: 99.22%)
- ✅ 0 Linting-Fehler
- ✅ 0 Type-Fehler
- ✅ 5 PVA-Module (Fundamentals, Sorting, Searching, Graphs, Strings)

## 📊 Projekt-Struktur

```text
ffhs-dua/
├── src/algs4/
│   ├── pva_1_fundamentals/    # Stack, Queue, Bag, Union-Find
│   ├── pva_2_sorting/         # Sortieralgorithmen
│   ├── pva_3_searching/       # Suchbäume und Hash Tables
│   ├── pva_4_graphs/          # Graphen-Algorithmen (Dijkstra, etc.)
│   ├── pva_5_strings/         # String-Algorithmen (Trie, Patricia-Trie)
│   ├── errors/                # Exception-Klassen
│   └── utils/                 # Utility-Funktionen
├── tests/
│   ├── test_fundamentals/     # Tests für PVA 1
│   ├── test_sorting/          # Tests für PVA 2
│   ├── test_searching/        # Tests für PVA 3
│   ├── test_graphs/           # Tests für PVA 4
│   └── test_strings/          # Tests für PVA 5
├── docs/                      # Dokumentation
│   └── summaries/             # Zusammenfassungen (Tries, etc.)
├── scripts/                   # Hilfsskripte
├── benchmarks/                # Performance-Benchmarks
└── .github/workflows/         # CI/CD Pipelines
```

## 🔗 Links

- 📚 **[Dokumentation](docs/index.adoc)** - Vollständige Projektdokumentation
- 🧪 **[Coverage-Reports](docs/coverage.md)** - Code-Coverage-Dokumentation
- ⚙️ **[CI/CD](docs/ci-cd.md)** - GitHub Actions Workflows
- 📦 **[Benchmarks](docs/benchmarks.md)** - Performance-Messungen
- 🛠️ **[Entwicklung](CLAUDE.md)** - Entwicklungsrichtlinien

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe [LICENSE](LICENSE) für Details.

## 👤 Autor

**Daniel Senften** - [daniel.senften@ffhs.ch](mailto:daniel.senften@ffhs.ch)

Fernfachhochschule Schweiz (FFHS)

## 🙏 Danksagungen

Dieses Projekt basiert auf zwei Hauptquellen:

1. **"Algorithms, 4th Edition"** von Robert Sedgewick und Kevin Wayne - Das
   Standardwerk für Algorithmen und Datenstrukturen
2. **"Praktische Algorithmik mit Python"** von Tobias Häberlein - Besonders
   wertvoll für die praktische Python-Implementierung und Integration in den
   FFHS Moodle-Kurs

Das Projekt wurde speziell für den akademischen Gebrauch an der
Fernfachhochschule Schweiz (FFHS) angepasst und integriert die Inhalte aus
beiden Lehrbüchern in einem kohärenten Python-Framework.
