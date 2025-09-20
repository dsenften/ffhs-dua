"""
Beispieldaten für Tests.
"""

from typing import Any


def get_small_integer_dataset() -> list[int]:
    """Kleine Integer-Datensätze für Unit-Tests."""
    return [1, 5, 3, 9, 2, 8, 4, 7, 6]


def get_medium_string_dataset() -> list[str]:
    """Mittlere String-Datensätze für Integration-Tests."""
    return [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon",
        "mango", "nectarine", "orange", "papaya", "quince"
    ]


def get_large_integer_dataset() -> list[int]:
    """Grosse Integer-Datensaetze für Performance-Tests."""
    return list(range(10000))


def get_sorting_test_cases() -> dict[str, list[int]]:
    """Verschiedene Test-Fälle für Sortieralgorithmen."""
    return {
        "already_sorted": [1, 2, 3, 4, 5],
        "reverse_sorted": [5, 4, 3, 2, 1],
        "random": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
        "duplicates": [1, 3, 2, 3, 1, 2, 1],
        "single_element": [42],
        "empty": [],
        "two_elements": [2, 1]
    }


def get_graph_test_data() -> dict[str, Any]:
    """Test-Daten für Graph-Algorithmen."""
    return {
        "simple_graph": {
            "vertices": 5,
            "edges": [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]
        },
        "disconnected_graph": {
            "vertices": 6,
            "edges": [(0, 1), (1, 2), (3, 4)]
        },
        "complete_graph": {
            "vertices": 4,
            "edges": [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        }
    }
