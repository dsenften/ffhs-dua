"""
Benchmarks für ffhs-dua Algorithmen und Datenstrukturen.

Dieses Paket enthält Performance-Benchmarks für:
- Sortieralgorithmen (Shell Sort, Quick Sort, Merge Sort, Heap Sort)
- Datenstrukturen (Union-Find, Suchbäume, Hash Tables)
- Verschiedene Datentypen und Größen

Beispiel:
    >>> from benchmarks.sorting_benchmarks import run_sorting_benchmarks
    >>> results = run_sorting_benchmarks()
"""

__version__ = "1.0.0"
__author__ = "FFHS DUA Team"

from benchmarks.sorting_benchmarks import (
    benchmark_algorithm,
    generate_test_data,
    run_sorting_benchmarks,
)

__all__ = [
    "benchmark_algorithm",
    "generate_test_data",
    "run_sorting_benchmarks",
]
