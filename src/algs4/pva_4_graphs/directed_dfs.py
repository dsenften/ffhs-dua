"""Tiefensuche (DFS) für gerichtete Graphen mit Erreichbarkeitsprüfung.

Dieses Modul enthält die DirectedDFS-Klasse, die Tiefensuche für gerichtete
Graphen implementiert. Dieser Algorithmus bestimmt, welche Knoten von einem
oder mehreren Startknoten aus erreichbar sind.

Der Algorithmus funktioniert nach dem Backtracking-Prinzip:
1. Für jeden Startknoten:
   - Markiere den Knoten als besucht
   - Für jeden unbesuchten Nachbarn:
     - Rekursiv DFS aufrufen (Backtracking)

Komplexität: O(V + E)

Beispiele:
    >>> from src.algs4.pva_4_graphs import DirectedDFS, EdgeWeightedDigraph
    >>> g = EdgeWeightedDigraph(6)
    >>> g.add_edge(0, 1, 0.5)
    >>> g.add_edge(1, 2, 0.3)
    >>> g.add_edge(2, 3, 0.2)
    >>> dfs = DirectedDFS(g, [0])
    >>> dfs.marked(3)
    True
    >>> dfs.marked(4)
    False
"""


class DirectedDFS:
    """Tiefensuche für gerichtete Graphen mit Erreichbarkeitsprüfung.

    Diese Klasse implementiert Tiefensuche zur Bestimmung der Erreichbarkeit
    in gerichteten Graphen. Sie nutzt Backtracking, um alle erreichbaren
    Knoten von einem oder mehreren Startknoten zu finden.

    Attribute:
        marked (list): Markiert erreichbare Knoten
    """

    def __init__(self, G: "EdgeWeightedDigraph", sources: list) -> None:
        """Initialisiert DFS von mehreren Startknoten.

        Args:
            G: Der gerichtete gewichtete Graph
            sources: Liste der Startknoten

        Raises:
            ValueError: Wenn ein Startknoten nicht zwischen 0 und V-1 liegt
        """
        self._marked = [False for _ in range(G.V)]

        for s in sources:
            s = int(s)
            if s < 0 or s >= G.V:
                raise ValueError(f"Startknoten {s} ist nicht zwischen 0 und {G.V - 1}")

            if not self._marked[s]:
                self.dfs(G, s)

    def dfs(self, G: "EdgeWeightedDigraph", v: int) -> None:
        """Führt Tiefensuche rekursiv durch (Backtracking).

        Args:
            G: Der Graph
            v: Der aktuelle Knoten
        """
        self._marked[v] = True

        for e in G.adj[v]:
            w = e.To()
            if not self._marked[w]:
                self.dfs(G, w)

    def marked(self, v: int) -> bool:
        """Prüft ob ein Knoten vom Startknoten erreichbar ist.

        Args:
            v: Der zu prüfende Knoten

        Returns:
            True wenn der Knoten erreichbar ist, False sonst
        """
        return self._marked[v]


if __name__ == "__main__":
    import sys

    from src.algs4.pva_4_graphs import EdgeWeightedDigraph

    g = EdgeWeightedDigraph(file=open(sys.argv[1]))
    sources = [int(s) for s in sys.argv[2:]]
    dfs = DirectedDFS(g, sources)

    for v in range(g.V):
        if dfs.marked(v):
            print(v, end=" ")
    print()
