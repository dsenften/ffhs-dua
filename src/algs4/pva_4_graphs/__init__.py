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

# Lazy loading für Module - verhindert RuntimeWarning bei Ausführung als Script
_LAZY_IMPORTS = {
    "BFS": (".bfs", "BFS"),
    "DFSPaths": (".dfs_paths", "DFSPaths"),
    "DijkstraSP": (".dijkstra_sp", "DijkstraSP"),
    "DirectedDFS": (".directed_dfs", "DirectedDFS"),
    "DirectedEdge": (".directed_edge", "DirectedEdge"),
    "Edge": (".edge", "Edge"),
    "EdgeWeightedDigraph": (".edge_weighted_digraph", "EdgeWeightedDigraph"),
    "EdgeWeightedDirectedCycle": (
        ".edge_weighted_directed_cycle",
        "EdgeWeightedDirectedCycle",
    ),
    "EdgeWeightedGraph": (".edge_weighted_graph", "EdgeWeightedGraph"),
    "IndexMinPQ": (".index_min_pq", "IndexMinPQ"),
    "KruskalMST": (".kruskal_mst", "KruskalMST"),
    "PrimMST": (".prim_mst", "PrimMST"),
    "Topological": (".topological", "Topological"),
}


def __getattr__(name: str):
    """
    Return the requested public attribute by importing its submodule on first access.
    
    Parameters:
        name (str): The attribute name being accessed on the package.
    
    Returns:
        Any: The attribute object loaded from the mapped submodule.
    
    Raises:
        AttributeError: If `name` is not defined in the lazy-import mapping.
    """
    if name in _LAZY_IMPORTS:
        module_path, attr_name = _LAZY_IMPORTS[name]
        import importlib

        module = importlib.import_module(module_path, __package__)
        return getattr(module, attr_name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")