"""FFHS-DUA Algorithmen und Datenstrukturen

Eine Python-Implementierung grundlegender Datenstrukturen basierend auf
das Lehrbuch "Algorithms, 4th Edition" von Robert Sedgewick und Kevin Wayne.

Dieses Paket implementiert die wichtigsten Datenstrukturen aus dem ersten
Teil des Algorithms-Lehrbuchs in Python, angepasst für den akademischen
Gebrauch an der Fernfachhochschule Schweiz (FFHS).

Module:
    fundamentals: Grundlegende Datenstrukturen (Stack, Queue, Bag)
    errors: Benutzerdefinierte Exception-Klassen
"""

__version__ = "0.1.0"
__author__ = "FFHS-DUA"
__email__ = "support@ffhs.ch"

# Hauptmodule für einfachen Import
from . import fundamentals
from . import errors

__all__ = [
    "fundamentals",
    "errors",
]
