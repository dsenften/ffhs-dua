"""Tests für Trie Symbol Table (TrieST).

Diese Testdatei enthält umfassende Tests für die TrieST-Implementierung,
einschliesslich Basisfunktionalität, Präfix-Operationen, Wildcard-Suche,
Deletion und Grenzfälle.
"""

import pytest

from src.algs4.pva_5_strings.trie_st import TrieST


class TestTrieSTBasics:
    """Tests für grundlegende TrieST-Funktionalität."""

    def test_leerer_trie_creation(self):
        """Teste Erstellung eines leeren Trie."""
        st: TrieST[int] = TrieST()
        assert st.is_empty()
        assert st.size() == 0
        assert len(st) == 0

    def test_single_put_get(self):
        """Teste Einfügen und Abrufen eines einzelnen Elements."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)

        assert not st.is_empty()
        assert st.size() == 1
        assert st.get("sea") == 1
        assert st.contains("sea")

    def test_multiple_put_get(self):
        """
        Verify that inserting multiple string keys with distinct integer values stores all entries and that size, get, and contains report the expected results.
        """
        st: TrieST[int] = TrieST()
        keys = ["she", "sells", "sea", "shells", "by", "the", "shore"]

        for i, key in enumerate(keys):
            st.put(key, i)

        assert st.size() == len(keys)
        for i, key in enumerate(keys):
            assert st.get(key) == i
            assert st.contains(key)

    def test_put_update_existing(self):
        """Teste Überschreiben eines existierenden Schlüssels."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)
        assert st.get("sea") == 1

        st.put("sea", 99)
        assert st.get("sea") == 99
        assert st.size() == 1  # Grösse sollte gleich bleiben

    def test_get_nonexistent_key(self):
        """Teste Abrufen eines nicht-existierenden Schlüssels."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)

        assert st.get("land") is None
        assert not st.contains("land")

    def test_contains(self):
        """Teste contains-Methode."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)
        st.put("shore", 2)

        assert st.contains("sea")
        assert st.contains("shore")
        assert not st.contains("land")

    def test_none_key_raises_exception(self):
        """Teste dass None als Schlüssel eine Exception auslöst."""
        st: TrieST[int] = TrieST()

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            st.put(None, 1)  # type: ignore

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            st.get(None)  # type: ignore

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            st.contains(None)  # type: ignore

    def test_empty_string_key(self):
        """
        Verifies that an empty string can be used as a key in the TrieST.
        
        Asserts that inserting the empty string stores the value, that the key is contained, and that the trie size is 1.
        """
        st: TrieST[int] = TrieST()
        st.put("", 0)

        assert st.get("") == 0
        assert st.contains("")
        assert st.size() == 1

    def test_prefix_not_a_key(self):
        """
        Check that a prefix of an inserted key is not treated as a stored key if it was not inserted.
        
        Verifies that after inserting "shells", the prefix "she" is not contained and retrieval returns None.
        """
        st: TrieST[int] = TrieST()
        st.put("shells", 1)

        # "she" ist Präfix von "shells", aber kein eigenständiger Schlüssel
        assert not st.contains("she")
        assert st.get("she") is None

    def test_gemeinsame_praefixe(self):
        """Teste Wörter mit gemeinsamen Präfixen."""
        st: TrieST[int] = TrieST()
        st.put("shell", 1)
        st.put("shells", 2)
        st.put("she", 3)

        assert st.get("shell") == 1
        assert st.get("shells") == 2
        assert st.get("she") == 3
        assert st.size() == 3


class TestTrieSTKeys:
    """Tests für keys-Operation."""

    def test_keys_empty_trie(self):
        """Teste keys auf leerem Trie."""
        st: TrieST[int] = TrieST()
        assert list(st.keys()) == []

    def test_keys_single_element(self):
        """Teste keys mit einem Element."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)

        assert list(st.keys()) == ["sea"]

    def test_keys_multiple_elements_sorted(self):
        """
        Verifies that keys() yields all stored keys in lexicographic (sorted) order.
        """
        st: TrieST[int] = TrieST()
        keys = ["she", "sells", "sea", "shells", "by", "the", "shore"]

        for i, key in enumerate(keys):
            st.put(key, i)

        result = list(st.keys())
        assert result == sorted(keys)

    def test_keys_with_numbers(self):
        """
        Verify that keys() returns numeric-string keys in lexicographic order.
        """
        st: TrieST[int] = TrieST()
        st.put("1", 1)
        st.put("10", 10)
        st.put("2", 2)
        st.put("20", 20)

        result = list(st.keys())
        assert result == ["1", "10", "2", "20"]  # Lexikographisch sortiert

    def test_iter(self):
        """
        Verifies that iterating over a TrieST yields the same sequence of keys as returned by keys().
        
        The test inserts a sequence of keys with associated values and asserts that list(st) produces the expected key order.
        """
        st: TrieST[int] = TrieST()
        keys = ["a", "b", "c"]

        for i, key in enumerate(keys):
            st.put(key, i)

        # __iter__ sollte keys() aufrufen
        result = list(st)
        assert result == keys


class TestTrieSTKeysWithPrefix:
    """Tests für keys_with_prefix-Operation."""

    def test_keys_with_prefix_empty_trie(self):
        """Teste keys_with_prefix auf leerem Trie."""
        st: TrieST[int] = TrieST()
        assert list(st.keys_with_prefix("sh")) == []

    def test_keys_with_prefix_no_match(self):
        """Teste keys_with_prefix ohne Treffer."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)
        st.put("shore", 2)

        assert list(st.keys_with_prefix("land")) == []

    def test_keys_with_prefix_single_match(self):
        """Teste keys_with_prefix mit einem Treffer."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)
        st.put("shore", 2)

        assert list(st.keys_with_prefix("sea")) == ["sea"]

    def test_keys_with_prefix_multiple_matches(self):
        """Teste keys_with_prefix mit mehreren Treffern."""
        st: TrieST[int] = TrieST()
        st.put("she", 0)
        st.put("sells", 1)
        st.put("sea", 2)
        st.put("shells", 3)
        st.put("shore", 4)

        result = list(st.keys_with_prefix("sh"))
        assert result == ["she", "shells", "shore"]

    def test_keys_with_prefix_empty_prefix(self):
        """Teste keys_with_prefix mit leerem Präfix (sollte alle Schlüssel zurückgeben)."""
        st: TrieST[int] = TrieST()
        keys = ["sea", "sells", "she"]

        for i, key in enumerate(keys):
            st.put(key, i)

        result = list(st.keys_with_prefix(""))
        assert result == sorted(keys)

    def test_keys_with_prefix_none_raises_exception(self):
        """Teste dass None als Präfix eine Exception auslöst."""
        st: TrieST[int] = TrieST()

        with pytest.raises(ValueError, match="Präfix darf nicht None sein"):
            list(st.keys_with_prefix(None))  # type: ignore


class TestTrieSTKeysThatMatch:
    """Tests für keys_that_match-Operation."""

    def test_keys_that_match_empty_trie(self):
        """Teste keys_that_match auf leerem Trie."""
        st: TrieST[int] = TrieST()
        assert list(st.keys_that_match("s..")) == []

    def test_keys_that_match_no_wildcard(self):
        """Teste keys_that_match ohne Wildcard (exakte Suche)."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)
        st.put("she", 2)

        assert list(st.keys_that_match("sea")) == ["sea"]

    def test_keys_that_match_single_wildcard(self):
        """Teste keys_that_match mit einzelnem Wildcard."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)
        st.put("she", 2)
        st.put("ski", 3)

        result = list(st.keys_that_match("s.e"))
        assert result == ["she"]

    def test_keys_that_match_multiple_wildcards(self):
        """Teste keys_that_match mit mehreren Wildcards."""
        st: TrieST[int] = TrieST()
        st.put("shell", 1)
        st.put("shells", 2)
        st.put("shelf", 3)

        result = list(st.keys_that_match(".he.l."))
        assert result == ["shells"]

    def test_keys_that_match_all_wildcards(self):
        """Teste keys_that_match mit nur Wildcards."""
        st: TrieST[int] = TrieST()
        st.put("abc", 1)
        st.put("def", 2)
        st.put("xyz", 3)

        result = list(st.keys_that_match("..."))
        assert result == ["abc", "def", "xyz"]

    def test_keys_that_match_no_match(self):
        """Teste keys_that_match ohne Treffer."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)
        st.put("she", 2)

        assert list(st.keys_that_match("x..")) == []

    def test_keys_that_match_none_raises_exception(self):
        """Teste dass None als Muster eine Exception auslöst."""
        st: TrieST[int] = TrieST()

        with pytest.raises(ValueError, match="Muster darf nicht None sein"):
            list(st.keys_that_match(None))  # type: ignore


class TestTrieSTLongestPrefixOf:
    """Tests für longest_prefix_of-Operation."""

    def test_longest_prefix_of_empty_trie(self):
        """Teste longest_prefix_of auf leerem Trie."""
        st: TrieST[int] = TrieST()
        assert st.longest_prefix_of("shellsort") == ""

    def test_longest_prefix_of_no_match(self):
        """Teste longest_prefix_of ohne Treffer."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)
        st.put("shore", 2)

        assert st.longest_prefix_of("land") == ""

    def test_longest_prefix_of_exact_match(self):
        """Teste longest_prefix_of mit exaktem Treffer."""
        st: TrieST[int] = TrieST()
        st.put("shell", 1)
        st.put("shells", 2)

        assert st.longest_prefix_of("shells") == "shells"

    def test_longest_prefix_of_partial_match(self):
        """
        Verify that longest_prefix_of returns the longest stored key that is a prefix of the given query when a partial (prefix) match exists.
        """
        st: TrieST[int] = TrieST()
        st.put("she", 1)
        st.put("shell", 2)

        assert st.longest_prefix_of("shellsort") == "shell"

    def test_longest_prefix_of_multiple_prefixes(self):
        """Teste longest_prefix_of mit mehreren Präfixen (sollte den längsten nehmen)."""
        st: TrieST[int] = TrieST()
        st.put("s", 1)
        st.put("sh", 2)
        st.put("she", 3)
        st.put("shell", 4)

        assert st.longest_prefix_of("shellsort") == "shell"

    def test_longest_prefix_of_query_shorter_than_key(self):
        """Teste longest_prefix_of wenn Query kürzer als gespeicherter Schlüssel."""
        st: TrieST[int] = TrieST()
        st.put("shellsort", 1)

        assert st.longest_prefix_of("she") == ""

    def test_longest_prefix_of_none_raises_exception(self):
        """Teste dass None als Query eine Exception auslöst."""
        st: TrieST[int] = TrieST()

        with pytest.raises(ValueError, match="Query darf nicht None sein"):
            st.longest_prefix_of(None)  # type: ignore


class TestTrieSTDelete:
    """Tests für delete-Operation."""

    def test_delete_single_element(self):
        """Teste Löschen eines einzelnen Elements."""
        st: TrieST[int] = TrieST()
        st.put("sea", 1)
        assert st.size() == 1

        st.delete("sea")
        assert st.size() == 0
        assert st.is_empty()
        assert not st.contains("sea")

    def test_delete_multiple_elements(self):
        """Teste Löschen mehrerer Elemente."""
        st: TrieST[int] = TrieST()
        keys = ["sea", "sells", "she"]

        for i, key in enumerate(keys):
            st.put(key, i)

        st.delete("sea")
        assert st.size() == 2
        assert not st.contains("sea")
        assert st.contains("sells")
        assert st.contains("she")

    def test_delete_nonexistent_key(self):
        """
        Verifies that deleting a non-existent key does not change the trie.
        
        After attempting to delete a key that was never inserted, the trie size remains unchanged and existing keys remain present.
        """
        st: TrieST[int] = TrieST()
        st.put("sea", 1)

        st.delete("land")  # Sollte keinen Fehler werfen
        assert st.size() == 1
        assert st.contains("sea")

    def test_delete_with_gemeinsame_praefixe(self):
        """Teste Löschen bei gemeinsamen Präfixen."""
        st: TrieST[int] = TrieST()
        st.put("she", 1)
        st.put("shell", 2)
        st.put("shells", 3)

        # Lösche "shell" - "she" und "shells" sollten bleiben
        st.delete("shell")
        assert st.size() == 2
        assert st.contains("she")
        assert not st.contains("shell")
        assert st.contains("shells")

    def test_delete_prefix_of_existing_key(self):
        """Teste Löschen eines Präfix eines existierenden Schlüssels."""
        st: TrieST[int] = TrieST()
        st.put("shells", 1)

        st.delete("she")  # "she" ist Präfix von "shells", aber kein Schlüssel
        assert st.size() == 1
        assert st.contains("shells")

    def test_delete_cleanup_empty_nodes(self):
        """Teste dass leere Knoten nach dem Löschen entfernt werden."""
        st: TrieST[int] = TrieST()
        st.put("abc", 1)

        st.delete("abc")
        assert st.is_empty()

        # Prüfe dass der Trie wirklich leer ist (auch intern)
        assert st._root is None or (
            st._root.val is None and len(st._root.children) == 0
        )

    def test_delete_none_raises_exception(self):
        """
        Verifies that attempting to delete None as a key raises a ValueError.
        
        Asserts the raised ValueError's message contains "Schlüssel darf nicht None sein".
        """
        st: TrieST[int] = TrieST()

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            st.delete(None)  # type: ignore


class TestTrieSTRepr:
    """Tests für __repr__ Methode."""

    def test_repr_empty_trie(self):
        """Teste __repr__ bei leerem Trie."""
        st: TrieST[int] = TrieST()
        assert repr(st) == "TrieST(empty)"

    def test_repr_few_elements(self):
        """Teste __repr__ bei wenigen Elementen."""
        st: TrieST[int] = TrieST()
        st.put("a", 1)
        st.put("b", 2)

        repr_str = repr(st)
        assert "TrieST" in repr_str
        assert "a" in repr_str
        assert "b" in repr_str

    def test_repr_many_elements(self):
        """Teste __repr__ bei vielen Elementen (sollte gekürzt werden)."""
        st: TrieST[int] = TrieST()
        keys = [chr(ord("a") + i) for i in range(20)]  # a-t

        for i, key in enumerate(keys):
            st.put(key, i)

        repr_str = repr(st)
        assert "TrieST" in repr_str
        assert "..." in repr_str
        assert "20 total" in repr_str


class TestTrieSTTypeSafety:
    """Tests für Type-Safety mit verschiedenen Werttypen."""

    def test_int_values(self):
        """Teste mit int-Werten."""
        st: TrieST[int] = TrieST()
        st.put("a", 1)
        st.put("b", 2)

        assert st.get("a") == 1
        assert st.get("b") == 2

    def test_str_values(self):
        """Teste mit str-Werten."""
        st: TrieST[str] = TrieST()
        st.put("name", "Alice")
        st.put("city", "Zürich")

        assert st.get("name") == "Alice"
        assert st.get("city") == "Zürich"

    def test_float_values(self):
        """Teste mit float-Werten."""
        st: TrieST[float] = TrieST()
        st.put("pi", 3.14159)
        st.put("e", 2.71828)

        assert st.get("pi") == 3.14159
        assert st.get("e") == 2.71828

    def test_list_values(self):
        """
        Verifies that list values can be stored and retrieved from the TrieST.
        
        Inserts two keys with list[int] values and asserts that get returns the exact lists.
        """
        st: TrieST[list[int]] = TrieST()
        st.put("primes", [2, 3, 5, 7])
        st.put("evens", [2, 4, 6, 8])

        assert st.get("primes") == [2, 3, 5, 7]
        assert st.get("evens") == [2, 4, 6, 8]


class TestTrieSTUnicodeSupport:
    """Tests für Unicode-Unterstützung."""

    def test_unicode_keys(self):
        """Teste mit Unicode-Schlüsseln."""
        st: TrieST[int] = TrieST()
        st.put("äpfel", 1)
        st.put("über", 2)
        st.put("zürich", 3)

        assert st.get("äpfel") == 1
        assert st.get("über") == 2
        assert st.get("zürich") == 3

    def test_unicode_prefix_search(self):
        """Teste Präfix-Suche mit Unicode."""
        st: TrieST[int] = TrieST()
        st.put("über", 1)
        st.put("überlegen", 2)
        st.put("übersicht", 3)

        result = list(st.keys_with_prefix("über"))
        assert len(result) == 3
        assert "über" in result
        assert "überlegen" in result
        assert "übersicht" in result

    def test_emojis(self):
        """
        Verify that emoji characters can be used as keys and their associated values are stored and retrieved correctly.
        """
        st: TrieST[str] = TrieST()
        st.put("😀", "happy")
        st.put("😢", "sad")

        assert st.get("😀") == "happy"
        assert st.get("😢") == "sad"


class TestTrieSTEdgeCases:
    """Tests für Grenzfälle."""

    def test_very_long_key(self):
        """Teste mit sehr langem Schlüssel.

        Hinweis: Python hat eine Rekursionstiefe-Grenze von ~1000,
        daher verwenden wir 500 Zeichen statt 1000.
        """
        st: TrieST[int] = TrieST()
        long_key = "a" * 500

        st.put(long_key, 42)
        assert st.get(long_key) == 42
        assert st.contains(long_key)

    def test_single_character_keys(self):
        """
        Verify that storing single-character keys 'a' through 'z' with integer values preserves size and allows correct retrieval.
        
        Inserts the keys "a".."z" mapped to integers 0..25, asserts the trie size is 26, and verifies each key returns its corresponding value.
        """
        st: TrieST[int] = TrieST()
        for i in range(26):
            st.put(chr(ord("a") + i), i)

        assert st.size() == 26
        for i in range(26):
            assert st.get(chr(ord("a") + i)) == i

    def test_numeric_string_keys(self):
        """Teste mit numerischen String-Schlüsseln."""
        st: TrieST[str] = TrieST()
        st.put("123", "eins-zwei-drei")
        st.put("456", "vier-fünf-sechs")

        assert st.get("123") == "eins-zwei-drei"
        assert st.get("456") == "vier-fünf-sechs"

    def test_special_characters(self):
        """Teste mit Sonderzeichen."""
        st: TrieST[int] = TrieST()
        st.put("hello-world", 1)
        st.put("hello_world", 2)
        st.put("hello.world", 3)
        st.put("hello world", 4)

        assert st.get("hello-world") == 1
        assert st.get("hello_world") == 2
        assert st.get("hello.world") == 3
        assert st.get("hello world") == 4
        assert st.size() == 4


class TestTrieSTIntegration:
    """Integrationstests für komplexe Szenarien."""

    def test_shellsst_example(self):
        """
        Exercise the TrieST example from the documentation to validate longest-prefix, prefix, and wildcard queries.
        
        Inserts a sample set of words with integer values, then verifies that:
        - longest_prefix_of returns the longest stored prefix for a query,
        - keys_with_prefix yields keys matching a given prefix,
        - keys_that_match finds keys matching a wildcard pattern.
        """
        st: TrieST[int] = TrieST()
        words = ["she", "sells", "sea", "shells", "by", "the", "shore"]

        for i, word in enumerate(words):
            st.put(word, i)

        # Teste longest_prefix_of
        assert st.longest_prefix_of("shellsort") == "shells"
        assert st.longest_prefix_of("quicksort") == ""

        # Teste keys_with_prefix
        shor_keys = list(st.keys_with_prefix("shor"))
        assert shor_keys == ["shore"]

        # Teste keys_that_match
        match_keys = list(st.keys_that_match(".he.l."))
        assert "shells" in match_keys

    def test_update_and_delete_sequence(self):
        """Teste eine Sequenz von Updates und Deletions."""
        st: TrieST[int] = TrieST()

        # Füge Einträge hinzu
        st.put("a", 1)
        st.put("ab", 2)
        st.put("abc", 3)
        assert st.size() == 3

        # Update
        st.put("ab", 20)
        assert st.get("ab") == 20
        assert st.size() == 3

        # Delete
        st.delete("ab")
        assert st.size() == 2
        assert st.contains("a")
        assert not st.contains("ab")
        assert st.contains("abc")

        # Füge wieder hinzu
        st.put("ab", 200)
        assert st.get("ab") == 200
        assert st.size() == 3

    def test_dictionary_use_case(self):
        """
        Test dictionary-like use of TrieST with German words.
        
        Inserts German word→definition pairs, verifies that keys_with_prefix("haus") returns the three expected "haus" entries, and verifies that keys_that_match("....") includes the four-letter words "haus" and "hund".
        """
        st: TrieST[str] = TrieST()

        # Deutsches Wörterbuch
        st.put("haus", "Gebäude zum Wohnen")
        st.put("haustür", "Tür eines Hauses")
        st.put("hausdach", "Dach eines Hauses")
        st.put("hund", "Haustier")

        # Suche alle Wörter mit Präfix "haus"
        haus_words = list(st.keys_with_prefix("haus"))
        assert len(haus_words) == 3
        assert "haus" in haus_words
        assert "haustür" in haus_words
        assert "hausdach" in haus_words

        # Suche mit Wildcard
        four_letter_words = list(st.keys_that_match("...."))
        assert "haus" in four_letter_words
        assert "hund" in four_letter_words