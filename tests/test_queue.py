import unittest
from typing import List
import sys
import os

# Füge das Hauptverzeichnis zum Pfad hinzu, um die Module zu finden
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algs4.fundamentals.queue import Queue
from algs4.errors.errors import NoSuchElementException


class TestQueue(unittest.TestCase):
    """Testfälle für die Queue-Implementierung."""

    def setUp(self):
        """Erstellt eine neue Queue für jeden Test."""
        self.queue = Queue()

    def test_empty_queue(self):
        """Testet, ob eine neu erstellte Queue leer ist."""
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)
        self.assertEqual(len(self.queue), 0)

    def test_enqueue_dequeue(self):
        """Testet die grundlegenden Enqueue- und Dequeue-Operationen."""
        # Elemente hinzufügen
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        # Überprüfen der Größe
        self.assertEqual(self.queue.size(), 3)
        self.assertFalse(self.queue.is_empty())

        # Elemente entfernen und überprüfen
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)

        # Queue sollte jetzt leer sein
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

    def test_peek(self):
        """Testet die Peek-Funktion."""
        # Elemente hinzufügen
        self.queue.enqueue("a")
        self.queue.enqueue("b")

        # Peek sollte das erste Element zurückgeben, ohne es zu entfernen
        self.assertEqual(self.queue.peek(), "a")
        self.assertEqual(self.queue.size(), 2)

        # Nach dem Entfernen des ersten Elements sollte peek das nächste Element zurückgeben
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), "b")

    def test_iterator(self):
        """Testet die Iterator-Funktionalität."""
        # Elemente hinzufügen
        elements = ["a", "b", "c", "d"]
        for element in elements:
            self.queue.enqueue(element)

        # Überprüfen, ob die Iteration in der richtigen Reihenfolge erfolgt
        result = []
        for item in self.queue:
            result.append(item)

        self.assertEqual(result, elements)

        # Die Queue sollte nach der Iteration unverändert sein
        self.assertEqual(self.queue.size(), 4)
        self.assertEqual(self.queue.dequeue(), "a")

    def test_repr(self):
        """Testet die String-Repräsentation der Queue."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        # Überprüfen der String-Repräsentation
        self.assertEqual(repr(self.queue), "1 2 3 ")

    def test_exception_dequeue_empty(self):
        """Testet, ob eine Exception geworfen wird, wenn dequeue auf einer leeren Queue aufgerufen wird."""
        with self.assertRaises(NoSuchElementException):
            self.queue.dequeue()

    def test_exception_peek_empty(self):
        """Testet, ob eine Exception geworfen wird, wenn peek auf einer leeren Queue aufgerufen wird."""
        with self.assertRaises(NoSuchElementException):
            self.queue.peek()

    def test_different_types(self):
        """Testet die Queue mit verschiedenen Datentypen."""
        # Integer
        int_queue = Queue[int]()
        int_queue.enqueue(1)
        self.assertEqual(int_queue.peek(), 1)

        # String
        str_queue = Queue[str]()
        str_queue.enqueue("test")
        self.assertEqual(str_queue.peek(), "test")

        # Liste
        list_queue = Queue[List[int]]()
        test_list = [1, 2, 3]
        list_queue.enqueue(test_list)
        self.assertEqual(list_queue.peek(), test_list)

    def test_fifo_order(self):
        """Testet, ob die Queue die FIFO-Reihenfolge einhält."""
        elements = [10, 20, 30, 40, 50]
        for element in elements:
            self.queue.enqueue(element)

        for expected in elements:
            self.assertEqual(self.queue.dequeue(), expected)

    def test_enqueue_after_dequeue(self):
        """Testet das Hinzufügen von Elementen nach dem Entfernen."""
        # Elemente hinzufügen und entfernen
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)

        # Weitere Elemente hinzufügen
        self.queue.enqueue(3)
        self.queue.enqueue(4)

        # Überprüfen der Reihenfolge
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)


if __name__ == "__main__":
    unittest.main()
