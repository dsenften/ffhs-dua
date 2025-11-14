"""Tests für die EdgeWeightedDirectedCycle-Klasse."""

import pytest

from src.algs4.pva_4_graphs.directed_edge import DirectedEdge
from src.algs4.pva_4_graphs.edge_weighted_digraph import EdgeWeightedDigraph
from src.algs4.pva_4_graphs.edge_weighted_directed_cycle import (
    EdgeWeightedDirectedCycle,
)


class TestEdgeWeightedDirectedCycle:
    """Tests für Zyklenerkennung in gewichteten gerichteten Graphen."""

    def test_no_cycle_empty_graph(self):
        """Test: Leerer Graph hat keinen Zyklus."""
        g = EdgeWeightedDigraph(5)
        finder = EdgeWeightedDirectedCycle(g)
        assert not finder.has_cycle()

    def test_no_cycle_single_vertex(self):
        """Test: Graph mit einzelnem Knoten hat keinen Zyklus."""
        g = EdgeWeightedDigraph(1)
        finder = EdgeWeightedDirectedCycle(g)
        assert not finder.has_cycle()

    def test_no_cycle_linear_path(self):
        """Test: Linearer Pfad hat keinen Zyklus."""
        g = EdgeWeightedDigraph(4)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.6))
        g.add_edge(DirectedEdge(2, 3, 0.7))
        finder = EdgeWeightedDirectedCycle(g)
        assert not finder.has_cycle()

    def test_cycle_self_loop(self):
        """Test: Selbstschleife ist ein Zyklus."""
        g = EdgeWeightedDigraph(2)
        g.add_edge(DirectedEdge(0, 0, 0.5))
        finder = EdgeWeightedDirectedCycle(g)
        assert finder.has_cycle()

    def test_cycle_two_vertices(self):
        """Test: Zyklus zwischen zwei Knoten."""
        g = EdgeWeightedDigraph(2)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 0, 0.6))
        finder = EdgeWeightedDirectedCycle(g)
        assert finder.has_cycle()

    def test_cycle_three_vertices(self):
        """Test: Zyklus zwischen drei Knoten."""
        g = EdgeWeightedDigraph(3)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.6))
        g.add_edge(DirectedEdge(2, 0, 0.7))
        finder = EdgeWeightedDirectedCycle(g)
        assert finder.has_cycle()

    def test_cycle_detection_returns_cycle(self):
        """Test: Zyklus wird als Stack zurückgegeben."""
        g = EdgeWeightedDigraph(3)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.6))
        g.add_edge(DirectedEdge(2, 0, 0.7))
        finder = EdgeWeightedDirectedCycle(g)
        assert finder.cycle is not None
        # Zyklus sollte 3 Kanten haben
        assert len(list(finder.cycle)) == 3

    def test_no_cycle_disconnected_graph(self):
        """Test: Unzusammenhängender Graph ohne Zyklus."""
        g = EdgeWeightedDigraph(4)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(2, 3, 0.6))
        finder = EdgeWeightedDirectedCycle(g)
        assert not finder.has_cycle()

    def test_cycle_in_disconnected_graph(self):
        """Test: Zyklus in einer Komponente eines unzusammenhängenden Graphen."""
        g = EdgeWeightedDigraph(4)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 0, 0.6))
        g.add_edge(DirectedEdge(2, 3, 0.7))
        finder = EdgeWeightedDirectedCycle(g)
        assert finder.has_cycle()

    def test_complex_cycle(self):
        """Test: Komplexer Graph mit Zyklus."""
        g = EdgeWeightedDigraph(5)
        g.add_edge(DirectedEdge(0, 1, 0.5))
        g.add_edge(DirectedEdge(1, 2, 0.6))
        g.add_edge(DirectedEdge(2, 3, 0.7))
        g.add_edge(DirectedEdge(3, 1, 0.8))  # Zyklus: 1 -> 2 -> 3 -> 1
        g.add_edge(DirectedEdge(3, 4, 0.9))
        finder = EdgeWeightedDirectedCycle(g)
        assert finder.has_cycle()

