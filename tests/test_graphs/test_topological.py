"""Tests für topologische Sortierung."""

from src.algs4.pva_4_graphs import DirectedEdge, EdgeWeightedDigraph, Topological


class TestTopological:
    """Tests für die Topological-Klasse."""

    def test_topological_einfacher_dag(self):
        """Test topologische Sortierung auf einem einfachen DAG."""
        g = EdgeWeightedDigraph(4)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        g.add_edge(DirectedEdge(2, 3, 0.2))

        topo = Topological(g)

        assert topo.has_order()
        order = list(topo.order())
        assert len(order) == 4

    def test_topological_mit_zyklus(self):
        """Test dass topologische Sortierung None zurückgibt bei Zyklen."""
        g = EdgeWeightedDigraph(4)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        g.add_edge(DirectedEdge(2, 3, 0.2))
        g.add_edge(DirectedEdge(3, 0, 0.4))  # Zyklus

        topo = Topological(g)

        assert not topo.has_order()

    def test_topological_einzelner_knoten(self):
        """Test topologische Sortierung mit nur einem Knoten."""
        g = EdgeWeightedDigraph(1)
        topo = Topological(g)

        assert topo.has_order()
        order = list(topo.order())
        assert len(order) == 1
        assert order[0] == 0

    def test_topological_zwei_knoten(self):
        """Test topologische Sortierung mit zwei Knoten."""
        g = EdgeWeightedDigraph(2)
        g.add_edge(DirectedEdge(0, 1, 0.5))

        topo = Topological(g)

        assert topo.has_order()
        order = list(topo.order())
        assert len(order) == 2
        # 0 sollte vor 1 kommen
        assert order.index(0) < order.index(1)

    def test_topological_komplexer_dag(self):
        """Test topologische Sortierung auf einem komplexeren DAG."""
        g = EdgeWeightedDigraph(6)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(0, 2, 0.3))
        g.add_edge(DirectedEdge(1, 3, 0.2))
        g.add_edge(DirectedEdge(2, 3, 0.4))
        g.add_edge(DirectedEdge(3, 4, 0.1))
        g.add_edge(DirectedEdge(4, 5, 0.6))

        topo = Topological(g)

        assert topo.has_order()
        order = list(topo.order())
        assert len(order) == 6

        # Prüfe dass alle Kanten respektiert werden
        pos = {v: i for i, v in enumerate(order)}
        assert pos[0] < pos[1]
        assert pos[0] < pos[2]
        assert pos[1] < pos[3]
        assert pos[2] < pos[3]
        assert pos[3] < pos[4]
        assert pos[4] < pos[5]

    def test_topological_mehrere_komponenten(self):
        """Test topologische Sortierung mit mehreren Komponenten."""
        g = EdgeWeightedDigraph(6)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.3))
        g.add_edge(DirectedEdge(3, 4, 0.2))
        g.add_edge(DirectedEdge(4, 5, 0.4))

        topo = Topological(g)

        assert topo.has_order()
        order = list(topo.order())
        assert len(order) == 6

    def test_topological_stern_dag(self):
        """Test topologische Sortierung auf einem Stern-DAG."""
        g = EdgeWeightedDigraph(5)
        # Zentrum ist Knoten 0
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(0, 2, 0.3))
        g.add_edge(DirectedEdge(0, 3, 0.2))
        g.add_edge(DirectedEdge(0, 4, 0.4))

        topo = Topological(g)

        assert topo.has_order()
        order = list(topo.order())
        assert len(order) == 5
        # 0 sollte an erster Stelle sein
        assert order[0] == 0

    def test_topological_liniengraph(self):
        """Test topologische Sortierung auf einem Liniengraphen."""
        g = EdgeWeightedDigraph(5)
        g.add_edge(DirectedEdge(0, 1, 0.1))
        g.add_edge(DirectedEdge(1, 2, 0.2))
        g.add_edge(DirectedEdge(2, 3, 0.3))
        g.add_edge(DirectedEdge(3, 4, 0.4))

        topo = Topological(g)

        assert topo.has_order()
        order = list(topo.order())
        assert len(order) == 5
        # Sollte in Ordnung 0, 1, 2, 3, 4 sein
        assert order == [0, 1, 2, 3, 4]

    def test_topological_selbstschleife(self):
        """Test dass topologische Sortierung Selbstschleifen erkennt."""
        g = EdgeWeightedDigraph(3)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 1, 0.3))  # Selbstschleife
        g.add_edge(DirectedEdge(1, 2, 0.2))

        topo = Topological(g)

        # Sollte keinen Order haben wegen Zyklus
        assert not topo.has_order()

    def test_topological_zwei_knoten_zyklus(self):
        """Test dass topologische Sortierung 2-Knoten-Zyklen erkennt."""
        g = EdgeWeightedDigraph(2)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 0, 0.3))

        topo = Topological(g)

        assert not topo.has_order()
