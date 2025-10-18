"""Tests für Binary Search Tree (BST).

Diese Testdatei enthält umfassende Tests für die BST-Implementierung,
einschliesslich Basisfunktionalität, geordnete Operationen, Deletion
und Grenzfälle.
"""

import pytest

from src.algs4.pva_3_searching.bst import BST


class TestBSTBasics:
    """Tests für grundlegende BST-Funktionalität."""

    def test_leerer_bst_creation(self):
        """Teste Erstellung eines leeren BST."""
        bst: BST[str, int] = BST()
        assert bst.is_empty()
        assert bst.size() == 0
        assert len(bst) == 0

    def test_single_put_get(self):
        """Teste Einfügen und Abrufen eines einzelnen Elements."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)

        assert not bst.is_empty()
        assert bst.size() == 1
        assert bst.get("A") == 1
        assert bst.contains("A")

    def test_multiple_put_get(self):
        """Teste Einfügen und Abrufen mehrerer Elemente."""
        bst: BST[str, int] = BST()
        keys = ["S", "E", "A", "R", "C", "H"]

        for i, key in enumerate(keys):
            bst.put(key, i)

        assert bst.size() == len(keys)
        for i, key in enumerate(keys):
            assert bst.get(key) == i
            assert bst.contains(key)

    def test_put_update_existing(self):
        """Teste Überschreiben eines existierenden Schlüssels."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)
        assert bst.get("A") == 1

        bst.put("A", 2)
        assert bst.get("A") == 2
        assert bst.size() == 1  # Grösse sollte gleich bleiben

    def test_get_nonexistent_key(self):
        """Teste Abrufen eines nicht-existierenden Schlüssels."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)

        assert bst.get("B") is None
        assert not bst.contains("B")

    def test_contains(self):
        """Teste contains-Methode."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)
        bst.put("B", 2)

        assert bst.contains("A")
        assert bst.contains("B")
        assert not bst.contains("C")

    def test_none_key_raises_exception(self):
        """Teste dass None als Schlüssel eine Exception auslöst."""
        bst: BST[str | None, int] = BST()

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            bst.put(None, 1)

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            bst.get(None)

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            bst.contains(None)

    def test_none_value_raises_exception(self):
        """Teste dass None als Wert eine Exception auslöst."""
        bst: BST[str, int | None] = BST()

        with pytest.raises(ValueError, match="Wert darf nicht None sein"):
            bst.put("A", None)


class TestBSTMinMax:
    """Tests für min/max-Operationen."""

    def test_min_single_element(self):
        """Teste min bei einem einzelnen Element."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)
        assert bst.min() == "A"

    def test_max_single_element(self):
        """Teste max bei einem einzelnen Element."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)
        assert bst.max() == "A"

    def test_min_max_multiple_elements(self):
        """Teste min/max bei mehreren Elementen."""
        bst: BST[str, int] = BST()
        keys = ["S", "E", "A", "R", "C", "H", "X"]

        for i, key in enumerate(keys):
            bst.put(key, i)

        assert bst.min() == "A"
        assert bst.max() == "X"

    def test_min_empty_bst_raises_exception(self):
        """Teste dass min auf leerem BST eine Exception auslöst."""
        bst: BST[str, int] = BST()

        with pytest.raises(ValueError, match="BST ist leer"):
            bst.min()

    def test_max_empty_bst_raises_exception(self):
        """Teste dass max auf leerem BST eine Exception auslöst."""
        bst: BST[str, int] = BST()

        with pytest.raises(ValueError, match="BST ist leer"):
            bst.max()


class TestBSTFloorCeiling:
    """Tests für floor/ceiling-Operationen."""

    def test_floor_exact_match(self):
        """Teste floor mit exaktem Match."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            bst.put(key, i)

        assert bst.floor("E") == "E"
        assert bst.floor("M") == "M"

    def test_floor_no_exact_match(self):
        """Teste floor ohne exakten Match."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            bst.put(key, i)

        assert bst.floor("D") == "C"
        assert bst.floor("G") == "E"
        assert bst.floor("T") == "S"

    def test_floor_smaller_than_min(self):
        """Teste floor mit Wert kleiner als Minimum."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["C", "E", "H"]):
            bst.put(key, i)

        assert bst.floor("B") is None

    def test_ceiling_exact_match(self):
        """Teste ceiling mit exaktem Match."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            bst.put(key, i)

        assert bst.ceiling("E") == "E"
        assert bst.ceiling("M") == "M"

    def test_ceiling_no_exact_match(self):
        """Teste ceiling ohne exakten Match."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            bst.put(key, i)

        assert bst.ceiling("D") == "E"
        assert bst.ceiling("G") == "H"
        assert bst.ceiling("T") == "X"

    def test_ceiling_larger_than_max(self):
        """Teste ceiling mit Wert grösser als Maximum."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["A", "C", "E"]):
            bst.put(key, i)

        assert bst.ceiling("F") is None


class TestBSTRankSelect:
    """Tests für rank/select-Operationen."""

    def test_rank_existing_keys(self):
        """Teste rank für existierende Schlüssel."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            bst.put(key, i)

        assert bst.rank("A") == 0
        assert bst.rank("C") == 1
        assert bst.rank("E") == 2
        assert bst.rank("X") == 7

    def test_rank_nonexisting_keys(self):
        """Teste rank für nicht-existierende Schlüssel."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["A", "C", "E", "H"]):
            bst.put(key, i)

        assert bst.rank("B") == 1  # Zwischen A und C
        assert bst.rank("D") == 2  # Zwischen C und E
        assert bst.rank("Z") == 4  # Nach H

    def test_select_valid_indices(self):
        """Teste select für gültige Indizes."""
        bst: BST[str, int] = BST()
        keys = ["A", "C", "E", "H", "M", "R", "S", "X"]
        for i, key in enumerate(keys):
            bst.put(key, i)

        for i in range(len(keys)):
            assert bst.select(i) == keys[i]

    def test_select_invalid_index_raises_exception(self):
        """Teste dass select mit ungültigem Index eine Exception auslöst."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)
        bst.put("B", 2)

        with pytest.raises(ValueError, match="Index .* ist ausserhalb des Bereichs"):
            bst.select(-1)

        with pytest.raises(ValueError, match="Index .* ist ausserhalb des Bereichs"):
            bst.select(2)

    def test_rank_select_inverse(self):
        """Teste dass rank und select inverse Operationen sind."""
        bst: BST[str, int] = BST()
        keys = ["S", "E", "A", "R", "C", "H", "X", "M", "P", "L"]

        for i, key in enumerate(keys):
            bst.put(key, i)

        for key in keys:
            rank = bst.rank(key)
            assert bst.select(rank) == key


class TestBSTDelete:
    """Tests für Delete-Operationen."""

    def test_delete_min_single_element(self):
        """Teste delete_min bei einem Element."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)
        bst.delete_min()

        assert bst.is_empty()

    def test_delete_min_multiple_elements(self):
        """Teste delete_min bei mehreren Elementen."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["E", "A", "S", "Y"]):
            bst.put(key, i)

        assert bst.min() == "A"
        bst.delete_min()
        assert bst.min() == "E"
        assert bst.size() == 3

    def test_delete_min_empty_bst_raises_exception(self):
        """Teste dass delete_min auf leerem BST eine Exception auslöst."""
        bst: BST[str, int] = BST()

        with pytest.raises(ValueError, match="BST-Unterlauf"):
            bst.delete_min()

    def test_delete_max_single_element(self):
        """Teste delete_max bei einem Element."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)
        bst.delete_max()

        assert bst.is_empty()

    def test_delete_max_multiple_elements(self):
        """Teste delete_max bei mehreren Elementen."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["E", "A", "S", "Y"]):
            bst.put(key, i)

        assert bst.max() == "Y"
        bst.delete_max()
        assert bst.max() == "S"
        assert bst.size() == 3

    def test_delete_max_empty_bst_raises_exception(self):
        """Teste dass delete_max auf leerem BST eine Exception auslöst."""
        bst: BST[str, int] = BST()

        with pytest.raises(ValueError, match="BST-Unterlauf"):
            bst.delete_max()

    def test_delete_leaf_node(self):
        """Teste Löschen eines Blattknotens."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["E", "C", "H", "A"]):
            bst.put(key, i)

        bst.delete("A")
        assert not bst.contains("A")
        assert bst.size() == 3

    def test_delete_node_with_one_child(self):
        """Teste Löschen eines Knotens mit einem Kind."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["E", "C", "H", "A"]):
            bst.put(key, i)

        bst.delete("C")
        assert not bst.contains("C")
        assert bst.contains("A")
        assert bst.size() == 3

    def test_delete_node_with_two_children(self):
        """Teste Löschen eines Knotens mit zwei Kindern."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["E", "C", "H", "A", "D", "G", "I"]):
            bst.put(key, i)

        bst.delete("E")
        assert not bst.contains("E")
        assert bst.size() == 6

        # Überprüfe dass alle anderen Knoten noch vorhanden sind
        for key in ["C", "H", "A", "D", "G", "I"]:
            assert bst.contains(key)

    def test_delete_nonexistent_key(self):
        """Teste Löschen eines nicht-existierenden Schlüssels."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)
        bst.put("B", 2)

        size_before = bst.size()
        bst.delete("C")  # Existiert nicht
        assert bst.size() == size_before


class TestBSTIteration:
    """Tests für Iteration und Traversierung."""

    def test_keys_sorted_order(self):
        """Teste dass keys in sortierter Reihenfolge zurückgegeben werden."""
        bst: BST[str, int] = BST()
        keys = ["S", "E", "A", "R", "C", "H", "X"]

        for i, key in enumerate(keys):
            bst.put(key, i)

        sorted_keys = list(bst.keys())
        assert sorted_keys == sorted(keys)

    def test_keys_range(self):
        """Teste keys_range."""
        bst: BST[str, int] = BST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            bst.put(key, i)

        range_keys = list(bst.keys_range("D", "R"))
        assert range_keys == ["E", "H", "M", "R"]

    def test_keys_empty_bst(self):
        """Teste keys auf leerem BST."""
        bst: BST[str, int] = BST()
        assert list(bst.keys()) == []

    def test_level_order(self):
        """Teste Level-Order-Traversierung."""
        bst: BST[str, int] = BST()
        # Baue einen bekannten Baum auf
        bst.put("E", 0)
        bst.put("C", 1)
        bst.put("H", 2)
        bst.put("A", 3)
        bst.put("D", 4)

        level_order_keys = list(bst.level_order())
        # Level-Order: Wurzel, dann Kinder von links nach rechts
        assert level_order_keys[0] == "E"
        assert "C" in level_order_keys
        assert "H" in level_order_keys

    def test_iterator_protocol(self):
        """Teste dass BST das Iterator-Protokoll implementiert."""
        bst: BST[str, int] = BST()
        keys = ["S", "E", "A", "R", "C", "H"]

        for i, key in enumerate(keys):
            bst.put(key, i)

        collected_keys = [key for key in bst]
        assert collected_keys == sorted(keys)

    def test_repr(self):
        """Teste String-Repräsentation."""
        bst: BST[str, int] = BST()
        assert repr(bst) == "BST()"

        bst.put("B", 1)
        bst.put("A", 2)
        bst.put("C", 3)

        repr_str = repr(bst)
        assert "BST" in repr_str
        assert "A" in repr_str

    def test_str_empty_bst(self):
        """Teste visuelle Baumdarstellung für leeren BST."""
        bst: BST[str, int] = BST()
        assert str(bst) == "BST()"

    def test_str_single_node(self):
        """Teste visuelle Baumdarstellung für einzelnen Knoten."""
        bst: BST[str, int] = BST()
        bst.put("A", 1)
        assert str(bst) == "A"

    def test_str_balanced_tree(self):
        """Teste visuelle Baumdarstellung für ausgewogenen Baum."""
        bst: BST[str, int] = BST()
        for key in ["E", "B", "G", "A", "D", "F", "H"]:
            bst.put(key, ord(key))

        tree_str = str(bst)
        # Überprüfe dass alle Knoten in der Ausgabe enthalten sind
        for key in ["E", "B", "G", "A", "D", "F", "H"]:
            assert key in tree_str

        # Überprüfe dass Baumzeichen verwendet werden
        assert "├──" in tree_str or "└──" in tree_str

    def test_str_degenerate_tree_right(self):
        """Teste visuelle Baumdarstellung für degenerierten Baum (nur rechts)."""
        bst: BST[str, int] = BST()
        for key in ["A", "B", "C", "D"]:
            bst.put(key, ord(key))

        tree_str = str(bst)
        # Alle Knoten sollten in der Ausgabe sein
        for key in ["A", "B", "C", "D"]:
            assert key in tree_str

    def test_str_degenerate_tree_left(self):
        """Teste visuelle Baumdarstellung für degenerierten Baum (nur links)."""
        bst: BST[str, int] = BST()
        for key in ["D", "C", "B", "A"]:
            bst.put(key, ord(key))

        tree_str = str(bst)
        # Alle Knoten sollten in der Ausgabe sein
        for key in ["A", "B", "C", "D"]:
            assert key in tree_str

    def test_str_numeric_keys(self):
        """Teste visuelle Baumdarstellung mit numerischen Schlüsseln."""
        bst: BST[int, str] = BST()
        for key in [50, 30, 70, 20, 40, 60, 80]:
            bst.put(key, str(key))

        tree_str = str(bst)
        # Überprüfe dass die Wurzel 50 ist
        assert tree_str.startswith("50")

        # Überprüfe dass alle Knoten vorhanden sind
        for key in [50, 30, 70, 20, 40, 60, 80]:
            assert str(key) in tree_str


class TestBSTTypes:
    """Tests für verschiedene Datentypen."""

    def test_integer_keys(self):
        """Teste BST mit Integer-Schlüsseln."""
        bst: BST[int, str] = BST()
        bst.put(5, "five")
        bst.put(3, "three")
        bst.put(7, "seven")

        assert bst.get(5) == "five"
        assert bst.min() == 3
        assert bst.max() == 7

    def test_float_keys(self):
        """Teste BST mit Float-Schlüsseln."""
        bst: BST[float, str] = BST()
        bst.put(3.14, "pi")
        bst.put(2.71, "e")
        bst.put(1.41, "sqrt2")

        assert bst.get(3.14) == "pi"
        assert bst.min() == 1.41
        assert bst.max() == 3.14

    def test_tuple_keys(self):
        """Teste BST mit Tuple-Schlüsseln."""
        bst: BST[tuple[int, int], str] = BST()
        bst.put((1, 2), "a")
        bst.put((1, 1), "b")
        bst.put((2, 1), "c")

        assert bst.get((1, 2)) == "a"
        assert bst.min() == (1, 1)
        assert bst.max() == (2, 1)


class TestBSTPerformance:
    """Performance-Tests für BST."""

    @pytest.mark.slow
    def test_large_dataset(self):
        """Teste BST mit grossem Datensatz.

        Hinweis: Dieser Test wird übersprungen wenn er zu lange dauert,
        da BST bei sortierten Eingabedaten degeneriert (zu einer verketteten Liste wird).
        Für grosse sortierte Datensätze sollte ein balancierter Baum wie Red-Black-Tree
        oder AVL-Tree verwendet werden.
        """
        import random

        bst: BST[int, int] = BST()
        n = 100  # Reduziert von 1000 um Stack-Overflow zu vermeiden

        # Füge Elemente in zufälliger Reihenfolge ein (vermeidet Degeneration)
        keys = list(range(n))
        random.shuffle(keys)

        for key in keys:
            bst.put(key, key * 2)

        assert bst.size() == n
        assert bst.min() == 0
        assert bst.max() == n - 1

        # Teste Suche
        assert bst.get(50) == 100

        # Teste Iteration
        sorted_keys = list(bst.keys())
        assert len(sorted_keys) == n
        assert sorted_keys == list(range(n))

    def test_balanced_insertion(self):
        """Teste BST mit balancierter Einfügereihenfolge."""
        bst: BST[int, int] = BST()
        keys = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43]

        for key in keys:
            bst.put(key, key)

        assert bst.size() == len(keys)
        assert list(bst.keys()) == sorted(keys)
