"""Fundamentals - Grundlegende Datenstrukturen

Dieses Modul enthält die grundlegenden Datenstrukturen aus dem ersten
Teil des "Algorithms, 4th Edition" Lehrbuchs:

- Stack: Last-In-First-Out (LIFO) Stapel in drei Implementierungen
- Queue: First-In-First-Out (FIFO) Warteschlange
- Bag: Ungeordnete Sammlung von Elementen
- Union-Find: Datenstruktur für dynamische Konnektivität in vier Varianten

Alle Implementierungen unterstützen generische Typen und folgen den
Python-Konventionen für Container-Klassen.
"""

from .bag import Bag
from .queue import Queue
from .stack import FixedCapacityStack, ResizingArrayStack, Stack
from .uf import UF, QuickFindUF, QuickUnionUF, WeightedQuickUnionUF

__all__ = [
    # Stack-Implementierungen
    "Stack",
    "FixedCapacityStack",
    "ResizingArrayStack",
    # Queue-Implementierung
    "Queue",
    # Bag-Implementierung
    "Bag",
    # Union-Find-Implementierungen
    "UF",
    "QuickUnionUF",
    "WeightedQuickUnionUF",
    "QuickFindUF",
]
