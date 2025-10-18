"""Tests für Red-Black BST (Rot-Schwarz-Baum).

Diese Testdatei enthält umfassende Tests für die Red-Black-BST-Implementierung,
einschliesslich Balancierung, Farbinvarianten und alle Standard-Operationen.
"""

import random

import pytest

from src.algs4.pva_3_searching.red_black_bst import RedBlackBST


class TestRedBlackBSTBasics:
    """Tests für grundlegende Red-Black-BST-Funktionalität."""

    def test_leerer_rb_bst_creation(self):
        """Teste Erstellung eines leeren Red-Black-BST."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        assert rbt.is_empty()
        assert rbt.size() == 0
        assert len(rbt) == 0
        assert rbt.height() == -1

    def test_single_put_get(self):
        """Teste Einfügen und Abrufen eines einzelnen Elements."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("A", 1)

        assert not rbt.is_empty()
        assert rbt.size() == 1
        assert rbt.height() == 0
        assert rbt.get("A") == 1
        assert rbt.contains("A")

    def test_multiple_put_get(self):
        """Teste Einfügen und Abrufen mehrerer Elemente."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        keys = ["S", "E", "A", "R", "C", "H"]

        for i, key in enumerate(keys):
            rbt.put(key, i)

        assert rbt.size() == len(keys)
        for i, key in enumerate(keys):
            assert rbt.get(key) == i
            assert rbt.contains(key)

    def test_put_update_existing(self):
        """Teste Überschreiben eines existierenden Schlüssels."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("A", 1)
        assert rbt.get("A") == 1

        rbt.put("A", 2)
        assert rbt.get("A") == 2
        assert rbt.size() == 1

    def test_get_nonexistent_key(self):
        """Teste Abrufen eines nicht-existierenden Schlüssels."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("A", 1)

        assert rbt.get("B") is None
        assert not rbt.contains("B")

    def test_contains(self):
        """Teste contains-Methode."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("A", 1)
        rbt.put("B", 2)

        assert rbt.contains("A")
        assert rbt.contains("B")
        assert not rbt.contains("C")

    def test_none_key_raises_exception(self):
        """Teste dass None als Schlüssel eine Exception auslöst."""
        rbt: RedBlackBST[str | None, int] = RedBlackBST()

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            rbt.put(None, 1)

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            rbt.get(None)

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            rbt.contains(None)

    def test_none_value_raises_exception(self):
        """Teste dass None als Wert eine Exception auslöst."""
        rbt: RedBlackBST[str, int | None] = RedBlackBST()

        with pytest.raises(ValueError, match="Wert darf nicht None sein"):
            rbt.put("A", None)


class TestRedBlackBSTBalancing:
    """Tests für Red-Black-BST-Balancierung."""

    def test_sequential_insertion_stays_balanced(self):
        """Teste dass sequentielle Einfügung balanciert bleibt."""
        rbt: RedBlackBST[int, int] = RedBlackBST()

        # Füge viele Elemente in sortierter Reihenfolge ein
        n = 20
        for i in range(n):
            rbt.put(i, i)

        # Höhe sollte logarithmisch sein
        import math

        max_height = 2 * math.ceil(math.log2(n + 1))  # Red-Black maximale Höhe
        assert rbt.height() <= max_height
        assert rbt.size() == n

    def test_random_insertion_stays_balanced(self):
        """Teste dass zufällige Einfügung balanciert bleibt."""
        rbt: RedBlackBST[int, int] = RedBlackBST()

        n = 50
        keys = list(range(n))
        random.shuffle(keys)

        for key in keys:
            rbt.put(key, key)

        # Höhe sollte logarithmisch sein
        import math

        max_height = 2 * math.ceil(math.log2(n + 1))
        assert rbt.height() <= max_height
        assert rbt.size() == n

    def test_root_is_always_black(self):
        """Teste dass die Wurzel immer schwarz ist."""
        rbt: RedBlackBST[int, int] = RedBlackBST()

        for i in range(10):
            rbt.put(i, i)
            # Wurzel muss immer schwarz sein
            assert rbt._root is not None
            assert rbt._root.color == RedBlackBST.BLACK


class TestRedBlackBSTMinMax:
    """Tests für min/max-Operationen."""

    def test_min_single_element(self):
        """Teste min bei einem einzelnen Element."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("A", 1)
        assert rbt.min() == "A"

    def test_max_single_element(self):
        """Teste max bei einem einzelnen Element."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("A", 1)
        assert rbt.max() == "A"

    def test_min_max_multiple_elements(self):
        """Teste min/max bei mehreren Elementen."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        keys = ["S", "E", "A", "R", "C", "H", "X"]

        for i, key in enumerate(keys):
            rbt.put(key, i)

        assert rbt.min() == "A"
        assert rbt.max() == "X"

    def test_min_empty_rbt_raises_exception(self):
        """Teste dass min auf leerem Baum eine Exception auslöst."""
        rbt: RedBlackBST[str, int] = RedBlackBST()

        with pytest.raises(ValueError, match="RB-Baum ist leer"):
            rbt.min()

    def test_max_empty_rbt_raises_exception(self):
        """Teste dass max auf leerem Baum eine Exception auslöst."""
        rbt: RedBlackBST[str, int] = RedBlackBST()

        with pytest.raises(ValueError, match="RB-Baum ist leer"):
            rbt.max()


class TestRedBlackBSTDelete:
    """Tests für Delete-Operationen mit Balancierung."""

    def test_delete_min_single_element(self):
        """Teste delete_min bei einem Element."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("A", 1)
        rbt.delete_min()

        assert rbt.is_empty()

    def test_delete_min_multiple_elements(self):
        """Teste delete_min bei mehreren Elementen."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["E", "A", "S", "Y"]):
            rbt.put(key, i)

        assert rbt.min() == "A"
        rbt.delete_min()
        assert rbt.min() == "E"
        assert rbt.size() == 3

    def test_delete_min_empty_rbt_raises_exception(self):
        """Teste dass delete_min auf leerem Baum eine Exception auslöst."""
        rbt: RedBlackBST[str, int] = RedBlackBST()

        with pytest.raises(ValueError, match="RB-Baum-Unterlauf"):
            rbt.delete_min()

    def test_delete_max_single_element(self):
        """Teste delete_max bei einem Element."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("A", 1)
        rbt.delete_max()

        assert rbt.is_empty()

    def test_delete_max_multiple_elements(self):
        """Teste delete_max bei mehreren Elementen."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["E", "A", "S", "Y"]):
            rbt.put(key, i)

        assert rbt.max() == "Y"
        rbt.delete_max()
        assert rbt.max() == "S"
        assert rbt.size() == 3

    def test_delete_max_empty_rbt_raises_exception(self):
        """Teste dass delete_max auf leerem Baum eine Exception auslöst."""
        rbt: RedBlackBST[str, int] = RedBlackBST()

        with pytest.raises(ValueError, match="RB-Baum-Unterlauf"):
            rbt.delete_max()

    def test_delete_specific_key(self):
        """Teste Löschen eines spezifischen Schlüssels."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["E", "C", "H", "A", "D", "G", "I"]):
            rbt.put(key, i)

        rbt.delete("E")
        assert not rbt.contains("E")
        assert rbt.size() == 6

        # Überprüfe dass alle anderen Knoten noch vorhanden sind
        for key in ["C", "H", "A", "D", "G", "I"]:
            assert rbt.contains(key)

    def test_delete_nonexistent_key(self):
        """Teste Löschen eines nicht-existierenden Schlüssels."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("A", 1)
        rbt.put("B", 2)

        size_before = rbt.size()
        rbt.delete("C")  # Existiert nicht
        assert rbt.size() == size_before

    def test_delete_maintains_balance(self):
        """Teste dass Löschen die Balancierung erhält."""
        rbt: RedBlackBST[int, int] = RedBlackBST()

        # Füge viele Elemente ein
        n = 20
        for i in range(n):
            rbt.put(i, i)

        # Lösche die Hälfte
        for i in range(0, n, 2):
            rbt.delete(i)

        # Baum sollte immer noch balanciert sein
        import math

        remaining = n // 2
        max_height = 2 * math.ceil(math.log2(remaining + 1))
        assert rbt.height() <= max_height
        assert rbt.size() == remaining


class TestRedBlackBSTFloorCeiling:
    """Tests für floor/ceiling-Operationen."""

    def test_floor_exact_match(self):
        """Teste floor mit exaktem Match."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            rbt.put(key, i)

        assert rbt.floor("E") == "E"
        assert rbt.floor("M") == "M"

    def test_floor_no_exact_match(self):
        """Teste floor ohne exakten Match."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            rbt.put(key, i)

        assert rbt.floor("D") == "C"
        assert rbt.floor("G") == "E"
        assert rbt.floor("T") == "S"

    def test_floor_smaller_than_min(self):
        """Teste floor mit Wert kleiner als Minimum."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["C", "E", "H"]):
            rbt.put(key, i)

        assert rbt.floor("B") is None

    def test_ceiling_exact_match(self):
        """Teste ceiling mit exaktem Match."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            rbt.put(key, i)

        assert rbt.ceiling("E") == "E"
        assert rbt.ceiling("M") == "M"

    def test_ceiling_no_exact_match(self):
        """Teste ceiling ohne exakten Match."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            rbt.put(key, i)

        assert rbt.ceiling("D") == "E"
        assert rbt.ceiling("G") == "H"
        assert rbt.ceiling("T") == "X"

    def test_ceiling_larger_than_max(self):
        """Teste ceiling mit Wert grösser als Maximum."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["A", "C", "E"]):
            rbt.put(key, i)

        assert rbt.ceiling("F") is None


class TestRedBlackBSTRankSelect:
    """Tests für rank/select-Operationen."""

    def test_rank_existing_keys(self):
        """Teste rank für existierende Schlüssel."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            rbt.put(key, i)

        assert rbt.rank("A") == 0
        assert rbt.rank("C") == 1
        assert rbt.rank("E") == 2
        assert rbt.rank("X") == 7

    def test_rank_nonexisting_keys(self):
        """Teste rank für nicht-existierende Schlüssel."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["A", "C", "E", "H"]):
            rbt.put(key, i)

        assert rbt.rank("B") == 1  # Zwischen A und C
        assert rbt.rank("D") == 2  # Zwischen C und E
        assert rbt.rank("Z") == 4  # Nach H

    def test_select_valid_indices(self):
        """Teste select für gültige Indizes."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        keys = ["A", "C", "E", "H", "M", "R", "S", "X"]
        for i, key in enumerate(keys):
            rbt.put(key, i)

        for i in range(len(keys)):
            assert rbt.select(i) == keys[i]

    def test_select_invalid_index_raises_exception(self):
        """Teste dass select mit ungültigem Index eine Exception auslöst."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("A", 1)
        rbt.put("B", 2)

        with pytest.raises(ValueError, match="Index .* ist ausserhalb des Bereichs"):
            rbt.select(-1)

        with pytest.raises(ValueError, match="Index .* ist ausserhalb des Bereichs"):
            rbt.select(2)

    def test_rank_select_inverse(self):
        """Teste dass rank und select inverse Operationen sind."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        keys = ["S", "E", "A", "R", "C", "H", "X", "M", "P", "L"]

        for i, key in enumerate(keys):
            rbt.put(key, i)

        for key in keys:
            rank = rbt.rank(key)
            assert rbt.select(rank) == key


class TestRedBlackBSTIteration:
    """Tests für Iteration und Traversierung."""

    def test_keys_sorted_order(self):
        """Teste dass keys in sortierter Reihenfolge zurückgegeben werden."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        keys = ["S", "E", "A", "R", "C", "H", "X"]

        for i, key in enumerate(keys):
            rbt.put(key, i)

        sorted_keys = list(rbt.keys())
        assert sorted_keys == sorted(keys)

    def test_keys_range(self):
        """Teste keys_range."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            rbt.put(key, i)

        range_keys = list(rbt.keys_range("D", "R"))
        assert range_keys == ["E", "H", "M", "R"]

    def test_keys_empty_rbt(self):
        """Teste keys auf leerem Baum."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        assert list(rbt.keys()) == []

    def test_level_order(self):
        """Teste Level-Order-Traversierung."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        rbt.put("E", 0)
        rbt.put("C", 1)
        rbt.put("H", 2)
        rbt.put("A", 3)
        rbt.put("D", 4)

        level_order_keys = list(rbt.level_order())
        # Erste Element ist Wurzel
        assert len(level_order_keys) == 5

    def test_iterator_protocol(self):
        """Teste dass Red-Black-BST das Iterator-Protokoll implementiert."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        keys = ["S", "E", "A", "R", "C", "H"]

        for i, key in enumerate(keys):
            rbt.put(key, i)

        collected_keys = [key for key in rbt]
        assert collected_keys == sorted(keys)

    def test_repr(self):
        """Teste String-Repräsentation."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        assert repr(rbt) == "RedBlackBST()"

        rbt.put("B", 1)
        rbt.put("A", 2)
        rbt.put("C", 3)

        repr_str = repr(rbt)
        assert "RedBlackBST" in repr_str
        assert "A" in repr_str

    def test_str_visualization(self):
        """Teste visuelle Baumdarstellung."""
        rbt: RedBlackBST[str, int] = RedBlackBST()
        assert str(rbt) == "RedBlackBST()"

        rbt.put("E", 1)
        tree_str = str(rbt)
        assert "E" in tree_str
        assert "(B)" in tree_str or "(R)" in tree_str  # Farbmarkierung


class TestRedBlackBSTPerformance:
    """Performance-Tests für Red-Black-BST."""

    @pytest.mark.slow
    def test_large_sequential_dataset(self):
        """Teste Red-Black-BST mit grossem sequentiellem Datensatz.

        Red-Black-BST sollte auch bei sortierten Eingabedaten
        logarithmische Höhe behalten.
        """
        rbt: RedBlackBST[int, int] = RedBlackBST()
        n = 1000

        # Füge Elemente in sortierter Reihenfolge ein
        for key in range(n):
            rbt.put(key, key * 2)

        # Höhe sollte logarithmisch sein
        import math

        max_height = 2 * math.ceil(math.log2(n + 1))
        assert rbt.height() <= max_height
        assert rbt.size() == n
        assert rbt.min() == 0
        assert rbt.max() == n - 1

        # Teste Suche
        assert rbt.get(500) == 1000

        # Teste Iteration
        sorted_keys = list(rbt.keys())
        assert len(sorted_keys) == n
        assert sorted_keys == list(range(n))

    @pytest.mark.slow
    def test_large_random_dataset(self):
        """Teste Red-Black-BST mit grossem zufälligem Datensatz."""
        rbt: RedBlackBST[int, int] = RedBlackBST()
        n = 1000

        # Füge Elemente in zufälliger Reihenfolge ein
        keys = list(range(n))
        random.shuffle(keys)

        for key in keys:
            rbt.put(key, key * 2)

        # Höhe sollte logarithmisch sein
        import math

        max_height = 2 * math.ceil(math.log2(n + 1))
        assert rbt.height() <= max_height
        assert rbt.size() == n

    def test_balanced_insertion(self):
        """Teste Red-Black-BST mit balancierter Einfügereihenfolge."""
        rbt: RedBlackBST[int, int] = RedBlackBST()
        keys = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43]

        for key in keys:
            rbt.put(key, key)

        assert rbt.size() == len(keys)
        assert list(rbt.keys()) == sorted(keys)

        # Höhe sollte klein sein
        assert rbt.height() <= 5


class TestRedBlackBSTTypes:
    """Tests für verschiedene Datentypen."""

    def test_integer_keys(self):
        """Teste Red-Black-BST mit Integer-Schlüsseln."""
        rbt: RedBlackBST[int, str] = RedBlackBST()
        rbt.put(5, "five")
        rbt.put(3, "three")
        rbt.put(7, "seven")

        assert rbt.get(5) == "five"
        assert rbt.min() == 3
        assert rbt.max() == 7

    def test_float_keys(self):
        """Teste Red-Black-BST mit Float-Schlüsseln."""
        rbt: RedBlackBST[float, str] = RedBlackBST()
        rbt.put(3.14, "pi")
        rbt.put(2.71, "e")
        rbt.put(1.41, "sqrt2")

        assert rbt.get(3.14) == "pi"
        assert rbt.min() == 1.41
        assert rbt.max() == 3.14

    def test_tuple_keys(self):
        """Teste Red-Black-BST mit Tuple-Schlüsseln."""
        rbt: RedBlackBST[tuple[int, int], str] = RedBlackBST()
        rbt.put((1, 2), "a")
        rbt.put((1, 1), "b")
        rbt.put((2, 1), "c")

        assert rbt.get((1, 2)) == "a"
        assert rbt.min() == (1, 1)
        assert rbt.max() == (2, 1)
