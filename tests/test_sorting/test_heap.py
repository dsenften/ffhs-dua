"""
Tests für den Heap-Sort-Algorithmus.

Diese Datei enthält umfassende Tests für die Heap-Sort-Implementierung.
Verwendet Test-Vorrichtungen aus conftest.py für konsistente Testumgebungen.
"""

import pytest

from src.algs4.sorting.heap import Heap


class TestHeap:
    """Test-Klasse für die Heap-Sort-Implementierung."""

    def test_empty_list(self):
        """Test: Sortieren einer leeren Liste."""
        arr = []
        result = Heap.sort(arr)
        assert result == []
        assert Heap.is_sorted(result)

    def test_single_element(self):
        """Test: Sortieren einer Liste mit einem Element."""
        arr = [42]
        result = Heap.sort(arr)
        assert result == [42]
        assert Heap.is_sorted(result)

    def test_already_sorted(self, beispiel_ganzzahlen):
        """Test: Sortieren einer bereits sortierten Liste."""
        sorted_list = sorted(beispiel_ganzzahlen)
        result = Heap.sort(sorted_list.copy())
        assert result == sorted_list
        assert Heap.is_sorted(result)

    def test_reverse_sorted(self, beispiel_ganzzahlen):
        """Test: Sortieren einer umgekehrt sortierten Liste."""
        reversed_list = sorted(beispiel_ganzzahlen, reverse=True)
        expected = sorted(beispiel_ganzzahlen)
        result = Heap.sort(reversed_list)
        assert result == expected
        assert Heap.is_sorted(result)

    def test_random_integers(self, beispiel_ganzzahlen):
        """Test: Sortieren einer zufälligen Liste von Ganzzahlen."""
        import random
        shuffled = beispiel_ganzzahlen.copy()
        random.shuffle(shuffled)
        expected = sorted(beispiel_ganzzahlen)
        result = Heap.sort(shuffled)
        assert result == expected
        assert Heap.is_sorted(result)

    def test_duplicates(self):
        """Test: Sortieren einer Liste mit duplizierten Elementen."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        result = Heap.sort(arr)
        assert result == expected
        assert Heap.is_sorted(result)

    def test_strings(self, beispiel_zeichenketten):
        """Test: Sortieren einer Liste von Strings."""
        import random
        shuffled = beispiel_zeichenketten.copy()
        random.shuffle(shuffled)
        expected = sorted(beispiel_zeichenketten)
        result = Heap.sort(shuffled)
        assert result == expected
        assert Heap.is_sorted(result)

    def test_strings_case_sensitive(self):
        """Test: Sortieren von Strings mit Gross-/Kleinschreibung."""
        arr = ["Zebra", "apple", "Banana", "cherry"]
        expected = ["Banana", "Zebra", "apple", "cherry"]
        result = Heap.sort(arr)
        assert result == expected
        assert Heap.is_sorted(result)

    def test_negative_numbers(self):
        """Test: Sortieren einer Liste mit negativen Zahlen."""
        arr = [-3, -1, -4, 1, 5, -9, 2, -6]
        expected = [-9, -6, -4, -3, -1, 1, 2, 5]
        result = Heap.sort(arr)
        assert result == expected
        assert Heap.is_sorted(result)

    def test_mixed_numbers(self):
        """Test: Sortieren einer Liste mit positiven, negativen und null Werten."""
        arr = [0, -3, 7, -1, 0, 4, -2]
        expected = [-3, -2, -1, 0, 0, 4, 7]
        result = Heap.sort(arr)
        assert result == expected
        assert Heap.is_sorted(result)

    @pytest.mark.slow
    def test_large_list(self, grosser_datensatz):
        """Test: Sortieren einer grösseren Liste."""
        shuffled = grosser_datensatz.copy()
        import random
        random.shuffle(shuffled)
        expected = sorted(grosser_datensatz)
        result = Heap.sort(shuffled)
        assert result == expected
        assert Heap.is_sorted(result)

    def test_all_same_elements(self):
        """Test: Sortieren einer Liste mit identischen Elementen."""
        arr = [5, 5, 5, 5, 5]
        expected = [5, 5, 5, 5, 5]
        result = Heap.sort(arr)
        assert result == expected
        assert Heap.is_sorted(result)

    def test_two_elements(self):
        """Test: Sortieren einer Liste mit zwei Elementen."""
        # Unsortiert
        arr = [2, 1]
        expected = [1, 2]
        result = Heap.sort(arr)
        assert result == expected
        assert Heap.is_sorted(result)

        # Bereits sortiert
        arr = [1, 2]
        expected = [1, 2]
        result = Heap.sort(arr)
        assert result == expected
        assert Heap.is_sorted(result)

    def test_different_types(self):
        """Test: Heap-Sort mit verschiedenen Datentypen."""
        # Float-Zahlen
        float_arr = [3.14, 2.71, 1.41, 2.23]
        float_expected = [1.41, 2.23, 2.71, 3.14]
        float_result = Heap.sort(float_arr)
        assert float_result == float_expected
        assert Heap.is_sorted(float_result)

        # Zeichen
        char_arr = ["d", "a", "c", "b"]
        char_expected = ["a", "b", "c", "d"]
        char_result = Heap.sort(char_arr)
        assert char_result == char_expected
        assert Heap.is_sorted(char_result)

    def test_is_sorted_false(self):
        """Test: is_sorted-Methode mit unsortierten Listen."""
        assert not Heap.is_sorted([3, 1, 2])
        assert not Heap.is_sorted([1, 3, 2, 4])
        assert not Heap.is_sorted([5, 4, 3, 2, 1])

    def test_is_sorted_true(self):
        """Test: is_sorted-Methode mit sortierten Listen."""
        assert Heap.is_sorted([])
        assert Heap.is_sorted([1])
        assert Heap.is_sorted([1, 2, 3, 4, 5])
        assert Heap.is_sorted([1, 1, 2, 2, 3])

    def test_sort_preserves_original_if_needed(self):
        """Test: Ob die ursprüngliche Liste in-place sortiert wird."""
        original = [3, 1, 4, 1, 5]
        sorted_list = Heap.sort(original)
        # Heap.sort modifiziert die ursprüngliche Liste in-place und gibt sie zurück
        assert sorted_list is original
        assert original == [1, 1, 3, 4, 5]

    def test_sink_method_basic(self):
        """Test: Grundlegende Funktionalität der sink-Methode."""
        # Teste sink mit einem einfachen Heap
        arr = [1, 4, 3, 2]  # Verletzt Heap-Eigenschaft an Index 0
        Heap.sink(arr, 0, 3)
        
        # Nach dem Sinken sollte die Heap-Eigenschaft erfüllt sein
        # Das groesste Element sollte an der Wurzel stehen
        assert arr[0] >= arr[1] if len(arr) > 1 else True
        assert arr[0] >= arr[2] if len(arr) > 2 else True

    def test_sink_method_edge_cases(self):
        """Test: Grenzfälle der sink-Methode."""
        # Ein Element
        arr = [5]
        Heap.sink(arr, 0, 0)
        assert arr == [5]
        
        # Zwei Elemente - bereits korrekt
        arr = [5, 3]
        Heap.sink(arr, 0, 1)
        assert arr[0] >= arr[1]
        
        # Zwei Elemente - muss getauscht werden
        arr = [3, 5]
        Heap.sink(arr, 0, 1)
        assert arr == [5, 3]

    def test_heap_construction_phase(self):
        """Test: Heap-Konstruktionsphase separat testen."""
        arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        n = len(arr)
        
        # Führe nur die Heap-Konstruktionsphase durch
        k = n // 2 - 1
        while k >= 0:
            Heap.sink(arr, k, n - 1)
            k -= 1
        
        # Überprüfe Heap-Eigenschaft: Jeder Knoten >= seiner Kinder
        for i in range(n // 2):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            
            if left_child < n:
                assert arr[i] >= arr[left_child], f"Heap-Eigenschaft verletzt: arr[{i}]={arr[i]} < arr[{left_child}]={arr[left_child]}"
            
            if right_child < n:
                assert arr[i] >= arr[right_child], f"Heap-Eigenschaft verletzt: arr[{i}]={arr[i]} < arr[{right_child}]={arr[right_child]}"

    def test_heap_sort_phases(self):
        """Test: Beide Phasen des Heap-Sort-Algorithmus."""
        arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        original_arr = arr.copy()
        n = len(arr)
        
        # Phase 1: Heap-Konstruktion
        k = n // 2 - 1
        while k >= 0:
            Heap.sink(arr, k, n - 1)
            k -= 1
        
        # Überprüfe, dass ein gültiger Max-Heap erstellt wurde
        for i in range(n // 2):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            
            if left_child < n:
                assert arr[i] >= arr[left_child]
            if right_child < n:
                assert arr[i] >= arr[right_child]
        
        # Phase 2: Sortdown
        while n > 1:
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            n -= 1
            Heap.sink(arr, 0, n - 1)
        
        # Überprüfe, dass das Array sortiert ist
        assert Heap.is_sorted(arr)
        # Überprüfe, dass es die gleichen Elemente enthält
        assert sorted(arr) == sorted(original_arr)

    def test_heap_property_maintenance(self):
        """Test: Erhaltung der Heap-Eigenschaft während des Sortierens."""
        arr = [9, 5, 6, 2, 3, 7, 1, 4, 8]
        n = len(arr)
        
        # Baue initial einen Max-Heap
        k = n // 2 - 1
        while k >= 0:
            Heap.sink(arr, k, n - 1)
            k -= 1
        
        # Simuliere die Sortdown-Phase und überprüfe Heap-Eigenschaft nach jedem Schritt
        original_n = n
        while n > 1:
            # Das Maximum sollte an der Wurzel stehen
            max_element = arr[0]
            for i in range(n):
                assert arr[0] >= arr[i], f"Maximum nicht an Wurzel: arr[0]={arr[0]} < arr[{i}]={arr[i]}"
            
            # Tausche und reduziere Heap-Grösse
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            n -= 1
            
            # Stelle Heap-Eigenschaft wieder her
            if n > 1:
                Heap.sink(arr, 0, n - 1)
                
                # Überprüfe Heap-Eigenschaft für den reduzierten Heap
                for i in range(n // 2):
                    left_child = 2 * i + 1
                    right_child = 2 * i + 2
                    
                    if left_child < n:
                        assert arr[i] >= arr[left_child]
                    if right_child < n:
                        assert arr[i] >= arr[right_child]

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
        result = Heap.sort(shuffled)
        assert result == expected
        assert Heap.is_sorted(result)

    def test_consistent_performance(self):
        """Test: Heap Sort hat konsistente O(n log n) Performance."""
        # Heap Sort sollte für alle Eingabetypen ähnliche Performance haben
        import random
        
        # Bereits sortiert
        sorted_arr = list(range(100))
        result1 = Heap.sort(sorted_arr.copy())
        assert Heap.is_sorted(result1)
        
        # Umgekehrt sortiert
        reverse_arr = list(range(100, 0, -1))
        result2 = Heap.sort(reverse_arr)
        assert Heap.is_sorted(result2)
        
        # Zufällig
        random_arr = list(range(100))
        random.shuffle(random_arr)
        result3 = Heap.sort(random_arr)
        assert Heap.is_sorted(result3)
        
        # Alle sollten das gleiche Ergebnis haben
        expected = list(range(100))
        assert result1 == expected
        assert result2 == list(range(1, 101))  # range(100, 0, -1) erzeugt 100 bis 1
        assert result3 == expected

    def test_stability_not_guaranteed(self):
        """Test: Heap Sort ist nicht stabil - gleiche Elemente können ihre Reihenfolge ändern."""
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
        
        result = Heap.sort(arr)
        
        # Überprüfe, dass sortiert ist
        for i in range(1, len(result)):
            assert result[i].value >= result[i-1].value
        
        # Heap Sort ist nicht stabil, also testen wir nur die Korrektheit der Sortierung
        values = [item.value for item in result]
        assert values == [1, 1, 2, 3, 3]

    def test_heap_sort_vs_other_algorithms(self):
        """Test: Vergleiche Heap Sort mit Python's eingebautem sort."""
        import random
        
        test_cases = [
            [],  # Leer
            [1],  # Ein Element
            [2, 1],  # Zwei Elemente
            [1, 2, 3, 4, 5],  # Bereits sortiert
            [5, 4, 3, 2, 1],  # Umgekehrt sortiert
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],  # Mit Duplikaten
            [random.randint(1, 100) for _ in range(50)]  # Zufällig
        ]
        
        for test_case in test_cases:
            heap_result = Heap.sort(test_case.copy())
            python_result = sorted(test_case)
            assert heap_result == python_result, f"Heap Sort Ergebnis {heap_result} != Python sort {python_result} für Input {test_case}"

    def test_heap_sort_with_custom_objects(self):
        """Test: Heap Sort mit benutzerdefinierten Objekten."""
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
            Student("Eve", 88)
        ]
        
        result = Heap.sort(students)
        
        # Überprüfe, dass nach Noten sortiert ist
        for i in range(1, len(result)):
            assert result[i].grade >= result[i-1].grade
        
        # Überprüfe spezifische Reihenfolge
        expected_names = ["Charlie", "Alice", "Eve", "Bob", "Diana"]
        actual_names = [student.name for student in result]
        assert actual_names == expected_names
