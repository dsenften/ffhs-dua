"""Benutzerdefinierte Exception-Klassen für ffhs-dua.

Dieses Modul enthält Exception-Klassen für verschiedene Fehler:
- NoSuchElementException: Zugriff auf nicht vorhandene Elemente
- IllegalArgumentException: Ungültige Argumente
- UnsupportedOperationException: Nicht unterstützte Operationen
- StackOverflowException: Stack-Überlauf bei fester Kapazität
"""


class NoSuchElementException(Exception):
    """Exception für den Zugriff auf nicht vorhandene Elemente."""

    pass


class IllegalArgumentException(Exception):
    """Exception für ungültige Argumente."""

    pass


class UnsupportedOperationException(Exception):
    """Exception für nicht unterstützte Operationen."""

    pass


class StackOverflowException(Exception):
    """Exception für Stack-Überlauf bei fester Kapazität."""

    pass
