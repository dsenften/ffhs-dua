#!/usr/bin/env python3
"""Ausführbare Beispiele für Gruppe 1: BFS & DFS.

Dieses Skript zeigt praktische Beispiele für:
- Breitensuche (BFS)
- Tiefensuche (DFS)
- Topologische Sortierung

Verwendung:
    python3 beispiele_gruppe_1_bfs_dfs.py
"""

from src.algs4.pva_4_graphs import (
    BFS,
    DFSPaths,
    DirectedEdge,
    EdgeWeightedDigraph,
    EdgeWeightedGraph,
    Topological,
)


def beispiel_bfs():
    """Beispiel 1: Breitensuche (BFS) mit tinyEWG.txt."""
    print("\n" + "=" * 80)
    print("BEISPIEL 1: BREITENSUCHE (BFS) - tinyEWG.txt")
    print("=" * 80)

    # Graph aus Datei laden (Testdaten: 8 Knoten, 16 Kanten)
    with open("data/graphs/tinyEWG.txt") as f:
        g = EdgeWeightedGraph(file=f)

    # BFS von Knoten 0
    bfs = BFS(g, 0)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("BFS von Knoten 0:")
    print("-" * 80)
    for target in range(g.V):
        if bfs.has_path_to(target):
            dist = bfs.distance_to(target)
            print(f"  0 → {target}: Distanz={dist:2d}")
        else:
            print(f"  0 → {target}: nicht erreichbar")


def beispiel_dfs():
    """Beispiel 2: Tiefensuche (DFS) mit tinyEWG.txt."""
    print("\n" + "=" * 80)
    print("BEISPIEL 2: TIEFENSUCHE (DFS) - tinyEWG.txt")
    print("=" * 80)

    # Graph aus Datei laden (Testdaten: 8 Knoten, 16 Kanten)
    with open("data/graphs/tinyEWG.txt") as f:
        g = EdgeWeightedGraph(file=f)

    # DFS von Knoten 0
    dfs = DFSPaths(g, 0)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("DFS von Knoten 0:")
    print("-" * 80)
    for target in range(g.V):
        if dfs.has_path_to(target):
            print(f"  0 → {target}: erreichbar")
        else:
            print(f"  0 → {target}: nicht erreichbar")


def beispiel_topologische_sortierung():
    """Beispiel 3: Topologische Sortierung mit tinyDAG.txt."""
    print("\n" + "=" * 80)
    print("BEISPIEL 3: TOPOLOGISCHE SORTIERUNG - tinyDAG.txt")
    print("=" * 80)

    # DAG aus Datei laden (Testdaten: 13 Knoten, 22 Kanten)
    # Hinweis: tinyDAG.txt hat keine Gewichte, daher manuell laden
    with open("data/graphs/tinyDAG.txt") as f:
        lines = f.readlines()
        V = int(lines[0].strip())
        E = int(lines[1].strip())

        g = EdgeWeightedDigraph(V)
        for i in range(2, 2 + E):
            parts = lines[i].strip().split()
            v, w = int(parts[0]), int(parts[1])
            # Gewicht 0.0 für ungewichtete Kanten
            g.add_edge(DirectedEdge(int(v), int(w), 0.0))

    # Topologische Sortierung
    topo = Topological(g)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("Topologische Sortierung:")
    print("-" * 80)
    if topo.has_order():
        order = list(topo.order())
        print(f"  Ordnung: {order}")
        print(f"  Länge: {len(order)}")
    else:
        print("  Graph enthält Zyklus!")


def beispiel_vergleich_bfs_vs_dfs():
    """Beispiel 4: Vergleich BFS vs DFS mit tinyEWG.txt."""
    print("\n" + "=" * 80)
    print("BEISPIEL 4: VERGLEICH BFS vs DFS - tinyEWG.txt")
    print("=" * 80)

    # Graph aus Datei laden (Testdaten: 8 Knoten, 16 Kanten)
    with open("data/graphs/tinyEWG.txt") as f:
        g = EdgeWeightedGraph(file=f)

    # BFS
    bfs = BFS(g, 0)
    bfs_dist = bfs.distance_to(5) if bfs.has_path_to(5) else -1

    # DFS
    dfs = DFSPaths(g, 0)
    dfs_found = dfs.has_path_to(5)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("Pfad von 0 zu 5:")
    print("-" * 80)
    print(f"  BFS: Distanz={bfs_dist}")
    print(f"  DFS: Erreichbar={dfs_found}")
    print("\n  Beobachtung:")
    print("  - BFS findet den kürzesten Pfad (nach Kantenzahl)")
    print("  - DFS findet einen beliebigen Pfad (abhängig von Reihenfolge)")


if __name__ == "__main__":
    print("\n" + "╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "MUSTERLOESSUNG: GRUPPE 1 - BFS & DFS".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")

    beispiel_bfs()
    beispiel_dfs()
    beispiel_topologische_sortierung()
    beispiel_vergleich_bfs_vs_dfs()

    print("\n" + "=" * 80)
    print("✅ ALLE BEISPIELE ABGESCHLOSSEN")
    print("=" * 80 + "\n")
