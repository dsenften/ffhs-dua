"""
Tests für die Bag-Datenstruktur.
"""

import pytest
from src.algs4.fundamentals.bag import Bag


class TestBag:
    """Test-Klasse für die Bag-Datenstruktur."""

    def test_empty_bag_creation(self, empty_bag):
        """Test: Leerer Bag wird korrekt erstellt."""
        assert empty_bag.is_empty()
        assert empty_bag.size() == 0
        assert len(empty_bag) == 0

    def test_add_single_item(self, empty_bag):
        """Test: Einzelnes Element hinzufügen."""
        empty_bag.add("test")
        assert not empty_bag.is_empty()
        assert empty_bag.size() == 1
        assert len(empty_bag) == 1
        assert "test" in empty_bag

    @pytest.mark.parametrize("items", [
        [1, 2, 3],
        ["a", "b", "c"],
        [1.1, 2.2, 3.3]
    ])
    def test_add_multiple_items(self, empty_bag, items):
        """Test: Mehrere Elemente hinzufügen."""
        for item in items:
            empty_bag.add(item)
        assert empty_bag.size() == len(items)
        for item in items:
            assert item in empty_bag

    def test_iteration(self, empty_bag, sample_integers):
        """Test: Iteration über Bag-Elemente."""
        for item in sample_integers:
            empty_bag.add(item)
        
        collected_items = list(empty_bag)
        assert len(collected_items) == len(sample_integers)
        
        # Alle ursprünglichen Elemente sollten in der Iteration enthalten sein
        for item in sample_integers:
            assert item in collected_items

    def test_contains_method(self, empty_bag):
        """Test: contains-Methode und in-Operator."""
        empty_bag.add("apple")
        empty_bag.add("banana")
        
        assert empty_bag.contains("apple")
        assert "banana" in empty_bag
        assert not empty_bag.contains("cherry")
        assert "cherry" not in empty_bag

    def test_remove_single_item(self, empty_bag):
        """Test: Einzelnes Element entfernen."""
        empty_bag.add("test")
        assert empty_bag.remove("test")
        assert empty_bag.is_empty()
        assert not empty_bag.remove("nonexistent")

    def test_remove_all_items(self, empty_bag):
        """Test: Alle Vorkommen eines Elements entfernen."""
        empty_bag.add("duplicate")
        empty_bag.add("unique")
        empty_bag.add("duplicate")
        empty_bag.add("duplicate")
        
        removed_count = empty_bag.remove_all("duplicate")
        assert removed_count == 3
        assert empty_bag.size() == 1
        assert "unique" in empty_bag
        assert "duplicate" not in empty_bag

    def test_clear_bag(self, empty_bag, sample_integers):
        """Test: Bag leeren."""
        for item in sample_integers:
            empty_bag.add(item)
        
        empty_bag.clear()
        assert empty_bag.is_empty()
        assert empty_bag.size() == 0

    def test_peek_method(self, empty_bag):
        """Test: peek-Methode."""
        assert empty_bag.peek() is None
        
        empty_bag.add("first")
        empty_bag.add("second")
        
        peeked_item = empty_bag.peek()
        assert peeked_item == "second"  # Letztes hinzugefügtes Element
        assert empty_bag.size() == 2  # Größe sollte unverändert sein

    def test_to_list_conversion(self, empty_bag, sample_strings):
        """Test: Konvertierung zu Liste."""
        for item in sample_strings:
            empty_bag.add(item)
        
        bag_list = empty_bag.to_list()
        assert len(bag_list) == len(sample_strings)
        for item in sample_strings:
            assert item in bag_list

    def test_string_representation(self, empty_bag):
        """Test: String-Repräsentation."""
        assert str(empty_bag) == "{}"
        
        empty_bag.add(1)
        empty_bag.add(2)
        
        str_repr = str(empty_bag)
        assert str_repr.startswith("{")
        assert str_repr.endswith("}")
        assert "1" in str_repr
        assert "2" in str_repr

    @pytest.mark.unit
    def test_type_consistency(self):
        """Test: Typ-Konsistenz mit generischen Typen."""
        int_bag = Bag[int]()
        int_bag.add(42)
        assert 42 in int_bag
        
        str_bag = Bag[str]()
        str_bag.add("hello")
        assert "hello" in str_bag

    @pytest.mark.slow
    def test_large_dataset_performance(self, large_dataset):
        """Test: Performance mit großem Datensatz."""
        bag = Bag[int]()
        
        # Hinzufügen vieler Elemente
        for item in large_dataset:
            bag.add(item)
        
        assert bag.size() == len(large_dataset)
        
        # Überprüfung der Iteration
        collected = list(bag)
        assert len(collected) == len(large_dataset)
