"""Pytest-Konfiguration für die Tests des Projekts.

Diese Datei enthält Konfigurationen und Hilfsfunktionen für pytest.
Gemeinsame Test-Vorrichtungen für das ALGS4-Projekt.
"""


import pytest

from src.algs4.fundamentals.bag import Bag
from src.algs4.fundamentals.queue import Queue
from src.algs4.fundamentals.stack import Stack


@pytest.fixture
def leerer_bag():
    """Test-Vorrichtung: Erstellt einen leeren Bag für Tests.

    Diese Test-Vorrichtung stellt sicher, dass jeder Test mit einem
    frischen, leeren Bag-Objekt beginnt.
    """
    return Bag()


@pytest.fixture
def leere_queue():
    """Test-Vorrichtung: Erstellt eine leere Queue für Tests.

    Diese Test-Vorrichtung stellt sicher, dass jeder Test mit einer
    frischen, leeren Queue beginnt.
    """
    return Queue()


@pytest.fixture
def leerer_stack():
    """Test-Vorrichtung: Erstellt einen leeren Stack für Tests.

    Diese Test-Vorrichtung stellt sicher, dass jeder Test mit einem
    frischen, leeren Stack beginnt.
    """
    return Stack()


@pytest.fixture
def beispiel_ganzzahlen():
    """Test-Vorrichtung: Beispiel-Integer-Liste für Tests.

    Stellt eine konsistente Liste von Ganzzahlen für Testfälle bereit.
    """
    return [1, 2, 3, 4, 5]


@pytest.fixture
def beispiel_zeichenketten():
    """Test-Vorrichtung: Beispiel-String-Liste für Tests.

    Stellt eine konsistente Liste von Zeichenketten für Testfälle bereit.
    """
    return ["apple", "banana", "cherry", "date"]


@pytest.fixture
def grosser_datensatz():
    """Test-Vorrichtung: Grosser Datensatz für Performance-Tests.

    Erstellt einen grossen Datensatz mit 1000 Elementen für
    Leistungstests und Skalierbarkeitsanalysen.
    """
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
