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
