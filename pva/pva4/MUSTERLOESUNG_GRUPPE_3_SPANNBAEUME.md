# Musterlösung: Gruppe 3 - Spannbäume (MST)

## 1. Grundkonzepte

### Minimum Spanning Tree (MST)
- **Definition**: Baum mit V-1 Kanten, der alle Knoten verbindet und minimales Gesamtgewicht hat
- **Eigenschaft**: Eindeutig, wenn alle Gewichte unterschiedlich sind
- **Anwendung**: Netzwerk-Design, Verkehrsplanung

### Kruskal's Algorithmus
- **Strategie**: Greedy - sortiere Kanten, füge hinzu wenn kein Zyklus
- **Datenstruktur**: Union-Find
- **Komplexität**: O(E log E)
- **Beste für**: Dünne Graphen

### Prim's Algorithmus
- **Strategie**: Greedy - erweitere Baum um leichteste Kante
- **Datenstruktur**: Priority Queue
- **Komplexität**: O((V + E) log V)
- **Beste für**: Dichte Graphen

---

## 2. Implementierungen

### 2.1 Kruskal - Beispiel mit tinyEWG.txt

```python
from src.algs4.pva_4_graphs import KruskalMST, EdgeWeightedGraph

# Graph aus Datei laden (Testdaten: 8 Knoten, 16 Kanten)
with open("data/graphs/tinyEWG.txt") as f:
    g = EdgeWeightedGraph(file=f)

# Kruskal MST
mst = KruskalMST(g)

print(f"MST-Gewicht: {mst.weight():.2f}")
print("MST-Kanten:")
for edge in mst.edges():
    v = edge.either()
    w = edge.other(v)
    print(f"  {v}-{w}: {edge.weight:.2f}")
```

**Ausgabe:**
```
MST-Gewicht: 1.81
MST-Kanten:
  0-2: 0.26
  2-3: 0.17
  4-5: 0.35
  5-7: 0.28
  0-7: 0.16
  1-7: 0.19
  6-2: 0.40
```

### 2.2 Prim - Beispiel mit tinyEWG.txt

```python
from src.algs4.pva_4_graphs import PrimMST, EdgeWeightedGraph

# Graph aus Datei laden
with open("data/graphs/tinyEWG.txt") as f:
    g = EdgeWeightedGraph(file=f)

# Prim MST
mst = PrimMST(g)

print(f"MST-Gewicht: {mst.weight():.2f}")
print("MST-Kanten:")
for edge in mst.edges():
    v = edge.either()
    w = edge.other(v)
    print(f"  {v}-{w}: {edge.weight:.2f}")
```

---

## 3. Vergleich: Kruskal vs. Prim

| Aspekt | Kruskal | Prim |
|--------|---------|------|
| **Sortierung** | Alle Kanten | Keine |
| **Datenstruktur** | Union-Find | Priority Queue |
| **Komplexität** | O(E log E) | O((V+E)log V) |
| **Beste für** | Dünne Graphen | Dichte Graphen |
| **Parallelisierbar** | Ja | Schwierig |

---

## 4. Testdaten

| Datei | Knoten | Kanten | Format | Verwendung |
|-------|--------|--------|--------|-----------|
| **tinyEWG.txt** | 8 | 16 | Mit Gewichten | Basis-Tests |
| **mediumEWG.txt** | 250 | ~1000 | Mit Gewichten | Performance-Tests |
| **largeEWG.txt** | 1000+ | ~10000 | Mit Gewichten | Benchmark |

## 5. Häufige Fehler

- ❌ **Fehler 1**: Zyklenerkennung vergessen
- ✅ **Lösung**: Union-Find (Kruskal) oder Marked-Array (Prim) verwenden

- ❌ **Fehler 2**: Gewichte falsch addieren
- ✅ **Lösung**: Alle Kanten des MST addieren

- ❌ **Fehler 3**: Falsche Datenstruktur wählen
- ✅ **Lösung**: Kruskal für dünne, Prim für dichte Graphen

## 6. Präsentations-Tipps

1. **Algorithmen erklären** (4 Min)
   - Kruskal: Sortierung + Union-Find
   - Prim: Priority Queue

2. **Live-Demo** (3-4 Min)
   - Beide Algorithmen ausführen
   - Gleiche MST-Gewichte zeigen

3. **Vergleich** (2 Min)
   - Komplexität
   - Beste Anwendungsfälle

4. **Fragen beantworten** (1-2 Min)

## 7. Ressourcen

- **Buch**: Tobias Häberlein, "Praktische Algorithmik mit Python", Kapitel 5.3
- **Code**: `src/algs4/pva_4_graphs/kruskal_mst.py`, `prim_mst.py`
- **Tests**: `tests/test_graphs/test_kruskal_mst.py`, `test_prim_mst.py`
- **Daten**: `data/graphs/tinyEWG.txt`
