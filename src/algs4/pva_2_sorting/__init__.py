"""Sorting - Sortieralgorithmen

Dieses Modul enthält verschiedene Sortieralgorithmen aus dem zweiten
Teil des "Algorithms, 4th Edition" Lehrbuchs:

- Shell: Shell-Sort-Algorithmus mit Knuth-Sequenz
- Quick: Quick-Sort-Algorithmus mit Hoare-Partitionierung
- Heap: Heap-Sort-Algorithmus basierend auf der Heap-Datenstruktur
- Merge: Merge-Sort-Algorithmus mit Divide-and-Conquer-Ansatz

Die meisten Implementierungen arbeiten in-place und unterstützen verschiedene
Datentypen, die das Vergleichsprotokoll implementieren. Merge Sort benötigt
zusätzlichen Speicher, ist aber stabil.
"""

from .heap import Heap
from .merge import Merge
from .quick import Quick
from .shell import Shell

__all__ = [
    # Sortieralgorithmen
    "Shell",
    "Quick",
    "Heap",
    "Merge",
]
