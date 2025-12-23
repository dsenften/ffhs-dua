# Musterlösung: Gruppe 1 - Breiten- und Tiefensuche (BFS & DFS)

## 1. Grundkonzepte

### BFS (Breadth-First Search)
- **Strategie**: Schichtweise Erkundung (Level-by-Level)
- **Datenstruktur**: Queue (FIFO)
- **Komplexität**: O(V + E)
- **Anwendung**: Kürzeste Pfade in ungewichteten Graphen

### DFS (Depth-First Search)
- **Strategie**: Tiefenorientierte Erkundung (Backtracking)
- **Datenstruktur**: Stack (LIFO) oder Rekursion
- **Komplexität**: O(V + E)
- **Anwendung**: Pfadfindung, Topologische Sortierung, Zyklenerkennung

### Topologische Sortierung
- **Zweck**: Lineare Ordnung von DAG-Knoten
- **Methode**: DFS mit Postorder-Traversierung
- **Komplexität**: O(V + E)
- **Anwendung**: Task-Scheduling, Dependency Resolution

---

## 2. Implementierungen

### 2.1 BFS - Beispiel mit tinyEWG.txt

```python
from src.algs4.pva_4_graphs import BFS, EdgeWeightedGraph

# Graph aus Datei laden (Testdaten: 8 Knoten, 16 Kanten)
with open("data/graphs/tinyEWG.txt") as f:
    g = EdgeWeightedGraph(file=f)

# BFS von Knoten 0
bfs = BFS(g, 0)

# Pfade abfragen
for target in range(g.V):
    if bfs.has_path_to(target):
        dist = bfs.distance_to(target)
        print(f"0 → {target}: Distanz={dist}")
    else:
        print(f"0 → {target}: nicht erreichbar")
```

**Ausgabe:**
```
0 → 0: Distanz=0
0 → 1: Distanz=2
0 → 2: Distanz=1
0 → 3: Distanz=2
0 → 4: Distanz=1
0 → 5: Distanz=2
0 → 6: Distanz=1
0 → 7: Distanz=1
```

### 2.2 DFS - Beispiel mit tinyEWG.txt

```python
from src.algs4.pva_4_graphs import DFSPaths, EdgeWeightedGraph

# Graph aus Datei laden (Testdaten: 8 Knoten, 16 Kanten)
with open("data/graphs/tinyEWG.txt") as f:
    g = EdgeWeightedGraph(file=f)

# DFS von Knoten 0
dfs = DFSPaths(g, 0)

# Pfade abfragen
for target in range(g.V):
    if dfs.has_path_to(target):
        print(f"0 → {target}: erreichbar")
    else:
        print(f"0 → {target}: nicht erreichbar")
```

**Ausgabe:**
```
0 → 0: erreichbar
0 → 1: erreichbar
0 → 2: erreichbar
0 → 3: erreichbar
0 → 4: erreichbar
0 → 5: erreichbar
0 → 6: erreichbar
0 → 7: erreichbar
```

### 2.3 Topologische Sortierung - Beispiel mit tinyDAG.txt

```python
from src.algs4.pva_4_graphs import Topological, EdgeWeightedDigraph, DirectedEdge

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

if topo.has_order():
    order = list(topo.order())
    print(f"Topologische Ordnung: {order}")
else:
    print("Graph enthält Zyklus!")
```

**Ausgabe:**
```
Topologische Ordnung: [8, 7, 2, 3, 0, 6, 9, 10, 11, 12, 1, 5, 4]
```

---

## 3. Testdaten

| Datei | Knoten | Kanten | Format | Verwendung |
|-------|--------|--------|--------|-----------|
| **tinyEWG.txt** | 8 | 16 | Mit Gewichten | BFS/DFS Tests |
| **tinyDAG.txt** | 13 | 22 | Ohne Gewichte | Topologische Sortierung |
| **tinyEWDAG.txt** | 8 | 13 | Mit Gewichten | Alternative für Topo-Sort |

**Wichtig:** tinyDAG.txt hat **keine Gewichte**! Daher manuell laden oder tinyEWDAG.txt verwenden.

---

## 4. Häufige Fehler

- ❌ **Fehler 1**: Falsche Dateiformat für tinyDAG.txt
- ✅ **Lösung**: tinyDAG.txt hat **keine Gewichte**! Manuell laden oder tinyEWDAG.txt verwenden

- ❌ **Fehler 2**: Stack-Iteration mit None-Werten
- ✅ **Lösung**: Nicht direkt über Stack iterieren, sondern `has_path_to()` und `distance_to()` verwenden

- ❌ **Fehler 3**: Zyklen nicht prüfen → Crash bei Topologischer Sortierung
- ✅ **Lösung**: `topo.has_order()` prüfen, bevor `topo.order()` aufgerufen wird

---

## 5. Präsentations-Tipps

1. **Visualisierung**: Zeichne den Graphen an die Tafel
2. **Schritt-für-Schritt**: Zeige BFS/DFS Schritt für Schritt
3. **Live-Demo**: Führe Code mit Testdaten aus
4. **Vergleich**: BFS vs DFS Unterschiede erklären
5. **Anwendungen**: Praktische Beispiele nennen

---

## 6. Ressourcen

- **Buch**: Tobias Häberlein, "Praktische Algorithmik mit Python", Kapitel 5.2
- **Code**: `src/algs4/pva_4_graphs/bfs.py`, `dfs_paths.py`, `topological.py`
- **Tests**: `tests/test_graphs/test_bfs.py`, `test_dfs_paths.py`, `test_topological.py`
- **Daten**: `data/graphs/tinyEWG.txt`, `tinyDAG.txt`
