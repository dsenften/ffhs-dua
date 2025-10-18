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

from src.algs4.pva_3_searching.avl import AVL
from src.algs4.pva_3_searching.bst import BST
from src.algs4.pva_3_searching.hashing import (
    LinearProbingHashST,
    SeparateChainingHashST,
)
from src.algs4.pva_3_searching.red_black_bst import RedBlackBST

__all__ = [
    "BST",
    "AVL",
    "RedBlackBST",
    "SeparateChainingHashST",
    "LinearProbingHashST",
]
