"""Tests für AVL Tree (selbstbalancierender binärer Suchbaum).

Diese Testdatei enthält umfassende Tests für die AVL-Implementierung,
einschliesslich Balancierung, Rotationen und alle Standard-Operationen.
"""

import random

import pytest

from src.algs4.pva_3_searching.avl import AVL


class TestAVLBasics:
    """Tests für grundlegende AVL-Funktionalität."""

    def test_leerer_avl_creation(self):
        """Teste Erstellung eines leeren AVL-Baums."""
        avl: AVL[str, int] = AVL()
        assert avl.is_empty()
        assert avl.size() == 0
        assert len(avl) == 0
        assert avl.height() == -1

    def test_single_put_get(self):
        """Teste Einfügen und Abrufen eines einzelnen Elements."""
        avl: AVL[str, int] = AVL()
        avl.put("A", 1)

        assert not avl.is_empty()
        assert avl.size() == 1
        assert avl.height() == 0
        assert avl.get("A") == 1
        assert avl.contains("A")

    def test_multiple_put_get(self):
        """Teste Einfügen und Abrufen mehrerer Elemente."""
        avl: AVL[str, int] = AVL()
        keys = ["S", "E", "A", "R", "C", "H"]

        for i, key in enumerate(keys):
            avl.put(key, i)

        assert avl.size() == len(keys)
        for i, key in enumerate(keys):
            assert avl.get(key) == i
            assert avl.contains(key)

    def test_put_update_existing(self):
        """Teste Überschreiben eines existierenden Schlüssels."""
        avl: AVL[str, int] = AVL()
        avl.put("A", 1)
        assert avl.get("A") == 1

        avl.put("A", 2)
        assert avl.get("A") == 2
        assert avl.size() == 1  # Grösse sollte gleich bleiben

    def test_get_nonexistent_key(self):
        """Teste Abrufen eines nicht-existierenden Schlüssels."""
        avl: AVL[str, int] = AVL()
        avl.put("A", 1)

        assert avl.get("B") is None
        assert not avl.contains("B")

    def test_contains(self):
        """Teste contains-Methode."""
        avl: AVL[str, int] = AVL()
        avl.put("A", 1)
        avl.put("B", 2)

        assert avl.contains("A")
        assert avl.contains("B")
        assert not avl.contains("C")

    def test_none_key_raises_exception(self):
        """Teste dass None als Schlüssel eine Exception auslöst."""
        avl: AVL[str | None, int] = AVL()

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            avl.put(None, 1)

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            avl.get(None)

        with pytest.raises(ValueError, match="Schlüssel darf nicht None sein"):
            avl.contains(None)

    def test_none_value_raises_exception(self):
        """Teste dass None als Wert eine Exception auslöst."""
        avl: AVL[str, int | None] = AVL()

        with pytest.raises(ValueError, match="Wert darf nicht None sein"):
            avl.put("A", None)


class TestAVLBalancing:
    """Tests für AVL-Balancierung und Rotationen."""

    def test_right_rotation(self):
        """Teste Rechtsrotation (Left-Left Fall)."""
        avl: AVL[int, int] = AVL()

        # Einfügen in absteigender Reihenfolge erzwingt Rechtsrotation
        for key in [3, 2, 1]:
            avl.put(key, key)

        # Baum sollte balanciert sein
        assert avl.height() <= 1
        assert avl.size() == 3

        # Alle Elemente sollten vorhanden sein
        for key in [1, 2, 3]:
            assert avl.contains(key)

    def test_left_rotation(self):
        """Teste Linksrotation (Right-Right Fall)."""
        avl: AVL[int, int] = AVL()

        # Einfügen in aufsteigender Reihenfolge erzwingt Linksrotation
        for key in [1, 2, 3]:
            avl.put(key, key)

        # Baum sollte balanciert sein
        assert avl.height() <= 1
        assert avl.size() == 3

        # Alle Elemente sollten vorhanden sein
        for key in [1, 2, 3]:
            assert avl.contains(key)

    def test_left_right_rotation(self):
        """Teste Doppelrotation Left-Right."""
        avl: AVL[int, int] = AVL()

        # Einfüge-Reihenfolge die Left-Right-Rotation erzwingt
        avl.put(3, 3)
        avl.put(1, 1)
        avl.put(2, 2)  # Sollte Left-Right-Rotation auslösen

        # Baum sollte balanciert sein
        assert avl.height() <= 1
        assert avl.size() == 3

        # Alle Elemente sollten vorhanden sein
        for key in [1, 2, 3]:
            assert avl.contains(key)

    def test_right_left_rotation(self):
        """Teste Doppelrotation Right-Left."""
        avl: AVL[int, int] = AVL()

        # Einfüge-Reihenfolge die Right-Left-Rotation erzwingt
        avl.put(1, 1)
        avl.put(3, 3)
        avl.put(2, 2)  # Sollte Right-Left-Rotation auslösen

        # Baum sollte balanciert sein
        assert avl.height() <= 1
        assert avl.size() == 3

        # Alle Elemente sollten vorhanden sein
        for key in [1, 2, 3]:
            assert avl.contains(key)

    def test_sequential_insertion_keeps_balanced(self):
        """Teste dass sequentielle Einfügung den Baum balanciert hält."""
        avl: AVL[int, int] = AVL()

        # Füge viele Elemente in sortierter Reihenfolge ein
        n = 20
        for i in range(n):
            avl.put(i, i)

        # Höhe sollte logarithmisch sein (nicht linear wie bei unbalanciertem BST)
        import math

        max_height = math.ceil(1.44 * math.log2(n + 2))  # AVL maximale Höhe
        assert avl.height() <= max_height

        # Alle Elemente sollten vorhanden sein
        assert avl.size() == n
        for i in range(n):
            assert avl.contains(i)

    def test_random_insertion_keeps_balanced(self):
        """Teste dass zufällige Einfügung den Baum balanciert hält."""
        avl: AVL[int, int] = AVL()

        n = 50
        keys = list(range(n))
        random.shuffle(keys)

        for key in keys:
            avl.put(key, key)

        # Höhe sollte logarithmisch sein
        import math

        max_height = math.ceil(1.44 * math.log2(n + 2))
        assert avl.height() <= max_height
        assert avl.size() == n


class TestAVLMinMax:
    """Tests für min/max-Operationen."""

    def test_min_single_element(self):
        """Teste min bei einem einzelnen Element."""
        avl: AVL[str, int] = AVL()
        avl.put("A", 1)
        assert avl.min() == "A"

    def test_max_single_element(self):
        """Teste max bei einem einzelnen Element."""
        avl: AVL[str, int] = AVL()
        avl.put("A", 1)
        assert avl.max() == "A"

    def test_min_max_multiple_elements(self):
        """Teste min/max bei mehreren Elementen."""
        avl: AVL[str, int] = AVL()
        keys = ["S", "E", "A", "R", "C", "H", "X"]

        for i, key in enumerate(keys):
            avl.put(key, i)

        assert avl.min() == "A"
        assert avl.max() == "X"

    def test_min_empty_avl_raises_exception(self):
        """Teste dass min auf leerem AVL-Baum eine Exception auslöst."""
        avl: AVL[str, int] = AVL()

        with pytest.raises(ValueError, match="AVL-Baum ist leer"):
            avl.min()

    def test_max_empty_avl_raises_exception(self):
        """Teste dass max auf leerem AVL-Baum eine Exception auslöst."""
        avl: AVL[str, int] = AVL()

        with pytest.raises(ValueError, match="AVL-Baum ist leer"):
            avl.max()


class TestAVLDelete:
    """Tests für Delete-Operationen mit Balancierung."""

    def test_delete_min_single_element(self):
        """Teste delete_min bei einem Element."""
        avl: AVL[str, int] = AVL()
        avl.put("A", 1)
        avl.delete_min()

        assert avl.is_empty()

    def test_delete_min_multiple_elements(self):
        """Teste delete_min bei mehreren Elementen."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["E", "A", "S", "Y"]):
            avl.put(key, i)

        assert avl.min() == "A"
        avl.delete_min()
        assert avl.min() == "E"
        assert avl.size() == 3

    def test_delete_min_empty_avl_raises_exception(self):
        """Teste dass delete_min auf leerem AVL-Baum eine Exception auslöst."""
        avl: AVL[str, int] = AVL()

        with pytest.raises(ValueError, match="AVL-Baum-Unterlauf"):
            avl.delete_min()

    def test_delete_max_single_element(self):
        """Teste delete_max bei einem Element."""
        avl: AVL[str, int] = AVL()
        avl.put("A", 1)
        avl.delete_max()

        assert avl.is_empty()

    def test_delete_max_multiple_elements(self):
        """Teste delete_max bei mehreren Elementen."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["E", "A", "S", "Y"]):
            avl.put(key, i)

        assert avl.max() == "Y"
        avl.delete_max()
        assert avl.max() == "S"
        assert avl.size() == 3

    def test_delete_max_empty_avl_raises_exception(self):
        """Teste dass delete_max auf leerem AVL-Baum eine Exception auslöst."""
        avl: AVL[str, int] = AVL()

        with pytest.raises(ValueError, match="AVL-Baum-Unterlauf"):
            avl.delete_max()

    def test_delete_leaf_node(self):
        """Teste Löschen eines Blattknotens."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["E", "C", "H", "A"]):
            avl.put(key, i)

        avl.delete("A")
        assert not avl.contains("A")
        assert avl.size() == 3

    def test_delete_node_with_one_child(self):
        """Teste Löschen eines Knotens mit einem Kind."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["E", "C", "H", "A"]):
            avl.put(key, i)

        avl.delete("C")
        assert not avl.contains("C")
        assert avl.contains("A")
        assert avl.size() == 3

    def test_delete_node_with_two_children(self):
        """Teste Löschen eines Knotens mit zwei Kindern."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["E", "C", "H", "A", "D", "G", "I"]):
            avl.put(key, i)

        avl.delete("E")
        assert not avl.contains("E")
        assert avl.size() == 6

        # Überprüfe dass alle anderen Knoten noch vorhanden sind
        for key in ["C", "H", "A", "D", "G", "I"]:
            assert avl.contains(key)

    def test_delete_nonexistent_key(self):
        """Teste Löschen eines nicht-existierenden Schlüssels."""
        avl: AVL[str, int] = AVL()
        avl.put("A", 1)
        avl.put("B", 2)

        size_before = avl.size()
        avl.delete("C")  # Existiert nicht
        assert avl.size() == size_before

    def test_delete_maintains_balance(self):
        """Teste dass Löschen die Balancierung erhält."""
        avl: AVL[int, int] = AVL()

        # Füge viele Elemente ein
        n = 20
        for i in range(n):
            avl.put(i, i)

        # Lösche die Hälfte
        for i in range(0, n, 2):
            avl.delete(i)

        # Baum sollte immer noch balanciert sein
        import math

        remaining = n // 2
        max_height = math.ceil(1.44 * math.log2(remaining + 2))
        assert avl.height() <= max_height
        assert avl.size() == remaining


class TestAVLFloorCeiling:
    """Tests für floor/ceiling-Operationen."""

    def test_floor_exact_match(self):
        """Teste floor mit exaktem Match."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            avl.put(key, i)

        assert avl.floor("E") == "E"
        assert avl.floor("M") == "M"

    def test_floor_no_exact_match(self):
        """Teste floor ohne exakten Match."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            avl.put(key, i)

        assert avl.floor("D") == "C"
        assert avl.floor("G") == "E"
        assert avl.floor("T") == "S"

    def test_floor_smaller_than_min(self):
        """Teste floor mit Wert kleiner als Minimum."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["C", "E", "H"]):
            avl.put(key, i)

        assert avl.floor("B") is None

    def test_ceiling_exact_match(self):
        """Teste ceiling mit exaktem Match."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            avl.put(key, i)

        assert avl.ceiling("E") == "E"
        assert avl.ceiling("M") == "M"

    def test_ceiling_no_exact_match(self):
        """Teste ceiling ohne exakten Match."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            avl.put(key, i)

        assert avl.ceiling("D") == "E"
        assert avl.ceiling("G") == "H"
        assert avl.ceiling("T") == "X"

    def test_ceiling_larger_than_max(self):
        """Teste ceiling mit Wert grösser als Maximum."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["A", "C", "E"]):
            avl.put(key, i)

        assert avl.ceiling("F") is None


class TestAVLRankSelect:
    """Tests für rank/select-Operationen."""

    def test_rank_existing_keys(self):
        """Teste rank für existierende Schlüssel."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            avl.put(key, i)

        assert avl.rank("A") == 0
        assert avl.rank("C") == 1
        assert avl.rank("E") == 2
        assert avl.rank("X") == 7

    def test_rank_nonexisting_keys(self):
        """Teste rank für nicht-existierende Schlüssel."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["A", "C", "E", "H"]):
            avl.put(key, i)

        assert avl.rank("B") == 1  # Zwischen A und C
        assert avl.rank("D") == 2  # Zwischen C und E
        assert avl.rank("Z") == 4  # Nach H

    def test_select_valid_indices(self):
        """Teste select für gültige Indizes."""
        avl: AVL[str, int] = AVL()
        keys = ["A", "C", "E", "H", "M", "R", "S", "X"]
        for i, key in enumerate(keys):
            avl.put(key, i)

        for i in range(len(keys)):
            assert avl.select(i) == keys[i]

    def test_select_invalid_index_raises_exception(self):
        """Teste dass select mit ungültigem Index eine Exception auslöst."""
        avl: AVL[str, int] = AVL()
        avl.put("A", 1)
        avl.put("B", 2)

        with pytest.raises(ValueError, match="Index .* ist ausserhalb des Bereichs"):
            avl.select(-1)

        with pytest.raises(ValueError, match="Index .* ist ausserhalb des Bereichs"):
            avl.select(2)

    def test_rank_select_inverse(self):
        """Teste dass rank und select inverse Operationen sind."""
        avl: AVL[str, int] = AVL()
        keys = ["S", "E", "A", "R", "C", "H", "X", "M", "P", "L"]

        for i, key in enumerate(keys):
            avl.put(key, i)

        for key in keys:
            rank = avl.rank(key)
            assert avl.select(rank) == key


class TestAVLIteration:
    """Tests für Iteration und Traversierung."""

    def test_keys_sorted_order(self):
        """Teste dass keys in sortierter Reihenfolge zurückgegeben werden."""
        avl: AVL[str, int] = AVL()
        keys = ["S", "E", "A", "R", "C", "H", "X"]

        for i, key in enumerate(keys):
            avl.put(key, i)

        sorted_keys = list(avl.keys())
        assert sorted_keys == sorted(keys)

    def test_keys_range(self):
        """Teste keys_range."""
        avl: AVL[str, int] = AVL()
        for i, key in enumerate(["A", "C", "E", "H", "M", "R", "S", "X"]):
            avl.put(key, i)

        range_keys = list(avl.keys_range("D", "R"))
        assert range_keys == ["E", "H", "M", "R"]

    def test_keys_empty_avl(self):
        """Teste keys auf leerem AVL-Baum."""
        avl: AVL[str, int] = AVL()
        assert list(avl.keys()) == []

    def test_level_order(self):
        """Teste Level-Order-Traversierung."""
        avl: AVL[str, int] = AVL()
        # Baue einen bekannten Baum auf
        avl.put("E", 0)
        avl.put("C", 1)
        avl.put("H", 2)
        avl.put("A", 3)
        avl.put("D", 4)

        level_order_keys = list(avl.level_order())
        # Level-Order: Wurzel, dann Kinder von links nach rechts
        assert level_order_keys[0] in [
            "E",
            "C",
            "D",
        ]  # Wurzel kann variieren durch Balancierung

    def test_iterator_protocol(self):
        """Teste dass AVL-Baum das Iterator-Protokoll implementiert."""
        avl: AVL[str, int] = AVL()
        keys = ["S", "E", "A", "R", "C", "H"]

        for i, key in enumerate(keys):
            avl.put(key, i)

        collected_keys = list(avl)
        assert collected_keys == sorted(keys)

    def test_repr(self):
        """Teste String-Repräsentation."""
        avl: AVL[str, int] = AVL()
        assert repr(avl) == "AVL()"

        avl.put("B", 1)
        avl.put("A", 2)
        avl.put("C", 3)

        repr_str = repr(avl)
        assert "AVL" in repr_str
        assert "A" in repr_str

    def test_str_visualization(self):
        """Teste visuelle Baumdarstellung."""
        avl: AVL[str, int] = AVL()
        assert str(avl) == "AVL()"

        avl.put("E", 1)
        tree_str = str(avl)
        assert "E" in tree_str
        assert "h:0" in tree_str  # Höhe sollte angezeigt werden


class TestAVLPerformance:
    """Performance-Tests für AVL-Baum."""

    @pytest.mark.slow
    def test_large_sequential_dataset(self):
        """Teste AVL-Baum mit grossem sequentiellem Datensatz.

        Im Gegensatz zum unbalancierten BST sollte der AVL-Baum
        auch bei sortierten Eingabedaten logarithmische Höhe behalten.
        """
        avl: AVL[int, int] = AVL()
        n = 1000

        # Füge Elemente in sortierter Reihenfolge ein
        for key in range(n):
            avl.put(key, key * 2)

        # Höhe sollte logarithmisch sein
        import math

        max_height = math.ceil(1.44 * math.log2(n + 2))
        assert avl.height() <= max_height
        assert avl.size() == n
        assert avl.min() == 0
        assert avl.max() == n - 1

        # Teste Suche
        assert avl.get(500) == 1000

        # Teste Iteration
        sorted_keys = list(avl.keys())
        assert len(sorted_keys) == n
        assert sorted_keys == list(range(n))

    @pytest.mark.slow
    def test_large_random_dataset(self):
        """Teste AVL-Baum mit grossem zufälligem Datensatz."""
        avl: AVL[int, int] = AVL()
        n = 1000

        # Füge Elemente in zufälliger Reihenfolge ein
        keys = list(range(n))
        random.shuffle(keys)

        for key in keys:
            avl.put(key, key * 2)

        # Höhe sollte logarithmisch sein
        import math

        max_height = math.ceil(1.44 * math.log2(n + 2))
        assert avl.height() <= max_height
        assert avl.size() == n

    def test_balanced_insertion(self):
        """Teste AVL-Baum mit balancierter Einfügereihenfolge."""
        avl: AVL[int, int] = AVL()
        keys = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43]

        for key in keys:
            avl.put(key, key)

        assert avl.size() == len(keys)
        assert list(avl.keys()) == sorted(keys)

        # Höhe sollte klein sein
        assert avl.height() <= 4


class TestAVLTypes:
    """Tests für verschiedene Datentypen."""

    def test_integer_keys(self):
        """Teste AVL-Baum mit Integer-Schlüsseln."""
        avl: AVL[int, str] = AVL()
        avl.put(5, "five")
        avl.put(3, "three")
        avl.put(7, "seven")

        assert avl.get(5) == "five"
        assert avl.min() == 3
        assert avl.max() == 7

    def test_float_keys(self):
        """Teste AVL-Baum mit Float-Schlüsseln."""
        avl: AVL[float, str] = AVL()
        avl.put(3.14, "pi")
        avl.put(2.71, "e")
        avl.put(1.41, "sqrt2")

        assert avl.get(3.14) == "pi"
        assert avl.min() == 1.41
        assert avl.max() == 3.14

    def test_tuple_keys(self):
        """Teste AVL-Baum mit Tuple-Schlüsseln."""
        avl: AVL[tuple[int, int], str] = AVL()
        avl.put((1, 2), "a")
        avl.put((1, 1), "b")
        avl.put((2, 1), "c")

        assert avl.get((1, 2)) == "a"
        assert avl.min() == (1, 1)
        assert avl.max() == (2, 1)
