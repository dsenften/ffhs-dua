# Benchmarks für ffhs-dua

Dieses Dokument beschreibt die Performance-Benchmarks für die Algorithmen und Datenstrukturen im ffhs-dua Projekt.

## Überblick

Die Benchmarks messen die Ausführungszeit verschiedener Algorithmen unter verschiedenen Bedingungen:
- **Verschiedene Datengrößen**: 100, 1.000, 10.000 Elemente
- **Verschiedene Datentypen**: Zufällig, sortiert, umgekehrt, fast sortiert
- **Verschiedene Algorithmen**: Shell Sort, Quick Sort, Merge Sort, Heap Sort

## Sortieralgorithmen-Benchmarks

### Verfügbare Benchmarks

Die Sortieralgorithmen-Benchmarks befinden sich in `benchmarks/sorting_benchmarks.py`.

#### Getestete Algorithmen

1. **Shell Sort** - Inkrementelle Sortierung mit Knuth-Sequenz
   - Durchschnittliche Komplexität: O(n^(3/2))
   - Worst-Case: O(n^(3/2))
   - Space: O(1)
   - **Testdaten**: Alle Typen (random, sorted, reverse, nearly_sorted)
   - **Datengrößen**: 100, 1.000, 10.000 Elemente

2. **Quick Sort** - Divide-and-Conquer mit Hoare-Partitionierung
   - Durchschnittliche Komplexität: O(n log n)
   - Worst-Case: O(n²) bei sortierten/umgekehrten Daten
   - Space: O(log n)
   - **Testdaten**: Nur random und nearly_sorted (Worst-Case Schutz)
   - **Datengrößen**: 100, 1.000, 5.000 Elemente (kleinere Mengen wegen Worst-Case)

3. **Merge Sort** - Stabile Sortierung
   - Durchschnittliche Komplexität: O(n log n)
   - Worst-Case: O(n log n)
   - Space: O(n)
   - **Testdaten**: Alle Typen (random, sorted, reverse, nearly_sorted)
   - **Datengrößen**: 100, 1.000, 10.000 Elemente

4. **Heap Sort** - Heap-basierte Sortierung
   - Durchschnittliche Komplexität: O(n log n)
   - Worst-Case: O(n log n)
   - Space: O(1)
   - **Testdaten**: Alle Typen (random, sorted, reverse, nearly_sorted)
   - **Datengrößen**: 100, 1.000, 10.000 Elemente

#### Testdatentypen

- **random**: Zufällig generierte Daten
- **sorted**: Bereits sortierte Daten (Best-Case)
- **reverse**: Umgekehrt sortierte Daten (Worst-Case für viele Algorithmen)
- **nearly_sorted**: Fast sortierte Daten (5% der Elemente vertauscht)

### Ausführung der Benchmarks

```bash
# Sortieralgorithmen-Benchmarks ausführen
python3 benchmarks/sorting_benchmarks.py

# Mit Timing-Dekorator
python3 -c "
from benchmarks.sorting_benchmarks import run_sorting_benchmarks
results = run_sorting_benchmarks()
"
```

### Erwartete Ergebnisse

#### Typische Performance-Charakteristiken (macOS, Python 3.13)

**Bei 10.000 Elementen (zufällig):**
- Shell Sort: ~0.014-0.019s
- Merge Sort: ~0.010-0.011s
- Heap Sort: ~0.013-0.015s
- Quick Sort: Nicht getestet (Worst-Case Schutz)

**Bei 10.000 Elementen (sortiert):**
- Shell Sort: ~0.003-0.004s (sehr schnell)
- Merge Sort: ~0.009-0.010s (konstant)
- Heap Sort: ~0.014-0.015s (konstant)
- Quick Sort: Nicht getestet (würde O(n²) auslösen)

**Bei 10.000 Elementen (umgekehrt):**
- Shell Sort: ~0.006-0.007s
- Merge Sort: ~0.009-0.010s (konstant)
- Heap Sort: ~0.012-0.014s (konstant)
- Quick Sort: Nicht getestet (würde O(n²) auslösen)

**Bei 5.000 Elementen (zufällig) - Quick Sort:**
- Quick Sort: ~0.004-0.005s

**Bei 5.000 Elementen (nearly_sorted) - Quick Sort:**
- Quick Sort: ~0.015-0.020s (Worst-Case näher)

## Datenstruktur-Performance

### Union-Find (Disjoint Set Union)

Die Union-Find Implementierungen haben unterschiedliche Performance-Charakteristiken:

| Implementierung | Find | Union | Bemerkung |
|---|---|---|---|
| QuickFindUF | O(1) | O(n) | Schnelles Find, langsames Union |
| QuickUnionUF | O(n) | O(n) | Einfach, aber langsam |
| WeightedQuickUnionUF | O(log n) | O(log n) | Gewichtet nach Größe |
| UF (Optimiert) | O(α(n)) | O(α(n)) | Mit Path Compression & Rank |

### Suchbäume

| Datenstruktur | Get | Put | Delete | Bemerkung |
|---|---|---|---|---|
| BST | O(log n) avg | O(log n) avg | O(log n) avg | Unbalanciert, kann O(n) sein |
| AVL Tree | O(log n) | O(log n) | O(log n) | Garantiert balanciert |
| Red-Black BST | O(log n) | O(log n) | O(log n) | Garantiert balanciert |

### Hash Tables

| Implementierung | Get | Put | Delete | Bemerkung |
|---|---|---|---|---|
| Separate Chaining | O(1) avg | O(1) avg | O(1) avg | Mit Load Factor ≤ 10 |
| Linear Probing | O(1) avg | O(1) avg | O(1) avg | Mit Load Factor ≤ 0.5 |

## Benchmark-Infrastruktur

### Timing-Utilities

Das Projekt bietet Timing-Utilities in `src/utils/timing.py`:

```python
from src.utils.timing import timeit, measure_execution_time

# Dekorator-basierte Zeitmessung
@timeit
def my_algorithm():
    pass

# Einmalige Zeitmessung
result, exec_time = measure_execution_time(lambda: sorted([3, 1, 4, 2]))
print(f"Execution time: {exec_time:.4f}s")
```

### Benchmark-Struktur

```
benchmarks/
├── sorting_benchmarks.py      # Sortieralgorithmen-Benchmarks
├── __init__.py                # Package-Initialisierung
└── README.md                  # Benchmark-Dokumentation
```

## Best Practices für Benchmarking

1. **Mehrfache Durchläufe**: Führen Sie Benchmarks mehrfach aus, um Variabilität zu reduzieren
2. **Warme JVM**: Lassen Sie Python den Code vor dem Messen kompilieren
3. **Isolierte Umgebung**: Führen Sie Benchmarks in einer ruhigen Umgebung aus
4. **Realistische Daten**: Verwenden Sie Testdaten, die realen Szenarien ähneln
5. **Dokumentation**: Dokumentieren Sie die Umgebung und Bedingungen

## Erweiterung der Benchmarks

Um neue Benchmarks hinzuzufügen:

1. Erstellen Sie eine neue Benchmark-Funktion in `benchmarks/sorting_benchmarks.py`
2. Verwenden Sie `generate_test_data()` für konsistente Testdaten
3. Verwenden Sie `benchmark_algorithm()` für konsistente Zeitmessung
4. Dokumentieren Sie die erwarteten Ergebnisse

Beispiel:

```python
def benchmark_new_algorithm():
    """Benchmark für neuen Algorithmus."""
    from src.algs4.pva_2_sorting.new_sort import new_sort

    algorithms = {"New Sort": new_sort}
    # ... Rest der Implementierung
```

## Weitere Ressourcen

- [Algorithms, 4th Edition - Performance Analysis](https://algs4.cs.princeton.edu/14analysis/)
- [Python Timing Best Practices](https://docs.python.org/3/library/timeit.html)
- [Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation)
