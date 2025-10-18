# FFHS-DUA: Algorithmen und Datenstrukturen

Eine umfassende Python-Implementierung grundlegender Algorithmen und
Datenstrukturen für den akademischen Gebrauch an der
Fernfachhochschule Schweiz (FFHS).

## ✨ Features

- **Fundamentals**: Stack, Queue, Bag, Union-Find (4 Implementierungsvarianten)
- **Sorting**: Quick Sort, Merge Sort, Heap Sort, Shell Sort (mit CLI-Interface)
- **Searching**: Binary Search Tree (BST), AVL Tree (selbstbalancierend)
- **Utils**: Timing-Utilities für Performance-Messungen (`@timeit` Dekorator)
- **Umfassende Tests**: Vollständige Test-Abdeckung mit pytest (289 Tests)
- **Deutsche Dokumentation**: AsciiDoc-basierte Dokumentation und Jupyter Notebooks

## 🚀 Schnellstart

```bash
# Repository klonen
git clone <repository-url>
cd ffhs-dua

# Abhängigkeiten installieren mit uv
uv sync

# Tests ausführen
python3 -m pytest tests/ -v

# Sortieralgorithmus ausprobieren
cat data/sorting/tiny.txt | python3 -m src.algs4.pva_2_sorting.quick
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

## 👤 Autor

**Daniel Senften** - [daniel.senften@ffhs.ch](mailto:daniel.senften@ffhs.ch)
Fernfachhochschule Schweiz (FFHS)
