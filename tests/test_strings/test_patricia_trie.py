"""Tests für Patricia Trie.

Diese Testdatei enthält umfassende Tests für die PatriciaTrie-Implementierung,
einschliesslich Basisfunktionalität, Deletion mit Merge/Collapse-Verhalten,
und Grenzfälle.
"""

import pytest

from src.algs4.pva_5_strings.patricia_trie import PatriciaTrie


class TestPatriciaTrieBasics:
    """Tests für grundlegende PatriciaTrie-Funktionalität."""

    def test_leerer_trie_creation(self):
        """Teste Erstellung eines leeren Patricia-Trie."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        assert pt.is_empty()
        assert pt.size() == 0
        assert len(pt) == 0

    def test_single_put_get(self):
        """Teste Einfügen und Abrufen eines einzelnen Elements."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("sea", 1)

        assert not pt.is_empty()
        assert pt.size() == 1
        assert pt.get("sea") == 1
        assert pt.contains("sea")

    def test_multiple_put_get(self):
        """Teste Einfügen und Abrufen mehrerer Elemente."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        keys = ["she", "sells", "sea", "shells", "by", "the", "shore"]

        for i, key in enumerate(keys):
            pt.put(key, i)

        assert pt.size() == len(keys)
        for i, key in enumerate(keys):
            assert pt.get(key) == i
            assert pt.contains(key)

    def test_put_update_existing(self):
        """Teste Überschreiben eines existierenden Schlüssels."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("sea", 1)
        assert pt.get("sea") == 1

        pt.put("sea", 99)
        assert pt.get("sea") == 99
        assert pt.size() == 1  # Grösse sollte gleich bleiben

    def test_get_nonexistent_key(self):
        """Teste Abrufen eines nicht-existierenden Schlüssels."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("sea", 1)

        assert pt.get("land") is None
        assert not pt.contains("land")

    def test_contains(self):
        """Teste contains-Methode."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("sea", 1)
        pt.put("shore", 2)

        assert pt.contains("sea")
        assert pt.contains("shore")
        assert not pt.contains("land")

    def test_none_key_raises_exception(self):
        """Teste dass None als Schlüssel eine Exception auslöst."""
        pt: PatriciaTrie[int] = PatriciaTrie()

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            pt.put(None, 1)  # type: ignore

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            pt.get(None)  # type: ignore

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            pt.contains(None)  # type: ignore

    def test_empty_string_key(self):
        """Teste leerer String als Schlüssel."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("", 0)

        assert pt.get("") == 0
        assert pt.contains("")
        assert pt.size() == 1

    def test_prefix_not_a_key(self):
        """Teste dass ein Präfix nicht als Schlüssel gilt, wenn er nicht eingefügt wurde."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("shells", 1)

        # "she" ist Präfix von "shells", aber kein eigenständiger Schlüssel
        assert not pt.contains("she")
        assert pt.get("she") is None

    def test_gemeinsame_praefixe(self):
        """
        Verify that the PatriciaTrie correctly stores and retrieves keys that share common prefixes.
        
        Inserts 'shell', 'shells', and 'she' with different values and asserts each key returns its associated value and that the trie size equals 3.
        """
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("shell", 1)
        pt.put("shells", 2)
        pt.put("she", 3)

        assert pt.get("shell") == 1
        assert pt.get("shells") == 2
        assert pt.get("she") == 3
        assert pt.size() == 3


class TestPatriciaTrieKeys:
    """Tests für keys-Operation."""

    def test_keys_empty_trie(self):
        """Teste keys auf leerem Patricia-Trie."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        assert list(pt.keys()) == []

    def test_keys_single_element(self):
        """Teste keys mit einem Element."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("sea", 1)

        assert list(pt.keys()) == ["sea"]

    def test_keys_multiple_elements_sorted(self):
        """Teste dass keys in lexikographischer Reihenfolge zurückgegeben werden."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        keys = ["she", "sells", "sea", "shells", "by", "the", "shore"]

        for i, key in enumerate(keys):
            pt.put(key, i)

        result = list(pt.keys())
        assert result == sorted(keys)

    def test_iter(self):
        """Teste __iter__ Methode."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        keys = ["a", "b", "c"]

        for i, key in enumerate(keys):
            pt.put(key, i)

        # __iter__ sollte keys() aufrufen
        result = list(pt)
        assert result == keys


class TestPatriciaTrieDelete:
    """Tests für delete-Operation (Patricia-Trie-spezifisch)."""

    def test_delete_single_element(self):
        """Teste Löschen eines einzelnen Elements."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("sea", 1)
        assert pt.size() == 1

        pt.delete("sea")
        assert pt.size() == 0
        assert pt.is_empty()
        assert not pt.contains("sea")
        assert pt._root is None

    def test_delete_leaf_node(self):
        """
        Verifies that deleting a leaf node removes only that key and preserves its prefix entry.
        
        After inserting "test" and "testing" (where "testing" is a leaf), deleting "testing" reduces the trie size by one, leaves "test" present, and makes "testing" absent.
        """
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("test", 1)
        pt.put("testing", 2)  # "testing" ist Blatt

        pt.delete("testing")
        assert pt.size() == 1
        assert pt.contains("test")
        assert not pt.contains("testing")

    def test_delete_internal_node_with_merge(self):
        """Teste Löschen eines internen Knotens (erfordert Merge)."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("test", 1)
        pt.put("testing", 2)

        # Lösche "test" - sollte Knoten verschmelzen
        pt.delete("test")
        assert pt.size() == 1
        assert not pt.contains("test")
        assert pt.contains("testing")
        assert pt.get("testing") == 2

    def test_delete_with_multiple_children(self):
        """Teste Löschen eines Knotens mit mehreren Kindern (kein Merge)."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("test", 1)
        pt.put("testing", 2)
        pt.put("tester", 3)

        # Lösche "test" - Knoten sollte bleiben (hat 2 Kinder)
        pt.delete("test")
        assert pt.size() == 2
        assert not pt.contains("test")
        assert pt.contains("testing")
        assert pt.contains("tester")

    def test_delete_nonexistent_key(self):
        """Teste Löschen eines nicht-existierenden Schlüssels."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("sea", 1)

        pt.delete("land")  # Sollte keinen Fehler werfen
        assert pt.size() == 1
        assert pt.contains("sea")

    def test_delete_partial_prefix(self):
        """
        Verifies that deleting a key which is a prefix of an existing key does not remove or affect the longer key.
        """
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("testing", 1)

        # "test" ist Präfix von "testing", aber kein Schlüssel
        pt.delete("test")
        assert pt.size() == 1
        assert pt.contains("testing")

    def test_delete_with_gemeinsame_praefixe(self):
        """Teste Löschen bei gemeinsamen Präfixen."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("she", 1)
        pt.put("shell", 2)
        pt.put("shells", 3)

        # Lösche "shell" - "she" und "shells" sollten bleiben
        pt.delete("shell")
        assert pt.size() == 2
        assert pt.contains("she")
        assert not pt.contains("shell")
        assert pt.contains("shells")

    def test_delete_cascade_merge(self):
        """Teste dass Merge kaskadiert (bottom-up)."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("a", 1)
        pt.put("abc", 2)

        # Lösche "abc" - sollte komplett verschmelzen
        pt.delete("abc")
        assert pt.size() == 1
        assert pt.contains("a")
        assert not pt.contains("abc")

    def test_delete_all_elements(self):
        """Teste Löschen aller Elemente nacheinander."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        keys = ["a", "ab", "abc", "abcd"]

        for i, key in enumerate(keys):
            pt.put(key, i)

        # Lösche in umgekehrter Reihenfolge
        for key in reversed(keys):
            pt.delete(key)

        assert pt.is_empty()
        assert pt.size() == 0
        assert pt._root is None

    def test_delete_none_raises_exception(self):
        """Teste dass None als Schlüssel eine Exception auslöst."""
        pt: PatriciaTrie[int] = PatriciaTrie()

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            pt.delete(None)  # type: ignore

    def test_delete_from_empty_trie(self):
        """Teste Löschen aus leerem Trie."""
        pt: PatriciaTrie[int] = PatriciaTrie()

        # Sollte keinen Fehler werfen
        pt.delete("anything")
        assert pt.is_empty()

    def test_delete_updates_size_correctly(self):
        """Teste dass delete die Grösse korrekt aktualisiert."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("a", 1)
        pt.put("b", 2)
        pt.put("c", 3)
        assert pt.size() == 3

        pt.delete("b")
        assert pt.size() == 2

        pt.delete("nonexistent")
        assert pt.size() == 2  # Sollte gleich bleiben

        pt.delete("a")
        assert pt.size() == 1

        pt.delete("c")
        assert pt.size() == 0


class TestPatriciaTrieRepr:
    """Tests für __repr__ Methode."""

    def test_repr_empty_trie(self):
        """Teste __repr__ bei leerem Patricia-Trie."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        assert repr(pt) == "PatriciaTrie(empty)"

    def test_repr_few_elements(self):
        """Teste __repr__ bei wenigen Elementen."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("a", 1)
        pt.put("b", 2)

        repr_str = repr(pt)
        assert "PatriciaTrie" in repr_str
        assert "a" in repr_str
        assert "b" in repr_str

    def test_repr_many_elements(self):
        """Teste __repr__ bei vielen Elementen (sollte gekürzt werden)."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        keys = [chr(ord("a") + i) for i in range(20)]  # a-t

        for i, key in enumerate(keys):
            pt.put(key, i)

        repr_str = repr(pt)
        assert "PatriciaTrie" in repr_str
        assert "..." in repr_str
        assert "20 total" in repr_str


class TestPatriciaTrieTypeSafety:
    """Tests für Type-Safety mit verschiedenen Werttypen."""

    def test_int_values(self):
        """
        Verifies values can be stored and retrieved by string keys in a PatriciaTrie.
        
        Inserts two key-value pairs with integer values and asserts that each key returns the expected value.
        """
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("a", 1)
        pt.put("b", 2)

        assert pt.get("a") == 1
        assert pt.get("b") == 2

    def test_str_values(self):
        """Teste mit str-Werten."""
        pt: PatriciaTrie[str] = PatriciaTrie()
        pt.put("name", "Alice")
        pt.put("city", "Zürich")

        assert pt.get("name") == "Alice"
        assert pt.get("city") == "Zürich"

    def test_float_values(self):
        """Teste mit float-Werten."""
        pt: PatriciaTrie[float] = PatriciaTrie()
        pt.put("pi", 3.14159)
        pt.put("e", 2.71828)

        assert pt.get("pi") == 3.14159
        assert pt.get("e") == 2.71828


class TestPatriciaTrieEdgeCases:
    """Tests für Grenzfälle."""

    def test_very_long_key(self):
        """
        Verifies that a very long key (500 characters) can be inserted, retrieved, detected as present, deleted, and that the trie is empty after deletion.
        
        The test inserts a 500-character key with an integer value, checks retrieval and containment, deletes the key, and confirms the trie is empty.
        """
        pt: PatriciaTrie[int] = PatriciaTrie()
        long_key = "a" * 500

        pt.put(long_key, 42)
        assert pt.get(long_key) == 42
        assert pt.contains(long_key)

        # Teste auch Löschen
        pt.delete(long_key)
        assert not pt.contains(long_key)
        assert pt.is_empty()

    def test_single_character_keys(self):
        """
        Verify that the PatriciaTrie correctly stores and retrieves single-character lowercase keys.
        
        Inserts keys 'a' through 'z' with distinct integer values, asserts the trie reports size 26, and that each key returns the value originally stored.
        """
        pt: PatriciaTrie[int] = PatriciaTrie()
        for i in range(26):
            pt.put(chr(ord("a") + i), i)

        assert pt.size() == 26
        for i in range(26):
            assert pt.get(chr(ord("a") + i)) == i

    def test_numeric_string_keys(self):
        """Teste mit numerischen String-Schlüsseln."""
        pt: PatriciaTrie[str] = PatriciaTrie()
        pt.put("123", "eins-zwei-drei")
        pt.put("456", "vier-fünf-sechs")

        assert pt.get("123") == "eins-zwei-drei"
        assert pt.get("456") == "vier-fünf-sechs"

    def test_special_characters(self):
        """Teste mit Sonderzeichen."""
        pt: PatriciaTrie[int] = PatriciaTrie()
        pt.put("hello-world", 1)
        pt.put("hello_world", 2)
        pt.put("hello.world", 3)
        pt.put("hello world", 4)

        assert pt.get("hello-world") == 1
        assert pt.get("hello_world") == 2
        assert pt.get("hello.world") == 3
        assert pt.get("hello world") == 4
        assert pt.size() == 4


class TestPatriciaTrieIntegration:
    """Integrationstests für komplexe Szenarien."""

    def test_update_and_delete_sequence(self):
        """Teste eine Sequenz von Updates und Deletions."""
        pt: PatriciaTrie[int] = PatriciaTrie()

        # Füge Einträge hinzu
        pt.put("a", 1)
        pt.put("ab", 2)
        pt.put("abc", 3)
        assert pt.size() == 3

        # Update
        pt.put("ab", 20)
        assert pt.get("ab") == 20
        assert pt.size() == 3

        # Delete
        pt.delete("ab")
        assert pt.size() == 2
        assert pt.contains("a")
        assert not pt.contains("ab")
        assert pt.contains("abc")

        # Füge wieder hinzu
        pt.put("ab", 200)
        assert pt.get("ab") == 200
        assert pt.size() == 3

    def test_path_compression_benefit(self):
        """Teste dass Pfadkompression bei ähnlichen Schlüsseln funktioniert."""
        pt: PatriciaTrie[int] = PatriciaTrie()

        # Viele Schlüssel mit gleichem Präfix
        base = "veryveryverylongprefix"
        for i in range(10):
            pt.put(f"{base}{i}", i)

        assert pt.size() == 10

        # Alle sollten abrufbar sein
        for i in range(10):
            assert pt.get(f"{base}{i}") == i

        # Lösche einige
        pt.delete(f"{base}0")
        pt.delete(f"{base}5")
        assert pt.size() == 8

        # Verbleibende sollten noch da sein
        for i in range(10):
            if i not in [0, 5]:
                assert pt.get(f"{base}{i}") == i

    def test_complex_delete_scenario(self):
        """
        Exercise a complex deletion scenario that triggers node merges and verifies size and containment after each deletion.
        
        Verifies that deleting "apple" causes a merge preserving "app" and "application", deleting "app" triggers further merges preserving "application" and "apply", and deleting "bandana" removes it while keeping "banana" and "band".
        """
        pt: PatriciaTrie[int] = PatriciaTrie()

        # Erstelle eine Baumstruktur
        keys = [
            "app",
            "apple",
            "application",
            "apply",
            "banana",
            "band",
            "bandana",
        ]
        for i, key in enumerate(keys):
            pt.put(key, i)

        assert pt.size() == 7

        # Lösche "apple" - sollte mergen
        pt.delete("apple")
        assert pt.size() == 6
        assert pt.contains("app")
        assert pt.contains("application")

        # Lösche "app" - sollte wieder mergen
        pt.delete("app")
        assert pt.size() == 5
        assert pt.contains("application")
        assert pt.contains("apply")

        # Lösche "bandana"
        pt.delete("bandana")
        assert pt.size() == 4
        assert pt.contains("banana")
        assert pt.contains("band")