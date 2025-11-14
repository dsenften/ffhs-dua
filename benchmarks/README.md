# Benchmarks für ffhs-dua

Performance-Benchmarks für Algorithmen und Datenstrukturen.

## Schnellstart

```bash
# Sortieralgorithmen-Benchmarks ausführen
python3 benchmarks/sorting_benchmarks.py
```

## Verfügbare Benchmarks

### Sortieralgorithmen (`sorting_benchmarks.py`)

Misst die Performance verschiedener Sortieralgorithmen unter verschiedenen Bedingungen.

**Getestete Algorithmen:**
- Shell Sort
- Quick Sort
- Merge Sort
- Heap Sort

**Testdatentypen:**
- `random` - Zufällig generierte Daten
- `sorted` - Bereits sortierte Daten
- `reverse` - Umgekehrt sortierte Daten
- `nearly_sorted` - Fast sortierte Daten (5% Abweichung)

**Datengrößen:**
- 100 Elemente
- 1.000 Elemente
- 10.000 Elemente

### Beispiel-Output

```
Shell Sort - random (100 Elemente): 0.0001s
Shell Sort - sorted (100 Elemente): 0.0000s
Shell Sort - reverse (100 Elemente): 0.0001s
Shell Sort - nearly_sorted (100 Elemente): 0.0001s
...
```

## Benchmark-Funktionen

### `generate_test_data(size, data_type)`

Generiert Testdaten für Benchmarks.

**Parameter:**
- `size` (int): Anzahl der Elemente
- `data_type` (str): Typ der Daten ('random', 'sorted', 'reverse', 'nearly_sorted')

**Rückgabe:**
- `list[int]`: Generierte Testdaten

### `benchmark_algorithm(algorithm, data)`

Misst die Ausführungszeit eines Algorithmus.

**Parameter:**
- `algorithm` (Callable): Sortieralgorithmus-Funktion
- `data` (list[int]): Zu sortierende Daten

**Rückgabe:**
- `float`: Ausführungszeit in Sekunden

### `run_sorting_benchmarks()`

Führt umfassende Benchmarks für alle Sortieralgorithmen durch.

**Rückgabe:**
- `dict[str, dict[str, float]]`: Benchmark-Ergebnisse

## Verwendungsbeispiele

### Einfacher Benchmark

```python
from benchmarks.sorting_benchmarks import benchmark_algorithm, generate_test_data
from src.algs4.pva_2_sorting.quick import quick_sort

# Testdaten generieren
data = generate_test_data(10000, "random")

# Benchmark ausführen
execution_time = benchmark_algorithm(quick_sort, data)
print(f"Quick Sort: {execution_time:.4f}s")
```

### Mehrere Algorithmen vergleichen

```python
from benchmarks.sorting_benchmarks import benchmark_algorithm, generate_test_data
from src.algs4.pva_2_sorting.quick import quick_sort
from src.algs4.pva_2_sorting.merge import merge_sort
from src.algs4.pva_2_sorting.heap import heap_sort

algorithms = {
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
}

data = generate_test_data(10000, "random")

for name, algo in algorithms.items():
    time = benchmark_algorithm(algo, data)
    print(f"{name}: {time:.4f}s")
```

### Verschiedene Datentypen testen

```python
from benchmarks.sorting_benchmarks import benchmark_algorithm, generate_test_data
from src.algs4.pva_2_sorting.quick import quick_sort

data_types = ["random", "sorted", "reverse", "nearly_sorted"]

for dtype in data_types:
    data = generate_test_data(10000, dtype)
    time = benchmark_algorithm(quick_sort, data)
    print(f"Quick Sort ({dtype}): {time:.4f}s")
```

## Performance-Charakteristiken

### Sortieralgorithmen

| Algorithmus | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| Shell Sort | O(n) | O(n^(3/2)) | O(n^(3/2)) | O(1) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

## Tipps für aussagekräftige Benchmarks

1. **Mehrfache Durchläufe**: Führen Sie jeden Benchmark mehrfach aus
2. **Warme Umgebung**: Lassen Sie Python den Code vor dem Messen kompilieren
3. **Isolierte Umgebung**: Schließen Sie andere Anwendungen
4. **Realistische Daten**: Verwenden Sie Testdaten, die realen Szenarien ähneln
5. **Dokumentation**: Notieren Sie die Umgebung und Bedingungen

## Erweiterung

Um neue Benchmarks hinzuzufügen:

1. Erstellen Sie eine neue Funktion in `sorting_benchmarks.py`
2. Verwenden Sie `generate_test_data()` für konsistente Testdaten
3. Verwenden Sie `benchmark_algorithm()` für konsistente Zeitmessung
4. Dokumentieren Sie die erwarteten Ergebnisse

## Weitere Informationen

Siehe `docs/benchmarks.md` für detaillierte Dokumentation.
