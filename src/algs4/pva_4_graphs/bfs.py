"""Breitensuche (BFS) für ungerichtete Graphen.

Dieses Modul enthält die BFS-Klasse, die Breitensuche in einem ungerichteten
Graphen implementiert. BFS findet alle Knoten, die von einem Startknoten
erreichbar sind, und berechnet die kürzesten Pfade (in Bezug auf die Anzahl
der Kanten, nicht die Gewichte).

Komplexität: O(V + E)

Beispiele:
    >>> from src.algs4.pva_4_graphs import EdgeWeightedGraph, Edge, BFS
    >>> g = EdgeWeightedGraph(6)
    >>> g.add_edge(Edge(0, 1, 0.5))
    >>> g.add_edge(Edge(0, 2, 0.3))
    >>> g.add_edge(Edge(1, 3, 0.2))
    >>> bfs = BFS(g, 0)
    >>> bfs.has_path_to(3)
    True
    >>> bfs.distance_to(3)
    2
"""

from src.algs4.pva_1_fundamentals.queue import Queue
from src.algs4.pva_1_fundamentals.stack import Stack


class BFS:
    """Breitensuche für ungerichtete Graphen.

    Diese Klasse implementiert Breitensuche (BFS) zur Findung aller Knoten,
    die von einem Startknoten erreichbar sind. Sie berechnet auch die
    kürzesten Pfade in Bezug auf die Anzahl der Kanten.

    Attribute:
        marked (list): Markiert besuchte Knoten
        edge_to (list): Speichert die Kante zum Vorgänger
        distance (list): Speichert die Distanz vom Startknoten
        s (int): Der Startknoten
    """

    def __init__(self, G: "EdgeWeightedGraph", s: int) -> None:
        """Initialisiert BFS mit einem Graphen und Startknoten.

        Args:
            G: Der ungerichtete gewichtete Graph
            s: Der Startknoten

        Raises:
            ValueError: Wenn s ausserhalb des gültigen Bereichs liegt
        """
        if s < 0 or s >= G.V:
            raise ValueError(
                f"Startknoten {s} ist ausserhalb des Bereichs [0, {G.V - 1}]"
            )

        self.marked = [False for _ in range(G.V)]
        self.edge_to = [None for _ in range(G.V)]
        self.distance = [float("inf") for _ in range(G.V)]
        self.s = s
        self.distance[s] = 0
        self.bfs(G, s)

    def bfs(self, G: "EdgeWeightedGraph", s: int) -> None:
        """Führt Breitensuche durch.

        Args:
            G: Der Graph
            s: Der Startknoten
        """
        queue = Queue()
        self.marked[s] = True
        queue.enqueue(s)

        while not queue.is_empty():
            v = queue.dequeue()
            for e in G.adj[v]:
                w = e.other(v)
                if not self.marked[w]:
                    self.edge_to[w] = e
                    self.distance[w] = self.distance[v] + 1
                    self.marked[w] = True
                    queue.enqueue(w)

    def has_path_to(self, v: int) -> bool:
        """Überprüft, ob es einen Pfad zum Knoten v gibt.

        Args:
            v: Der Zielknoten

        Returns:
            True, wenn es einen Pfad gibt, False sonst
        """
        return self.marked[v]

    def distance_to(self, v: int) -> int:
        """Gibt die Distanz vom Startknoten zum Knoten v zurück.

        Die Distanz ist die Anzahl der Kanten im kürzesten Pfad.

        Args:
            v: Der Zielknoten

        Returns:
            Die Distanz, oder float('inf') wenn kein Pfad existiert
        """
        return self.distance[v]

    def path_to(self, v: int) -> "Stack":
        """Gibt den kürzesten Pfad zum Knoten v zurück.

        Args:
            v: Der Zielknoten

        Returns:
            Ein Stack mit den Kanten des kürzesten Pfades, oder None wenn kein Pfad existiert
        """
        if not self.has_path_to(v):
            return None

        path = Stack()
        x = v
        while self.distance[x] != 0:
            e = self.edge_to[x]
            path.push(e)
            x = e.other(x)
        return path


if __name__ == "__main__":
    import sys

    from src.algs4.pva_4_graphs import EdgeWeightedGraph

    graph = EdgeWeightedGraph(file=open(sys.argv[1]))
    s = int(sys.argv[2])
    bfs = BFS(graph, s)

    for t in range(graph.V):
        if bfs.has_path_to(t):
            print(f"{s} to {t} ({bfs.distance_to(t)}):  ", end="")
            for e in bfs.path_to(t):
                print(e, " ", end="")
            print()
        else:
            print(f"{s} to {t}: not connected")
