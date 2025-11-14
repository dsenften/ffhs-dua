"""Tests für die Edge-Klasse."""

import pytest

from src.algs4.pva_4_graphs.edge import Edge


class TestEdge:
    """Tests für ungerichtete Kanten mit Gewicht."""

    def test_edge_creation(self):
        """Test: Edge-Erstellung mit gültigen Parametern."""
        e = Edge(0, 1, 0.5)
        assert e.v == 0
        assert e.w == 1
        assert e.weight == 0.5

    def test_edge_negative_weight_raises_error(self):
        """Test: Negative Gewichte werfen ValueError."""
        with pytest.raises(ValueError, match="Kantengewicht darf nicht negativ sein"):
            Edge(0, 1, -0.5)

    def test_edge_zero_weight(self):
        """Test: Gewicht von 0 ist erlaubt."""
        e = Edge(0, 1, 0.0)
        assert e.weight == 0.0

    def test_edge_either(self):
        """Test: either() gibt den ersten Knoten zurück."""
        e = Edge(0, 1, 0.5)
        assert e.either() == 0

    def test_edge_other_with_first_vertex(self):
        """Test: other() mit erstem Knoten gibt zweiten Knoten zurück."""
        e = Edge(0, 1, 0.5)
        assert e.other(0) == 1

    def test_edge_other_with_second_vertex(self):
        """Test: other() mit zweitem Knoten gibt ersten Knoten zurück."""
        e = Edge(0, 1, 0.5)
        assert e.other(1) == 0

    def test_edge_other_with_invalid_vertex_raises_error(self):
        """Test: other() mit ungültigem Knoten wirft ValueError."""
        e = Edge(0, 1, 0.5)
        with pytest.raises(ValueError, match="Knoten 2 ist nicht Teil dieser Kante"):
            e.other(2)

    def test_edge_less_than(self):
        """Test: Vergleich mit < basierend auf Gewicht."""
        e1 = Edge(0, 1, 0.5)
        e2 = Edge(0, 2, 0.6)
        assert e1 < e2

    def test_edge_greater_than(self):
        """Test: Vergleich mit > basierend auf Gewicht."""
        e1 = Edge(0, 1, 0.6)
        e2 = Edge(0, 2, 0.5)
        assert e1 > e2

    def test_edge_string_representation(self):
        """Test: String-Darstellung der Kante."""
        e = Edge(0, 1, 0.5)
        assert str(e) == "0-1 0.50000"

    def test_edge_self_loop(self):
        """Test: Selbstschleife ist erlaubt."""
        e = Edge(0, 0, 0.5)
        assert e.either() == 0
        assert e.other(0) == 0

