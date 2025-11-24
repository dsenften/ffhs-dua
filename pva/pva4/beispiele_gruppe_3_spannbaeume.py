#!/usr/bin/env python3
"""
Musterloessung: Gruppe 3 - Spannbaeume (MST)

Demonstriert:
- Kruskal's Algorithmus mit tinyEWG.txt
- Prim's Algorithmus mit tinyEWG.txt
- Vergleich der beiden Algorithmen
"""

from src.algs4.pva_4_graphs import EdgeWeightedGraph, KruskalMST, PrimMST


def beispiel_kruskal():
    """Beispiel 1: Kruskal's Algorithmus mit tinyEWG.txt."""
    print("\n" + "=" * 80)
    print("BEISPIEL 1: KRUSKAL'S ALGORITHMUS - tinyEWG.txt")
    print("=" * 80)

    # Graph aus Datei laden (Testdaten: 8 Knoten, 16 Kanten)
    with open("data/graphs/tinyEWG.txt") as f:
        g = EdgeWeightedGraph(file=f)

    # Kruskal MST
    mst = KruskalMST(g)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print(f"MST-Gewicht: {mst.weight():.2f}")
    print("MST-Kanten:")
    print("-" * 80)
    for edge in mst.edges():
        v = edge.either()
        w = edge.other(v)
        print(f"  {v}-{w}: {edge.weight:.2f}")


def beispiel_prim():
    """Beispiel 2: Prim's Algorithmus mit tinyEWG.txt."""
    print("\n" + "=" * 80)
    print("BEISPIEL 2: PRIM'S ALGORITHMUS - tinyEWG.txt")
    print("=" * 80)

    # Graph aus Datei laden
    with open("data/graphs/tinyEWG.txt") as f:
        g = EdgeWeightedGraph(file=f)

    # Prim MST
    mst = PrimMST(g)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print(f"MST-Gewicht: {mst.weight():.2f}")
    print("MST-Kanten:")
    print("-" * 80)
    for edge in mst.edges():
        v = edge.either()
        w = edge.other(v)
        print(f"  {v}-{w}: {edge.weight:.2f}")


def beispiel_vergleich():
    """Beispiel 3: Vergleich Kruskal vs. Prim."""
    print("\n" + "=" * 80)
    print("BEISPIEL 3: VERGLEICH KRUSKAL vs. PRIM - tinyEWG.txt")
    print("=" * 80)

    # Graph aus Datei laden
    with open("data/graphs/tinyEWG.txt") as f:
        g = EdgeWeightedGraph(file=f)

    # Beide Algorithmen ausführen
    kruskal_mst = KruskalMST(g)
    prim_mst = PrimMST(g)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("-" * 80)
    print(f"Kruskal MST-Gewicht: {kruskal_mst.weight():.2f}")
    print(f"Prim MST-Gewicht:    {prim_mst.weight():.2f}")
    print()

    # Kanten vergleichen
    kruskal_edges = set()
    for edge in kruskal_mst.edges():
        v = edge.either()
        w = edge.other(v)
        kruskal_edges.add((min(v, w), max(v, w)))

    prim_edges = set()
    for edge in prim_mst.edges():
        v = edge.either()
        w = edge.other(v)
        prim_edges.add((min(v, w), max(v, w)))

    print("Beobachtung:")
    print("  ✓ Beide Algorithmen finden MST mit gleichem Gewicht")
    print("  ✓ Kanten können unterschiedlich sein (mehrere MSTs möglich)")
    print(f"  ✓ Kruskal: {len(kruskal_edges)} Kanten")
    print(f"  ✓ Prim: {len(prim_edges)} Kanten")


def beispiel_mst_eigenschaften():
    """Beispiel 4: Eigenschaften des MST."""
    print("\n" + "=" * 80)
    print("BEISPIEL 4: MST-EIGENSCHAFTEN - tinyEWG.txt")
    print("=" * 80)

    # Graph aus Datei laden
    with open("data/graphs/tinyEWG.txt") as f:
        g = EdgeWeightedGraph(file=f)

    mst = KruskalMST(g)

    print(f"\nGraph: {g.V} Knoten, {g.E} Kanten")
    print("-" * 80)
    print(f"MST-Gewicht: {mst.weight():.2f}")
    print(f"MST-Kanten: {len(list(mst.edges()))}")
    print()

    # Eigenschaften
    print("Eigenschaften des MST:")
    print(f"  ✓ Anzahl Kanten = V - 1 = {g.V - 1}")
    print(f"  ✓ Verbindet alle {g.V} Knoten")
    print(f"  ✓ Minimales Gesamtgewicht: {mst.weight():.2f}")
    print("  ✓ Keine Zyklen (ist ein Baum)")


if __name__ == "__main__":
    print()
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "MUSTERLOESSUNG: GRUPPE 3 - SPANNBAEUME (MST)".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")

    beispiel_kruskal()
    beispiel_prim()
    beispiel_vergleich()
    beispiel_mst_eigenschaften()

    print("\n" + "=" * 80)
    print("✅ ALLE BEISPIELE ABGESCHLOSSEN")
    print("=" * 80)
    print()
