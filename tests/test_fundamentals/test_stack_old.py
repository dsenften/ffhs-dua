import unittest
from typing import List

import sys
import os

# Füge das Hauptverzeichnis zum Pfad hinzu, um die Module zu finden
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algs4.fundamentals.stack import Stack, FixedCapacityStack, ResizingArrayStack


class TestStack(unittest.TestCase):
    """Testfälle für die Stack-Implementierung."""

    def setUp(self):
        """Erstellt einen neuen Stack für jeden Test."""
        self.stack = Stack()

    def test_empty_stack(self):
        """Testet, ob ein neu erstellter Stack leer ist."""
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(len(self.stack), 0)

    def test_push_pop(self):
        """Testet die grundlegenden Push- und Pop-Operationen."""
        # Elemente hinzufügen
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        # Überprüfen der Grösse
        self.assertEqual(self.stack.size(), 3)
        self.assertFalse(self.stack.is_empty())

        # Elemente entfernen und überprüfen (LIFO-Reihenfolge)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

        # Stack sollte jetzt leer sein
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

    def test_peek(self):
        """Testet die Peek-Funktion."""
        # Elemente hinzufügen
        self.stack.push("a")
        self.stack.push("b")

        # Peek sollte das oberste Element zurückgeben, ohne es zu entfernen
        self.assertEqual(self.stack.peek(), "b")
        self.assertEqual(self.stack.size(), 2)

        # Nach dem Entfernen des obersten Elements sollte peek das nächste Element zurückgeben
        self.stack.pop()
        self.assertEqual(self.stack.peek(), "a")

    def test_iterator(self):
        """Testet die Iterator-Funktionalität."""
        # Elemente hinzufügen
        elements = ["a", "b", "c", "d"]
        for element in elements:
            self.stack.push(element)

        # Überprüfen, ob die Iteration in der richtigen Reihenfolge erfolgt (LIFO)
        result = list(self.stack)
        self.assertEqual(result, list(reversed(elements)))

        # Der Stack sollte nach der Iteration unverändert sein
        self.assertEqual(self.stack.size(), 4)
        self.assertEqual(self.stack.pop(), "d")

    def test_repr(self):
        """Testet die String-Repräsentation des Stacks."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        # Überprüfen der String-Repräsentation (LIFO-Reihenfolge)
        self.assertEqual(repr(self.stack), "3 2 1")

    def test_exception_pop_empty(self):
        """Testet, ob eine Exception geworfen wird, wenn pop auf einem leeren Stack aufgerufen wird."""
        with self.assertRaises(ValueError):
            self.stack.pop()

    def test_exception_peek_empty(self):
        """Testet, ob eine Exception geworfen wird, wenn peek auf einem leeren Stack aufgerufen wird."""
        with self.assertRaises(ValueError):
            self.stack.peek()

    def test_different_types(self):
        """Testet den Stack mit verschiedenen Datentypen."""
        # Integer
        int_stack = Stack[int]()
        int_stack.push(1)
        self.assertEqual(int_stack.peek(), 1)

        # String
        str_stack = Stack[str]()
        str_stack.push("test")
        self.assertEqual(str_stack.peek(), "test")

        # Liste
        list_stack = Stack[List[int]]()
        test_list = [1, 2, 3]
        list_stack.push(test_list)
        self.assertEqual(list_stack.peek(), test_list)


class TestFixedCapacityStack(unittest.TestCase):
    """Testfälle für die FixedCapacityStack-Implementierung."""

    def setUp(self):
        """Erstellt einen neuen FixedCapacityStack für jeden Test."""
        self.stack = FixedCapacityStack(5)

    def test_empty_stack(self):
        """Testet, ob ein neu erstellter Stack leer ist."""
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(len(self.stack), 0)

    def test_push_pop(self):
        """Testet die grundlegenden Push- und Pop-Operationen."""
        # Elemente hinzufügen
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        # Überprüfen der Grösse
        self.assertEqual(self.stack.size(), 3)
        self.assertFalse(self.stack.is_empty())

        # Elemente entfernen und überprüfen (LIFO-Reihenfolge)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

        # Stack sollte jetzt leer sein
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

    def test_capacity(self):
        """Testet, ob der Stack die angegebene Kapazität einhält."""
        # Füllen des Stacks bis zur Kapazitätsgrenze
        for i in range(5):
            self.stack.push(i)

        self.assertEqual(self.stack.size(), 5)

        # Entfernen und Überprüfen der Elemente
        for i in range(4, -1, -1):
            self.assertEqual(self.stack.pop(), i)


class TestResizingArrayStack(unittest.TestCase):
    """Testfälle für die ResizingArrayStack-Implementierung."""

    def setUp(self):
        """Erstellt einen neuen ResizingArrayStack für jeden Test."""
        self.stack = ResizingArrayStack()

    def test_empty_stack(self):
        """Testet, ob ein neu erstellter Stack leer ist."""
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(len(self.stack), 0)

    def test_push_pop(self):
        """Testet die grundlegenden Push- und Pop-Operationen."""
        # Elemente hinzufügen
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        # Überprüfen der Grösse
        self.assertEqual(self.stack.size(), 3)
        self.assertFalse(self.stack.is_empty())

        # Elemente entfernen und überprüfen (LIFO-Reihenfolge)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

        # Stack sollte jetzt leer sein
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

    def test_resize(self):
        """Testet die automatische Größenanpassung des Stacks."""
        # Hinzufügen von mehr Elementen als die Anfangskapazität
        for i in range(10):
            self.stack.push(i)

        self.assertEqual(self.stack.size(), 10)

        # Überprüfen, ob die interne Array-Größe angepasst wurde
        self.assertTrue(len(self.stack.a) >= 10)

        # Entfernen aller Elemente
        for i in range(9, -1, -1):
            self.assertEqual(self.stack.pop(), i)

        # Überprüfen, ob die interne Array-Größe verkleinert wurde
        self.assertTrue(len(self.stack.a) < 10)

    def test_iterator(self):
        """Testet die Iterator-Funktionalität."""
        # Elemente hinzufügen
        elements = ["a", "b", "c", "d"]
        for element in elements:
            self.stack.push(element)

        # Überprüfen, ob die Iteration in der richtigen Reihenfolge erfolgt (LIFO)
        result = list(self.stack)
        self.assertEqual(result, list(reversed(elements)))

        # Der Stack sollte nach der Iteration unverändert sein
        self.assertEqual(self.stack.size(), 4)
        self.assertEqual(self.stack.pop(), "d")


if __name__ == "__main__":
    unittest.main()
