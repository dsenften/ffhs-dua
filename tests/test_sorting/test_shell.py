import os
import sys
import unittest

# Füge das Hauptverzeichnis zum Pfad hinzu, um die Module zu finden
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algs4.sorting.shell import Shell


class TestShell(unittest.TestCase):
    """Testfälle für die Shell-Sort-Implementierung."""

    def test_empty_list(self):
        """Testet das Sortieren einer leeren Liste."""
        arr = []
        result = Shell.sort(arr)
        self.assertEqual(result, [])
        self.assertTrue(Shell.is_sorted(result))

    def test_single_element(self):
        """Testet das Sortieren einer Liste mit einem Element."""
        arr = [42]
        result = Shell.sort(arr)
        self.assertEqual(result, [42])
        self.assertTrue(Shell.is_sorted(result))

    def test_already_sorted(self):
        """Testet das Sortieren einer bereits sortierten Liste."""
        arr = [1, 2, 3, 4, 5]
        result = Shell.sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertTrue(Shell.is_sorted(result))

    def test_reverse_sorted(self):
        """Testet das Sortieren einer umgekehrt sortierten Liste."""
        arr = [5, 4, 3, 2, 1]
        result = Shell.sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertTrue(Shell.is_sorted(result))

    def test_random_integers(self):
        """Testet das Sortieren einer zufälligen Liste von Ganzzahlen."""
        arr = [3, 7, 1, 9, 2, 8, 5, 4, 6]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = Shell.sort(arr)
        self.assertEqual(result, expected)
        self.assertTrue(Shell.is_sorted(result))

    def test_duplicates(self):
        """Testet das Sortieren einer Liste mit duplizierten Elementen."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        result = Shell.sort(arr)
        self.assertEqual(result, expected)
        self.assertTrue(Shell.is_sorted(result))

    def test_strings(self):
        """Testet das Sortieren einer Liste von Strings."""
        arr = ["banana", "apple", "cherry", "date"]
        expected = ["apple", "banana", "cherry", "date"]
        result = Shell.sort(arr)
        self.assertEqual(result, expected)
        self.assertTrue(Shell.is_sorted(result))

    def test_strings_case_sensitive(self):
        """Testet das Sortieren von Strings mit Groß-/Kleinschreibung."""
        arr = ["Zebra", "apple", "Banana", "cherry"]
        expected = ["Banana", "Zebra", "apple", "cherry"]
        result = Shell.sort(arr)
        self.assertEqual(result, expected)
        self.assertTrue(Shell.is_sorted(result))

    def test_negative_numbers(self):
        """Testet das Sortieren einer Liste mit negativen Zahlen."""
        arr = [-3, -1, -4, 1, 5, -9, 2, -6]
        expected = [-9, -6, -4, -3, -1, 1, 2, 5]
        result = Shell.sort(arr)
        self.assertEqual(result, expected)
        self.assertTrue(Shell.is_sorted(result))

    def test_mixed_numbers(self):
        """Testet das Sortieren einer Liste mit positiven, negativen und null Werten."""
        arr = [0, -3, 7, -1, 0, 4, -2]
        expected = [-3, -2, -1, 0, 0, 4, 7]
        result = Shell.sort(arr)
        self.assertEqual(result, expected)
        self.assertTrue(Shell.is_sorted(result))

    def test_large_list(self):
        """Testet das Sortieren einer größeren Liste."""
        arr = list(range(100, 0, -1))  # [100, 99, 98, ..., 2, 1]
        expected = list(range(1, 101))  # [1, 2, 3, ..., 99, 100]
        result = Shell.sort(arr)
        self.assertEqual(result, expected)
        self.assertTrue(Shell.is_sorted(result))

    def test_all_same_elements(self):
        """Testet das Sortieren einer Liste mit identischen Elementen."""
        arr = [5, 5, 5, 5, 5]
        expected = [5, 5, 5, 5, 5]
        result = Shell.sort(arr)
        self.assertEqual(result, expected)
        self.assertTrue(Shell.is_sorted(result))

    def test_two_elements(self):
        """Testet das Sortieren einer Liste mit zwei Elementen."""
        arr = [2, 1]
        expected = [1, 2]
        result = Shell.sort(arr)
        self.assertEqual(result, expected)
        self.assertTrue(Shell.is_sorted(result))

        # Bereits sortiert
        arr = [1, 2]
        expected = [1, 2]
        result = Shell.sort(arr)
        self.assertEqual(result, expected)
        self.assertTrue(Shell.is_sorted(result))

    def test_different_types(self):
        """Testet den Shell-Sort mit verschiedenen Datentypen."""
        # Float-Zahlen
        float_arr = [3.14, 2.71, 1.41, 2.23]
        float_expected = [1.41, 2.23, 2.71, 3.14]
        float_result = Shell.sort(float_arr)
        self.assertEqual(float_result, float_expected)
        self.assertTrue(Shell.is_sorted(float_result))

        # Zeichen
        char_arr = ["d", "a", "c", "b"]
        char_expected = ["a", "b", "c", "d"]
        char_result = Shell.sort(char_arr)
        self.assertEqual(char_result, char_expected)
        self.assertTrue(Shell.is_sorted(char_result))

    def test_is_sorted_false(self):
        """Testet die is_sorted-Methode mit unsortierten Listen."""
        self.assertFalse(Shell.is_sorted([3, 1, 2]))
        self.assertFalse(Shell.is_sorted([1, 3, 2, 4]))
        self.assertFalse(Shell.is_sorted([5, 4, 3, 2, 1]))

    def test_is_sorted_true(self):
        """Testet die is_sorted-Methode mit sortierten Listen."""
        self.assertTrue(Shell.is_sorted([]))
        self.assertTrue(Shell.is_sorted([1]))
        self.assertTrue(Shell.is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(Shell.is_sorted([1, 1, 2, 2, 3]))

    def test_sort_preserves_original_if_needed(self):
        """Testet, ob die ursprüngliche Liste in-place sortiert wird."""
        original = [3, 1, 4, 1, 5]
        sorted_list = Shell.sort(original)
        # Shell.sort modifiziert die ursprüngliche Liste in-place und gibt sie zurück
        self.assertIs(sorted_list, original)
        self.assertEqual(original, [1, 1, 3, 4, 5])

    def test_knuth_gap_sequence(self):
        """Testet indirekt die Knuth-Gap-Sequenz durch Sortierung verschiedener Größen."""
        # Teste verschiedene Listengrößen, um verschiedene Gap-Werte zu triggern
        for size in [3, 4, 13, 14, 40, 41]:
            arr = list(range(size, 0, -1))
            expected = list(range(1, size + 1))
            result = Shell.sort(arr)
            self.assertEqual(result, expected)
            self.assertTrue(Shell.is_sorted(result))


if __name__ == "__main__":
    unittest.main()
