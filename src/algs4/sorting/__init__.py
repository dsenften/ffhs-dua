"""Sorting - Sortieralgorithmen

Dieses Modul enthält verschiedene Sortieralgorithmen aus dem zweiten
Teil des "Algorithms, 4th Edition" Lehrbuchs:

- Shell: Shell-Sort-Algorithmus mit Knuth-Sequenz
- Quick: Quick-Sort-Algorithmus mit Hoare-Partitionierung

Alle Implementierungen arbeiten in-place und unterstützen verschiedene
Datentypen, die das Vergleichsprotokoll implementieren.
"""

from .quick import Quick
from .shell import Shell

__all__ = [
    # Sortieralgorithmen
    "Shell",
    "Quick",
]