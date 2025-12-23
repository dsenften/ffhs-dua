"""Sorting - Sortieralgorithmen

Dieses Modul enthält verschiedene Sortieralgorithmen aus dem zweiten
Teil des "Algorithms, 4th Edition" Lehrbuchs:

- Shell: Shell-Sort-Algorithmus mit Knuth-Sequenz
- Quick: Quick-Sort-Algorithmus mit Hoare-Partitionierung
- Heap: Heap-Sort-Algorithmus basierend auf der Heap-Datenstruktur
- Merge: Merge-Sort-Algorithmus mit Divide-and-Conquer-Ansatz

Die meisten Implementierungen arbeiten in-place und unterstützen verschiedene
Datentypen, die das Vergleichsprotokoll implementieren. Merge Sort benötigt
zusätzlichen Speicher, ist aber stabil.
"""

__all__ = [
    # Sortieralgorithmen
    "Shell",
    "Quick",
    "Heap",
    "Merge",
]

# Lazy loading für Module - verhindert RuntimeWarning bei Ausführung als Script
_LAZY_IMPORTS = {
    "Shell": (".shell", "Shell"),
    "Quick": (".quick", "Quick"),
    "Heap": (".heap", "Heap"),
    "Merge": (".merge", "Merge"),
}


def __getattr__(name: str):
    """
    Lazily load and return a named public symbol from a submodule on first attribute access.
    
    If `name` is a key in `_LAZY_IMPORTS`, import the corresponding submodule and return the mapped attribute; otherwise raise an AttributeError.
    
    Parameters:
        name (str): The attribute name being accessed on the module.
    
    Returns:
        The attribute object mapped to `name` in `_LAZY_IMPORTS`.
    
    Raises:
        AttributeError: If `name` is not present in `_LAZY_IMPORTS`.
    """
    if name in _LAZY_IMPORTS:
        module_path, attr_name = _LAZY_IMPORTS[name]
        import importlib

        module = importlib.import_module(module_path, __package__)
        return getattr(module, attr_name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")