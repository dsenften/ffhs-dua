# -*- coding: utf-8 -*-
"""Pytest-Konfiguration für die Tests des Projekts.

Diese Datei enthält Konfigurationen und Hilfsfunktionen für pytest.
"""
import pytest


def pytest_collection_modifyitems(items):
    """Modifiziert die gesammelten Testitems.
    
    Überspringt Tests, die direkt von der TestUnionFindBase-Klasse stammen,
    da diese eine abstrakte Basisklasse ist und nicht direkt getestet werden sollte.
    """
    for item in items:
        if item.cls and item.cls.__name__ == "TestUnionFindBase":
            item.add_marker(pytest.mark.skip(reason="Abstrakte Basisklasse, sollte nicht direkt ausgeführt werden"))
