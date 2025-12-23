"""
Performance-Benchmarks für Sortieralgorithmen.

Dieses Modul bietet Funktionen zum Benchmarking verschiedener Sortieralgorithmen
unter verschiedenen Bedingungen (zufällig, sortiert, umgekehrt, fast sortiert).

Beispiel:
    >>> from benchmarks.sorting_benchmarks import run_sorting_benchmarks
    >>> results = run_sorting_benchmarks()
    >>> print(results)
"""

import random
import time
from collections.abc import Callable

from src.algs4.pva_2_sorting import Heap, Merge, Quick, Shell


def generate_test_data(size: int, data_type: str = "random") -> list[int]:
    """
    Generiert Testdaten für Benchmarks.

    Args:
        size: Anzahl der zu generierenden Elemente
        data_type: Typ der Testdaten
            - 'random': Zufällig generierte Daten
            - 'sorted': Bereits sortierte Daten (Best-Case)
            - 'reverse': Umgekehrt sortierte Daten (Worst-Case)
            - 'nearly_sorted': Fast sortierte Daten (5% Abweichung)

    Returns:
        Liste mit generierten Testdaten

    Raises:
        ValueError: Wenn data_type nicht erkannt wird
    """
    if data_type == "random":
        return [random.randint(1, size) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reverse":
        return list(range(size, 0, -1))
    elif data_type == "nearly_sorted":
        data = list(range(size))
        # Vertausche 5% der Elemente
        swaps = size // 20
        for _ in range(swaps):
            i, j = random.randint(0, size - 1), random.randint(0, size - 1)
            data[i], data[j] = data[j], data[i]
        return data
    else:
        raise ValueError(f"Unbekannter Datentyp: {data_type}")


def benchmark_algorithm(algorithm: Callable, data: list[int]) -> float:
    """
    Misst die Ausführungszeit eines Sortieralgorithmus.

    Args:
        algorithm: Sortieralgorithmus-Funktion (z.B. quick_sort, merge_sort)
        data: Zu sortierende Daten

    Returns:
        Ausführungszeit in Sekunden (float)

    Note:
        Die Funktion erstellt eine Kopie der Eingabedaten, um die Originalität
        zu bewahren und faire Vergleiche zu ermöglichen.
    """
    data_copy = data.copy()
    start_time = time.perf_counter()
    algorithm(data_copy)
    end_time = time.perf_counter()
    return end_time - start_time


def run_sorting_benchmarks() -> dict[str, dict[str, float]]:
    """
    Run benchmarks for multiple sorting algorithms across predefined data patterns and sizes.
    
    Benchmarks Shell Sort, Merge Sort, and Heap Sort on data types "random", "sorted", "reverse", and "nearly_sorted" for sizes 100, 1000, and 10000. Benchmarks Quick Sort separately using sizes 100, 1000, and 5000 and only the "random" and "nearly_sorted" data types to avoid worst-case behavior on sorted inputs.
    
    Returns:
        dict[str, dict[str, float]]: Mapping from algorithm name to a mapping of
        keys formatted as "<data_type>_<size>" to execution time in seconds.
    """
    algorithms = {
        "Shell Sort": Shell.sort,
        "Merge Sort": Merge.sort,
        "Heap Sort": Heap.sort,
    }

    # Quick Sort separat mit kleineren Datenmengen
    quick_sort_algorithms = {"Quick Sort": Quick.sort}

    data_sizes = [100, 1000, 10000]
    data_types = ["random", "sorted", "reverse", "nearly_sorted"]

    # Kleinere Datenmengen für Quick Sort (Worst-Case Schutz)
    quick_sort_sizes = [100, 1000, 5000]

    results: dict[str, dict[str, float]] = {}

    # Benchmark für stabile Algorithmen
    for alg_name, algorithm in algorithms.items():
        results[alg_name] = {}

        for size in data_sizes:
            for data_type in data_types:
                test_data = generate_test_data(size, data_type)
                execution_time = benchmark_algorithm(algorithm, test_data)

                key = f"{data_type}_{size}"
                results[alg_name][key] = execution_time

                print(
                    f"{alg_name} - {data_type} ({size} Elemente): {execution_time:.4f}s"
                )

    # Benchmark für Quick Sort (mit kleineren Datenmengen und nur zufälligen Daten)
    # Quick Sort hat Worst-Case O(n²) bei sortierten/umgekehrten Daten
    quick_sort_data_types = ["random", "nearly_sorted"]

    for alg_name, algorithm in quick_sort_algorithms.items():
        results[alg_name] = {}

        for size in quick_sort_sizes:
            for data_type in quick_sort_data_types:
                test_data = generate_test_data(size, data_type)
                execution_time = benchmark_algorithm(algorithm, test_data)

                key = f"{data_type}_{size}"
                results[alg_name][key] = execution_time

                print(
                    f"{alg_name} - {data_type} ({size} Elemente): {execution_time:.4f}s"
                )

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("Sortieralgorithmus-Benchmarks für ffhs-dua")
    print("=" * 60)
    print()

    benchmark_results = run_sorting_benchmarks()

    print()
    print("=" * 60)
    print("Benchmarks abgeschlossen!")
    print("=" * 60)