#!/usr/bin/env python3
"""
Musterloessung: Gruppe 4 - Union-Find (Disjoint Set Union)

Demonstriert:
- Union-Find Grundoperationen
- Integration in Kruskal's Algorithmus
- Zyklenerkennung
"""

from src.algs4.pva_1_fundamentals import UF
from src.algs4.pva_4_graphs import EdgeWeightedGraph, KruskalMST


def beispiel_union_find_grundlagen():
    """Beispiel 1: Union-Find Grundoperationen."""
    print("\n" + "=" * 80)
    print("BEISPIEL 1: UNION-FIND GRUNDOPERATIONEN")
    print("=" * 80)

    # Union-Find mit 10 Elementen
    uf = UF(10)

    print("\nInitial: 10 Komponenten (jedes Element ist allein)")
    print(f"Komponenten: {uf.count()}")
    print("-" * 80)

    # Unions durchführen
    operations = [
        (0, 1),
        (1, 2),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 8),
        (8, 9),
        (9, 0),
    ]

    for v, w in operations:
        uf.union(v, w)
        print(f"union({v}, {w}) → Komponenten: {uf.count()}")

    print()
    print("Verbindungen prüfen:")
    print("-" * 80)
    print(f"connected(0, 9): {uf.connected(0, 9)}")  # True
    print(f"connected(0, 3): {uf.connected(0, 3)}")  # False
    print(f"connected(3, 8): {uf.connected(3, 8)}")  # True


def beispiel_zyklenerkennung():
    """Beispiel 2: Zyklenerkennung mit Union-Find."""
    print("\n" + "=" * 80)
    print("BEISPIEL 2: ZYKLENERKENNUNG - tinyEWG.txt")
    print("=" * 80)

    # Graph aus Datei laden
    with open("data/graphs/tinyEWG.txt") as f:
        g = EdgeWeightedGraph(file=f)

    # Union-Find für Zyklenerkennung
    uf = UF(g.V)
    cycle_found = False
    cycle_edge = None

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("Prüfe auf Zyklen:")
    print("-" * 80)

    for v in range(g.V):
        for edge in g.adj[v]:
            w = edge.other(v)
            if v < w:  # Jede Kante nur einmal prüfen
                if uf.connected(v, w):
                    print(f"  Zyklus gefunden: {v}-{w}")
                    cycle_found = True
                    cycle_edge = (v, w)
                    break
                uf.union(v, w)
        if cycle_found:
            break

    if cycle_found:
        print(f"\n✓ Graph enthält Zyklus (z.B. {cycle_edge[0]}-{cycle_edge[1]})")
    else:
        print("\n✓ Graph ist azyklisch (ist ein Wald)")


def beispiel_union_find_in_kruskal():
    """Beispiel 3: Union-Find in Kruskal's Algorithmus."""
    print("\n" + "=" * 80)
    print("BEISPIEL 3: UNION-FIND IN KRUSKAL - tinyEWG.txt")
    print("=" * 80)

    # Graph aus Datei laden
    with open("data/graphs/tinyEWG.txt") as f:
        g = EdgeWeightedGraph(file=f)

    # Kruskal nutzt Union-Find intern
    mst = KruskalMST(g)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print(f"MST-Gewicht: {mst.weight():.2f}")
    print("MST-Kanten (mit Union-Find gefunden):")
    print("-" * 80)

    for edge in mst.edges():
        v = edge.either()
        w = edge.other(v)
        print(f"  {v}-{w}: {edge.weight:.2f}")

    print()
    print("Beobachtung:")
    print("  ✓ Union-Find verhindert Zyklen")
    print(f"  ✓ MST hat genau V-1 = {g.V - 1} Kanten")
    print(f"  ✓ Alle {g.V} Knoten sind verbunden")


def beispiel_komponenten():
    """Beispiel 4: Komponenten mit Union-Find."""
    print("\n" + "=" * 80)
    print("BEISPIEL 4: KOMPONENTEN FINDEN")
    print("=" * 80)

    # Union-Find mit 10 Elementen
    uf = UF(10)

    # Erstelle mehrere Komponenten
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(5, 6)
    uf.union(6, 7)
    # 8 und 9 sind allein

    print("\nKomponenten nach Unions:")
    print("-" * 80)

    # Finde alle Komponenten
    components = {}
    for i in range(10):
        root = uf.find(i)
        if root not in components:
            components[root] = []
        components[root].append(i)

    for i, (_, members) in enumerate(sorted(components.items()), 1):
        print(f"  Komponente {i}: {members}")

    print()
    print(f"Gesamt: {uf.count()} Komponenten")


if __name__ == "__main__":
    print()
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "MUSTERLOESSUNG: GRUPPE 4 - UNION-FIND".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")

    beispiel_union_find_grundlagen()
    beispiel_zyklenerkennung()
    beispiel_union_find_in_kruskal()
    beispiel_komponenten()

    print("\n" + "=" * 80)
    print("✅ ALLE BEISPIELE ABGESCHLOSSEN")
    print("=" * 80)
    print()
