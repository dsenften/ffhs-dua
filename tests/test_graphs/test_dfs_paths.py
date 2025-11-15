"""Tests für Tiefensuche (DFS) in ungerichteten Graphen."""

from src.algs4.pva_4_graphs import DFSPaths, Edge, EdgeWeightedGraph


class TestDFSPaths:
    """Tests für die DFSPaths-Klasse."""

    def test_dfs_einfacher_graph(self):
        """Test DFS auf einem einfachen Graphen."""
        g = EdgeWeightedGraph(6)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(0, 2, 0.3))
        g.add_edge(Edge(1, 3, 0.2))
        g.add_edge(Edge(2, 3, 0.4))
        g.add_edge(Edge(3, 4, 0.1))
        g.add_edge(Edge(4, 5, 0.6))

        dfs = DFSPaths(g, 0)

        # Alle Knoten sollten erreichbar sein
        for v in range(6):
            assert dfs.has_path_to(v)

    def test_dfs_unzusammenhaengender_graph(self):
        """Test DFS auf einem unzusammenhängenden Graphen."""
        g = EdgeWeightedGraph(6)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(3, 4, 0.2))
        g.add_edge(Edge(4, 5, 0.4))

        dfs = DFSPaths(g, 0)

        # Knoten 0, 1, 2 sollten erreichbar sein
        assert dfs.has_path_to(0)
        assert dfs.has_path_to(1)
        assert dfs.has_path_to(2)

        # Knoten 3, 4, 5 sollten nicht erreichbar sein
        assert not dfs.has_path_to(3)
        assert not dfs.has_path_to(4)
        assert not dfs.has_path_to(5)

    def test_dfs_pfad(self):
        """Test dass DFS korrekte Pfade findet."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(2, 3, 0.2))

        dfs = DFSPaths(g, 0)

        # Pfad zu Knoten 3 sollte existieren
        path = dfs.path_to(3)
        assert path is not None

    def test_dfs_kein_pfad(self):
        """Test dass DFS None zurückgibt wenn kein Pfad existiert."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(2, 3, 0.3))

        dfs = DFSPaths(g, 0)

        # Kein Pfad zu Knoten 2 oder 3
        assert dfs.path_to(2) is None
        assert dfs.path_to(3) is None

    def test_dfs_einzelner_knoten(self):
        """Test DFS mit nur einem Knoten."""
        g = EdgeWeightedGraph(1)
        dfs = DFSPaths(g, 0)

        assert dfs.has_path_to(0)

    def test_dfs_zwei_knoten_verbunden(self):
        """Test DFS mit zwei verbundenen Knoten."""
        g = EdgeWeightedGraph(2)
        g.add_edge(Edge(0, 1, 0.5))

        dfs = DFSPaths(g, 0)

        assert dfs.has_path_to(0)
        assert dfs.has_path_to(1)

    def test_dfs_zwei_knoten_nicht_verbunden(self):
        """Test DFS mit zwei nicht verbundenen Knoten."""
        g = EdgeWeightedGraph(2)
        dfs = DFSPaths(g, 0)

        assert dfs.has_path_to(0)
        assert not dfs.has_path_to(1)

    def test_dfs_zyklischer_graph(self):
        """Test DFS auf einem zyklischen Graphen."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(2, 3, 0.2))
        g.add_edge(Edge(3, 0, 0.4))

        dfs = DFSPaths(g, 0)

        # Alle Knoten sollten erreichbar sein
        for v in range(4):
            assert dfs.has_path_to(v)

    def test_dfs_ungültiger_startknoten(self):
        """Test dass DFS ValueError wirft bei ungültigem Startknoten."""
        import pytest

        g = EdgeWeightedGraph(4)

        with pytest.raises(ValueError):
            DFSPaths(g, -1)

        with pytest.raises(ValueError):
            DFSPaths(g, 4)

    def test_dfs_stern_graph(self):
        """Test DFS auf einem Stern-Graphen."""
        g = EdgeWeightedGraph(5)
        # Zentrum ist Knoten 0
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(0, 2, 0.3))
        g.add_edge(Edge(0, 3, 0.2))
        g.add_edge(Edge(0, 4, 0.4))

        dfs = DFSPaths(g, 0)

        # Alle Knoten sollten erreichbar sein
        for v in range(5):
            assert dfs.has_path_to(v)

    def test_dfs_liniengraph(self):
        """Test DFS auf einem Liniengraphen."""
        g = EdgeWeightedGraph(5)
        g.add_edge(Edge(0, 1, 0.1))
        g.add_edge(Edge(1, 2, 0.2))
        g.add_edge(Edge(2, 3, 0.3))
        g.add_edge(Edge(3, 4, 0.4))

        dfs = DFSPaths(g, 0)

        # Alle Knoten sollten erreichbar sein
        for v in range(5):
            assert dfs.has_path_to(v)
