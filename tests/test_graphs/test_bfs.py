"""Tests für Breitensuche (BFS)."""

import pytest

from src.algs4.pva_4_graphs import BFS, Edge, EdgeWeightedGraph


class TestBFS:
    """Tests für die BFS-Klasse."""

    def test_bfs_einfacher_graph(self):
        """Test BFS auf einem einfachen Graphen."""
        g = EdgeWeightedGraph(6)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(0, 2, 0.3))
        g.add_edge(Edge(1, 3, 0.2))
        g.add_edge(Edge(2, 3, 0.4))
        g.add_edge(Edge(3, 4, 0.1))
        g.add_edge(Edge(4, 5, 0.6))

        bfs = BFS(g, 0)

        # Alle Knoten sollten erreichbar sein
        for v in range(6):
            assert bfs.has_path_to(v)

    def test_bfs_distanzen(self):
        """Test dass BFS korrekte Distanzen berechnet."""
        g = EdgeWeightedGraph(6)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(0, 2, 0.3))
        g.add_edge(Edge(1, 3, 0.2))
        g.add_edge(Edge(2, 3, 0.4))
        g.add_edge(Edge(3, 4, 0.1))
        g.add_edge(Edge(4, 5, 0.6))

        bfs = BFS(g, 0)

        assert bfs.distance_to(0) == 0
        assert bfs.distance_to(1) == 1
        assert bfs.distance_to(2) == 1
        assert bfs.distance_to(3) == 2
        assert bfs.distance_to(4) == 3
        assert bfs.distance_to(5) == 4

    def test_bfs_unzusammenhaengender_graph(self):
        """Test BFS auf einem unzusammenhängenden Graphen."""
        g = EdgeWeightedGraph(6)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(3, 4, 0.2))
        g.add_edge(Edge(4, 5, 0.4))

        bfs = BFS(g, 0)

        # Knoten 0, 1, 2 sollten erreichbar sein
        assert bfs.has_path_to(0)
        assert bfs.has_path_to(1)
        assert bfs.has_path_to(2)

        # Knoten 3, 4, 5 sollten nicht erreichbar sein
        assert not bfs.has_path_to(3)
        assert not bfs.has_path_to(4)
        assert not bfs.has_path_to(5)

    def test_bfs_pfad(self):
        """Test dass BFS korrekte Pfade findet."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(2, 3, 0.2))

        bfs = BFS(g, 0)

        # Pfad zu Knoten 3 sollte 3 Kanten haben
        path = bfs.path_to(3)
        assert path is not None
        assert bfs.distance_to(3) == 3

    def test_bfs_kein_pfad(self):
        """Test dass BFS None zurückgibt wenn kein Pfad existiert."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(2, 3, 0.3))

        bfs = BFS(g, 0)

        # Kein Pfad zu Knoten 2 oder 3
        assert bfs.path_to(2) is None
        assert bfs.path_to(3) is None

    def test_bfs_einzelner_knoten(self):
        """Test BFS mit nur einem Knoten."""
        g = EdgeWeightedGraph(1)
        bfs = BFS(g, 0)

        assert bfs.has_path_to(0)
        assert bfs.distance_to(0) == 0

    def test_bfs_zwei_knoten_verbunden(self):
        """Test BFS mit zwei verbundenen Knoten."""
        g = EdgeWeightedGraph(2)
        g.add_edge(Edge(0, 1, 0.5))

        bfs = BFS(g, 0)

        assert bfs.has_path_to(0)
        assert bfs.has_path_to(1)
        assert bfs.distance_to(1) == 1

    def test_bfs_zwei_knoten_nicht_verbunden(self):
        """Test BFS mit zwei nicht verbundenen Knoten."""
        g = EdgeWeightedGraph(2)
        bfs = BFS(g, 0)

        assert bfs.has_path_to(0)
        assert not bfs.has_path_to(1)
        assert bfs.distance_to(1) == float("inf")

    def test_bfs_zyklischer_graph(self):
        """Test BFS auf einem zyklischen Graphen."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(2, 3, 0.2))
        g.add_edge(Edge(3, 0, 0.4))

        bfs = BFS(g, 0)

        # Alle Knoten sollten erreichbar sein
        for v in range(4):
            assert bfs.has_path_to(v)

    def test_bfs_ungültiger_startknoten(self):
        """Test dass BFS ValueError wirft bei ungültigem Startknoten."""
        g = EdgeWeightedGraph(4)

        with pytest.raises(ValueError):
            BFS(g, -1)

        with pytest.raises(ValueError):
            BFS(g, 4)

    def test_bfs_stern_graph(self):
        """Test BFS auf einem Stern-Graphen."""
        g = EdgeWeightedGraph(5)
        # Zentrum ist Knoten 0
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(0, 2, 0.3))
        g.add_edge(Edge(0, 3, 0.2))
        g.add_edge(Edge(0, 4, 0.4))

        bfs = BFS(g, 0)

        # Alle Knoten sollten Distanz 1 haben
        for v in range(1, 5):
            assert bfs.distance_to(v) == 1
