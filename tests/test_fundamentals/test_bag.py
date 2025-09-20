"""
Tests für die Bag-Datenstruktur.

Diese Datei enthält umfassende Tests für die Bag-Implementierung.
Verwendet Test-Vorrichtungen aus conftest.py für konsistente Testumgebungen.
"""

import pytest

from src.algs4.fundamentals.bag import Bag


class TestBag:
    """Test-Klasse für die Bag-Datenstruktur."""

    def test_empty_bag_creation(self, leerer_bag):
        """Test: Leerer Bag wird korrekt erstellt."""
        assert leerer_bag.is_empty()
        assert leerer_bag.size() == 0
        assert len(leerer_bag) == 0

    def test_add_single_item(self, leerer_bag):
        """Test: Einzelnes Element hinzufügen."""
        leerer_bag.add("test")
        assert not leerer_bag.is_empty()
        assert leerer_bag.size() == 1
        assert len(leerer_bag) == 1
        assert "test" in leerer_bag

    @pytest.mark.parametrize("items", [
        [1, 2, 3],
        ["a", "b", "c"],
        [1.1, 2.2, 3.3]
    ])
    def test_add_multiple_items(self, leerer_bag, items):
        """Test: Mehrere Elemente hinzufügen."""
        for item in items:
            leerer_bag.add(item)
        assert leerer_bag.size() == len(items)
        for item in items:
            assert item in leerer_bag

    def test_iteration(self, leerer_bag, beispiel_ganzzahlen):
        """Test: Iteration über Bag-Elemente."""
        for item in beispiel_ganzzahlen:
            leerer_bag.add(item)

        collected_items = list(leerer_bag)
        assert len(collected_items) == len(beispiel_ganzzahlen)

        # Alle ursprünglichen Elemente sollten in der Iteration enthalten sein
        for item in beispiel_ganzzahlen:
            assert item in collected_items

    def test_contains_method(self, leerer_bag):
        """Test: contains-Methode und in-Operator."""
        leerer_bag.add("apple")
        leerer_bag.add("banana")

        assert leerer_bag.contains("apple")
        assert "banana" in leerer_bag
        assert not leerer_bag.contains("cherry")
        assert "cherry" not in leerer_bag

    def test_remove_single_item(self, leerer_bag):
        """Test: Einzelnes Element entfernen."""
        leerer_bag.add("test")
        assert leerer_bag.remove("test")
        assert leerer_bag.is_empty()
        assert not leerer_bag.remove("nonexistent")

    def test_remove_all_items(self, leerer_bag):
        """Test: Alle Vorkommen eines Elements entfernen."""
        leerer_bag.add("duplicate")
        leerer_bag.add("unique")
        leerer_bag.add("duplicate")
        leerer_bag.add("duplicate")

        removed_count = leerer_bag.remove_all("duplicate")
        assert removed_count == 3
        assert leerer_bag.size() == 1
        assert "unique" in leerer_bag
        assert "duplicate" not in leerer_bag

    def test_clear_bag(self, leerer_bag, beispiel_ganzzahlen):
        """Test: Bag leeren."""
        for item in beispiel_ganzzahlen:
            leerer_bag.add(item)

        leerer_bag.clear()
        assert leerer_bag.is_empty()
        assert leerer_bag.size() == 0

    def test_peek_method(self, leerer_bag):
        """Test: peek-Methode."""
        assert leerer_bag.peek() is None

        leerer_bag.add("first")
        leerer_bag.add("second")

        peeked_item = leerer_bag.peek()
        assert peeked_item == "second"  # Letztes hinzugefügtes Element
        assert leerer_bag.size() == 2  # Grösse sollte unverändert sein

    def test_to_list_conversion(self, leerer_bag, beispiel_zeichenketten):
        """Test: Konvertierung zu Liste."""
        for item in beispiel_zeichenketten:
            leerer_bag.add(item)

        bag_list = leerer_bag.to_list()
        assert len(bag_list) == len(beispiel_zeichenketten)
        for item in beispiel_zeichenketten:
            assert item in bag_list

    def test_string_representation(self, leerer_bag):
        """Test: String-Repräsentation."""
        assert str(leerer_bag) == "{}"

        leerer_bag.add(1)
        leerer_bag.add(2)

        str_repr = str(leerer_bag)
        assert str_repr.startswith("{")
        assert str_repr.endswith("}")
        assert "1" in str_repr
        assert "2" in str_repr

    def test_type_consistency(self):
        """Test: Typ-Konsistenz bei verschiedenen Datentypen."""
        # Integer Bag
        int_bag = Bag[int]()
        int_bag.add(42)
        assert 42 in int_bag

        # String Bag
        str_bag = Bag[str]()
        str_bag.add("hello")
        assert "hello" in str_bag

    @pytest.mark.slow
    def test_large_dataset_performance(self, grosser_datensatz):
        """Test: Performance mit grossem Datensatz."""
        bag = Bag[int]()

        # Hinzufügen vieler Elemente
        for item in grosser_datensatz:
            bag.add(item)

        assert bag.size() == len(grosser_datensatz)

        # Überprüfung der Iteration
        collected = list(bag)
        assert len(collected) == len(grosser_datensatz)
