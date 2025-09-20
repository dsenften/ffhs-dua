# FFHS-DUA: Algorithmen und Datenstrukturen

Eine umfassende Python-Implementierung grundlegender Algorithmen und
Datenstrukturen für den akademischen Gebrauch an der
Fernfachhochschule Schweiz (FFHS).

## Inhalt

* **Fundamentals**: Stack, Queue, Bag, Union-Find (verschiedene Implementierungen)
* **Sorting**: Quick Sort, Shell Sort, Heap Sort, Merge Sort

## Schnellstart

```bash
# Repository klonen
git clone <repository-url>
cd ffhs-dua

# Virtuelle Umgebung erstellen und Abhängigkeiten installieren
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Entwicklung

```bash
# Tests ausführen
python3 -m pytest tests/ -v

# Code formatieren und überprüfen
ruff format
ruff check --fix
```

## Verwendung

```python
# Stack verwenden
from src.algs4.fundamentals.stack import Stack

stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.pop())  # 2

# Sortierung verwenden
from src.algs4.sorting import Quick

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = Quick.sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 34, 64, 90]
```

## Dokumentation

Vollständige Dokumentation und Tutorials in `docs/index.adoc`

## Autor

**Daniel Senften** - [daniel.senften@ffhs.ch](mailto:daniel.senften@ffhs.ch)
Fernfachhochschule Schweiz (FFHS)
