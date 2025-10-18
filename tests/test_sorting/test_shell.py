"""
Tests für den Shell-Sort-Algorithmus.

Diese Datei enthält umfassende Tests für die Shell-Sort-Implementierung.
Verwendet Test-Vorrichtungen aus conftest.py für konsistente Testumgebungen.
"""

import pytest

from src.algs4.pva_2_sorting.shell import Shell


class TestShell:
    """Test-Klasse für die Shell-Sort-Implementierung."""

    def test_empty_list(self):
        """Test: Sortieren einer leeren Liste."""
        arr = []
        result = Shell.sort(arr)
        assert result == []
        assert Shell.is_sorted(result)

    def test_single_element(self):
        """Test: Sortieren einer Liste mit einem Element."""
        arr = [42]
        result = Shell.sort(arr)
        assert result == [42]
        assert Shell.is_sorted(result)

    def test_already_sorted(self, beispiel_ganzzahlen):
        """Test: Sortieren einer bereits sortierten Liste."""
        sorted_list = sorted(beispiel_ganzzahlen)
        result = Shell.sort(sorted_list.copy())
        assert result == sorted_list
        assert Shell.is_sorted(result)

    def test_reverse_sorted(self, beispiel_ganzzahlen):
        """Test: Sortieren einer umgekehrt sortierten Liste."""
        reversed_list = sorted(beispiel_ganzzahlen, reverse=True)
        expected = sorted(beispiel_ganzzahlen)
        result = Shell.sort(reversed_list)
        assert result == expected
        assert Shell.is_sorted(result)

    def test_random_integers(self, beispiel_ganzzahlen):
        """Test: Sortieren einer zufälligen Liste von Ganzzahlen."""
        import random

        shuffled = beispiel_ganzzahlen.copy()
        random.shuffle(shuffled)
        expected = sorted(beispiel_ganzzahlen)
        result = Shell.sort(shuffled)
        assert result == expected
        assert Shell.is_sorted(result)

    def test_duplicates(self):
        """Test: Sortieren einer Liste mit duplizierten Elementen."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        result = Shell.sort(arr)
        assert result == expected
        assert Shell.is_sorted(result)

    def test_strings(self, beispiel_zeichenketten):
        """Test: Sortieren einer Liste von Strings."""
        import random

        shuffled = beispiel_zeichenketten.copy()
        random.shuffle(shuffled)
        expected = sorted(beispiel_zeichenketten)
        result = Shell.sort(shuffled)
        assert result == expected
        assert Shell.is_sorted(result)

    def test_strings_case_sensitive(self):
        """Test: Sortieren von Strings mit Gross-/Kleinschreibung."""
        arr = ["Zebra", "apple", "Banana", "cherry"]
        expected = ["Banana", "Zebra", "apple", "cherry"]
        result = Shell.sort(arr)
        assert result == expected
        assert Shell.is_sorted(result)

    def test_negative_numbers(self):
        """Test: Sortieren einer Liste mit negativen Zahlen."""
        arr = [-3, -1, -4, 1, 5, -9, 2, -6]
        expected = [-9, -6, -4, -3, -1, 1, 2, 5]
        result = Shell.sort(arr)
        assert result == expected
        assert Shell.is_sorted(result)

    def test_mixed_numbers(self):
        """Test: Sortieren einer Liste mit positiven, negativen und null Werten."""
        arr = [0, -3, 7, -1, 0, 4, -2]
        expected = [-3, -2, -1, 0, 0, 4, 7]
        result = Shell.sort(arr)
        assert result == expected
        assert Shell.is_sorted(result)

    @pytest.mark.slow
    def test_large_list(self, grosser_datensatz):
        """Test: Sortieren einer grösseren Liste."""
        shuffled = grosser_datensatz.copy()
        import random

        random.shuffle(shuffled)
        expected = sorted(grosser_datensatz)
        result = Shell.sort(shuffled)
        assert result == expected
        assert Shell.is_sorted(result)

    def test_all_same_elements(self):
        """Test: Sortieren einer Liste mit identischen Elementen."""
        arr = [5, 5, 5, 5, 5]
        expected = [5, 5, 5, 5, 5]
        result = Shell.sort(arr)
        assert result == expected
        assert Shell.is_sorted(result)

    def test_two_elements(self):
        """Test: Sortieren einer Liste mit zwei Elementen."""
        # Unsortiert
        arr = [2, 1]
        expected = [1, 2]
        result = Shell.sort(arr)
        assert result == expected
        assert Shell.is_sorted(result)

        # Bereits sortiert
        arr = [1, 2]
        expected = [1, 2]
        result = Shell.sort(arr)
        assert result == expected
        assert Shell.is_sorted(result)

    def test_different_types(self):
        """Test: Shell-Sort mit verschiedenen Datentypen."""
        # Float-Zahlen
        float_arr = [3.14, 2.71, 1.41, 2.23]
        float_expected = [1.41, 2.23, 2.71, 3.14]
        float_result = Shell.sort(float_arr)
        assert float_result == float_expected
        assert Shell.is_sorted(float_result)

        # Zeichen
        char_arr = ["d", "a", "c", "b"]
        char_expected = ["a", "b", "c", "d"]
        char_result = Shell.sort(char_arr)
        assert char_result == char_expected
        assert Shell.is_sorted(char_result)

    def test_is_sorted_false(self):
        """Test: is_sorted-Methode mit unsortierten Listen."""
        assert not Shell.is_sorted([3, 1, 2])
        assert not Shell.is_sorted([1, 3, 2, 4])
        assert not Shell.is_sorted([5, 4, 3, 2, 1])

    def test_is_sorted_true(self):
        """Test: is_sorted-Methode mit sortierten Listen."""
        assert Shell.is_sorted([])
        assert Shell.is_sorted([1])
        assert Shell.is_sorted([1, 2, 3, 4, 5])
        assert Shell.is_sorted([1, 1, 2, 2, 3])

    def test_sort_preserves_original_if_needed(self):
        """Test: Ob die ursprüngliche Liste in-place sortiert wird."""
        original = [3, 1, 4, 1, 5]
        sorted_list = Shell.sort(original)
        # Shell.sort modifiziert die ursprüngliche Liste in-place und gibt sie zurück
        assert sorted_list is original
        assert original == [1, 1, 3, 4, 5]

    def test_knuth_gap_sequence(self):
        """Test: Indirekt die Knuth-Gap-Sequenz durch Sortierung verschiedener Grössen."""
        # Teste verschiedene Listengrössen, um verschiedene Gap-Werte zu triggern
        for size in [3, 4, 13, 14, 40, 41]:
            arr = list(range(size, 0, -1))
            expected = list(range(1, size + 1))
            result = Shell.sort(arr)
            assert result == expected
            assert Shell.is_sorted(result)

    @pytest.mark.parametrize(
        "data_type,test_data",
        [
            (int, [64, 34, 25, 12, 22, 11, 90]),
            (float, [3.14, 2.71, 1.41, 2.23, 0.57]),
            (str, ["zebra", "apple", "banana", "cherry"]),
        ],
    )
    def test_parametrized_sorting(self, data_type, test_data):
        """Test: Parametrisierte Tests für verschiedene Datentypen."""
        shuffled = test_data.copy()
        import random

        random.shuffle(shuffled)
        expected = sorted(test_data)
        result = Shell.sort(shuffled)
        assert result == expected
        assert Shell.is_sorted(result)
