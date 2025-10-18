"""FFHS-DUA Algorithmen und Datenstrukturen

Eine Python-Implementierung grundlegender Datenstrukturen und Algorithmen.

Dieses Paket implementiert die wichtigsten Datenstrukturen und Algorithmen
in Python, angepasst für den akademischen Gebrauch an der Fernfachhochschule Schweiz (FFHS).

Module (nach PVA-Struktur):
    pva_1_fundamentals: Grundlegende Datenstrukturen (Stack, Queue, Bag, Union-Find)
    pva_2_sorting: Sortieralgorithmen (Quick-Sort, Merge-Sort, Heap-Sort, Shell-Sort)
    errors: Benutzerdefinierte Exception-Klassen
"""

__version__ = "0.1.0"
__author__ = "Daniel Senften"
__email__ = "daniel.senften@ffhs.ch"

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
