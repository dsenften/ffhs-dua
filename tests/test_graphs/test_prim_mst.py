"""Tests für Prim's Algorithmus."""

from src.algs4.pva_4_graphs import Edge, EdgeWeightedGraph, PrimMST


class TestPrimMST:
    """Tests für die PrimMST-Klasse."""

    def test_prim_einfacher_graph(self):
        """Test Prim auf einem einfachen Graphen."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(2, 3, 0.2))
        g.add_edge(Edge(3, 0, 0.4))

        mst = PrimMST(g)

        # MST sollte V-1 = 3 Kanten haben
        assert len(mst.edges()) == 3

    def test_prim_gewicht(self):
        """Test dass Prim das korrekte Gewicht berechnet."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(2, 3, 0.2))
        g.add_edge(Edge(3, 0, 0.4))

        mst = PrimMST(g)

        # Minimales Gewicht sollte 0.2 + 0.3 + 0.4 = 0.9 sein
        assert abs(mst.weight() - 0.9) < 1e-6

    def test_prim_einzelner_knoten(self):
        """Test Prim mit nur einem Knoten."""
        g = EdgeWeightedGraph(1)
        mst = PrimMST(g)

        # MST sollte 0 Kanten haben
        assert len(mst.edges()) == 0
        assert mst.weight() == 0.0

    def test_prim_zwei_knoten(self):
        """Test Prim mit zwei Knoten."""
        g = EdgeWeightedGraph(2)
        g.add_edge(Edge(0, 1, 0.5))

        mst = PrimMST(g)

        # MST sollte 1 Kante haben
        assert len(mst.edges()) == 1
        assert abs(mst.weight() - 0.5) < 1e-6

    def test_prim_komplexer_graph(self):
        """Test Prim auf einem komplexeren Graphen."""
        g = EdgeWeightedGraph(6)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(0, 2, 0.3))
        g.add_edge(Edge(1, 3, 0.2))
        g.add_edge(Edge(2, 3, 0.4))
        g.add_edge(Edge(3, 4, 0.1))
        g.add_edge(Edge(4, 5, 0.6))

        mst = PrimMST(g)

        # MST sollte V-1 = 5 Kanten haben
        assert len(mst.edges()) == 5

    def test_prim_mehrfache_kanten_gleichen_gewichts(self):
        """Test Prim mit mehreren Kanten gleichen Gewichts."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.5))
        g.add_edge(Edge(2, 3, 0.5))
        g.add_edge(Edge(3, 0, 0.5))

        mst = PrimMST(g)

        # MST sollte V-1 = 3 Kanten haben
        assert len(mst.edges()) == 3
        assert abs(mst.weight() - 1.5) < 1e-6

    def test_prim_stern_graph(self):
        """Test Prim auf einem Stern-Graphen."""
        g = EdgeWeightedGraph(5)
        # Zentrum ist Knoten 0
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(0, 2, 0.3))
        g.add_edge(Edge(0, 3, 0.2))
        g.add_edge(Edge(0, 4, 0.4))

        mst = PrimMST(g)

        # MST sollte V-1 = 4 Kanten haben
        assert len(mst.edges()) == 4
        # Gewicht sollte 0.2 + 0.3 + 0.4 + 0.5 = 1.4 sein
        assert abs(mst.weight() - 1.4) < 1e-6

    def test_prim_liniengraph(self):
        """Test Prim auf einem Liniengraphen."""
        g = EdgeWeightedGraph(5)
        g.add_edge(Edge(0, 1, 0.1))
        g.add_edge(Edge(1, 2, 0.2))
        g.add_edge(Edge(2, 3, 0.3))
        g.add_edge(Edge(3, 4, 0.4))

        mst = PrimMST(g)

        # MST sollte V-1 = 4 Kanten haben
        assert len(mst.edges()) == 4
        # Gewicht sollte 0.1 + 0.2 + 0.3 + 0.4 = 1.0 sein
        assert abs(mst.weight() - 1.0) < 1e-6

    def test_prim_redundante_kanten(self):
        """Test Prim mit redundanten Kanten."""
        g = EdgeWeightedGraph(3)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(0, 2, 0.4))  # Redundante Kante

        mst = PrimMST(g)

        # MST sollte V-1 = 2 Kanten haben
        assert len(mst.edges()) == 2
        # Gewicht sollte 0.3 + 0.4 = 0.7 sein
        assert abs(mst.weight() - 0.7) < 1e-6

    def test_prim_gewichte_sind_positiv(self):
        """Test dass alle MST-Kantengewichte positiv sind."""
        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(2, 3, 0.2))
        g.add_edge(Edge(3, 0, 0.4))

        mst = PrimMST(g)

        for e in mst.edges():
            assert e.weight > 0

    def test_prim_vs_kruskal_gleiches_gewicht(self):
        """Test dass Prim und Kruskal das gleiche Gewicht liefern."""
        from src.algs4.pva_4_graphs import KruskalMST

        g = EdgeWeightedGraph(4)
        g.add_edge(Edge(0, 1, 0.5))
        g.add_edge(Edge(1, 2, 0.3))
        g.add_edge(Edge(2, 3, 0.2))
        g.add_edge(Edge(3, 0, 0.4))

        prim = PrimMST(g)
        kruskal = KruskalMST(g)

        # Beide sollten das gleiche Gewicht haben
        assert abs(prim.weight() - kruskal.weight()) < 1e-6
