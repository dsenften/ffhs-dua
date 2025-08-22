import unittest
from typing import List

import sys
import os

# Füge das Hauptverzeichnis zum Pfad hinzu, um die Module zu finden
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algs4.fundamentals.bag import Bag


class TestBag(unittest.TestCase):
    """Testfälle für die Bag-Implementierung."""

    def setUp(self):
        """Erstellt eine neue Bag für jeden Test."""
        self.bag = Bag()

    def test_empty_bag(self):
        """Testet, ob eine neu erstellte Bag leer ist."""
        self.assertTrue(self.bag.is_empty())
        self.assertEqual(self.bag.size(), 0)
        self.assertEqual(len(self.bag), 0)

    def test_add(self):
        """Testet die grundlegende Add-Operation."""
        # Elemente hinzufügen
        self.bag.add(1)
        self.bag.add(2)
        self.bag.add(3)

        # Überprüfen der Grösse
        self.assertEqual(self.bag.size(), 3)
        self.assertFalse(self.bag.is_empty())

        # Überprüfen, dass die Elemente in der Bag sind
        elements = list(self.bag)
        self.assertEqual(len(elements), 3)
        self.assertIn(1, elements)
        self.assertIn(2, elements)
        self.assertIn(3, elements)

    def test_size_and_len(self):
        """Testet die size() und __len__() Methoden."""
        self.assertEqual(self.bag.size(), 0)
        self.assertEqual(len(self.bag), 0)

        self.bag.add("a")
        self.assertEqual(self.bag.size(), 1)
        self.assertEqual(len(self.bag), 1)

        self.bag.add("b")
        self.assertEqual(self.bag.size(), 2)
        self.assertEqual(len(self.bag), 2)

    def test_iterator(self):
        """Testet die Iterator-Funktionalität."""
        # Elemente hinzufügen
        elements = ["a", "b", "c", "d"]
        for element in elements:
            self.bag.add(element)

        # Überprüfen, ob alle Elemente in der Bag sind
        bag_elements = list(self.bag)
        self.assertEqual(len(bag_elements), 4)

        # Überprüfen, dass jedes Element in der Bag ist
        for element in elements:
            self.assertIn(element, bag_elements)

        # Die Bag sollte nach der Iteration unverändert sein
        self.assertEqual(self.bag.size(), 4)

    def test_repr(self):
        """Testet die String-Repräsentation der Bag."""
        self.bag.add(1)
        self.bag.add(2)
        self.bag.add(3)

        # Überprüfen der String-Repräsentation
        repr_str = repr(self.bag)
        self.assertTrue(repr_str.startswith("{"))
        self.assertTrue(repr_str.endswith("}"))

        # Überprüfen, dass alle Elemente in der Repräsentation enthalten sind
        self.assertIn("1", repr_str)
        self.assertIn("2", repr_str)
        self.assertIn("3", repr_str)

    def test_different_types(self):
        """Testet die Bag mit verschiedenen Datentypen."""
        # Integer
        int_bag = Bag[int]()
        int_bag.add(1)
        elements = list(int_bag)
        self.assertEqual(elements[0], 1)

        # String
        str_bag = Bag[str]()
        str_bag.add("test")
        elements = list(str_bag)
        self.assertEqual(elements[0], "test")

        # Liste
        list_bag = Bag[List[int]]()
        test_list = [1, 2, 3]
        list_bag.add(test_list)
        elements = list(list_bag)
        self.assertEqual(elements[0], test_list)

    def test_add_multiple_same_item(self):
        """Testet das Hinzufügen des gleichen Elements mehrmals."""
        self.bag.add("a")
        self.bag.add("a")
        self.bag.add("a")

        self.assertEqual(self.bag.size(), 3)

        # Zählen, wie oft "a" in der Bag vorkommt
        count = 0
        for item in self.bag:
            if item == "a":
                count += 1

        self.assertEqual(count, 3)

    def test_add_after_iteration(self):
        """Testet das Hinzufügen von Elementen nach der Iteration."""
        self.bag.add(1)
        self.bag.add(2)

        # Iteration durchführen
        list(self.bag)

        # Weitere Elemente hinzufügen
        self.bag.add(3)
        self.bag.add(4)

        # Überprüfen der Grösse
        self.assertEqual(self.bag.size(), 4)

        # Überprüfen, dass alle Elemente in der Bag sind
        elements = list(self.bag)
        self.assertIn(1, elements)
        self.assertIn(2, elements)
        self.assertIn(3, elements)
        self.assertIn(4, elements)


if __name__ == "__main__":
    unittest.main()
