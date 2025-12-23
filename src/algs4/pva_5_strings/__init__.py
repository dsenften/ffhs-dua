"""String-Algorithmen und Symbol Tables (PVA 5 - Strings).

Dieses Modul enthält Implementierungen von String-basierten Symbol Tables
und Suchalgorithmen für Textverarbeitung.

Module:
    trie_st: Trie Symbol Table - Dictionary-basierter Trie für String-Schlüssel
    patricia_trie: Patricia-Trie - Kompakter Trie mit Pfadkompression
    kmp: KMP String-Suchalgorithmus - Knuth-Morris-Pratt Pattern Matching
    boyer_moore: Boyer-Moore String-Suchalgorithmus - Bad Character Rule
    rabin_karp: Rabin-Karp String-Suchalgorithmus - Rolling Hash

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

    >>> from src.algs4.pva_5_strings.boyer_moore import BoyerMoore
    >>> bm = BoyerMoore("NEEDLE")
    >>> bm.search("HAYSTACK WITH NEEDLE IN IT")
    14

    >>> from src.algs4.pva_5_strings.rabin_karp import RabinKarp
    >>> rk = RabinKarp("NEEDLE")
    >>> rk.search("HAYSTACK WITH NEEDLE IN IT")
    14
"""

__all__ = [
    "TrieST",
    "PatriciaTrie",
    "KMP",
    "BoyerMoore",
    "RabinKarp",
]

# Lazy loading für Module - verhindert RuntimeWarning bei Ausführung als Script
_LAZY_IMPORTS = {
    "TrieST": (".trie_st", "TrieST"),
    "PatriciaTrie": (".patricia_trie", "PatriciaTrie"),
    "KMP": (".kmp", "KMP"),
    "BoyerMoore": (".boyer_moore", "BoyerMoore"),
    "RabinKarp": (".rabin_karp", "RabinKarp"),
}


def __getattr__(name: str):
    """
    Provide lazy access to exported submodule attributes.
    
    Looks up `name` in the module's _LAZY_IMPORTS mapping, imports the corresponding submodule on first access, and returns the mapped attribute.
    
    Parameters:
        name (str): The attribute name being accessed; valid values are the keys of `_LAZY_IMPORTS`.
    
    Returns:
        The attribute (class, function, or value) exported by the mapped submodule for `name`.
    
    Raises:
        AttributeError: If `name` is not present in `_LAZY_IMPORTS`.
    """
    if name in _LAZY_IMPORTS:
        module_path, attr_name = _LAZY_IMPORTS[name]
        import importlib

        module = importlib.import_module(module_path, __package__)
        return getattr(module, attr_name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")