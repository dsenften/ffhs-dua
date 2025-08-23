# -*- coding: utf-8 -*-
"""Fundamentals - Grundlegende Datenstrukturen

Dieses Modul enthält die grundlegenden Datenstrukturen aus dem ersten
Teil des "Algorithms, 4th Edition" Lehrbuchs:

- Stack: Last-In-First-Out (LIFO) Stapel in drei Implementierungen
- Queue: First-In-First-Out (FIFO) Warteschlange
- Bag: Ungeordnete Sammlung von Elementen

Alle Implementierungen unterstützen generische Typen und folgen den
Python-Konventionen für Container-Klassen.
"""

from .stack import Stack, FixedCapacityStack, ResizingArrayStack
from .queue import Queue
from .bag import Bag

__all__ = [
    # Stack-Implementierungen
    "Stack",
    "FixedCapacityStack",
    "ResizingArrayStack",
    # Queue-Implementierung
    "Queue",
    # Bag-Implementierung
    "Bag",
]
