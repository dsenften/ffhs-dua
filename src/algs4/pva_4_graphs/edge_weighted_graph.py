"""Ungerichteter gewichteter Graph mit Adjazenzlisten.

Ein ungerichteter gewichteter Graph, implementiert mit Adjazenzlisten.
Parallele Kanten und Selbstschleifen sind erlaubt.

Ausführung:
    python edge_weighted_graph.py dateiname.txt

Beispiel-Ausgabe:
    8 16
    0: 6-0 0.58000  0-2 0.26000  0-4 0.38000  0-7 0.16000
    1: 1-3 0.29000  1-2 0.36000  1-7 0.19000  1-5 0.32000
    2: 6-2 0.40000  2-7 0.34000  1-2 0.36000  0-2 0.26000  2-3 0.17000
    3: 3-6 0.52000  1-3 0.29000  2-3 0.17000
    4: 6-4 0.93000  0-4 0.38000  4-7 0.37000  4-5 0.35000
    5: 1-5 0.32000  5-7 0.28000  4-5 0.35000
    6: 6-4 0.93000  6-0 0.58000  3-6 0.52000  6-2 0.40000
    7: 2-7 0.34000  1-7 0.19000  0-7 0.16000  5-7 0.28000  4-7 0.37000
"""

from src.algs4.pva_1_fundamentals.bag import Bag

from .edge import Edge


class EdgeWeightedGraph:
    """Ungerichteter gewichteter Graph mit Adjazenzlisten."""

    def __init__(self, v: int = 0, **kwargs) -> None:
        """Initialisiert einen ungerichteten gewichteten Graphen.

        Args:
            v: Anzahl der Knoten.
            **kwargs: Optional 'file' für Datei-basierte Initialisierung.
        """
        self.V = v
        self.E = 0
        self.adj = {}
        for i in range(self.V):
            self.adj[i] = Bag()

        if "file" in kwargs:
            # Initialisiere Graphen aus Datei
            in_file = kwargs["file"]
            self.V = int(in_file.readline())
            for i in range(self.V):
                self.adj[i] = Bag()
            E = int(in_file.readline())
            for _ in range(E):
                v, w, weight = in_file.readline().split()
                self.add_edge(Edge(int(v), int(w), float(weight)))

    def __str__(self) -> str:
        """Gibt den Graphen als String zurück."""
        s = f"{self.V} vertices, {self.E} edges\n"
        for i in range(self.V):
            adjs = " ".join([str(x) for x in self.adj[i]])
            s += f"{i}: {adjs}\n"
        return s

    def add_edge(self, e: Edge) -> None:
        """Fügt eine Kante zum Graphen hinzu.

        Args:
            e: Die hinzuzufügende Kante.
        """
        v = e.either()
        w = e.other(v)
        self.adj[v].add(e)
        self.adj[w].add(e)
        self.E += 1

    def edges(self) -> list:
        """Gibt alle Kanten des Graphen zurück.

        Returns:
            Liste aller Kanten (ohne Duplikate).
        """
        edges = []
        for v in range(self.V):
            for e in self.adj[v]:
                if e.other(v) > v:
                    edges.append(e)
        return edges


if __name__ == "__main__":
    import sys

    graph = EdgeWeightedGraph(file=open(sys.argv[1]))
    print(graph)
