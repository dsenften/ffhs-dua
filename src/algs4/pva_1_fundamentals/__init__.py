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

# Lazy loading für Module - verhindert RuntimeWarning bei Ausführung als Script
_LAZY_IMPORTS = {
    "Bag": (".bag", "Bag"),
    "Queue": (".queue", "Queue"),
    "Stack": (".stack", "Stack"),
    "FixedCapacityStack": (".stack", "FixedCapacityStack"),
    "ResizingArrayStack": (".stack", "ResizingArrayStack"),
    "UF": (".uf", "UF"),
    "QuickFindUF": (".uf", "QuickFindUF"),
    "QuickUnionUF": (".uf", "QuickUnionUF"),
    "WeightedQuickUnionUF": (".uf", "WeightedQuickUnionUF"),
}


def __getattr__(name: str):
    """
    Load and return a public symbol on first access by importing its module on demand.
    
    Parameters:
        name (str): The attribute name being accessed on the module; must be a key in the module's _LAZY_IMPORTS mapping.
    
    Returns:
        The resolved attribute (class, function, or object) corresponding to `name` from the lazily imported module.
    
    Raises:
        AttributeError: If `name` is not present in the module's _LAZY_IMPORTS mapping.
    """
    if name in _LAZY_IMPORTS:
        module_path, attr_name = _LAZY_IMPORTS[name]
        import importlib

        module = importlib.import_module(module_path, __package__)
        return getattr(module, attr_name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")