"""Quick Sort Implementierung.

Diese Klasse implementiert den Quick-Sort-Algorithmus, einen effizienten
Divide-and-Conquer-Sortieralgorithmus mit durchschnittlicher Zeitkomplexität O(n log n).

Beispiele:
    % more tiny.txt
    S O R T E X A M P L E

    % python quick.py < tiny.txt
    A E E L M O P R S T X                 [ one string per line ]

    % more words3.txt
    bed bug dad yes zoo ... all bad yet

    % python quick.py < words3.txt
    all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Quick:
    """Quick-Sort-Implementierung.

    Diese Klasse bietet Methoden zum Sortieren von Listen mit dem Quick-Sort-Algorithmus
    und zum Überprüfen, ob eine Liste sortiert ist.
    """

    @classmethod
    def partition(cls, arr: list, lo: int, hi: int) -> int:
        """Partitioniert das Array um ein Pivot-Element.

        Args:
            arr: Die zu partitionierende Liste.
            lo: Der untere Index des zu partitionierenden Bereichs.
            hi: Der obere Index des zu partitionierenden Bereichs.

        Returns:
            Der Index des Pivot-Elements nach der Partitionierung.
        """
        # Wähle das erste Element als Pivot
        v = arr[lo]
        i = lo
        j = hi + 1

        while True:
            # Finde Element von links, das >= Pivot ist
            while True:
                i += 1
                if not (i < hi and arr[i] < v):
                    break

            # Finde Element von rechts, das <= Pivot ist
            while True:
                j -= 1
                if not (j > lo and arr[j] > v):
                    break

            # Überprüfe, ob sich die Zeiger gekreuzt haben
            if i >= j:
                break

            # Tausche Elemente
            arr[i], arr[j] = arr[j], arr[i]

        # Setze Pivot an die richtige Position
        arr[lo], arr[j] = arr[j], arr[lo]
        return j

    @classmethod
    def quicksort(cls, arr: list, lo: int, hi: int) -> list:
        """Rekursive Quick-Sort-Implementierung.

        Args:
            arr: Die zu sortierende Liste.
            lo: Der untere Index des zu sortierenden Bereichs.
            hi: Der obere Index des zu sortierenden Bereichs.

        Returns:
            Die sortierte Liste.
        """
        if lo >= hi:
            return arr

        # Partitioniere das Array und erhalte die Pivot-Position
        j = cls.partition(arr, lo, hi)

        # Sortiere rekursiv die beiden Teilarrays
        cls.quicksort(arr, lo, j - 1)
        cls.quicksort(arr, j + 1, hi)

        return arr

    @classmethod
    def sort(cls, arr: list) -> list:
        """Sortiert eine Liste mit dem Quick-Sort-Algorithmus.

        Args:
            arr: Die zu sortierende Liste.

        Returns:
            Die sortierte Liste.
        """
        return cls.quicksort(arr, 0, len(arr) - 1)

    @classmethod
    def is_sorted(cls, arr: list) -> bool:
        """Überprüft, ob eine Liste sortiert ist.

        Args:
            arr: Die zu überprüfende Liste.

        Returns:
            True, wenn die Liste sortiert ist, sonst False.
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
    print("sort items: ", Quick.sort(items))

    # Überprüfe, ob die Liste korrekt sortiert wurde
    assert Quick.is_sorted(items)
