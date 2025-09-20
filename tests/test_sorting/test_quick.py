"""
Tests für den Quick-Sort-Algorithmus.

Diese Datei enthält umfassende Tests für die Quick-Sort-Implementierung.
Verwendet Test-Vorrichtungen aus conftest.py für konsistente Testumgebungen.
"""

import pytest

from src.algs4.sorting.quick import Quick


class TestQuick:
    """Test-Klasse für die Quick-Sort-Implementierung."""

    def test_empty_list(self):
        """Test: Sortieren einer leeren Liste."""
        arr = []
        result = Quick.sort(arr)
        assert result == []
        assert Quick.is_sorted(result)

    def test_single_element(self):
        """Test: Sortieren einer Liste mit einem Element."""
        arr = [42]
        result = Quick.sort(arr)
        assert result == [42]
        assert Quick.is_sorted(result)

    def test_already_sorted(self, beispiel_ganzzahlen):
        """Test: Sortieren einer bereits sortierten Liste."""
        sorted_list = sorted(beispiel_ganzzahlen)
        result = Quick.sort(sorted_list.copy())
        assert result == sorted_list
        assert Quick.is_sorted(result)

    def test_reverse_sorted(self, beispiel_ganzzahlen):
        """Test: Sortieren einer umgekehrt sortierten Liste."""
        reversed_list = sorted(beispiel_ganzzahlen, reverse=True)
        expected = sorted(beispiel_ganzzahlen)
        result = Quick.sort(reversed_list)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_random_integers(self, beispiel_ganzzahlen):
        """Test: Sortieren einer zufälligen Liste von Ganzzahlen."""
        import random
        shuffled = beispiel_ganzzahlen.copy()
        random.shuffle(shuffled)
        expected = sorted(beispiel_ganzzahlen)
        result = Quick.sort(shuffled)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_duplicates(self):
        """Test: Sortieren einer Liste mit duplizierten Elementen."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        result = Quick.sort(arr)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_strings(self, beispiel_zeichenketten):
        """Test: Sortieren einer Liste von Strings."""
        import random
        shuffled = beispiel_zeichenketten.copy()
        random.shuffle(shuffled)
        expected = sorted(beispiel_zeichenketten)
        result = Quick.sort(shuffled)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_strings_case_sensitive(self):
        """Test: Sortieren von Strings mit Gross-/Kleinschreibung."""
        arr = ["Zebra", "apple", "Banana", "cherry"]
        expected = ["Banana", "Zebra", "apple", "cherry"]
        result = Quick.sort(arr)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_negative_numbers(self):
        """Test: Sortieren einer Liste mit negativen Zahlen."""
        arr = [-3, -1, -4, 1, 5, -9, 2, -6]
        expected = [-9, -6, -4, -3, -1, 1, 2, 5]
        result = Quick.sort(arr)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_mixed_numbers(self):
        """Test: Sortieren einer Liste mit positiven, negativen und null Werten."""
        arr = [0, -3, 7, -1, 0, 4, -2]
        expected = [-3, -2, -1, 0, 0, 4, 7]
        result = Quick.sort(arr)
        assert result == expected
        assert Quick.is_sorted(result)

    @pytest.mark.slow
    def test_large_list(self, grosser_datensatz):
        """Test: Sortieren einer grösseren Liste."""
        shuffled = grosser_datensatz.copy()
        import random
        random.shuffle(shuffled)
        expected = sorted(grosser_datensatz)
        result = Quick.sort(shuffled)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_all_same_elements(self):
        """Test: Sortieren einer Liste mit identischen Elementen."""
        arr = [5, 5, 5, 5, 5]
        expected = [5, 5, 5, 5, 5]
        result = Quick.sort(arr)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_two_elements(self):
        """Test: Sortieren einer Liste mit zwei Elementen."""
        # Unsortiert
        arr = [2, 1]
        expected = [1, 2]
        result = Quick.sort(arr)
        assert result == expected
        assert Quick.is_sorted(result)

        # Bereits sortiert
        arr = [1, 2]
        expected = [1, 2]
        result = Quick.sort(arr)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_different_types(self):
        """Test: Quick-Sort mit verschiedenen Datentypen."""
        # Float-Zahlen
        float_arr = [3.14, 2.71, 1.41, 2.23]
        float_expected = [1.41, 2.23, 2.71, 3.14]
        float_result = Quick.sort(float_arr)
        assert float_result == float_expected
        assert Quick.is_sorted(float_result)

        # Zeichen
        char_arr = ["d", "a", "c", "b"]
        char_expected = ["a", "b", "c", "d"]
        char_result = Quick.sort(char_arr)
        assert char_result == char_expected
        assert Quick.is_sorted(char_result)

    def test_is_sorted_false(self):
        """Test: is_sorted-Methode mit unsortierten Listen."""
        assert not Quick.is_sorted([3, 1, 2])
        assert not Quick.is_sorted([1, 3, 2, 4])
        assert not Quick.is_sorted([5, 4, 3, 2, 1])

    def test_is_sorted_true(self):
        """Test: is_sorted-Methode mit sortierten Listen."""
        assert Quick.is_sorted([])
        assert Quick.is_sorted([1])
        assert Quick.is_sorted([1, 2, 3, 4, 5])
        assert Quick.is_sorted([1, 1, 2, 2, 3])

    def test_sort_preserves_original_if_needed(self):
        """Test: Ob die ursprüngliche Liste in-place sortiert wird."""
        original = [3, 1, 4, 1, 5]
        sorted_list = Quick.sort(original)
        # Quick.sort modifiziert die ursprüngliche Liste in-place und gibt sie zurück
        assert sorted_list is original
        assert original == [1, 1, 3, 4, 5]

    def test_partition_method(self):
        """Test: Direkte Tests der partition-Methode."""
        # Test mit einfachem Array
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        pivot_index = Quick.partition(arr, 0, len(arr) - 1)
        
        # Überprüfe, dass das Pivot-Element korrekt positioniert ist
        pivot_value = arr[pivot_index]
        
        # Alle Elemente links vom Pivot sollten <= Pivot sein
        for i in range(pivot_index):
            assert arr[i] <= pivot_value
        
        # Alle Elemente rechts vom Pivot sollten >= Pivot sein
        for i in range(pivot_index + 1, len(arr)):
            assert arr[i] >= pivot_value

    def test_partition_edge_cases(self):
        """Test: Partitionierung mit Grenzfällen."""
        # Zwei Elemente
        arr = [2, 1]
        pivot_index = Quick.partition(arr, 0, 1)
        assert pivot_index in [0, 1]
        assert Quick.is_sorted(arr) or arr == [2, 1]  # Kann sortiert oder unverändert sein
        
        # Alle gleichen Elemente
        arr = [5, 5, 5, 5]
        pivot_index = Quick.partition(arr, 0, 3)
        assert 0 <= pivot_index <= 3
        # Bei gleichen Elementen sollte das Array unverändert bleiben
        assert all(x == 5 for x in arr)

    def test_quicksort_recursive_calls(self):
        """Test: Indirekte Tests der rekursiven quicksort-Methode."""
        # Test mit verschiedenen Array-Grössen
        for size in [3, 5, 10, 20]:
            arr = list(range(size, 0, -1))  # Umgekehrt sortiert
            expected = list(range(1, size + 1))
            result = Quick.quicksort(arr, 0, len(arr) - 1)
            assert result == expected
            assert Quick.is_sorted(result)

    @pytest.mark.parametrize("data_type,test_data", [
        (int, [64, 34, 25, 12, 22, 11, 90]),
        (float, [3.14, 2.71, 1.41, 2.23, 0.57]),
        (str, ["zebra", "apple", "banana", "cherry"])
    ])
    def test_parametrized_sorting(self, data_type, test_data):
        """Test: Parametrisierte Tests für verschiedene Datentypen."""
        shuffled = test_data.copy()
        import random
        random.shuffle(shuffled)
        expected = sorted(test_data)
        result = Quick.sort(shuffled)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_worst_case_scenario(self):
        """Test: Worst-Case-Szenario für Quick-Sort (bereits sortierte Liste)."""
        # Quick-Sort hat im Worst-Case O(n²) bei bereits sortierten Listen
        # wenn das erste Element als Pivot gewählt wird
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = Quick.sort(arr.copy())
        assert result == expected
        assert Quick.is_sorted(result)

    def test_best_case_scenario(self):
        """Test: Best-Case-Szenario für Quick-Sort."""
        # Best-Case ist wenn das Pivot-Element immer in der Mitte liegt
        # Hier simulieren wir das mit einem Array, das gut partitionierbar ist
        arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
        expected = sorted(arr)
        result = Quick.sort(arr)
        assert result == expected
        assert Quick.is_sorted(result)

    def test_stability_not_guaranteed(self):
        """Test: Quick-Sort ist nicht stabil - gleiche Elemente können ihre Reihenfolge ändern."""
        # Verwende Tupel um Stabilität zu testen
        class ComparableItem:
            def __init__(self, value, original_index):
                self.value = value
                self.original_index = original_index
            
            def __lt__(self, other):
                return self.value < other.value
            
            def __le__(self, other):
                return self.value <= other.value
            
            def __gt__(self, other):
                return self.value > other.value
            
            def __ge__(self, other):
                return self.value >= other.value
            
            def __eq__(self, other):
                return self.value == other.value
            
            def __repr__(self):
                return f"({self.value}, {self.original_index})"

        # Erstelle Array mit duplizierten Werten
        arr = [
            ComparableItem(3, 0),
            ComparableItem(1, 1),
            ComparableItem(3, 2),
            ComparableItem(2, 3),
            ComparableItem(1, 4)
        ]
        
        result = Quick.sort(arr)
        
        # Überprüfe, dass sortiert ist
        for i in range(1, len(result)):
            assert result[i].value >= result[i-1].value
        
        # Quick-Sort ist nicht stabil, also testen wir nur die Korrektheit der Sortierung
        values = [item.value for item in result]
        assert values == [1, 1, 2, 3, 3]
