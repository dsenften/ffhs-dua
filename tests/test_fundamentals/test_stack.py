"""
Tests für die Stack-Datenstrukturen.

Diese Datei enthält umfassende Tests für alle Stack-Implementierungen.
Verwendet Test-Vorrichtungen aus conftest.py für konsistente Testumgebungen.
"""

import pytest

from src.algs4.fundamentals.stack import FixedCapacityStack, ResizingArrayStack, Stack


class TestStack:
    """Test-Klasse für die grundlegende Stack-Implementierung."""

    def test_empty_stack_creation(self, leerer_stack):
        """Test: Leerer Stack wird korrekt erstellt."""
        assert leerer_stack.is_empty()
        assert leerer_stack.size() == 0
        assert len(leerer_stack) == 0

    def test_push_single_item(self, leerer_stack):
        """Test: Einzelnes Element auf Stack legen."""
        leerer_stack.push("test")
        assert not leerer_stack.is_empty()
        assert leerer_stack.size() == 1
        assert len(leerer_stack) == 1

    @pytest.mark.parametrize("items", [
        [1, 2, 3],
        ["a", "b", "c"],
        [1.1, 2.2, 3.3]
    ])
    def test_push_multiple_items(self, leerer_stack, items):
        """Test: Mehrere Elemente auf Stack legen."""
        for item in items:
            leerer_stack.push(item)
        assert leerer_stack.size() == len(items)

    def test_pop_single_item(self, leerer_stack):
        """Test: Einzelnes Element vom Stack nehmen."""
        leerer_stack.push("test")
        item = leerer_stack.pop()
        assert item == "test"
        assert leerer_stack.is_empty()

    def test_lifo_behavior(self, leerer_stack, beispiel_ganzzahlen):
        """Test: LIFO-Verhalten (Last In, First Out)."""
        # Elemente auf Stack legen
        for item in beispiel_ganzzahlen:
            leerer_stack.push(item)

        # Elemente in umgekehrter Reihenfolge vom Stack nehmen
        for expected_item in reversed(beispiel_ganzzahlen):
            assert leerer_stack.pop() == expected_item

        assert leerer_stack.is_empty()

    def test_pop_empty_stack_raises_exception(self, leerer_stack):
        """Test: Pop aus leerem Stack wirft Exception."""
        with pytest.raises(ValueError, match="Stack-Unterlauf"):
            leerer_stack.pop()

    def test_peek_method(self, leerer_stack):
        """Test: Peek-Methode zeigt oberstes Element ohne Entfernung."""
        leerer_stack.push("first")
        leerer_stack.push("second")

        # Peek sollte oberstes Element zurückgeben
        assert leerer_stack.peek() == "second"
        assert leerer_stack.size() == 2  # Stack unverändert

        # Nach pop sollte peek das darunterliegende Element zeigen
        leerer_stack.pop()
        assert leerer_stack.peek() == "first"

    def test_peek_empty_stack_raises_exception(self, leerer_stack):
        """Test: Peek auf leeren Stack wirft Exception."""
        with pytest.raises(ValueError, match="Stack-Unterlauf"):
            leerer_stack.peek()

    def test_iteration(self, leerer_stack, beispiel_zeichenketten):
        """Test: Iteration über Stack-Elemente (LIFO-Reihenfolge)."""
        for item in beispiel_zeichenketten:
            leerer_stack.push(item)

        collected_items = list(leerer_stack)
        assert len(collected_items) == len(beispiel_zeichenketten)
        assert collected_items == list(reversed(beispiel_zeichenketten))

    def test_string_representation(self, leerer_stack):
        """Test: String-Repräsentation des Stacks."""
        leerer_stack.push("first")
        leerer_stack.push("second")

        repr_str = repr(leerer_stack)
        assert "first" in repr_str
        assert "second" in repr_str

    def test_type_consistency(self):
        """Test: Typisierte Stack-Konsistenz."""
        # Integer Stack
        int_stack = Stack[int]()
        int_stack.push(42)
        assert int_stack.pop() == 42

        # String Stack
        str_stack = Stack[str]()
        str_stack.push("hello")
        assert str_stack.pop() == "hello"

    @pytest.mark.slow
    def test_large_dataset_performance(self, grosser_datensatz):
        """Test: Performance mit großem Datensatz."""
        stack = Stack[int]()

        # Alle Elemente auf Stack legen
        for item in grosser_datensatz:
            stack.push(item)

        assert stack.size() == len(grosser_datensatz)

        # Alle Elemente vom Stack nehmen
        popped_items = []
        while not stack.is_empty():
            popped_items.append(stack.pop())

        assert popped_items == list(reversed(grosser_datensatz))


class TestFixedCapacityStack:
    """Test-Klasse für FixedCapacityStack."""

    def test_fixed_capacity_creation(self):
        """Test: FixedCapacityStack mit fester Kapazität erstellen."""
        stack = FixedCapacityStack[str](5)
        assert stack.is_empty()
        assert stack.size() == 0

    def test_push_within_capacity(self):
        """Test: Elemente innerhalb der Kapazität hinzufügen."""
        stack = FixedCapacityStack[int](3)
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.size() == 3
        assert not stack.is_empty()

    def test_push_exceeds_capacity_raises_exception(self):
        """Test: Überschreitung der Kapazität wirft Exception."""
        stack = FixedCapacityStack[str](2)
        stack.push("first")
        stack.push("second")

        with pytest.raises(IndexError):
            stack.push("third")

    def test_lifo_behavior_fixed_capacity(self):
        """Test: LIFO-Verhalten bei FixedCapacityStack."""
        stack = FixedCapacityStack[str](3)
        items = ["first", "second", "third"]

        for item in items:
            stack.push(item)

        for expected_item in reversed(items):
            assert stack.pop() == expected_item


class TestResizingArrayStack:
    """Test-Klasse für ResizingArrayStack."""

    def test_resizing_stack_creation(self):
        """Test: ResizingArrayStack wird korrekt erstellt."""
        stack = ResizingArrayStack[int]()
        assert stack.is_empty()
        assert stack.size() == 0

    def test_automatic_resizing_up(self):
        """Test: Automatische Vergrößerung des Arrays."""
        stack = ResizingArrayStack[int]()

        # Viele Elemente hinzufügen (mehr als initiale Kapazität)
        for i in range(20):
            stack.push(i)

        assert stack.size() == 20

        # Alle Elemente in korrekter LIFO-Reihenfolge
        for i in range(19, -1, -1):
            assert stack.pop() == i

    def test_automatic_resizing_down(self):
        """Test: Automatische Verkleinerung des Arrays."""
        stack = ResizingArrayStack[str]()

        # Viele Elemente hinzufügen
        items = [f"item_{i}" for i in range(20)]
        for item in items:
            stack.push(item)

        # Die meisten Elemente entfernen
        for _ in range(18):
            stack.pop()

        # Stack sollte noch funktionieren
        assert stack.size() == 2
        assert not stack.is_empty()

    def test_mixed_operations_resizing(self):
        """Test: Gemischte Push/Pop-Operationen mit Resizing."""
        stack = ResizingArrayStack[str]()

        # Elemente hinzufügen
        stack.push("a")
        stack.push("b")

        # Ein Element entfernen
        assert stack.pop() == "b"

        # Weitere Elemente hinzufügen
        stack.push("c")
        stack.push("d")

        # Verbleibende Elemente in korrekter Reihenfolge
        assert stack.pop() == "d"
        assert stack.pop() == "c"
        assert stack.pop() == "a"
        assert stack.is_empty()

    @pytest.mark.slow
    def test_large_dataset_resizing_performance(self, grosser_datensatz):
        """Test: Performance mit großem Datensatz und Resizing."""
        stack = ResizingArrayStack[int]()

        # Alle Elemente hinzufügen (mehrfache Resizing-Operationen)
        for item in grosser_datensatz:
            stack.push(item)

        assert stack.size() == len(grosser_datensatz)

        # Alle Elemente entfernen
        popped_items = []
        while not stack.is_empty():
            popped_items.append(stack.pop())

        assert popped_items == list(reversed(grosser_datensatz))
