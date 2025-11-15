"""Praktische Vertiefungsaufgaben 4: Graphen-Algorithmen.

Dieses Modul enthält Implementierungen von Graphen-Algorithmen:

Gerichtete Graphen:
- **DirectedEdge**: Gerichtete Kante mit Gewicht
- **EdgeWeightedDigraph**: Gewichteter gerichteter Graph
- **EdgeWeightedDirectedCycle**: Zyklenerkennung in gerichteten Graphen
- **IndexMinPQ**: Indexed Min Priority Queue
- **DijkstraSP**: Dijkstras Algorithmus für kürzeste Pfade

Ungerichtete Graphen:
- **Edge**: Ungerichtete Kante mit Gewicht
- **EdgeWeightedGraph**: Ungerichteter gewichteter Graph
- **BFS**: Breitensuche für ungerichtete Graphen
- **KruskalMST**: Kruskal's Algorithmus für Minimum Spanning Tree
- **PrimMST**: Prim's Algorithmus für Minimum Spanning Tree

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

from .bfs import BFS
from .dfs_paths import DFSPaths
from .dijkstra_sp import DijkstraSP
from .directed_dfs import DirectedDFS
from .directed_edge import DirectedEdge
from .edge import Edge
from .edge_weighted_digraph import EdgeWeightedDigraph
from .edge_weighted_directed_cycle import EdgeWeightedDirectedCycle
from .edge_weighted_graph import EdgeWeightedGraph
from .index_min_pq import IndexMinPQ
from .kruskal_mst import KruskalMST
from .prim_mst import PrimMST
from .topological import Topological

__all__ = [
    "BFS",
    "DFSPaths",
    "DijkstraSP",
    "DirectedDFS",
    "DirectedEdge",
    "Edge",
    "EdgeWeightedDigraph",
    "EdgeWeightedDirectedCycle",
    "EdgeWeightedGraph",
    "IndexMinPQ",
    "KruskalMST",
    "PrimMST",
    "Topological",
]
