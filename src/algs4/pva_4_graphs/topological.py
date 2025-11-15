"""Topologische Sortierung für gerichtete azyklische Graphen (DAGs).

Dieses Modul enthält die Topological-Klasse, die topologische Sortierung
implementiert. Dieser Algorithmus ordnet die Knoten eines DAG so an, dass
für jede gerichtete Kante (u, v) der Knoten u vor v in der Ordnung kommt.

Der Algorithmus funktioniert nach dem Backtracking-Prinzip:
1. Führe DFS durch und berechne die Postorder
2. Gebe die Knoten in umgekehrter Postorder zurück
3. Dies ist eine gültige topologische Ordnung

Komplexität: O(V + E)

Anwendungen:
- Abhängigkeitsauflösung (z.B. Paketmanager)
- Aufgabenplanung
- Compiler-Optimierung
- Kursvoraussetzungen

Beispiele:
    >>> from src.algs4.pva_4_graphs import Topological, EdgeWeightedDigraph
    >>> g = EdgeWeightedDigraph(4)
    >>> g.add_edge(0, 1, 0.5)
    >>> g.add_edge(1, 2, 0.3)
    >>> g.add_edge(2, 3, 0.2)
    >>> topo = Topological(g)
    >>> topo.has_order()
    True
    >>> list(topo.order())
    [0, 1, 2, 3]
"""

from src.algs4.pva_1_fundamentals.queue import Queue
from src.algs4.pva_1_fundamentals.stack import Stack
from src.algs4.pva_4_graphs.edge_weighted_directed_cycle import (
    EdgeWeightedDirectedCycle,
)


class Topological:
    """Topologische Sortierung für gerichtete azyklische Graphen (DAGs).

    Diese Klasse implementiert topologische Sortierung mittels Tiefensuche.
    Sie prüft zuerst, ob der Graph azyklisch ist, und berechnet dann die
    topologische Ordnung.

    Attribute:
        order (Stack): Die topologische Ordnung der Knoten
    """

    def __init__(self, G: "EdgeWeightedDigraph") -> None:
        """Initialisiert topologische Sortierung.

        Args:
            G: Der gerichtete gewichtete Graph (sollte azyklisch sein)
        """
        self._order = None

        # Prüfe ob der Graph azyklisch ist
        finder = EdgeWeightedDirectedCycle(G)
        if not finder.has_cycle():
            self._order = self._compute_order(G)

    def _compute_order(self, G: "EdgeWeightedDigraph") -> Stack:
        """Berechnet die topologische Ordnung mittels DFS.

        Args:
            G: Der Graph

        Returns:
            Stack mit der topologischen Ordnung
        """
        marked = [False for _ in range(G.V)]
        post = Queue()

        for v in range(G.V):
            if not marked[v]:
                self._dfs(G, v, marked, post)

        # Gebe die Knoten in umgekehrter Postorder zurück
        order = Stack()
        for v in post:
            order.push(v)

        return order

    def _dfs(self, G: "EdgeWeightedDigraph", v: int, marked: list, post: Queue) -> None:
        """Führt DFS durch und berechnet Postorder.

        Args:
            G: Der Graph
            v: Der aktuelle Knoten
            marked: Liste der besuchten Knoten
            post: Queue für Postorder
        """
        marked[v] = True

        for e in G.adj[v]:
            w = e.To()
            if not marked[w]:
                self._dfs(G, w, marked, post)

        post.enqueue(v)

    def has_order(self) -> bool:
        """Prüft ob eine topologische Ordnung existiert.

        Returns:
            True wenn der Graph azyklisch ist, False sonst
        """
        return self._order is not None

    def order(self) -> Stack:
        """Gibt die topologische Ordnung zurück.

        Returns:
            Stack mit der topologischen Ordnung, oder None wenn Zyklen existieren
        """
        return self._order


if __name__ == "__main__":
    import sys

    from src.algs4.pva_4_graphs import EdgeWeightedDigraph

    g = EdgeWeightedDigraph(file=open(sys.argv[1]))
    topo = Topological(g)

    if topo.has_order():
        for v in topo.order():
            print(v, end=" ")
        print()
    else:
        print("Graph hat Zyklen - keine topologische Ordnung möglich")
