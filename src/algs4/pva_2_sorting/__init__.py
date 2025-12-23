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
    """Lazy loading von Modulen bei erstem Zugriff."""
    if name in _LAZY_IMPORTS:
        module_path, attr_name = _LAZY_IMPORTS[name]
        import importlib

        module = importlib.import_module(module_path, __package__)
        return getattr(module, attr_name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
