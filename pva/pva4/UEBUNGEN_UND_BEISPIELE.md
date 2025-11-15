# PVA 4 - Übungen und Beispiele

## 📚 Empfohlene Übungen aus Literatur

### Abschnitt 5.1 - Graphen und Repräsentation
- **Aufgabe 5.1-5.5**: Graphen-Repräsentation
  - Adjazenzmatrix vs. Adjazenzlisten
  - Dichte vs. spärliche Graphen
  - Speicherverbrauch

### Abschnitt 5.2 - Traversierung
- **Aufgabe 5.6-5.15**: DFS und BFS
  - Pfadfindung
  - Zusammenhängende Komponenten
  - Zykluserkennung

### Abschnitt 5.3 - Kürzeste Pfade
- **Aufgabe 5.16-5.25**: Dijkstra und Bellman-Ford
  - Kürzeste Pfade berechnen
  - Negative Gewichte
  - Komplexitätsanalyse

### Abschnitt 5.4 - Spannbäume
- **Aufgabe 5.26-5.30**: Kruskal und Prim
  - MST berechnen
  - Gewichte vergleichen
  - Anwendungen

## 💻 Praktische Übungen

### Übung 1: Graphen-Repräsentation
```python
# Erstelle einen Graphen und vergleiche Repräsentationen
from src.algs4.pva_4_graphs import EdgeWeightedGraph, Edge

g = EdgeWeightedGraph(5)
# Füge Kanten hinzu und analysiere Speicherverbrauch
```

### Übung 2: Pfadfindung
```python
# Finde Pfade zwischen Knoten
from src.algs4.pva_4_graphs import DijkstraSP, EdgeWeightedDigraph

# Berechne kürzeste Pfade
# Vergleiche mit BFS für ungewichtete Graphen
```

### Übung 3: MST-Berechnung
```python
# Berechne Minimum Spanning Tree
from src.algs4.pva_4_graphs import KruskalMST, PrimMST

# Vergleiche Kruskal vs. Prim
# Analysiere Komplexität
```

### Übung 4: Topologische Sortierung
```python
# Sortiere DAG topologisch
from src.algs4.pva_4_graphs import TopologicalSort

# Finde Abhängigkeitsordnung
# Erkenne Zyklen
```

## 🎯 Lernziele pro Übung

| Übung | Lernziel | Algorithmus |
|-------|----------|-------------|
| 1 | Graphen-Repräsentation verstehen | - |
| 2 | Pfadfindung implementieren | BFS, Dijkstra |
| 3 | MST-Algorithmen vergleichen | Kruskal, Prim |
| 4 | DAG-Verarbeitung | Topologische Sortierung |
| 5 | Komplexitätsanalyse | Alle |

## 📊 Testdaten

### Kleine Graphen (für Debugging)
- `data/graphs/tinyEWG.txt` - 8 Knoten, 16 Kanten
- `data/graphs/tinyEWD.txt` - 8 Knoten, 15 Kanten
- `data/graphs/tinyDAG.txt` - 13 Knoten, DAG

### Mittlere Graphen (für Performance-Tests)
- `data/graphs/mediumEWG.txt` - 250 Knoten
- `data/graphs/mediumDG.txt` - 250 Knoten

## 🔗 Externe Ressourcen

- **Algs4 Website**: https://algs4.cs.princeton.edu/
- **Visualisierungen**: https://www.cs.usfca.edu/~galles/visualization/
- **Komplexitätsanalyse**: https://en.wikipedia.org/wiki/Analysis_of_algorithms
