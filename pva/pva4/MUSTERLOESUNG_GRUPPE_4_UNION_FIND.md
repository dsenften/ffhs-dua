# Musterlösung: Gruppe 4 - Union-Find (Disjoint Set Union)

## 1. Grundkonzepte

### Union-Find Datenstruktur
- **Zweck**: Verwaltet disjunkte Mengen (Äquivalenzklassen)
- **Operationen**: `find()`, `union()`, `connected()`
- **Komplexität**: O(α(n)) amortisiert mit Optimierungen (α = inverse Ackermann)
- **Anwendung**: Zyklenerkennung, Kruskal's Algorithmus, Äquivalenzklassen

### Implementierungsvarianten

| Variante | find() | union() | Bemerkung |
|----------|--------|---------|-----------|
| **Quick Find** | O(1) | O(n) | Schlecht für viele Unions |
| **Quick Union** | O(n) | O(n) | Besser, aber noch nicht optimal |
| **Weighted Quick Union** | O(log n) | O(log n) | Gute Balance |
| **WQU + Path Compression** | O(α(n)) | O(α(n)) | Praktisch konstant! |

### Optimierungen

**Path Compression**: Komprimiere Pfade während find()
```python
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])  # Komprimiere Pfad
    return parent[x]
```

**Union by Rank**: Verbinde kleinere Bäume unter größere
```python
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
```

---

## 2. Implementierungen

### 2.1 Union-Find Grundoperationen

```python
from src.algs4.pva_1_fundamentals import UF

# Union-Find mit 10 Elementen
uf = UF(10)

# Unions durchführen
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)
uf.union(4, 5)

# Verbindungen prüfen
print(uf.connected(0, 2))  # True
print(uf.connected(0, 3))  # False
print(uf.count())  # 7 Komponenten
```

### 2.2 Union-Find in Kruskal

```python
from src.algs4.pva_4_graphs import KruskalMST, EdgeWeightedGraph

# Graph laden
with open("data/graphs/tinyEWG.txt") as f:
    g = EdgeWeightedGraph(file=f)

# Kruskal nutzt Union-Find intern
mst = KruskalMST(g)

print(f"MST-Gewicht: {mst.weight():.2f}")
```

---

## 3. Testdaten

| Datei | Knoten | Kanten | Verwendung |
|-------|--------|--------|-----------|
| **tinyEWG.txt** | 8 | 16 | Basis-Tests |
| **mediumEWG.txt** | 250 | ~1000 | Performance-Tests |
| **largeEWG.txt** | 1000+ | ~10000 | Benchmark |

## 4. Häufige Fehler

- ❌ **Fehler 1**: Path Compression vergessen
- ✅ **Lösung**: Komprimiere Pfade in find() für bessere Performance

- ❌ **Fehler 2**: Union by Rank nicht implementiert
- ✅ **Lösung**: Verbinde kleinere Bäume unter größere

- ❌ **Fehler 3**: Zyklenerkennung falsch
- ✅ **Lösung**: Prüfe `connected()` vor `union()`

## 5. Anwendungen

### Zyklenerkennung
```python
def has_cycle(edges, V):
    uf = UF(V)
    for v, w in edges:
        if uf.connected(v, w):
            return True  # Zyklus gefunden
        uf.union(v, w)
    return False
```

### Äquivalenzklassen
```python
uf = UF(n)
# Vereinige äquivalente Elemente
for x, y in equivalences:
    uf.union(x, y)

# Finde Äquivalenzklassen
classes = {}
for i in range(n):
    root = uf.find(i)
    if root not in classes:
        classes[root] = []
    classes[root].append(i)
```

## 6. Präsentations-Tipps

1. **Union-Find erklären** (2-3 Min)
   - Grundkonzept
   - Operationen

2. **Varianten vergleichen** (2 Min)
   - Komplexität
   - Trade-offs

3. **Live-Demo** (3-4 Min)
   - Grundoperationen
   - Integration in Kruskal

4. **Performance-Ergebnisse** (2 Min)
   - Unterschied zwischen Varianten

5. **Fragen beantworten** (1-2 Min)

## 7. Ressourcen

- **Buch**: Tobias Häberlein, "Praktische Algorithmik mit Python", Kapitel 1.5
- **Code**: `src/algs4/pva_1_fundamentals/uf.py`
- **Tests**: `tests/test_fundamentals/test_uf.py`
- **Daten**: `data/graphs/tinyEWG.txt`
