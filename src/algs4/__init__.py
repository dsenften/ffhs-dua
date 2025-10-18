"""FFHS-DUA: Algorithmen und Datenstrukturen

Eine umfassende Python-Implementierung grundlegender Algorithmen und Datenstrukturen
für den akademischen Gebrauch an der Fernfachhochschule Schweiz (FFHS).

Dieses Paket implementiert die wichtigsten Datenstrukturen und Algorithmen
in Python, basierend auf dem Lehrbuch "Algorithms, 4th Edition" von Sedgewick und Wayne.

Module (nach PVA-Struktur):
    pva_1_fundamentals: Grundlegende Datenstrukturen
        - Stack (3 Varianten: LinkedList, Fixed, Resizing)
        - Queue (LinkedList-basiert)
        - Bag (ungeordnete Sammlung)
        - Union-Find (4 Varianten mit verschiedenen Optimierungen)

    pva_2_sorting: Sortieralgorithmen
        - Shell Sort (O(n^3/2))
        - Quick Sort (O(n log n) durchschnittlich)
        - Merge Sort (O(n log n) garantiert, stabil)
        - Heap Sort (O(n log n) garantiert)

    pva_3_searching: Suchalgorithmen und Symbol Tables
        - Binary Search Tree (BST)
        - AVL Tree (selbstbalancierend)
        - Red-Black BST (links-lastiger Rot-Schwarz-Baum)
        - Hash Tables (Separate Chaining, Linear Probing)

    errors: Benutzerdefinierte Exception-Klassen

Beispiele:
    >>> from src.algs4.pva_2_sorting import Quick
    >>> Quick.sort([3, 1, 4, 1, 5, 9, 2, 6])
    [1, 1, 2, 3, 4, 5, 6, 9]

    >>> from src.algs4.pva_1_fundamentals import Stack
    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.pop()
    1
"""

__version__ = "1.0.0"
__author__ = "Daniel Senften"
__email__ = "daniel.senften@ffhs.ch"
__license__ = "MIT"

# Hauptmodule für einfachen Import
from . import errors, pva_1_fundamentals, pva_2_sorting

# Aliase für Abwärtskompatibilität
fundamentals = pva_1_fundamentals
sorting = pva_2_sorting

__all__ = [
    "pva_1_fundamentals",
    "pva_2_sorting",
    "fundamentals",  # Alias
    "sorting",  # Alias
    "errors",
]
