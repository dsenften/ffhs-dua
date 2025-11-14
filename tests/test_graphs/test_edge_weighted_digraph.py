"""Tests für EdgeWeightedDigraph."""

import pytest
from src.algs4.pva_4_graphs import EdgeWeightedDigraph, DirectedEdge


class TestEdgeWeightedDigraph:
    """Tests für die EdgeWeightedDigraph-Klasse."""

    def test_create_empty_graph(self):
        """Test: Erstelle einen leeren Graphen."""
        g = EdgeWeightedDigraph(5)
        assert g.V == 5
        assert g.E == 0

    def test_create_graph_with_zero_vertices(self):
        """Test: Erstelle einen Graphen mit 0 Knoten."""
        g = EdgeWeightedDigraph(0)
        assert g.V == 0
        assert g.E == 0

    def test_add_single_edge(self):
        """Test: Füge eine Kante hinzu."""
        g = EdgeWeightedDigraph(5)
        edge = DirectedEdge(0, 1, 0.5)
        g.add_edge(edge)
        assert g.E == 1

    def test_add_multiple_edges(self):
        """Test: Füge mehrere Kanten hinzu."""
        g = EdgeWeightedDigraph(5)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        g.add_edge(DirectedEdge(2, 3, 0.7))
        assert g.E == 3

    def test_edges_method(self):
        """Test: edges() gibt alle Kanten zurück."""
        g = EdgeWeightedDigraph(5)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        edges = g.edges()
        assert len(edges) == 2

    def test_adjacency_list(self):
        """Test: Adjazenzlisten werden korrekt verwaltet."""
        g = EdgeWeightedDigraph(5)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(0, 2, 0.3))
        # Knoten 0 sollte 2 ausgehende Kanten haben
        adj_edges = list(g.adj[0])
        assert len(adj_edges) == 2

    def test_parallel_edges_allowed(self):
        """Test: Parallele Kanten sind erlaubt."""
        g = EdgeWeightedDigraph(5)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(0, 1, 0.3))
        assert g.E == 2

    def test_self_loop_allowed(self):
        """Test: Selbstschleifen sind erlaubt."""
        g = EdgeWeightedDigraph(5)
        g.add_edge(DirectedEdge(0, 0, 1.0))
        assert g.E == 1

    def test_string_representation(self):
        """Test: String-Darstellung des Graphen."""
        g = EdgeWeightedDigraph(3)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        s = str(g)
        assert "3 vertices" in s
        assert "2 edges" in s

    def test_repr(self):
        """Test: repr() gibt detaillierte Darstellung."""
        g = EdgeWeightedDigraph(5)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        r = repr(g)
        assert "EdgeWeightedDigraph" in r
        assert "5 vertices" in r
        assert "1 edges" in r

    def test_negative_vertices_raises_error(self):
        """Test: Negative Knotenzahl wirft ValueError."""
        with pytest.raises(ValueError):
            EdgeWeightedDigraph(-1)

    def test_large_graph(self):
        """Test: Großer Graph mit vielen Kanten."""
        g = EdgeWeightedDigraph(100)
        for i in range(50):
            g.add_edge(DirectedEdge(i, i + 1, 0.5))
        assert g.E == 50
        assert g.V == 100

