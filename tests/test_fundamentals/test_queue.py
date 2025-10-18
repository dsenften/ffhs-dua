"""
Tests für die Queue-Datenstruktur.

Diese Datei enthält umfassende Tests für die Queue-Implementierung.
Verwendet Test-Vorrichtungen aus conftest.py für konsistente Testumgebungen.
"""

import pytest

from src.algs4.errors.errors import NoSuchElementException
from src.algs4.pva_1_fundamentals.queue import Queue


class TestQueue:
    """Test-Klasse für die Queue-Datenstruktur."""

    def test_empty_queue_creation(self, leere_queue):
        """Test: Leere Queue wird korrekt erstellt."""
        assert leere_queue.is_empty()
        assert leere_queue.size() == 0
        assert len(leere_queue) == 0

    def test_enqueue_single_item(self, leere_queue):
        """Test: Einzelnes Element einreihen."""
        leere_queue.enqueue("test")
        assert not leere_queue.is_empty()
        assert leere_queue.size() == 1
        assert len(leere_queue) == 1

    @pytest.mark.parametrize("items", [
        [1, 2, 3],
        ["a", "b", "c"],
        [1.1, 2.2, 3.3]
    ])
    def test_enqueue_multiple_items(self, leere_queue, items):
        """Test: Mehrere Elemente einreihen."""
        for item in items:
            leere_queue.enqueue(item)
        assert leere_queue.size() == len(items)

    def test_dequeue_single_item(self, leere_queue):
        """Test: Einzelnes Element ausreihen (FIFO)."""
        leere_queue.enqueue("first")
        item = leere_queue.dequeue()
        assert item == "first"
        assert leere_queue.is_empty()

    def test_fifo_behavior(self, leere_queue, beispiel_ganzzahlen):
        """Test: FIFO-Verhalten (First In, First Out)."""
        # Elemente einreihen
        for item in beispiel_ganzzahlen:
            leere_queue.enqueue(item)

        # Elemente in derselben Reihenfolge ausreihen
        for expected_item in beispiel_ganzzahlen:
            assert leere_queue.dequeue() == expected_item

        assert leere_queue.is_empty()

    def test_dequeue_empty_queue_raises_exception(self, leere_queue):
        """Test: Dequeue aus leerer Queue wirft Exception."""
        with pytest.raises(NoSuchElementException):
            leere_queue.dequeue()

    def test_peek_method(self, leere_queue):
        """Test: Peek-Methode zeigt erstes Element ohne Entfernung."""
        leere_queue.enqueue("first")
        leere_queue.enqueue("second")

        # Peek sollte erstes Element zurückgeben
        assert leere_queue.peek() == "first"
        assert leere_queue.size() == 2  # Queue unverändert

        # Nach dequeue sollte peek das nächste Element zeigen
        leere_queue.dequeue()
        assert leere_queue.peek() == "second"

    def test_peek_empty_queue_raises_exception(self, leere_queue):
        """Test: Peek auf leere Queue wirft Exception."""
        with pytest.raises(NoSuchElementException):
            leere_queue.peek()

    def test_iteration(self, leere_queue, beispiel_zeichenketten):
        """Test: Iteration über Queue-Elemente."""
        for item in beispiel_zeichenketten:
            leere_queue.enqueue(item)

        collected_items = list(leere_queue)
        assert len(collected_items) == len(beispiel_zeichenketten)
        assert collected_items == beispiel_zeichenketten

    def test_string_representation(self, leere_queue):
        """Test: String-Repräsentation der Queue."""
        leere_queue.enqueue("first")
        leere_queue.enqueue("second")

        repr_str = repr(leere_queue)
        assert "first" in repr_str
        assert "second" in repr_str

    def test_type_consistency(self):
        """Test: Typisierte Queue-Konsistenz."""
        # Integer Queue
        int_queue = Queue[int]()
        int_queue.enqueue(42)
        assert int_queue.dequeue() == 42

        # String Queue
        str_queue = Queue[str]()
        str_queue.enqueue("hello")
        assert str_queue.dequeue() == "hello"

    @pytest.mark.slow
    def test_large_dataset_performance(self, grosser_datensatz):
        """Test: Performance mit grossem Datensatz."""
        queue = Queue[int]()

        # Alle Elemente einreihen
        for item in grosser_datensatz:
            queue.enqueue(item)

        assert queue.size() == len(grosser_datensatz)

        # Alle Elemente ausreihen
        dequeued_items = []
        while not queue.is_empty():
            dequeued_items.append(queue.dequeue())

        assert dequeued_items == grosser_datensatz

    def test_mixed_operations(self, leere_queue):
        """Test: Gemischte Enqueue/Dequeue-Operationen."""
        # Einige Elemente einreihen
        leere_queue.enqueue("a")
        leere_queue.enqueue("b")

        # Ein Element ausreihen
        assert leere_queue.dequeue() == "a"

        # Weitere Elemente einreihen
        leere_queue.enqueue("c")
        leere_queue.enqueue("d")

        # Verbleibende Elemente in korrekter Reihenfolge
        assert leere_queue.dequeue() == "b"
        assert leere_queue.dequeue() == "c"
        assert leere_queue.dequeue() == "d"
        assert leere_queue.is_empty()
