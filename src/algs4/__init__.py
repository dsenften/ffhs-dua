"""FFHS-DUA Algorithmen und Datenstrukturen

Eine Python-Implementierung grundlegender Datenstrukturen und Algorithmen.

Dieses Paket implementiert die wichtigsten Datenstrukturen und Algorithmen
in Python, angepasst für den akademischen Gebrauch an der Fernfachhochschule Schweiz (FFHS).

Module:
    fundamentals: Grundlegende Datenstrukturen (Stack, Queue, Bag, Union-Find)
    sorting: Sortieralgorithmen (Shell-Sort, Quick-Sort, Heap-Sort)
    errors: Benutzerdefinierte Exception-Klassen
"""

__version__ = "0.1.0"
__author__ = "Daniel Senften"
__email__ = "daniel.senften@ffhs.ch"

# Hauptmodule für einfachen Import
from . import errors, fundamentals, sorting

__all__ = [
    "fundamentals",
    "sorting",
    "errors",
]
