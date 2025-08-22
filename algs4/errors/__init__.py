"""Errors - Benutzerdefinierte Exception-Klassen

Dieses Modul enthält spezielle Exception-Klassen, die in den
Datenstruktur-Implementierungen verwendet werden:

- NoSuchElementException: Wird geworfen wenn auf ein nicht existierendes Element zugegriffen wird
- IllegalArgumentException: Wird bei ungültigen Argumenten geworfen
- UnsupportedOperationException: Wird bei nicht unterstützten Operationen geworfen

Alle Exceptions sind von der Python-Standardklasse Exception abgeleitet.
"""

from .errors import (
    NoSuchElementException,
    IllegalArgumentException,
    UnsupportedOperationException,
)

__all__ = [
    "NoSuchElementException",
    "IllegalArgumentException",
    "UnsupportedOperationException",
]
