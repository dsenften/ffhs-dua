"""Tiefensuche (DFS) für ungerichtete Graphen mit Pfadfindung.

Dieses Modul enthält die DFSPaths-Klasse, die Tiefensuche implementiert.
Dieser Algorithmus findet Pfade zwischen Knoten in ungerichteten Graphen.

Der Algorithmus funktioniert nach dem Backtracking-Prinzip:
1. Starte mit einem Startknoten
2. Markiere den Knoten als besucht
3. Für jeden unbesuchten Nachbarn:
   - Rekursiv DFS aufrufen (Backtracking)
4. Speichere die Kanten zum Rekonstruieren von Pfaden

Komplexität: O(V + E)

Beispiele:
    >>> from src.algs4.pva_4_graphs import DFSPaths, EdgeWeightedGraph, Edge
    >>> g = EdgeWeightedGraph(6)
    >>> g.add_edge(Edge(0, 1, 0.5))
    >>> g.add_edge(Edge(1, 2, 0.3))
    >>> g.add_edge(Edge(2, 3, 0.2))
    >>> dfs = DFSPaths(g, 0)
    >>> dfs.has_path_to(3)
    True
    >>> path = dfs.path_to(3)
"""

from src.algs4.pva_1_fundamentals.stack import Stack


class DFSPaths:
    """Tiefensuche für ungerichtete Graphen mit Pfadfindung.

    Diese Klasse implementiert Tiefensuche zur Pfadfindung in ungerichteten
    Graphen. Sie nutzt Backtracking, um alle erreichbaren Knoten zu finden.

    Attribute:
        marked (list): Markiert besuchte Knoten
        edge_to (list): Speichert die Kante zum Vorgänger
        s (int): Der Startknoten
    """

    def __init__(self, G: "EdgeWeightedGraph", s: int) -> None:
        """Initialisiert DFS und findet alle erreichbaren Knoten.

        Args:
            G: Der ungerichtete gewichtete Graph
            s: Der Startknoten

        Raises:
            ValueError: Wenn s nicht zwischen 0 und V-1 liegt
        """
        if s < 0 or s >= G.V:
            raise ValueError(f"Startknoten {s} ist nicht zwischen 0 und {G.V - 1}")

        self.marked = [False for _ in range(G.V)]
        self.edge_to = [None for _ in range(G.V)]
        self.s = s
        self.dfs(G, s)

    def dfs(self, G: "EdgeWeightedGraph", v: int) -> None:
        """Führt Tiefensuche rekursiv durch (Backtracking).

        Args:
            G: Der Graph
            v: Der aktuelle Knoten
        """
        self.marked[v] = True

        for e in G.adj[v]:
            w = e.other(v)

            # Überspringe bereits besuchte Knoten
            if self.marked[w]:
                continue

            # Speichere die Kante und rekursiv DFS (Backtracking)
            self.edge_to[w] = e
            self.dfs(G, w)

    def has_path_to(self, v: int) -> bool:
        """Prüft ob ein Pfad zum Knoten v existiert.

        Args:
            v: Der Zielknoten

        Returns:
            True wenn ein Pfad existiert, False sonst
        """
        return self.marked[v]

    def path_to(self, v: int) -> "Stack":
        """Gibt den Pfad vom Startknoten zum Knoten v zurück.

        Args:
            v: Der Zielknoten

        Returns:
            Stack mit den Kanten des Pfades, oder None wenn kein Pfad existiert
        """
        if not self.has_path_to(v):
            return None

        path = Stack()
        x = v

        while x != self.s:
            e = self.edge_to[x]
            path.push(e)
            x = e.other(x)

        path.push(None)  # Markiere den Startknoten
        return path


if __name__ == "__main__":
    import sys

    from src.algs4.pva_4_graphs import EdgeWeightedGraph

    g = EdgeWeightedGraph(file=open(sys.argv[1]))
    s = int(sys.argv[2])
    dfs = DFSPaths(g, s)

    for v in range(g.V):
        if dfs.has_path_to(v):
            print(f"{s} to {v}: ", end="")
            for e in dfs.path_to(v):
                if e is None:
                    print(s, end="")
                else:
                    print(f"-{e.other(e.either())}", end="")
            print()
        else:
            print(f"{s} to {v}: not connected")
