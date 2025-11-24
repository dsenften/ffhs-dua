#!/usr/bin/env python3
"""
Musterloessung: Gruppe 2 - Kuerzeste Wege (Dijkstra)

Demonstriert:
- Dijkstra's Algorithmus mit tinyEWD.txt
- Pfadrekonstruktion
- Vergleich verschiedener Startknoten
"""

from src.algs4.pva_4_graphs import DijkstraSP, EdgeWeightedDigraph


def beispiel_dijkstra():
    """Beispiel 1: Dijkstra's Algorithmus mit tinyEWD.txt."""
    print("\n" + "=" * 80)
    print("BEISPIEL 1: DIJKSTRA'S ALGORITHMUS - tinyEWD.txt")
    print("=" * 80)

    # Graph aus Datei laden (Testdaten: 8 Knoten, 15 Kanten)
    with open("data/graphs/tinyEWD.txt") as f:
        g = EdgeWeightedDigraph(file=f)

    # Dijkstra von Knoten 0
    sp = DijkstraSP(g, 0)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("Kuerzeste Pfade von Knoten 0:")
    print("-" * 80)
    for v in range(g.V):
        if sp.has_path_to(v):
            dist = sp.distTo[v]
            print(f"  0 → {v}: Distanz={dist:.2f}")
        else:
            print(f"  0 → {v}: nicht erreichbar")


def beispiel_pfadrekonstruktion():
    """Beispiel 2: Pfadrekonstruktion mit Dijkstra."""
    print("\n" + "=" * 80)
    print("BEISPIEL 2: PFADREKONSTRUKTION - tinyEWD.txt")
    print("=" * 80)

    # Graph aus Datei laden
    with open("data/graphs/tinyEWD.txt") as f:
        g = EdgeWeightedDigraph(file=f)

    # Dijkstra von Knoten 0
    sp = DijkstraSP(g, 0)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("Pfade von Knoten 0:")
    print("-" * 80)
    for target in range(g.V):
        if sp.has_path_to(target):
            dist = sp.distTo[target]
            print(f"  0 → {target}: Distanz={dist:.2f}")
        else:
            print(f"  0 → {target}: nicht erreichbar")


def beispiel_mehrere_startknoten():
    """Beispiel 3: Dijkstra von verschiedenen Startknoten."""
    print("\n" + "=" * 80)
    print("BEISPIEL 3: MEHRERE STARTKNOTEN - tinyEWD.txt")
    print("=" * 80)

    # Graph aus Datei laden
    with open("data/graphs/tinyEWD.txt") as f:
        g = EdgeWeightedDigraph(file=f)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("-" * 80)

    # Dijkstra von verschiedenen Startknoten
    for start in [0, 1, 2]:
        sp = DijkstraSP(g, start)
        print(f"\nVon Knoten {start}:")
        for target in range(g.V):
            if sp.has_path_to(target):
                dist = sp.distTo[target]
                print(f"  {start} → {target}: {dist:.2f}")


def beispiel_vergleich_startknoten():
    """Beispiel 4: Vergleich der Distanzen von verschiedenen Startknoten."""
    print("\n" + "=" * 80)
    print("BEISPIEL 4: VERGLEICH STARTKNOTEN - tinyEWD.txt")
    print("=" * 80)

    # Graph aus Datei laden
    with open("data/graphs/tinyEWD.txt") as f:
        g = EdgeWeightedDigraph(file=f)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("-" * 80)

    # Dijkstra von Knoten 0 und 1
    sp0 = DijkstraSP(g, 0)
    sp1 = DijkstraSP(g, 1)

    print("\nDistanzen von Knoten 0 vs. Knoten 1:")
    print("-" * 80)
    for v in range(g.V):
        dist0 = sp0.distTo[v] if sp0.has_path_to(v) else float("inf")
        dist1 = sp1.distTo[v] if sp1.has_path_to(v) else float("inf")
        print(f"  Zu {v}: von 0={dist0:.2f}, von 1={dist1:.2f}")


if __name__ == "__main__":
    print()
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "MUSTERLOESSUNG: GRUPPE 2 - KUERZESTE WEGE (DIJKSTRA)".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")

    beispiel_dijkstra()
    beispiel_pfadrekonstruktion()
    beispiel_mehrere_startknoten()
    beispiel_vergleich_startknoten()

    print("\n" + "=" * 80)
    print("✅ ALLE BEISPIELE ABGESCHLOSSEN")
    print("=" * 80)
    print()
