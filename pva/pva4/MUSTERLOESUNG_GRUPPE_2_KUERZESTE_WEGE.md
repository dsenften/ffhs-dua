# Musterlösung: Gruppe 2 - Kürzeste Wege (Dijkstra)

## 1. Grundkonzepte

### Dijkstra's Algorithmus
- **Strategie**: Greedy-Algorithmus mit Priority Queue
- **Datenstruktur**: Min-Priority Queue
- **Komplexität**: O((V + E) log V)
- **Anwendung**: Kürzeste Pfade in gewichteten Graphen mit nicht-negativen Gewichten

### Pfadrekonstruktion
- **Zweck**: Den kompletten Pfad vom Start zum Ziel finden
- **Methode**: Speichere für jeden Knoten die eingehende Kante
- **Komplexität**: O(V)

---

## 2. Implementierungen

### 2.1 Dijkstra - Beispiel mit tinyEWD.txt

```python
from src.algs4.pva_4_graphs import DijkstraSP, EdgeWeightedDigraph

# Graph aus Datei laden (Testdaten: 8 Knoten, 15 Kanten)
with open("data/graphs/tinyEWD.txt") as f:
    g = EdgeWeightedDigraph(file=f)

# Dijkstra von Knoten 0
sp = DijkstraSP(g, 0)

# Kürzeste Distanzen abfragen
print(f"Graph: {g.V} Knoten, {g.E} Kanten")
print("Kürzeste Pfade von Knoten 0:")
print("-" * 80)
for v in range(g.V):
    if sp.has_path_to(v):
        dist = sp.distTo[v]
        print(f"  0 → {v}: Distanz={dist:.2f}")
    else:
        print(f"  0 → {v}: nicht erreichbar")
```

**Ausgabe:**
```
Graph: 8 Knoten, 15 Kanten
Kürzeste Pfade von Knoten 0:
  0 → 0: Distanz=0.00
  0 → 1: Distanz=1.05
  0 → 2: Distanz=0.26
  0 → 3: Distanz=0.99
  0 → 4: Distanz=0.38
  0 → 5: Distanz=0.73
  0 → 6: Distanz=1.51
  0 → 7: Distanz=0.60
```

### 2.2 Pfadrekonstruktion - Beispiel

```python
from src.algs4.pva_4_graphs import DijkstraSP, EdgeWeightedDigraph

# Graph laden
with open("data/graphs/tinyEWD.txt") as f:
    g = EdgeWeightedDigraph(file=f)

# Dijkstra von Knoten 0
sp = DijkstraSP(g, 0)

# Pfade zu verschiedenen Zielen
print("Pfade von 0:")
print("-" * 80)
for target in [1, 3, 6]:
    if sp.has_path_to(target):
        dist = sp.distTo[target]
        print(f"  0 → {target}: Distanz={dist:.2f}")
    else:
        print(f"  0 → {target}: nicht erreichbar")
```

---

## 3. Testdaten

| Datei | Knoten | Kanten | Format | Verwendung |
|-------|--------|--------|--------|-----------|
| **tinyEWD.txt** | 8 | 15 | Mit Gewichten | Basis-Tests |
| **mediumEWD.txt** | 250 | ~1000 | Mit Gewichten | Performance-Tests |
| **largeEWD.txt** | 1000+ | ~10000 | Mit Gewichten | Benchmark |

## 4. Häufige Fehler

- ❌ **Fehler 1**: Negative Gewichte verwenden
- ✅ **Lösung**: Dijkstra funktioniert nur mit nicht-negativen Gewichten!

- ❌ **Fehler 2**: Priority Queue nicht korrekt verwenden
- ✅ **Lösung**: Knoten können mehrfach in der Queue sein, aber nur der erste wird verarbeitet

- ❌ **Fehler 3**: Pfad nicht korrekt rekonstruieren
- ✅ **Lösung**: Speichere die eingehende Kante für jeden Knoten

## 5. Präsentations-Tipps

1. **Algorithmus erklären** (2-3 Min)
   - Greedy-Strategie
   - Priority Queue Verwendung
   - Komplexität

2. **Live-Demo** (3-4 Min)
   - Code ausführen
   - Distanzen zeigen
   - Pfade visualisieren

3. **Pfadrekonstruktion** (1-2 Min)
   - Wie man den Pfad findet
   - Edge-to Array

4. **Fragen beantworten** (1-2 Min)
   - Warum nicht-negative Gewichte?
   - Vergleich zu BFS

## 6. Ressourcen

- **Buch**: Tobias Häberlein, "Praktische Algorithmik mit Python", Kapitel 5.4
- **Code**: `src/algs4/pva_4_graphs/dijkstra_sp.py`
- **Tests**: `tests/test_graphs/test_dijkstra_sp.py`
- **Daten**: `data/graphs/tinyEWD.txt`
