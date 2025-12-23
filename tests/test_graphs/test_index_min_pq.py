"""Tests für IndexMinPQ."""

import pytest

from src.algs4.pva_4_graphs import IndexMinPQ


class TestIndexMinPQ:
    """Tests für die IndexMinPQ-Klasse."""

    def test_create_pq(self):
        """Test: Erstelle eine neue Priority Queue."""
        pq = IndexMinPQ(5)
        assert pq.is_empty()
        assert pq.size() == 0

    def test_insert_single_element(self):
        """Test: Füge ein Element ein."""
        pq = IndexMinPQ(5)
        pq.insert(0, 1.0)
        assert not pq.is_empty()
        assert pq.size() == 1

    def test_insert_multiple_elements(self):
        """Test: Füge mehrere Elemente ein."""
        pq = IndexMinPQ(5)
        pq.insert(0, 1.0)
        pq.insert(1, 0.5)
        pq.insert(2, 2.0)
        assert pq.size() == 3

    def test_del_min_returns_minimum(self):
        """Test: del_min() gibt das Element mit kleinster Priorität zurück."""
        pq = IndexMinPQ(5)
        pq.insert(0, 1.0)
        pq.insert(1, 0.5)
        pq.insert(2, 2.0)
        assert pq.del_min() == 1  # Index mit Priorität 0.5

    def test_del_min_order(self):
        """Test: del_min() gibt Elemente in aufsteigender Priorität zurück."""
        pq = IndexMinPQ(5)
        pq.insert(0, 3.0)
        pq.insert(1, 1.0)
        pq.insert(2, 2.0)
        assert pq.del_min() == 1
        assert pq.del_min() == 2
        assert pq.del_min() == 0

    def test_contains(self):
        """Test: contains() überprüft ob Index in PQ ist."""
        pq = IndexMinPQ(5)
        pq.insert(0, 1.0)
        assert pq.contains(0)
        assert not pq.contains(1)

    def test_change_key(self):
        """Test: change() ändert die Priorität eines Elements."""
        pq = IndexMinPQ(5)
        pq.insert(0, 1.0)
        pq.insert(1, 2.0)
        pq.change(0, 3.0)
        assert pq.del_min() == 1  # Index 1 hat jetzt kleinste Priorität

    def test_min_returns_minimum_key(self):
        """Test: min() gibt die kleinste Priorität zurück."""
        pq = IndexMinPQ(5)
        pq.insert(0, 1.0)
        pq.insert(1, 0.5)
        assert pq.min() == 0.5

    def test_size_after_operations(self):
        """
        Verifies that size() reflects the number of elements after inserts and deletions.
        """
        pq = IndexMinPQ(5)
        assert pq.size() == 0
        pq.insert(0, 1.0)
        assert pq.size() == 1
        pq.insert(1, 2.0)
        assert pq.size() == 2
        pq.del_min()
        assert pq.size() == 1

    def test_is_empty_after_all_deletions(self):
        """Test: is_empty() gibt True nach Löschen aller Elemente."""
        pq = IndexMinPQ(5)
        pq.insert(0, 1.0)
        pq.del_min()
        assert pq.is_empty()

    def test_delete_method(self):
        """Test: delete() entfernt ein Element."""
        pq = IndexMinPQ(5)
        pq.insert(0, 1.0)
        pq.insert(1, 2.0)
        pq.delete(0)
        assert not pq.contains(0)
        assert pq.contains(1)

    def test_decrease_key(self):
        """Test: decrease_key() verringert die Priorität."""
        pq = IndexMinPQ(5)
        pq.insert(0, 5.0)
        pq.decrease_key(0, 1.0)
        assert pq.min() == 1.0

    def test_decrease_key_invalid_raises_error(self):
        """Test: decrease_key() mit höherem Wert wirft Exception."""
        pq = IndexMinPQ(5)
        pq.insert(0, 1.0)
        with pytest.raises((Exception, ValueError)):
            pq.decrease_key(0, 2.0)