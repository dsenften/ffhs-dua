"""Shell Sort Implementierung.

Diese Klasse implementiert den Shell-Sort-Algorithmus, der eine Erweiterung
des Insertion-Sort-Algorithmus ist und für größere Datenmengen besser geeignet ist.

Beispiele:
    % more tiny.txt
    S O R T E X A M P L E

    % python shell.py < tiny.txt
    A E E L M O P R S T X                 [ one string per line ]

    % more words3.txt
    bed bug dad yes zoo ... all bad yet

    % python shell.py < words3.txt
    all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Shell:
    """Shell-Sort-Implementierung.

    Diese Klasse bietet Methoden zum Sortieren von Listen mit dem Shell-Sort-Algorithmus
    und zum Überprüfen, ob eine Liste sortiert ist.
    """

    @classmethod
    def sort(cls, arr: list) -> list:
        """Sortiert eine Liste mit dem Shell-Sort-Algorithmus.

        Args:
            arr: Die zu sortierende Liste.

        Returns:
            Die sortierte Liste.
        """
        array_length = len(arr)
        gap = 1

        # Berechne die initiale Schrittweite nach Knuth-Sequenz: 1, 4, 13, 40, ...
        while gap < array_length // 3:
            gap = 3 * gap + 1

        # Führe h-sort für abnehmende Werte von h durch
        while gap >= 1:
            # h-sort des Arrays
            for i in range(gap, array_length):
                j = i
                # Insertion sort für jede h-Sequenz
                while j >= gap:
                    if arr[j] > arr[j - gap]:
                        break
                    # Tausche Elemente, die gap Positionen auseinander liegen
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                    j -= gap
            # Reduziere die Schrittweite
            gap //= 3
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
    print("sort items: ", Shell.sort(items))

    # Überprüfe, ob die Liste korrekt sortiert wurde
    assert Shell.is_sorted(items)
