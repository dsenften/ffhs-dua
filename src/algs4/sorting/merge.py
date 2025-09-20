"""Merge Sort Implementierung.

Diese Klasse implementiert den Merge-Sort-Algorithmus, einen effizienten
Divide-and-Conquer-Sortieralgorithmus mit garantierter O(n log n) Zeitkomplexität.

Beispiele:
    % more tiny.txt
    S O R T E X A M P L E

    % python merge.py < tiny.txt
    A E E L M O P R S T X                 [ one string per line ]

    % more words3.txt
    bed bug dad yes zoo ... all bad yet

    % python merge.py < words3.txt
    all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Merge:
    """Merge-Sort-Implementierung.

    Diese Klasse bietet Methoden zum Sortieren von Listen mit dem Merge-Sort-Algorithmus
    und zum Überprüfen, ob eine Liste sortiert ist. Merge Sort ist ein stabiler
    Sortieralgorithmus mit garantierter O(n log n) Zeitkomplexität.
    """

    @classmethod
    def merge(cls, arr: list, lo: int, mid: int, hi: int) -> None:
        """Führt zwei sortierte Teilarrays zu einem sortierten Array zusammen.

        Diese Methode implementiert den Merge-Schritt des Merge-Sort-Algorithmus.
        Sie nimmt zwei sortierte Teilarrays arr[lo..mid] und arr[mid+1..hi]
        und führt sie zu einem sortierten Array arr[lo..hi] zusammen.

        Args:
            arr: Das Array, das die zu verschmelzenden Teilarrays enthält
            lo: Der untere Index des ersten Teilarrays
            mid: Der obere Index des ersten Teilarrays
            hi: Der obere Index des zweiten Teilarrays

        Returns:
            None: Modifiziert das Array in-place
        """
        # Erstelle eine Kopie des Arrays für den Merge-Prozess
        aux = arr[lo : hi + 1]

        # Initialisiere Zeiger für die beiden Teilarrays
        i = 0  # Zeiger für das erste Teilarray (aux[0..mid-lo])
        j = mid - lo + 1  # Zeiger für das zweite Teilarray (aux[mid-lo+1..hi-lo])

        # Führe die beiden sortierten Teilarrays zusammen
        for k in range(lo, hi + 1):
            if i > mid - lo:
                # Erstes Teilarray ist erschöpft, nimm vom zweiten
                arr[k] = aux[j]
                j += 1
            elif j > hi - lo:
                # Zweites Teilarray ist erschöpft, nimm vom ersten
                arr[k] = aux[i]
                i += 1
            elif aux[i] <= aux[j]:
                # Element aus erstem Teilarray ist kleiner oder gleich
                # Bei Gleichheit nehmen wir aus dem ersten Array (Stabilität)
                arr[k] = aux[i]
                i += 1
            else:
                # Element aus zweitem Teilarray ist kleiner
                arr[k] = aux[j]
                j += 1

    @classmethod
    def mergesort(cls, arr: list, lo: int, hi: int) -> list:
        """Sortiert ein Teilarray rekursiv mit dem Merge-Sort-Algorithmus.

        Diese Methode implementiert den rekursiven Teil des Merge-Sort-Algorithmus.
        Sie teilt das Array in zwei Hälften, sortiert beide rekursiv und
        führt sie dann zusammen.

        Args:
            arr: Die zu sortierende Liste
            lo: Der untere Index des zu sortierenden Bereichs
            hi: Der obere Index des zu sortierenden Bereichs

        Returns:
            Die sortierte Liste (in-place modifiziert)
        """
        # Basisfall: Array mit 0 oder 1 Element ist bereits sortiert
        if lo >= hi:
            return arr

        # Teile das Array in der Mitte
        mid = lo + (hi - lo) // 2

        # Sortiere rekursiv beide Hälften
        cls.mergesort(arr, lo, mid)  # Sortiere erste Hälfte
        cls.mergesort(arr, mid + 1, hi)  # Sortiere zweite Hälfte

        # Führe die beiden sortierten Hälften zusammen
        cls.merge(arr, lo, mid, hi)

        return arr

    @classmethod
    def sort(cls, arr: list) -> list:
        """Sortiert eine Liste mit dem Merge-Sort-Algorithmus.

        Args:
            arr: Die zu sortierende Liste

        Returns:
            Die sortierte Liste (in-place modifiziert)

        Zeitkomplexität:
            - Best Case: O(n log n)
            - Average Case: O(n log n)
            - Worst Case: O(n log n)

        Speicherkomplexität: O(n) - benötigt zusätzlichen Speicher für Hilfarray

        Eigenschaften:
            - Stabil: Gleiche Elemente behalten ihre relative Reihenfolge
            - Nicht in-place: Benötigt zusätzlichen Speicher
            - Divide-and-Conquer: Teilt das Problem rekursiv auf
        """
        if not arr:
            return arr

        return cls.mergesort(arr, 0, len(arr) - 1)

    @classmethod
    def is_sorted(cls, arr: list) -> bool:
        """Überprüft, ob eine Liste sortiert ist.

        Args:
            arr: Die zu überprüfende Liste

        Returns:
            True, wenn die Liste sortiert ist, sonst False

        Zeitkomplexität: O(n)
        """
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True


if __name__ == "__main__":
    import sys

    # Lese Eingabe von stdin und erstelle eine Liste von Elementen
    items = []
    for line in sys.stdin:
        items.extend(line.split())

    # Zeige die ursprüngliche und sortierte Liste an
    print("     items: ", items)
    print("sort items: ", Merge.sort(items))

    # Überprüfe, ob die Liste korrekt sortiert wurde
    assert Merge.is_sorted(items)
