"""
Performance-Benchmarks für Sortieralgorithmen.
"""

import time
import random
from typing import List, Callable, Dict
from src.algs4.sorting.shell import shell_sort


def generate_test_data(size: int, data_type: str = "random") -> List[int]:
    """Generiert Testdaten für Benchmarks."""
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
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            data[i], data[j] = data[j], data[i]
        return data
    else:
        raise ValueError(f"Unbekannter Datentyp: {data_type}")


def benchmark_algorithm(algorithm: Callable, data: List[int]) -> float:
    """Misst die Ausführungszeit eines Sortieralgorithmus."""
    data_copy = data.copy()
    start_time = time.perf_counter()
    algorithm(data_copy)
    end_time = time.perf_counter()
    return end_time - start_time


def run_sorting_benchmarks() -> Dict[str, Dict[str, float]]:
    """Führt umfassende Benchmarks für Sortieralgorithmen durch."""
    algorithms = {
        "Shell Sort": shell_sort
    }
    
    data_sizes = [100, 1000, 10000]
    data_types = ["random", "sorted", "reverse", "nearly_sorted"]
    
    results = {}
    
    for alg_name, algorithm in algorithms.items():
        results[alg_name] = {}
        
        for size in data_sizes:
            for data_type in data_types:
                test_data = generate_test_data(size, data_type)
                execution_time = benchmark_algorithm(algorithm, test_data)
                
                key = f"{data_type}_{size}"
                results[alg_name][key] = execution_time
                
                print(f"{alg_name} - {data_type} ({size} Elemente): {execution_time:.4f}s")
    
    return results


if __name__ == "__main__":
    print("Starte Sortieralgorithmus-Benchmarks...")
    benchmark_results = run_sorting_benchmarks()
    print("\nBenchmarks abgeschlossen!")
