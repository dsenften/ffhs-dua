"""Zyklenerkennung in gewichteten gerichteten Graphen.

Findet einen gerichteten Zyklus in einem gewichteten gerichteten Graphen
mit Tiefensuche (DFS). Läuft in O(V + E) Zeit.

Ausführung:
    python edge_weighted_directed_cycle.py V E F

Wobei:
    V: Anzahl der Knoten
    E: Anzahl der Kanten
    F: Anzahl zusätzlicher Kanten für Zyklenerkennung
"""

import random

from src.algs4.pva_1_fundamentals.stack import Stack

from .directed_edge import DirectedEdge
from .edge_weighted_digraph import EdgeWeightedDigraph


class EdgeWeightedDirectedCycle:
    """Findet einen gerichteten Zyklus in einem gewichteten gerichteten Graphen."""

    def __init__(self, G: "EdgeWeightedDigraph") -> None:
        """Initialisiert die Zyklenerkennung.

        Args:
            G: Der zu analysierende gewichtete gerichtete Graph.
        """
        self.cycle = None
        self.marked = [False for _ in range(G.V)]
        self.on_stack = [False for _ in range(G.V)]
        self.edge_to = [None for _ in range(G.V)]
        for v in range(G.V):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G: "EdgeWeightedDigraph", v: int) -> None:
        """Tiefensuche zur Zyklenerkennung.

        Args:
            G: Der Graph.
            v: Der aktuelle Knoten.
        """
        self.on_stack[v] = True
        self.marked[v] = True
        for e in G.adj[v]:
            w = e.To()
            if self.cycle is not None:
                return
            elif not self.marked[w]:
                self.edge_to[w] = e
                self.dfs(G, w)
            elif self.on_stack[w]:
                # Rückverfolgung des gerichteten Zyklus
                self.cycle = Stack()
                f = e
                while f.From() != w:
                    self.cycle.push(f)
                    f = self.edge_to[f.From()]
                self.cycle.push(f)
                return
        self.on_stack[v] = False

    def has_cycle(self) -> bool:
        """Überprüft, ob ein Zyklus vorhanden ist.

        Returns:
            True, wenn ein Zyklus gefunden wurde, sonst False.
        """
        return self.cycle is not None


if __name__ == "__main__":
    import sys

    V, E, F = sys.argv[1:]
    V = int(V)
    E = int(E)
    F = int(F)
    graph = EdgeWeightedDigraph(V)
    for _ in range(int(E)):
        v = 0
        w = 0
        while v >= w:
            v = random.randint(0, V - 1)
            w = random.randint(0, V - 1)
        weight = random.uniform(0, 1)
        graph.add_edge(DirectedEdge(v, w, weight))
    # Füge F zusätzliche Kanten hinzu
    for _ in range(int(F)):
        v = random.randint(0, V - 1)
        w = random.randint(0, V - 1)
        weight = random.uniform(0, 1)
        graph.add_edge(DirectedEdge(v, w, weight))
    print(graph)

    finder = EdgeWeightedDirectedCycle(graph)
    if finder.has_cycle():
        print("Zyklus gefunden:\n")
        for e in finder.cycle:
            print(e, " ")
        print()
    else:
        print("Kein gerichteter Zyklus")
