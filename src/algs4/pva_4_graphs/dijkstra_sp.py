"""Dijkstras Algorithmus für kürzeste Pfade.

Dieses Modul enthält die DijkstraSP-Klasse, die Dijkstras Algorithmus
implementiert zur Berechnung der kürzesten Pfade von einem Startknoten
zu allen anderen Knoten in einem gewichteten Digraph mit nicht-negativen
Kantengewichten.

Beispiele:
    >>> from src.algs4.pva_4_graphs import EdgeWeightedDigraph, DijkstraSP, DirectedEdge
    >>> g = EdgeWeightedDigraph(8)
    >>> g.add_edge(DirectedEdge(0, 2, 0.26))
    >>> g.add_edge(DirectedEdge(0, 4, 0.38))
    >>> sp = DijkstraSP(g, 0)
    >>> sp.has_path_to(2)
    True
    >>> sp.distTo[2]
    0.26
"""

from src.algs4.pva_1_fundamentals.stack import Stack
from src.algs4.pva_4_graphs.edge_weighted_digraph import EdgeWeightedDigraph
from src.algs4.pva_4_graphs.index_min_pq import IndexMinPQ

POSITIVE_INFINITY = 999999.0


class DijkstraSP:
    """Dijkstras Algorithmus für kürzeste Pfade.

    Diese Klasse berechnet die kürzesten Pfade von einem Startknoten s
    zu allen anderen Knoten in einem gewichteten Digraph mit nicht-negativen
    Kantengewichten. Die Laufzeit ist O((V + E) log V) mit einer IndexMinPQ.

    Attribute:
        edgeTo (list): Die letzte Kante auf dem kürzesten Pfad zu jedem Knoten
        distTo (list): Die Distanz vom Startknoten zu jedem Knoten
        pq (IndexMinPQ): Priority Queue für die Verarbeitung von Knoten
    """

    def __init__(self, g: "EdgeWeightedDigraph", s: int) -> None:
        """Initialisiert Dijkstras Algorithmus.

        Args:
            g: Der gewichtete Digraph
            s: Der Startknoten

        Raises:
            ValueError: Wenn s außerhalb des gültigen Bereichs liegt
        """
        if s < 0 or s >= g.V:
            raise ValueError(
                f"Startknoten {s} ist außerhalb des Bereichs [0, {g.V - 1}]"
            )

        self.edgeTo = [None for _ in range(g.V)]
        self.distTo = [float("inf") for _ in range(g.V)]
        for v in range(g.V):
            self.distTo[v] = POSITIVE_INFINITY
        self.distTo[s] = 0.0
        self.pq = IndexMinPQ(g.V)
        self.pq.insert(s, self.distTo[s])
        while not self.pq.is_empty():
            self.relax(g, self.pq.del_min())

    def relax(self, g: "EdgeWeightedDigraph", v: int) -> None:
        """Relaxiert alle Kanten von Knoten v.

        Args:
            g: Der gewichtete Digraph
            v: Der Knoten, dessen Kanten relaxiert werden sollen
        """
        for e in g.adj[v]:
            w = e.To()
            if self.distTo[w] > self.distTo[v] + e.weight:
                self.distTo[w] = self.distTo[v] + e.weight
                self.edgeTo[w] = e
                if self.pq.contains(w):
                    self.pq.change(w, self.distTo[w])
                else:
                    self.pq.insert(w, self.distTo[w])

    def has_path_to(self, v: int) -> bool:
        """Überprüft, ob es einen Pfad zum Knoten v gibt.

        Args:
            v: Der Zielknoten

        Returns:
            True, wenn es einen Pfad gibt, False sonst
        """
        return self.distTo[v] < POSITIVE_INFINITY

    def path_to(self, v: int) -> "Stack":
        """Gibt den kürzesten Pfad zum Knoten v zurück.

        Args:
            v: Der Zielknoten

        Returns:
            Ein Stack mit den Kanten des kürzesten Pfades, oder None wenn kein Pfad existiert
        """
        if not self.has_path_to(v):
            return None
        edges = Stack()
        e = self.edgeTo[v]
        while e is not None:
            edges.push(e)
            e = self.edgeTo[e.From()]
        return edges


if __name__ == "__main__":
    import sys

    graph = EdgeWeightedDigraph(file=open(sys.argv[1]))
    s = int(sys.argv[2])
    sp = DijkstraSP(graph, s)
    for t in range(graph.V):
        if sp.has_path_to(t):
            print(f"{s} to {t} ({sp.distTo[t]:.2f})  ", end="")
            for e in sp.path_to(t):
                print(e, " ", end="")
            print()
        else:
            print(f"{s} to {t}  no path")
