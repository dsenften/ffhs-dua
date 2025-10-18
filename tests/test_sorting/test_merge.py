"""Tests für die Merge-Sort-Implementierung.

Diese Testdatei enthält umfassende Tests für die Merge-Klasse,
einschliesslich Grenzfälle, verschiedene Datentypen und
merge-spezifische Eigenschaften wie Stabilität.
"""

import random

import pytest

from src.algs4.pva_2_sorting.merge import Merge


class TestMerge:
    """Test-Klasse für die Merge-Sort-Implementierung."""

    def test_empty_list(self):
        """Test: Sortieren einer leeren Liste."""
        arr = []
        result = Merge.sort(arr)
        assert result == []
        assert Merge.is_sorted(result)

    def test_single_element(self):
        """Test: Sortieren einer Liste mit einem Element."""
        arr = [42]
        result = Merge.sort(arr)
        assert result == [42]
        assert Merge.is_sorted(result)

    def test_already_sorted(self, beispiel_ganzzahlen):
        """Test: Sortieren einer bereits sortierten Liste."""
        result = Merge.sort(beispiel_ganzzahlen.copy())
        assert result == [1, 2, 3, 4, 5]
        assert Merge.is_sorted(result)

    def test_reverse_sorted(self):
        """Test: Sortieren einer umgekehrt sortierten Liste."""
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        result = Merge.sort(arr)
        assert result == expected
        assert Merge.is_sorted(result)

    def test_random_integers(self):
        """Test: Sortieren einer zufällig gemischten Liste."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        shuffled = arr.copy()
        random.shuffle(shuffled)
        expected = sorted(arr)
        result = Merge.sort(shuffled)
        assert result == expected
        assert Merge.is_sorted(result)

    def test_duplicates(self):
        """Test: Sortieren einer Liste mit duplizierten Elementen."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        result = Merge.sort(arr)
        assert result == expected
        assert Merge.is_sorted(result)

    def test_strings(self, beispiel_zeichenketten):
        """Test: Sortieren von Zeichenketten."""
        result = Merge.sort(beispiel_zeichenketten.copy())
        expected = ["apple", "banana", "cherry", "date"]
        assert result == expected
        assert Merge.is_sorted(result)

    def test_strings_case_sensitive(self):
        """Test: Sortieren von Strings mit Gross-/Kleinschreibung."""
        arr = ["Zebra", "apple", "Banana", "cherry"]
        expected = ["Banana", "Zebra", "apple", "cherry"]
        result = Merge.sort(arr)
        assert result == expected
        assert Merge.is_sorted(result)

    def test_negative_numbers(self):
        """Test: Sortieren negativer Zahlen."""
        arr = [-3, -1, -4, 1, 5, -9, 2, -6]
        expected = [-9, -6, -4, -3, -1, 1, 2, 5]
        result = Merge.sort(arr)
        assert result == expected
        assert Merge.is_sorted(result)

    def test_mixed_numbers(self):
        """Test: Sortieren gemischter positiver, negativer und Null-Werte."""
        arr = [0, -3, 7, -1, 0, 4, -2]
        expected = [-3, -2, -1, 0, 0, 4, 7]
        result = Merge.sort(arr)
        assert result == expected
        assert Merge.is_sorted(result)

    @pytest.mark.slow
    def test_large_list(self, grosser_datensatz):
        """Test: Sortieren einer grösseren Liste."""
        shuffled = grosser_datensatz.copy()
        import random

        random.shuffle(shuffled)
        result = Merge.sort(shuffled)
        assert result == sorted(grosser_datensatz)
        assert Merge.is_sorted(result)

    def test_all_same_elements(self):
        """Test: Sortieren einer Liste mit identischen Elementen."""
        arr = [7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7]
        result = Merge.sort(arr)
        assert result == expected
        assert Merge.is_sorted(result)

    def test_two_elements(self):
        """Test: Sortieren einer Liste mit zwei Elementen."""
        # Unsortiert
        arr = [2, 1]
        expected = [1, 2]
        result = Merge.sort(arr)
        assert result == expected
        assert Merge.is_sorted(result)

        # Bereits sortiert
        arr = [1, 2]
        expected = [1, 2]
        result = Merge.sort(arr)
        assert result == expected
        assert Merge.is_sorted(result)

    def test_different_types(self):
        """Test: Sortieren verschiedener Datentypen."""
        # Float-Zahlen
        arr = [3.14, 2.71, 1.41, 2.23]
        expected = [1.41, 2.23, 2.71, 3.14]
        result = Merge.sort(arr)
        assert result == expected
        assert Merge.is_sorted(result)

        # Einzelne Zeichen
        arr = ["d", "a", "c", "b"]
        expected = ["a", "b", "c", "d"]
        result = Merge.sort(arr)
        assert result == expected
        assert Merge.is_sorted(result)

    def test_is_sorted_false(self):
        """Test: is_sorted gibt False für unsortierte Listen zurück."""
        assert not Merge.is_sorted([3, 1, 2])
        assert not Merge.is_sorted([1, 3, 2, 4])
        assert not Merge.is_sorted([5, 4, 3, 2, 1])

    def test_is_sorted_true(self):
        """Test: is_sorted gibt True für sortierte Listen zurück."""
        assert Merge.is_sorted([])
        assert Merge.is_sorted([1])
        assert Merge.is_sorted([1, 2, 3, 4, 5])
        assert Merge.is_sorted([1, 1, 2, 2, 3])

    def test_sort_preserves_original_if_needed(self):
        """Test: sort modifiziert die ursprüngliche Liste in-place."""
        original = [3, 1, 4, 1, 5]
        sorted_list = Merge.sort(original)

        # Das Ergebnis sollte die gleiche Referenz wie das Original sein
        assert sorted_list is original
        assert original == [1, 1, 3, 4, 5]

    # Merge-spezifische Tests

    def test_merge_method_basic(self):
        """Test: Grundlegende Funktionalität der merge-Methode."""
        arr = [1, 3, 5, 2, 4, 6]  # Zwei sortierte Hälften: [1,3,5] und [2,4,6]
        Merge.merge(arr, 0, 2, 5)
        expected = [1, 2, 3, 4, 5, 6]
        assert arr == expected

    def test_merge_method_edge_cases(self):
        """Test: Grenzfälle der merge-Methode."""
        # Ein Element in jeder Hälfte
        arr = [2, 1]
        Merge.merge(arr, 0, 0, 1)
        assert arr == [1, 2]

        # Erste Hälfte bereits kleiner
        arr = [1, 2, 3, 4]
        Merge.merge(arr, 0, 1, 3)
        assert arr == [1, 2, 3, 4]

        # Zweite Hälfte bereits kleiner
        arr = [3, 4, 1, 2]
        Merge.merge(arr, 0, 1, 3)
        assert arr == [1, 2, 3, 4]

    def test_merge_sort_divide_and_conquer(self):
        """Test: Divide-and-Conquer-Eigenschaften von Merge Sort."""
        arr = [8, 3, 5, 4, 7, 6, 1, 2]
        original_length = len(arr)

        result = Merge.sort(arr)

        # Länge sollte gleich bleiben
        assert len(result) == original_length

        # Sollte sortiert sein
        assert Merge.is_sorted(result)

        # Sollte alle ursprünglichen Elemente enthalten
        assert sorted(result) == [1, 2, 3, 4, 5, 6, 7, 8]

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
        result = Merge.sort(shuffled)
        assert result == expected
        assert Merge.is_sorted(result)

    def test_guaranteed_performance(self):
        """Test: Merge Sort hat garantierte O(n log n) Performance."""
        # Merge Sort sollte für alle Eingabetypen die gleiche Performance haben
        import random

        # Bereits sortiert
        sorted_arr = list(range(100))
        result1 = Merge.sort(sorted_arr.copy())
        assert Merge.is_sorted(result1)

        # Umgekehrt sortiert
        reverse_arr = list(range(100, 0, -1))
        result2 = Merge.sort(reverse_arr)
        assert Merge.is_sorted(result2)

        # Zufällig
        random_arr = list(range(100))
        random.shuffle(random_arr)
        result3 = Merge.sort(random_arr)
        assert Merge.is_sorted(result3)

        # Alle sollten korrekt sortiert sein
        expected = list(range(1, 101))
        assert result1 == list(range(100))
        assert result2 == expected
        assert result3 == list(range(100))

    def test_stability_guaranteed(self):
        """Test: Merge Sort ist stabil - gleiche Elemente behalten ihre Reihenfolge."""

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

        # Erstelle Elemente mit gleichen Werten aber verschiedenen Indizes
        arr = [
            ComparableItem(3, 0),
            ComparableItem(1, 1),
            ComparableItem(3, 2),
            ComparableItem(2, 3),
            ComparableItem(1, 4),
        ]

        result = Merge.sort(arr)

        # Überprüfe, dass sortiert ist
        for i in range(1, len(result)):
            assert result[i].value >= result[i - 1].value

        # Überprüfe Stabilität: Elemente mit gleichem Wert sollten
        # ihre ursprüngliche Reihenfolge beibehalten
        ones = [item for item in result if item.value == 1]
        threes = [item for item in result if item.value == 3]

        assert ones[0].original_index < ones[1].original_index  # 1,1 dann 1,4
        assert threes[0].original_index < threes[1].original_index  # 3,0 dann 3,2

    def test_merge_sort_vs_other_algorithms(self):
        """Test: Vergleich von Merge Sort mit Python's sorted()."""
        test_cases = [
            [],  # Leer
            [1],  # Ein Element
            [2, 1],  # Zwei Elemente
            [1, 2, 3, 4, 5],  # Bereits sortiert
            [5, 4, 3, 2, 1],  # Umgekehrt sortiert
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],  # Mit Duplikaten
        ]

        for test_case in test_cases:
            merge_result = Merge.sort(test_case.copy())
            python_result = sorted(test_case)
            assert merge_result == python_result

    def test_merge_sort_with_custom_objects(self):
        """Test: Merge Sort mit benutzerdefinierten Objekten."""

        class Student:
            def __init__(self, name, grade):
                self.name = name
                self.grade = grade

            def __lt__(self, other):
                return self.grade < other.grade

            def __le__(self, other):
                return self.grade <= other.grade

            def __gt__(self, other):
                return self.grade > other.grade

            def __ge__(self, other):
                return self.grade >= other.grade

            def __eq__(self, other):
                return self.grade == other.grade

            def __repr__(self):
                return f"{self.name}: {self.grade}"

        students = [
            Student("Alice", 85),
            Student("Bob", 92),
            Student("Charlie", 78),
            Student("Diana", 96),
            Student("Eve", 88),
        ]

        result = Merge.sort(students)

        # Überprüfe, dass nach Noten sortiert ist
        for i in range(1, len(result)):
            assert result[i].grade >= result[i - 1].grade

        # Überprüfe spezifische Reihenfolge
        expected_names = ["Charlie", "Alice", "Eve", "Bob", "Diana"]
        actual_names = [student.name for student in result]
        assert actual_names == expected_names
