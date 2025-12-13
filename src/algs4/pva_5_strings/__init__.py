"""String-Algorithmen und Symbol Tables (PVA 5 - Strings).

Dieses Modul enthält Implementierungen von String-basierten Symbol Tables
und Suchalgorithmen für Textverarbeitung.

Module:
    trie_st: Trie Symbol Table - Dictionary-basierter Trie für String-Schlüssel
    patricia_trie: Patricia-Trie - Kompakter Trie mit Pfadkompression
    kmp: KMP String-Suchalgorithmus - Knuth-Morris-Pratt Pattern Matching

Beispiel:
    >>> from src.algs4.pva_5_strings.trie_st import TrieST
    >>> st = TrieST()
    >>> st.put("sea", 1)
    >>> st.put("shells", 2)
    >>> st.get("sea")
    1
    >>> list(st.keys_with_prefix("se"))
    ['sea']

    >>> from src.algs4.pva_5_strings.patricia_trie import PatriciaTrie
    >>> pt = PatriciaTrie()
    >>> pt.put("test", 1)
    >>> pt.put("testing", 2)
    >>> pt.get("test")
    1

    >>> from src.algs4.pva_5_strings.kmp import KMP
    >>> kmp = KMP("NEEDLE")
    >>> kmp.search("HAYSTACK WITH NEEDLE IN IT")
    14
"""

from src.algs4.pva_5_strings.kmp import KMP
from src.algs4.pva_5_strings.patricia_trie import PatriciaTrie
from src.algs4.pva_5_strings.trie_st import TrieST

__all__ = [
    "TrieST",
    "PatriciaTrie",
    "KMP",
]
