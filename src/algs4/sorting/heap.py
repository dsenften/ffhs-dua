"""Heap Sort Implementierung.

Diese Klasse implementiert den Heap-Sort-Algorithmus, einen effizienten
Sortieralgorithmus basierend auf der Heap-Datenstruktur mit garantierter
Zeitkomplexität O(n log n) in allen Fällen.

Beispiele:
    % more tiny.txt
    S O R T E X A M P L E

    % python heap.py < tiny.txt
    A E E L M O P R S T X                 [ one string per line ]

    % more words3.txt
    bed bug dad yes zoo ... all bad yet

    % python heap.py < words3.txt
    all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Heap:
    """Heap-Sort-Implementierung.

    Diese Klasse bietet Methoden zum Sortieren von Listen mit dem Heap-Sort-Algorithmus
    und zum Überprüfen, ob eine Liste sortiert ist. Der Algorithmus basiert auf der
    Heap-Datenstruktur und garantiert O(n log n) Zeitkomplexität in allen Fällen.
    """

    @classmethod
    def sink(cls, arr: list, i: int, length: int) -> None:
        """Lässt ein Element im Heap nach unten sinken (Heapify).

        Diese Methode stellt die Heap-Eigenschaft wieder her, indem sie ein Element
        so lange nach unten bewegt, bis es an der richtigen Position steht.

        Args:
            arr: Die zu bearbeitende Liste (Heap).
            i: Der Index des Elements, das sinken soll.
            length: Die Länge des aktiven Heap-Bereichs.
        """
        while 2 * i + 1 <= length:
            # Finde den Index des linken Kindes
            j = 2 * i + 1
            
            # Waehle das grössere der beiden Kinder
            if j < length and arr[j] < arr[j + 1]:
                j += 1
            
            # Wenn das aktuelle Element bereits grösser ist, sind wir fertig
            if arr[i] >= arr[j]:
                break
            
            # Tausche das aktuelle Element mit dem grösseren Kind
            arr[i], arr[j] = arr[j], arr[i]
            i = j

    @classmethod
    def sort(cls, arr: list) -> list:
        """Sortiert eine Liste mit dem Heap-Sort-Algorithmus.

        Der Algorithmus arbeitet in zwei Phasen:
        1. Heap-Konstruktion: Wandelt das Array in einen Max-Heap um
        2. Sortdown: Extrahiert wiederholt das Maximum und stellt den Heap wieder her

        Args:
            arr: Die zu sortierende Liste.

        Returns:
            Die sortierte Liste (in-place modifiziert).
        """
        n = len(arr)
        
        # Phase 1: Heap-Konstruktion (Heapify)
        # Beginne mit dem letzten Nicht-Blatt-Knoten und arbeite rückwärts
        k = n // 2 - 1
        while k >= 0:
            cls.sink(arr, k, n - 1)
            k -= 1

        # Phase 2: Sortdown
        # Extrahiere wiederholt das Maximum (Wurzel) und stelle den Heap wieder her
        while n > 1:
            # Tausche Maximum (Index 0) mit letztem Element
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            n -= 1
            # Stelle Heap-Eigenschaft für reduzierten Heap wieder her
            cls.sink(arr, 0, n - 1)

        return arr

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
    print("sort items: ", Heap.sort(items))

    # Überprüfe, ob die Liste korrekt sortiert wurde
    assert Heap.is_sorted(items)
