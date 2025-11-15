"""Prim's Algorithmus für Minimum Spanning Tree (MST).

Dieses Modul enthält die PrimMST-Klasse, die Prim's Algorithmus implementiert.
Dieser Algorithmus findet einen Minimum Spanning Tree in einem ungerichteten
gewichteten Graphen.

Der Algorithmus funktioniert nach dem Greedy-Prinzip:
1. Starte mit einem beliebigen Knoten
2. Wiederhole bis alle Knoten im MST sind:
   - Finde die Kante mit kleinstem Gewicht, die einen Knoten im MST mit einem
     Knoten außerhalb des MST verbindet
   - Füge diese Kante und den neuen Knoten zum MST hinzu

Komplexität: O((V + E) log V) mit IndexMinPQ

Beispiele:
    >>> from src.algs4.pva_4_graphs import EdgeWeightedGraph, Edge, PrimMST
    >>> g = EdgeWeightedGraph(4)
    >>> g.add_edge(Edge(0, 1, 0.5))
    >>> g.add_edge(Edge(1, 2, 0.3))
    >>> g.add_edge(Edge(2, 3, 0.2))
    >>> mst = PrimMST(g)
    >>> mst.weight()
    1.0
"""

from src.algs4.pva_4_graphs.index_min_pq import IndexMinPQ


class PrimMST:
    """Prim's Algorithmus für Minimum Spanning Tree.

    Diese Klasse implementiert Prim's Algorithmus zur Berechnung eines
    Minimum Spanning Tree in einem ungerichteten gewichteten Graphen.

    Attribute:
        edge_to (list): Die Kante zum Vorgänger im MST
        dist_to (list): Die Distanz zum MST
        marked (list): Markiert Knoten im MST
        pq (IndexMinPQ): Priority Queue für effiziente Verwaltung
    """

    def __init__(self, G: "EdgeWeightedGraph") -> None:
        """Initialisiert Prim's Algorithmus und berechnet den MST.

        Args:
            G: Der ungerichtete gewichtete Graph
        """
        self.edge_to = [None for _ in range(G.V)]
        self.dist_to = [float("inf") for _ in range(G.V)]
        self.marked = [False for _ in range(G.V)]
        self.pq = IndexMinPQ(G.V)

        # Starte mit Knoten 0
        self.dist_to[0] = 0.0
        self.pq.insert(0, self.dist_to[0])

        while not self.pq.is_empty():
            v = self.pq.del_min()
            self.visit(G, v)

    def visit(self, G: "EdgeWeightedGraph", v: int) -> None:
        """Besucht einen Knoten und relaxiert alle ausgehenden Kanten.

        Args:
            G: Der Graph
            v: Der zu besuchende Knoten
        """
        self.marked[v] = True

        for e in G.adj[v]:
            w = e.other(v)

            # Überspringe Kanten zu bereits besuchten Knoten
            if self.marked[w]:
                continue

            # Relaxiere die Kante
            if e.weight < self.dist_to[w]:
                self.dist_to[w] = e.weight
                self.edge_to[w] = e

                if self.pq.contains(w):
                    self.pq.change(w, self.dist_to[w])
                else:
                    self.pq.insert(w, self.dist_to[w])

    def edges(self) -> list:
        """Gibt die Kanten des MST zurück.

        Returns:
            Liste der Kanten des Minimum Spanning Tree
        """
        return [e for e in self.edge_to if e is not None]

    def weight(self) -> float:
        """Gibt das Gesamtgewicht des MST zurück.

        Returns:
            Das Gesamtgewicht aller Kanten im MST
        """
        return sum(e.weight for e in self.edges())


if __name__ == "__main__":
    import sys

    from src.algs4.pva_4_graphs import EdgeWeightedGraph

    g = EdgeWeightedGraph(file=open(sys.argv[1]))
    mst = PrimMST(g)
    for e in mst.edges():
        print(e)
    print(f"{mst.weight():.5f}")
