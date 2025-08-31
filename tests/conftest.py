"""Pytest-Konfiguration für die Tests des Projekts.

Diese Datei enthält Konfigurationen und Hilfsfunktionen für pytest.
Gemeinsame Test-Fixtures für das ALGS4-Projekt.
"""


import pytest

from src.algs4.fundamentals.bag import Bag
from src.algs4.fundamentals.queue import Queue
from src.algs4.fundamentals.stack import Stack


@pytest.fixture
def empty_bag():
    """Erstellt einen leeren Bag für Tests."""
    return Bag()


@pytest.fixture
def empty_queue():
    """Erstellt eine leere Queue für Tests."""
    return Queue()


@pytest.fixture
def empty_stack():
    """Erstellt einen leeren Stack für Tests."""
    return Stack()


@pytest.fixture
def sample_integers():
    """Beispiel-Integer-Liste für Tests."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_strings():
    """Beispiel-String-Liste für Tests."""
    return ["apple", "banana", "cherry", "date"]


@pytest.fixture
def large_dataset():
    """Großer Datensatz für Performance-Tests."""
    return list(range(1000))


def pytest_collection_modifyitems(items):
    """Modifiziert die gesammelten Testitems.

    Überspringt Tests, die direkt von der TestUnionFindBase-Klasse stammen,
    da diese eine abstrakte Basisklasse ist und nicht direkt getestet werden sollte.
    """
    for item in items:
        if item.cls and item.cls.__name__ == "TestUnionFindBase":
            item.add_marker(
                pytest.mark.skip(
                    reason="Abstrakte Basisklasse, sollte nicht direkt ausgeführt werden"
                )
            )
