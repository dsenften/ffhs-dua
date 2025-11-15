"""Tests für die EdgeWeightedGraph-Klasse."""


from src.algs4.pva_4_graphs.edge import Edge
from src.algs4.pva_4_graphs.edge_weighted_graph import EdgeWeightedGraph


class TestEdgeWeightedGraph:
    """Tests für ungerichtete gewichtete Graphen."""

    def test_graph_creation_empty(self):
        """Test: Erstellung eines leeren Graphen."""
        g = EdgeWeightedGraph(5)
        assert g.V == 5
        assert g.E == 0

    def test_graph_creation_zero_vertices(self):
        """Test: Erstellung eines Graphen mit 0 Knoten."""
        g = EdgeWeightedGraph(0)
        assert g.V == 0
        assert g.E == 0

    def test_graph_add_single_edge(self):
        """Test: Hinzufügen einer einzelnen Kante."""
        g = EdgeWeightedGraph(3)
        e = Edge(0, 1, 0.5)
        g.add_edge(e)
        assert g.E == 1

    def test_graph_add_multiple_edges(self):
        """Test: Hinzufügen mehrerer Kanten."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.6))
        g.add_edge(Edge(2, 3, 0.7))
        assert g.E == 3

    def test_graph_parallel_edges(self):
        """Test: Parallele Kanten sind erlaubt."""
        g = EdgeWeightedGraph(2)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(0, 1, 0.6))
        assert g.E == 2

    def test_graph_self_loop(self):
        """Test: Selbstschleifen sind erlaubt."""
        g = EdgeWeightedGraph(2)
        g.add_edge(Edge(0, 0, 0.5))
        assert g.E == 1

    def test_graph_edges_method(self):
        """Test: edges() gibt alle Kanten zurück."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.6))
        g.add_edge(Edge(2, 3, 0.7))
        edges = g.edges()
        assert len(edges) == 3

    def test_graph_edges_no_duplicates(self):
        """Test: edges() gibt keine Duplikate zurück."""
        g = EdgeWeightedGraph(3)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.6))
        edges = g.edges()
        # Jede Kante sollte nur einmal vorkommen
        assert len(edges) == 2

    def test_graph_adjacency_list(self):
        """Test: Adjazenzlisten sind korrekt."""
        g = EdgeWeightedGraph(3)
        e = Edge(0, 1, 0.5)
        g.add_edge(e)
        # Kante sollte in beiden Adjazenzlisten sein
        assert len(list(g.adj[0])) == 1
        assert len(list(g.adj[1])) == 1

    def test_graph_string_representation(self):
        """Test: String-Darstellung des Graphen."""
        g = EdgeWeightedGraph(2)
        g.add_edge(Edge(0, 1, 0.5))
        s = str(g)
        assert "2 vertices, 1 edges" in s
        assert "0:" in s
        assert "1:" in s

    def test_graph_large(self):
        """Test: Großer Graph mit vielen Kanten."""
        g = EdgeWeightedGraph(100)
        for i in range(99):
            g.add_edge(Edge(i, i + 1, 0.5))
        assert g.E == 99
        assert len(g.edges()) == 99
