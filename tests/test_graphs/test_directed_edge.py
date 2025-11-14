"""Tests für DirectedEdge."""

import pytest

from src.algs4.pva_4_graphs import DirectedEdge


class TestDirectedEdge:
    """Tests für die DirectedEdge-Klasse."""

    def test_create_edge(self):
        """Test: Erstelle eine neue Kante."""
        edge = DirectedEdge(0, 1, 0.5)
        assert edge.From() == 0
        assert edge.To() == 1
        assert edge.weight == 0.5

    def test_edge_from_method(self):
        """Test: From() gibt den Startknoten zurück."""
        edge = DirectedEdge(5, 10, 1.5)
        assert edge.From() == 5

    def test_edge_to_method(self):
        """Test: To() gibt den Endknoten zurück."""
        edge = DirectedEdge(5, 10, 1.5)
        assert edge.To() == 10

    def test_edge_weight(self):
        """Test: Gewicht wird korrekt gespeichert."""
        edge = DirectedEdge(0, 1, 2.5)
        assert edge.weight == 2.5

    def test_edge_zero_weight(self):
        """Test: Kante mit Gewicht 0 ist erlaubt."""
        edge = DirectedEdge(0, 1, 0.0)
        assert edge.weight == 0.0

    def test_edge_negative_weight_raises_error(self):
        """Test: Negative Gewichte werfen ValueError."""
        with pytest.raises(ValueError):
            DirectedEdge(0, 1, -0.5)

    def test_edge_string_representation(self):
        """Test: String-Darstellung der Kante."""
        edge = DirectedEdge(0, 1, 0.5)
        assert "0->1" in str(edge)
        assert "0.50000" in str(edge)

    def test_edge_repr(self):
        """Test: repr() gibt detaillierte Darstellung."""
        edge = DirectedEdge(0, 1, 0.5)
        assert "DirectedEdge" in repr(edge)
        assert "0" in repr(edge)
        assert "1" in repr(edge)

    def test_edge_self_loop(self):
        """Test: Selbstschleife ist erlaubt."""
        edge = DirectedEdge(0, 0, 1.0)
        assert edge.From() == 0
        assert edge.To() == 0

    def test_edge_large_weight(self):
        """Test: Große Gewichte sind erlaubt."""
        edge = DirectedEdge(0, 1, 999999.0)
        assert edge.weight == 999999.0
