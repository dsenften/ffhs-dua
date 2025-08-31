import os
import sys
import unittest

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
        list_bag = Bag[list[int]]()
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

    # Tests für die erweiterten Methoden
    def test_contains(self):
        """Testet die contains-Methode."""
        # Füge einige Elemente für die Tests hinzu
        self.bag.add(1)
        self.bag.add(2)
        self.bag.add(3)

        self.assertTrue(self.bag.contains(1))
        self.assertTrue(self.bag.contains(2))
        self.assertTrue(self.bag.contains(3))
        self.assertFalse(self.bag.contains(4))
        self.assertFalse(self.bag.contains("nicht vorhanden"))

    def test_contains_operator(self):
        """Testet den 'in'-Operator (implementiert durch __contains__)."""
        # Füge einige Elemente für die Tests hinzu
        self.bag.add(1)
        self.bag.add(2)
        self.bag.add(3)

        self.assertTrue(1 in self.bag)
        self.assertTrue(2 in self.bag)
        self.assertTrue(3 in self.bag)
        self.assertFalse(4 in self.bag)
        self.assertFalse("nicht vorhanden" in self.bag)

    def test_remove(self):
        """Testet die remove-Methode."""
        # Füge einige Elemente für die Tests hinzu
        self.bag.add(1)
        self.bag.add(2)
        self.bag.add(3)
        self.bag.add(2)  # Doppeltes Element für Tests

        # Entferne ein vorhandenes Element
        self.assertTrue(self.bag.remove(1))
        self.assertEqual(self.bag.size(), 3)
        self.assertFalse(self.bag.contains(1))

        # Entferne ein Element, das mehrfach vorkommt (nur ein Vorkommen wird entfernt)
        self.assertTrue(self.bag.remove(2))
        self.assertEqual(self.bag.size(), 2)
        self.assertTrue(self.bag.contains(2))  # Es gibt noch ein weiteres '2'

        # Entferne ein nicht vorhandenes Element
        self.assertFalse(self.bag.remove(4))
        self.assertEqual(self.bag.size(), 2)

        # Entferne alle verbleibenden Elemente
        self.assertTrue(self.bag.remove(2))
        self.assertTrue(self.bag.remove(3))
        self.assertEqual(self.bag.size(), 0)
        self.assertTrue(self.bag.is_empty())

        # Versuche, aus einer leeren Bag zu entfernen
        self.assertFalse(self.bag.remove(1))

    def test_remove_all(self):
        """Testet die remove_all-Methode."""
        # Füge einige Elemente für die Tests hinzu
        self.bag.add(1)
        self.bag.add(2)
        self.bag.add(3)
        self.bag.add(2)  # Doppeltes Element
        self.bag.add(2)  # Weiteres doppeltes Element
        self.bag.add(2)  # Weiteres doppeltes Element

        # Entferne alle Vorkommen von 2
        self.assertEqual(self.bag.remove_all(2), 4)
        self.assertEqual(self.bag.size(), 2)
        self.assertFalse(self.bag.contains(2))

        # Entferne ein Element, das nur einmal vorkommt
        self.assertEqual(self.bag.remove_all(1), 1)
        self.assertEqual(self.bag.size(), 1)
        self.assertFalse(self.bag.contains(1))

        # Entferne ein nicht vorhandenes Element
        self.assertEqual(self.bag.remove_all(4), 0)
        self.assertEqual(self.bag.size(), 1)

        # Entferne alle verbleibenden Elemente
        self.assertEqual(self.bag.remove_all(3), 1)
        self.assertEqual(self.bag.size(), 0)

        # Leere Bag
        self.bag.clear()
        self.assertEqual(self.bag.remove_all(1), 0)

    def test_clear(self):
        """Testet die clear-Methode."""
        # Füge einige Elemente für die Tests hinzu
        self.bag.add(1)
        self.bag.add(2)

        self.assertFalse(self.bag.is_empty())
        self.bag.clear()
        self.assertTrue(self.bag.is_empty())
        self.assertEqual(self.bag.size(), 0)

        # Erneutes Leeren einer bereits leeren Bag
        self.bag.clear()
        self.assertTrue(self.bag.is_empty())
        self.assertEqual(self.bag.size(), 0)

    def test_peek(self):
        """Testet die peek-Methode."""
        # Erstelle eine neue Bag mit bekannter Reihenfolge
        test_bag = Bag()
        test_bag.add(10)

        # Das erste Element sollte 10 sein
        self.assertEqual(test_bag.peek(), 10)

        # Peek sollte die Bag nicht verändern
        self.assertEqual(test_bag.size(), 1)

        # Füge ein weiteres Element hinzu
        test_bag.add(20)

        # Das erste Element sollte jetzt 20 sein (LIFO-Verhalten)
        self.assertEqual(test_bag.peek(), 20)

        # Leere Bag
        test_bag.clear()
        self.assertIsNone(test_bag.peek())

    def test_to_list(self):
        """Testet die to_list-Methode."""
        # Füge einige Elemente für die Tests hinzu
        self.bag.add(1)
        self.bag.add(2)
        self.bag.add(3)
        self.bag.add(2)  # Doppeltes Element

        # Konvertiere die Bag in eine Liste
        bag_list = self.bag.to_list()

        # Überprüfe die Länge
        self.assertEqual(len(bag_list), 4)

        # Überprüfe, dass alle Elemente in der Liste sind
        self.assertIn(1, bag_list)
        self.assertIn(2, bag_list)
        self.assertIn(3, bag_list)

        # Überprüfe, dass die Liste das doppelte Element enthält
        count_2 = bag_list.count(2)
        self.assertEqual(count_2, 2)

        # Leere Bag
        empty_bag = Bag()
        self.assertEqual(empty_bag.to_list(), [])

    def test_improved_repr(self):
        """Testet die verbesserte __repr__-Methode."""
        # Füge einige Elemente für die Tests hinzu
        self.bag.add(1)
        self.bag.add(2)
        self.bag.add(3)

        # Teste mit normaler Bag
        repr_str = repr(self.bag)
        self.assertTrue(repr_str.startswith("{"))
        self.assertTrue(repr_str.endswith("}"))

        # Überprüfe, dass keine überflüssigen Kommas am Ende stehen
        self.assertNotIn(", }", repr_str)

        # Teste mit leerer Bag
        empty_bag = Bag()
        self.assertEqual(repr(empty_bag), "{}")

        # Teste mit Bag, die nur ein Element enthält
        single_bag = Bag()
        single_bag.add(42)
        self.assertEqual(repr(single_bag), "{42}")


if __name__ == "__main__":
    unittest.main()
