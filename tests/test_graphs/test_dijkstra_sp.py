"""Tests für DijkstraSP."""

import pytest
from src.algs4.pva_4_graphs import DijkstraSP, EdgeWeightedDigraph, DirectedEdge


class TestDijkstraSP:
    """Tests für die DijkstraSP-Klasse."""

    def test_single_vertex_graph(self):
        """Test: Dijkstra auf Graph mit einem Knoten."""
        g = EdgeWeightedDigraph(1)
        sp = DijkstraSP(g, 0)
        assert sp.has_path_to(0)
        assert sp.distTo[0] == 0.0

    def test_simple_path(self):
        """Test: Einfacher Pfad von 0 zu 1."""
        g = EdgeWeightedDigraph(2)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        sp = DijkstraSP(g, 0)
        assert sp.has_path_to(1)
        assert sp.distTo[1] == 0.5

    def test_no_path(self):
        """Test: Kein Pfad zu erreichbarem Knoten."""
        g = EdgeWeightedDigraph(3)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        sp = DijkstraSP(g, 0)
        assert not sp.has_path_to(2)

    def test_shortest_path_selection(self):
        """Test: Wählt den kürzesten Pfad."""
        g = EdgeWeightedDigraph(4)
        # Längerer direkter Pfad: 0 -> 3 (Gewicht 2.0)
        g.add_edge(DirectedEdge(0, 3, 2.0))
        # Kürzerer Pfad: 0 -> 1 -> 2 -> 3 (Gewicht 0.5 + 0.5 + 0.5 = 1.5)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.5))
        g.add_edge(DirectedEdge(2, 3, 0.5))
        sp = DijkstraSP(g, 0)
        # Der Algorithmus sollte den kürzeren Pfad wählen
        assert abs(sp.distTo[3] - 1.5) < 1e-9

    def test_path_to_method(self):
        """Test: path_to() gibt den Pfad zurück."""
        g = EdgeWeightedDigraph(3)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        sp = DijkstraSP(g, 0)
        path = sp.path_to(2)
        assert path is not None
        # Der Pfad sollte 2 Kanten enthalten
        edges = list(path)
        assert len(edges) == 2

    def test_path_to_nonexistent_returns_none(self):
        """Test: path_to() gibt None für unerreichbare Knoten."""
        g = EdgeWeightedDigraph(3)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        sp = DijkstraSP(g, 0)
        path = sp.path_to(2)
        assert path is None

    def test_multiple_paths_to_same_vertex(self):
        """Test: Mehrere Pfade zum gleichen Knoten."""
        g = EdgeWeightedDigraph(4)
        # Pfad 1: 0 -> 1 -> 3 (Gewicht 1.0 + 1.0 = 2.0)
        g.add_edge(DirectedEdge(0, 1, 1.0))
        g.add_edge(DirectedEdge(1, 3, 1.0))
        # Pfad 2: 0 -> 2 -> 3 (Gewicht 0.5 + 0.5 = 1.0)
        g.add_edge(DirectedEdge(0, 2, 0.5))
        g.add_edge(DirectedEdge(2, 3, 0.5))
        sp = DijkstraSP(g, 0)
        assert sp.distTo[3] == 1.0

    def test_invalid_start_vertex_raises_error(self):
        """Test: Ungültiger Startknoten wirft ValueError."""
        g = EdgeWeightedDigraph(5)
        with pytest.raises(ValueError):
            DijkstraSP(g, 5)

    def test_negative_start_vertex_raises_error(self):
        """Test: Negativer Startknoten wirft ValueError."""
        g = EdgeWeightedDigraph(5)
        with pytest.raises(ValueError):
            DijkstraSP(g, -1)

    def test_complex_graph(self):
        """Test: Komplexerer Graph mit mehreren Knoten."""
        g = EdgeWeightedDigraph(6)
        g.add_edge(DirectedEdge(0, 1, 0.4))
        g.add_edge(DirectedEdge(0, 2, 0.2))
        g.add_edge(DirectedEdge(1, 3, 0.1))
        g.add_edge(DirectedEdge(2, 3, 0.3))
        g.add_edge(DirectedEdge(3, 4, 0.2))
        g.add_edge(DirectedEdge(3, 5, 0.6))
        sp = DijkstraSP(g, 0)
        assert sp.has_path_to(4)
        assert sp.has_path_to(5)
        # Kürzester Pfad zu 4: 0 -> 2 -> 3 -> 4 (0.2 + 0.3 + 0.2 = 0.7)
        assert abs(sp.distTo[4] - 0.7) < 1e-9

    def test_zero_weight_edges(self):
        """Test: Kanten mit Gewicht 0."""
        g = EdgeWeightedDigraph(3)
        g.add_edge(DirectedEdge(0, 1, 0.0))
        g.add_edge(DirectedEdge(1, 2, 0.5))
        sp = DijkstraSP(g, 0)
        assert sp.distTo[2] == 0.5

