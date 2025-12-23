"""Suchalgorithmen und Symbol Tables (PVA 3 - Searching).

Dieses Modul enthält Implementierungen von Symbol Tables (geordneten
Dictionaries) und Suchalgorithmen.

Module:
    bst: Binary Search Tree - Binärer Suchbaum (unbalanciert)
    avl: AVL Tree - Selbstbalancierender binärer Suchbaum
    red_black_bst: Red-Black BST - Links-lastiger Rot-Schwarz-Baum
    hashing: Hash Tables - Hash-Tabellen mit Separate Chaining und Linear Probing

Beispiel:
    >>> from src.algs4.pva_3_searching.bst import BST
    >>> bst = BST()
    >>> bst.put("key", "value")
    >>> bst.get("key")
    'value'

    >>> from src.algs4.pva_3_searching.avl import AVL
    >>> avl = AVL()
    >>> avl.put("key", "value")
    >>> avl.get("key")
    'value'

    >>> from src.algs4.pva_3_searching.red_black_bst import RedBlackBST
    >>> rbt = RedBlackBST()
    >>> rbt.put("key", "value")
    >>> rbt.get("key")
    'value'

    >>> from src.algs4.pva_3_searching.hashing import SeparateChainingHashST
    >>> sc = SeparateChainingHashST()
    >>> sc.put("key", "value")
    >>> sc.get("key")
    'value'
"""

__all__ = [
    "BST",
    "AVL",
    "RedBlackBST",
    "SeparateChainingHashST",
    "LinearProbingHashST",
]

# Lazy loading für Module - verhindert RuntimeWarning bei Ausführung als Script
_LAZY_IMPORTS = {
    "BST": (".bst", "BST"),
    "AVL": (".avl", "AVL"),
    "RedBlackBST": (".red_black_bst", "RedBlackBST"),
    "SeparateChainingHashST": (".hashing", "SeparateChainingHashST"),
    "LinearProbingHashST": (".hashing", "LinearProbingHashST"),
}


def __getattr__(name: str):
    """
    Dynamically import and return a public symbol from a lazily-loaded submodule on first attribute access.
    
    Parameters:
        name (str): The attribute name being accessed on the package module.
    
    Returns:
        Any: The attribute object (class, function, or value) retrieved from the target submodule.
    
    Raises:
        AttributeError: If `name` is not registered for lazy import.
    """
    if name in _LAZY_IMPORTS:
        module_path, attr_name = _LAZY_IMPORTS[name]
        import importlib

        module = importlib.import_module(module_path, __package__)
        return getattr(module, attr_name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")