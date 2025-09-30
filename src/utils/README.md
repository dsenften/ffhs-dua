# Utils Module

Dieses Modul enthält wiederverwendbare Hilfsfunktionen und Dekoratoren für das FFHS DUA Projekt.

## Timing Utilities (`timing.py`)

### `@timeit` Dekorator

Ein flexibler Dekorator zur Zeitmessung von Funktionen.

#### Verwendung

```python
from src.utils import timeit
import src.utils.timing

# Aktiviere Zeitmessung global
src.utils.timing.ENABLE_TIMING = True

@timeit
def my_sorting_function(arr):
    # Sortierlogik hier
    return sorted(arr)

# Funktionsaufruf mit automatischer Zeitmessung
result = my_sorting_function([3, 1, 4, 2])
# Ausgabe: my_sorting_function Laufzeit: 0.000012 Sekunden
```

#### Mit Classmethods

```python
class MySorter:
    @classmethod
    @timeit
    def sort(cls, arr):
        return sorted(arr)

# Aktiviere Zeitmessung
src.utils.timing.enable_timing()
result = MySorter.sort([3, 1, 4, 2])
```

### Hilfsfunktionen

#### `enable_timing()` / `disable_timing()`

```python
from src.utils.timing import enable_timing, disable_timing

# Aktiviere Zeitmessung für alle @timeit dekorierten Funktionen
enable_timing()

# Deaktiviere Zeitmessung
disable_timing()
```

#### `measure_execution_time()`

Für einmalige Zeitmessungen ohne Dekorator:

```python
from src.utils.timing import measure_execution_time

result, exec_time = measure_execution_time(lambda: sorted([3, 1, 4, 2]))
print(f"Sortierung dauerte {exec_time:.6f} Sekunden")
```

## Beispiele in Sortieralgorithmen

### MergeSort mit Zeitmessung

```bash
# Mit Zeitmessung und Array-Ausgabe
echo "5 2 8 1 9 3" | uv run src/algs4/sorting/merge.py --timing

# Nur Zeitmessung (ohne Arrays)
echo "5 2 8 1 9 3" | uv run src/algs4/sorting/merge.py --timing --quiet
```

### HeapSort mit Zeitmessung

```bash
# Mit Zeitmessung und Array-Ausgabe
echo "5 2 8 1 9 3" | uv run src/algs4/sorting/heap.py --timing

# Nur Zeitmessung (ohne Arrays)
echo "5 2 8 1 9 3" | uv run src/algs4/sorting/heap.py --timing --quiet
```

## Tests

Das Modul ist vollständig getestet:

```bash
# Alle Utils-Tests ausführen
uv run python -m pytest tests/test_utils/ -v

# Nur Timing-Tests
uv run python -m pytest tests/test_utils/test_timing.py -v
```

## Erweiterung

Das `utils` Modul kann einfach um weitere Hilfsfunktionen erweitert werden:

1. Neue Datei in `src/utils/` erstellen
2. Funktionen in `src/utils/__init__.py` exportieren
3. Tests in `tests/test_utils/` hinzufügen

Beispiel für neue Utility:

```python
# src/utils/validation.py
def is_sorted(arr):
    """Prüft, ob ein Array sortiert ist."""
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# src/utils/__init__.py
from .timing import timeit
from .validation import is_sorted

__all__ = ["timeit", "is_sorted"]
```
