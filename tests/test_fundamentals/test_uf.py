"""
Tests für die Union-Find-Datenstrukturen.

Diese Datei enthält umfassende Tests für alle Union-Find-Implementierungen.
Verwendet Test-Vorrichtungen aus conftest.py für konsistente Testumgebungen.
"""

import pytest

from src.algs4.pva_1_fundamentals.uf import (
    UF,
    QuickFindUF,
    QuickUnionUF,
    WeightedQuickUnionUF,
)


class TestUF:
    """Test-Klasse für die optimierte Union-Find-Implementierung."""

    def test_uf_creation(self):
        """Test: UF-Struktur wird korrekt erstellt."""
        uf = UF(10)
        assert uf.count() == 10

        # Alle Elemente sollten anfangs getrennt sein
        for i in range(10):
            for j in range(i + 1, 10):
                assert not uf.connected(i, j)

    def test_union_operation(self):
        """Test: Union-Operation verbindet Elemente."""
        uf = UF(5)

        # Verbinde 0 und 1
        uf.union(0, 1)
        assert uf.connected(0, 1)
        assert uf.count() == 4

        # Verbinde 2 und 3
        uf.union(2, 3)
        assert uf.connected(2, 3)
        assert uf.count() == 3

        # 0,1 und 2,3 sollten noch getrennt sein
        assert not uf.connected(0, 2)
        assert not uf.connected(1, 3)

    def test_transitive_connections(self):
        """Test: Transitive Verbindungen funktionieren."""
        uf = UF(6)

        # Kette: 0-1-2-3
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)

        # Alle sollten verbunden sein
        assert uf.connected(0, 3)
        assert uf.connected(1, 3)
        assert uf.connected(0, 2)
        assert uf.count() == 3  # {0,1,2,3}, {4}, {5}

    def test_find_operation(self):
        """Test: Find-Operation gibt korrekte Wurzel zurück."""
        uf = UF(5)

        # Anfangs ist jedes Element seine eigene Wurzel
        for i in range(5):
            assert uf.find(i) == i

        # Nach Union haben verbundene Elemente dieselbe Wurzel
        uf.union(0, 1)
        uf.union(2, 3)

        assert uf.find(0) == uf.find(1)
        assert uf.find(2) == uf.find(3)
        assert uf.find(0) != uf.find(2)

    def test_invalid_indices_raise_exception(self):
        """Test: Ungültige Indizes werfen Exception."""
        uf = UF(5)

        with pytest.raises(ValueError, match="Index -1 ist nicht zwischen 0 und 4"):
            uf.union(-1, 0)

        with pytest.raises(ValueError, match="Index 5 ist nicht zwischen 0 und 4"):
            uf.union(0, 5)

        with pytest.raises(ValueError, match="Index 10 ist nicht zwischen 0 und 4"):
            uf.connected(10, 0)

        with pytest.raises(ValueError, match="Index -1 ist nicht zwischen 0 und 4"):
            uf.find(-1)

    def test_self_union_no_effect(self):
        """Test: Union eines Elements mit sich selbst hat keinen Effekt."""
        uf = UF(3)
        initial_count = uf.count()

        uf.union(1, 1)
        assert uf.count() == initial_count
        assert uf.connected(1, 1)  # Element ist immer mit sich selbst verbunden

    @pytest.mark.slow
    def test_large_dataset_performance(self, grosser_datensatz):
        """Test: Performance mit grossem Datensatz."""
        n = len(grosser_datensatz)
        uf = UF(n)

        # Verbinde aufeinanderfolgende Paare
        for i in range(0, n - 1, 2):
            uf.union(i, i + 1)

        # Überprüfe Verbindungen
        for i in range(0, n - 1, 2):
            assert uf.connected(i, i + 1)


class TestQuickFindUF:
    """Test-Klasse für QuickFindUF-Implementierung."""

    def test_quick_find_creation(self):
        """Test: QuickFindUF wird korrekt erstellt."""
        uf = QuickFindUF(8)
        assert uf.count() == 8

    def test_quick_find_union_and_connected(self):
        """Test: Union und Connected bei QuickFindUF."""
        uf = QuickFindUF(6)

        uf.union(0, 1)
        uf.union(2, 3)
        uf.union(4, 5)

        assert uf.connected(0, 1)
        assert uf.connected(2, 3)
        assert uf.connected(4, 5)
        assert not uf.connected(0, 2)
        assert uf.count() == 3

    def test_quick_find_large_component(self):
        """Test: Grosse Komponente bei QuickFindUF."""
        uf = QuickFindUF(10)

        # Verbinde alle Elemente zu einer Komponente
        for i in range(9):
            uf.union(i, i + 1)

        # Alle sollten verbunden sein
        for i in range(10):
            for j in range(i + 1, 10):
                assert uf.connected(i, j)

        assert uf.count() == 1


class TestQuickUnionUF:
    """Test-Klasse für QuickUnionUF-Implementierung."""

    def test_quick_union_creation(self):
        """Test: QuickUnionUF wird korrekt erstellt."""
        uf = QuickUnionUF(7)
        assert uf.count() == 7

    def test_quick_union_basic_operations(self):
        """Test: Grundlegende Operationen bei QuickUnionUF."""
        uf = QuickUnionUF(5)

        uf.union(0, 1)
        uf.union(3, 4)

        assert uf.connected(0, 1)
        assert uf.connected(3, 4)
        assert not uf.connected(0, 3)
        assert uf.count() == 3

    def test_quick_union_tree_structure(self):
        """Test: Baum-Struktur bei QuickUnionUF."""
        uf = QuickUnionUF(6)

        # Erstelle eine Kette: 0-1-2-3
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)

        # Alle sollten dieselbe Wurzel haben
        root = uf.find(0)
        assert uf.find(1) == root
        assert uf.find(2) == root
        assert uf.find(3) == root


class TestWeightedQuickUnionUF:
    """Test-Klasse für WeightedQuickUnionUF-Implementierung."""

    def test_weighted_quick_union_creation(self):
        """Test: WeightedQuickUnionUF wird korrekt erstellt."""
        uf = WeightedQuickUnionUF(9)
        assert uf.count() == 9

    def test_weighted_union_balancing(self):
        """Test: Gewichtete Union hält Bäume balanciert."""
        uf = WeightedQuickUnionUF(8)

        # Erstelle zwei Komponenten unterschiedlicher Grösse
        uf.union(0, 1)  # Komponente 1: {0, 1}
        uf.union(2, 3)  # Komponente 2: {2, 3}
        uf.union(2, 4)  # Komponente 2: {2, 3, 4}
        uf.union(2, 5)  # Komponente 2: {2, 3, 4, 5}

        # Verbinde die Komponenten - grössere sollte Wurzel werden
        uf.union(0, 2)

        # Alle sollten verbunden sein
        for i in range(6):
            for j in range(i + 1, 6):
                if i < 6 and j < 6:
                    assert uf.connected(i, j)

    def test_weighted_performance_characteristics(self):
        """Test: Performance-Eigenschaften der gewichteten Union."""
        uf = WeightedQuickUnionUF(16)

        # Erstelle balancierte Struktur
        for i in range(8):
            uf.union(i, i + 8)

        for i in range(4):
            uf.union(i, i + 4)
            uf.union(i + 8, i + 12)

        for i in range(2):
            uf.union(i, i + 2)
            uf.union(i + 4, i + 6)
            uf.union(i + 8, i + 10)
            uf.union(i + 12, i + 14)

        # Finale Verbindungen
        uf.union(0, 1)
        uf.union(4, 5)
        uf.union(8, 9)
        uf.union(12, 13)

        # Alle sollten in einer Komponente sein
        assert uf.count() == 1


class TestUnionFindComparison:
    """Vergleichstests für verschiedene Union-Find-Implementierungen."""

    @pytest.mark.parametrize("uf_class", [
        UF, QuickFindUF, QuickUnionUF, WeightedQuickUnionUF
    ])
    def test_consistent_behavior_across_implementations(self, uf_class):
        """Test: Konsistentes Verhalten aller Implementierungen."""
        uf = uf_class(10)

        # Dieselben Operationen auf allen Implementierungen
        operations = [
            (0, 1), (2, 3), (4, 5), (6, 7), (8, 9),
            (0, 2), (4, 6), (1, 8)
        ]

        for i, j in operations:
            uf.union(i, j)

        # Erwartete Verbindungen testen
        expected_connections = [
            (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
            (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7),
            (8, 9), (0, 8), (1, 9)
        ]

        for i, j in expected_connections:
            assert uf.connected(i, j), f"Should be connected: {i}, {j}"

    def test_dynamic_connectivity_example(self):
        """Test: Klassisches dynamisches Konnektivitätsproblem."""
        # Beispiel aus Algorithms 4th Edition
        uf = UF(10)

        connections = [
            (4, 3), (3, 8), (6, 5), (9, 4), (2, 1),
            (8, 9), (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)
        ]

        for p, q in connections:
            if not uf.connected(p, q):
                uf.union(p, q)

        # Finale Überprüfungen
        assert uf.connected(0, 7)
        assert uf.connected(4, 9)
        assert uf.count() == 2  # Zwei grosse Komponenten
