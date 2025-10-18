# FFHS-DUA: Algorithmen und Datenstrukturen

Eine umfassende Python-Implementierung grundlegender Algorithmen und
Datenstrukturen für den akademischen Gebrauch an der
Fernfachhochschule Schweiz (FFHS).

## ✨ Features

- **Fundamentals**: Stack, Queue, Bag, Union-Find (4 Implementierungsvarianten)
- **Sorting**: Quick Sort, Merge Sort, Heap Sort, Shell Sort (mit CLI-Interface)
- **Searching**: Binary Search Tree (BST), AVL Tree, Red-Black BST (selbstbalancierend)
- **Utils**: Timing-Utilities für Performance-Messungen (`@timeit` Dekorator)
- **Umfassende Tests**: Vollständige Test-Abdeckung mit pytest (362 Tests)
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

## 📖 Dokumentation

- 📚 **[Vollständige Dokumentation](docs/index.adoc)** - Umfassende Projektdokumentation
- 🎓 **[Erste Schritte](docs/tutorials/getting_started.adoc)** - Tutorial für Einsteiger
- ⚙️ **[Entwicklungsrichtlinien](CLAUDE.md)** - Für Entwickler und Beiträge

## 📚 Referenzen

Diese Implementierung basiert auf dem Lehrbuch "Algorithms, 4th Edition" von Robert Sedgewick und Kevin Wayne:

- 📖 **[Algorithms, 4th Edition](https://algs4.cs.princeton.edu/)** - Offizielles Lehrbuch und Java-Implementierung
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
- ✅ 362 Tests (100% bestanden)
- ✅ 93.08% Code-Coverage
- ✅ 0 Linting-Fehler
- ✅ 0 Type-Fehler

## 📊 Projekt-Struktur

```
ffhs-dua/
├── src/algs4/
│   ├── pva_1_fundamentals/    # Stack, Queue, Bag, Union-Find
│   ├── pva_2_sorting/         # Sortieralgorithmen
│   ├── pva_3_searching/       # Suchbäume und Hash Tables
│   └── errors/                # Exception-Klassen
├── tests/                     # Umfassende Test-Suite
├── docs/                      # Dokumentation
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

Dieses Projekt basiert auf dem Lehrbuch "Algorithms, 4th Edition" von Robert Sedgewick und Kevin Wayne und wurde für den akademischen Gebrauch an der FFHS angepasst.
