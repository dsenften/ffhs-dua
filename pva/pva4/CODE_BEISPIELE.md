# PVA 4 - Code-Beispiele

## 1. Graphen-Repräsentation

```python
from src.algs4.pva_4_graphs import EdgeWeightedGraph, Edge

# Erstelle einen ungerichteten gewichteten Graphen
g = EdgeWeightedGraph(5)
g.add_edge(Edge(0, 1, 0.5))
g.add_edge(Edge(1, 2, 0.3))
g.add_edge(Edge(2, 3, 0.7))

print(f"Knoten: {g.V}, Kanten: {g.E}")
```

## 2. Kürzeste Pfade (Dijkstra)

```python
from src.algs4.pva_4_graphs import (
    EdgeWeightedDigraph, DirectedEdge, DijkstraSP
)

# Erstelle einen gerichteten gewichteten Graphen
g = EdgeWeightedDigraph(8)
g.add_edge(DirectedEdge(0, 2, 0.26))
g.add_edge(DirectedEdge(0, 4, 0.38))
g.add_edge(DirectedEdge(2, 7, 0.34))

# Berechne kürzeste Pfade von Knoten 0
sp = DijkstraSP(g, 0)

# Finde Pfad zu Knoten 7
if sp.has_path_to(7):
    print(f"Distanz: {sp.distTo[7]}")
    for edge in sp.path_to(7):
        print(edge)
```

## 3. Zyklenerkennung

```python
from src.algs4.pva_4_graphs import (
    EdgeWeightedDigraph, DirectedEdge, EdgeWeightedDirectedCycle
)

g = EdgeWeightedDigraph(3)
g.add_edge(DirectedEdge(0, 1, 0.5))
g.add_edge(DirectedEdge(1, 2, 0.6))
g.add_edge(DirectedEdge(2, 0, 0.7))  # Zyklus!

finder = EdgeWeightedDirectedCycle(g)
if finder.has_cycle():
    print("Zyklus gefunden:")
    for edge in finder.cycle:
        print(edge)
```

## 4. BFS (zu implementieren)

```python
# Zukünftige Implementierung
from src.algs4.pva_4_graphs import BFS

g = EdgeWeightedGraph(5)
# ... Kanten hinzufügen ...

bfs = BFS(g, 0)
if bfs.has_path_to(4):
    print(f"Pfad: {bfs.path_to(4)}")
    print(f"Distanz: {bfs.distance_to(4)}")
```

## 5. MST - Kruskal (zu implementieren)

```python
# Zukünftige Implementierung
from src.algs4.pva_4_graphs import KruskalMST

g = EdgeWeightedGraph(5)
# ... Kanten hinzufügen ...

mst = KruskalMST(g)
print(f"MST-Gewicht: {mst.weight()}")
for edge in mst.edges():
    print(edge)
```

## 6. MST - Prim (zu implementieren)

```python
# Zukünftige Implementierung
from src.algs4.pva_4_graphs import PrimMST

g = EdgeWeightedGraph(5)
# ... Kanten hinzufügen ...

mst = PrimMST(g)
print(f"MST-Gewicht: {mst.weight()}")
for edge in mst.edges():
    print(edge)
```

## 7. Topologische Sortierung (zu implementieren)

```python
# Zukünftige Implementierung
from src.algs4.pva_4_graphs import TopologicalSort

dag = EdgeWeightedDigraph(5)
# ... DAG-Kanten hinzufügen ...

topo = TopologicalSort(dag)
if topo.has_order():
    print("Topologische Ordnung:")
    for v in topo.order():
        print(v)
```

## 8. Datei-basierte Graphen

```python
from src.algs4.pva_4_graphs import EdgeWeightedDigraph, DijkstraSP

# Lade Graphen aus Datei
with open("data/graphs/tinyEWD.txt") as f:
    g = EdgeWeightedDigraph(file=f)

# Berechne kürzeste Pfade
sp = DijkstraSP(g, 0)
for t in range(g.V):
    if sp.has_path_to(t):
        print(f"0 to {t}: {sp.distTo[t]:.2f}")
```
