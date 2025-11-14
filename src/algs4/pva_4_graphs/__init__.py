"""Praktische Vertiefungsaufgaben 4: Graphen-Algorithmen.

Dieses Modul enthält Implementierungen von Graphen-Algorithmen:

- **DirectedEdge**: Gerichtete Kante mit Gewicht
- **EdgeWeightedDigraph**: Gewichteter gerichteter Graph
- **IndexMinPQ**: Indexed Min Priority Queue
- **DijkstraSP**: Dijkstras Algorithmus für kürzeste Pfade

Beispiele:
    >>> from src.algs4.pva_4_graphs import EdgeWeightedDigraph, DijkstraSP
    >>> # Graph mit 8 Knoten erstellen
    >>> g = EdgeWeightedDigraph(8)
    >>> # Kanten hinzufügen
    >>> from src.algs4.pva_4_graphs import DirectedEdge
    >>> g.add_edge(DirectedEdge(0, 1, 0.5))
    >>> # Kürzeste Pfade berechnen
    >>> sp = DijkstraSP(g, 0)
    >>> sp.has_path_to(1)
    True
"""

from .dijkstra_sp import DijkstraSP
from .directed_edge import DirectedEdge
from .edge_weighted_digraph import EdgeWeightedDigraph
from .index_min_pq import IndexMinPQ

__all__ = [
    "DirectedEdge",
    "EdgeWeightedDigraph",
    "IndexMinPQ",
    "DijkstraSP",
]

