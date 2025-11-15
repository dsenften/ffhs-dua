"""Tests für Tiefensuche (DFS) in gerichteten Graphen."""

from src.algs4.pva_4_graphs import DirectedDFS, DirectedEdge, EdgeWeightedDigraph


class TestDirectedDFS:
    """Tests für die DirectedDFS-Klasse."""

    def test_directed_dfs_einfacher_graph(self):
        """Test DirectedDFS auf einem einfachen Graphen."""
        g = EdgeWeightedDigraph(6)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        g.add_edge(DirectedEdge(2, 3, 0.2))
        g.add_edge(DirectedEdge(3, 4, 0.1))
        g.add_edge(DirectedEdge(4, 5, 0.6))

        dfs = DirectedDFS(g, [0])

        # Alle Knoten sollten erreichbar sein
        for v in range(6):
            assert dfs.marked(v)

    def test_directed_dfs_nicht_erreichbar(self):
        """Test DirectedDFS mit nicht erreichbaren Knoten."""
        g = EdgeWeightedDigraph(6)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        g.add_edge(DirectedEdge(3, 4, 0.2))
        g.add_edge(DirectedEdge(4, 5, 0.4))

        dfs = DirectedDFS(g, [0])

        # Knoten 0, 1, 2 sollten erreichbar sein
        assert dfs.marked(0)
        assert dfs.marked(1)
        assert dfs.marked(2)

        # Knoten 3, 4, 5 sollten nicht erreichbar sein
        assert not dfs.marked(3)
        assert not dfs.marked(4)
        assert not dfs.marked(5)

    def test_directed_dfs_mehrere_startknoten(self):
        """Test DirectedDFS mit mehreren Startknoten."""
        g = EdgeWeightedDigraph(6)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        g.add_edge(DirectedEdge(3, 4, 0.2))
        g.add_edge(DirectedEdge(4, 5, 0.4))

        dfs = DirectedDFS(g, [0, 3])

        # Alle Knoten sollten erreichbar sein
        for v in range(6):
            assert dfs.marked(v)

    def test_directed_dfs_einzelner_knoten(self):
        """Test DirectedDFS mit nur einem Knoten."""
        g = EdgeWeightedDigraph(1)
        dfs = DirectedDFS(g, [0])

        assert dfs.marked(0)

    def test_directed_dfs_zwei_knoten_verbunden(self):
        """Test DirectedDFS mit zwei verbundenen Knoten."""
        g = EdgeWeightedDigraph(2)
        g.add_edge(DirectedEdge(0, 1, 0.5))

        dfs = DirectedDFS(g, [0])

        assert dfs.marked(0)
        assert dfs.marked(1)

    def test_directed_dfs_zwei_knoten_nicht_verbunden(self):
        """Test DirectedDFS mit zwei nicht verbundenen Knoten."""
        g = EdgeWeightedDigraph(2)
        dfs = DirectedDFS(g, [0])

        assert dfs.marked(0)
        assert not dfs.marked(1)

    def test_directed_dfs_zyklischer_graph(self):
        """Test DirectedDFS auf einem zyklischen Graphen."""
        g = EdgeWeightedDigraph(4)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        g.add_edge(DirectedEdge(2, 3, 0.2))
        g.add_edge(DirectedEdge(3, 0, 0.4))

        dfs = DirectedDFS(g, [0])

        # Alle Knoten sollten erreichbar sein
        for v in range(4):
            assert dfs.marked(v)

    def test_directed_dfs_ungültiger_startknoten(self):
        """Test dass DirectedDFS ValueError wirft bei ungültigem Startknoten."""
        import pytest

        g = EdgeWeightedDigraph(4)

        with pytest.raises(ValueError):
            DirectedDFS(g, [-1])

        with pytest.raises(ValueError):
            DirectedDFS(g, [4])

    def test_directed_dfs_stern_graph(self):
        """Test DirectedDFS auf einem Stern-Graphen."""
        g = EdgeWeightedDigraph(5)
        # Zentrum ist Knoten 0
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(0, 2, 0.3))
        g.add_edge(DirectedEdge(0, 3, 0.2))
        g.add_edge(DirectedEdge(0, 4, 0.4))

        dfs = DirectedDFS(g, [0])

        # Alle Knoten sollten erreichbar sein
        for v in range(5):
            assert dfs.marked(v)

    def test_directed_dfs_liniengraph(self):
        """Test DirectedDFS auf einem Liniengraphen."""
        g = EdgeWeightedDigraph(5)
        g.add_edge(DirectedEdge(0, 1, 0.1))
        g.add_edge(DirectedEdge(1, 2, 0.2))
        g.add_edge(DirectedEdge(2, 3, 0.3))
        g.add_edge(DirectedEdge(3, 4, 0.4))

        dfs = DirectedDFS(g, [0])

        # Alle Knoten sollten erreichbar sein
        for v in range(5):
            assert dfs.marked(v)

    def test_directed_dfs_leere_startknoten(self):
        """Test DirectedDFS mit leerer Startknoten-Liste."""
        g = EdgeWeightedDigraph(4)
        g.add_edge(DirectedEdge(0, 1, 0.5))

        dfs = DirectedDFS(g, [])

        # Kein Knoten sollte erreichbar sein
        for v in range(4):
            assert not dfs.marked(v)
