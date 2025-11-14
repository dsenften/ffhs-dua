# Graphen-Algorithmen (PVA 4)

Dieses Dokument beschreibt die Implementierung von Graphen-Algorithmen in ffhs-dua.

## Überblick

Die PVA 4 enthält Implementierungen von Graphen-Algorithmen, insbesondere Dijkstras Algorithmus für kürzeste Pfade.

### Module

- **DirectedEdge**: Gerichtete Kante mit Gewicht
- **EdgeWeightedDigraph**: Gewichteter gerichteter Graph
- **IndexMinPQ**: Indexed Min Priority Queue
- **DijkstraSP**: Dijkstras Algorithmus für kürzeste Pfade

## DirectedEdge

Eine gerichtete Kante mit Gewicht.

```python
from src.algs4.pva_4_graphs import DirectedEdge

# Erstelle eine Kante von Knoten 0 zu Knoten 1 mit Gewicht 0.5
edge = DirectedEdge(0, 1, 0.5)
print(edge.From())  # 0
print(edge.To())    # 1
print(edge.weight)  # 0.5
```

## EdgeWeightedDigraph

Ein gewichteter gerichteter Graph mit Adjazenzlisten.

```python
from src.algs4.pva_4_graphs import EdgeWeightedDigraph, DirectedEdge

# Erstelle einen Graphen mit 8 Knoten
g = EdgeWeightedDigraph(8)

# Füge Kanten hinzu
g.add_edge(DirectedEdge(0, 2, 0.26))
g.add_edge(DirectedEdge(0, 4, 0.38))
g.add_edge(DirectedEdge(2, 7, 0.34))

# Gib alle Kanten aus
edges = g.edges()
print(f"Graph hat {g.V} Knoten und {g.E} Kanten")
```

## IndexMinPQ

Eine Indexed Min Priority Queue für effiziente Prioritätsverwaltung.

```python
from src.algs4.pva_4_graphs import IndexMinPQ

# Erstelle eine PQ mit Kapazität 5
pq = IndexMinPQ(5)

# Füge Elemente ein
pq.insert(0, 1.0)
pq.insert(1, 0.5)
pq.insert(2, 2.0)

# Hole das Element mit kleinster Priorität
min_index = pq.del_min()  # 1 (mit Priorität 0.5)

# Ändere die Priorität eines Elements
pq.change(0, 0.3)
```

## DijkstraSP

Dijkstras Algorithmus für kürzeste Pfade.

```python
from src.algs4.pva_4_graphs import EdgeWeightedDigraph, DijkstraSP, DirectedEdge

# Erstelle einen Graphen
g = EdgeWeightedDigraph(8)
g.add_edge(DirectedEdge(0, 2, 0.26))
g.add_edge(DirectedEdge(0, 4, 0.38))
g.add_edge(DirectedEdge(2, 7, 0.34))
g.add_edge(DirectedEdge(4, 5, 0.35))
g.add_edge(DirectedEdge(5, 1, 0.32))

# Berechne kürzeste Pfade von Knoten 0
sp = DijkstraSP(g, 0)

# Überprüfe ob Pfad zu Knoten 1 existiert
if sp.has_path_to(1):
    print(f"Distanz zu 1: {sp.distTo[1]}")
    for edge in sp.path_to(1):
        print(f"  {edge}")
```

## Komplexität

| Operation | Komplexität |
|-----------|------------|
| DirectedEdge.From() | O(1) |
| DirectedEdge.To() | O(1) |
| EdgeWeightedDigraph.add_edge() | O(1) |
| EdgeWeightedDigraph.edges() | O(V + E) |
| IndexMinPQ.insert() | O(log n) |
| IndexMinPQ.del_min() | O(log n) |
| IndexMinPQ.change() | O(log n) |
| DijkstraSP.__init__() | O((V + E) log V) |
| DijkstraSP.has_path_to() | O(1) |
| DijkstraSP.path_to() | O(V) |

## Tests

Umfassende Tests für alle Graphen-Algorithmen sind in `tests/test_graphs/` verfügbar:

- `test_directed_edge.py`: Tests für DirectedEdge
- `test_edge_weighted_digraph.py`: Tests für EdgeWeightedDigraph
- `test_index_min_pq.py`: Tests für IndexMinPQ
- `test_dijkstra_sp.py`: Tests für DijkstraSP

Führe die Tests aus mit:

```bash
python3 -m pytest tests/test_graphs/ -v
```

## Referenzen

- Sedgewick, R., & Wayne, K. (2011). Algorithms, 4th Edition. Addison-Wesley.
- https://algs4.cs.princeton.edu/44sp/
