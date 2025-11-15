"""Kruskal's Algorithmus für Minimum Spanning Tree (MST).

Dieses Modul enthält die KruskalMST-Klasse, die Kruskal's Algorithmus
implementiert. Dieser Algorithmus findet einen Minimum Spanning Tree in
einem ungerichteten gewichteten Graphen.

Der Algorithmus funktioniert nach dem Greedy-Prinzip:
1. Sortiere alle Kanten nach Gewicht
2. Für jede Kante (in aufsteigender Reihenfolge):
   - Wenn die Kante zwei verschiedene Komponenten verbindet, füge sie zum MST hinzu
   - Verwende Union-Find zur Komponentenverwaltung

Komplexität: O(E log E) für Sortierung, O(E α(V)) für Union-Find
Gesamtkomplexität: O(E log E)

Beispiele:
    >>> from src.algs4.pva_4_graphs import EdgeWeightedGraph, Edge, KruskalMST
    >>> g = EdgeWeightedGraph(4)
    >>> g.add_edge(Edge(0, 1, 0.5))
    >>> g.add_edge(Edge(1, 2, 0.3))
    >>> g.add_edge(Edge(2, 3, 0.2))
    >>> mst = KruskalMST(g)
    >>> mst.weight()
    1.0
"""

from src.algs4.pva_1_fundamentals.queue import Queue
from src.algs4.pva_1_fundamentals.uf import UF


class KruskalMST:
    """Kruskal's Algorithmus für Minimum Spanning Tree.

    Diese Klasse implementiert Kruskal's Algorithmus zur Berechnung eines
    Minimum Spanning Tree in einem ungerichteten gewichteten Graphen.

    Attribute:
        mst (Queue): Die Kanten des MST
        weight (float): Das Gesamtgewicht des MST
    """

    def __init__(self, G: "EdgeWeightedGraph") -> None:
        """Initialisiert Kruskal's Algorithmus und berechnet den MST.

        Args:
            G: Der ungerichtete gewichtete Graph
        """
        self.mst = Queue()
        self._weight = 0.0

        # Sortiere alle Kanten nach Gewicht
        edges = sorted(G.edges(), key=lambda e: e.weight)

        # Verwende Union-Find zur Komponentenverwaltung
        uf = UF(G.V)

        # Greedy: Füge Kanten hinzu, die zwei verschiedene Komponenten verbinden
        for e in edges:
            v = e.either()
            w = e.other(v)

            # Überspringe Kanten, die zwei Knoten in derselben Komponente verbinden
            if uf.connected(v, w):
                continue

            # Verbinde die beiden Komponenten
            uf.union(v, w)
            self.mst.enqueue(e)
            self._weight += e.weight

            # MST hat V-1 Kanten
            if self.mst.size() == G.V - 1:
                break

    def edges(self) -> list:
        """Gibt die Kanten des MST zurück.

        Returns:
            Liste der Kanten des Minimum Spanning Tree
        """
        result = []
        while not self.mst.is_empty():
            result.append(self.mst.dequeue())
        # Wiederherstellen der Queue für mehrfache Aufrufe
        for e in result:
            self.mst.enqueue(e)
        return result

    def weight(self) -> float:
        """Gibt das Gesamtgewicht des MST zurück.

        Returns:
            Das Gesamtgewicht aller Kanten im MST
        """
        return self._weight


if __name__ == "__main__":
    import sys

    from src.algs4.pva_4_graphs import EdgeWeightedGraph

    g = EdgeWeightedGraph(file=open(sys.argv[1]))
    mst = KruskalMST(g)
    for e in mst.edges():
        print(e)
    print(f"{mst.weight():.5f}")
