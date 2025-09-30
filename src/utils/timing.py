"""Timing-Utilities für Performance-Messungen.

Dieses Modul stellt Dekoratoren und Funktionen zur Zeitmessung bereit,
die zur Analyse der Performance von Algorithmen verwendet werden können.
"""

import functools
import time
from collections.abc import Callable
from typing import Any


def timeit(func: Callable) -> Callable:
    """Dekorator zur Zeitmessung von Funktionen.

    Misst die Ausführungszeit einer Funktion und gibt sie aus,
    wenn die globale Variable ENABLE_TIMING auf True gesetzt ist.

    Args:
        func: Die zu messende Funktion

    Returns:
        Die dekorierte Funktion

    Beispiel:
        ```python
        from src.utils import timeit

        # Globale Aktivierung der Zeitmessung
        import src.utils.timing
        src.utils.timing.ENABLE_TIMING = True

        @timeit
        def my_function():
            # Funktionslogik hier
            pass
        ```
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if globals().get('ENABLE_TIMING', False):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"{func.__name__} Laufzeit: {execution_time:.6f} Sekunden")
            return result
        else:
            return func(*args, **kwargs)
    return wrapper


# Globale Variable zur Steuerung der Zeitmessung
ENABLE_TIMING = False


def enable_timing() -> None:
    """Aktiviert die globale Zeitmessung für alle @timeit dekorierten Funktionen."""
    global ENABLE_TIMING
    ENABLE_TIMING = True


def disable_timing() -> None:
    """Deaktiviert die globale Zeitmessung für alle @timeit dekorierten Funktionen."""
    global ENABLE_TIMING
    ENABLE_TIMING = False


def measure_execution_time(func: Callable) -> tuple[Any, float]:
    """Misst die Ausführungszeit einer Funktion einmalig.

    Args:
        func: Die zu messende Funktion (ohne Parameter)

    Returns:
        Tuple aus (Funktionsergebnis, Ausführungszeit in Sekunden)

    Beispiel:
        ```python
        result, exec_time = measure_execution_time(lambda: sorted([3, 1, 4, 2]))
        print(f"Sortierung dauerte {exec_time:.6f} Sekunden")
        ```
    """
    start_time = time.perf_counter()
    result = func()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time
