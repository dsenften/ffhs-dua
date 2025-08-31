from collections.abc import Iterator
from typing import Generic, TypeVar

T = TypeVar("T")
S = TypeVar("S")


class Bag(Generic[T]):
    """Die Bag-Klasse repräsentiert einen Beutel (oder Multiset) von generischen Elementen.
    Sie unterstützt das Einfügen und Iterieren über die Elemente in beliebiger Reihenfolge.

    Diese Implementierung verwendet eine einfach verkettete Liste mit einer statischen
    verschachtelten Node-Klasse. Siehe LinkedBag für die Version aus dem
    Lehrbuch, die eine nicht-statische verschachtelte Klasse verwendet.

    Die Operationen add, is_empty und size benötigen konstante Zeit.
    Die Iteration benötigt Zeit proportional zur Anzahl der Elemente.

    """

    class Node(Generic[S]):
        # Hilfsklasse für verkettete Liste
        def __init__(self):
            self.next: Bag.Node[T] | None = None
            self.item: S | None = None

    def __init__(self) -> None:
        """Initialisiert einen leeren Beutel."""
        self._first: Bag.Node[T] | None = None  # Anfang des Beutels
        self._n = 0  # Anzahl der Elemente im Beutel

    def is_empty(self) -> bool:
        """Gibt True zurück, wenn dieser Beutel leer ist.

        :returns: True, wenn dieser Beutel leer ist,
                  False andernfalls

        """
        return self._first is None

    def size(self) -> int:
        """Gibt die Anzahl der Elemente in diesem Beutel zurück.

        :returns: Die Anzahl der Elemente in diesem Beutel

        """
        return self._n

    def __len__(self) -> int:
        return self.size()

    def add(self, item: T) -> None:
        """Fügt das Element zu diesem Beutel hinzu.

        :param item: Das Element, das zu diesem Beutel hinzugefügt werden soll

        """
        oldfirst = self._first
        self._first = Bag.Node()
        self._first.item = item
        self._first.next = oldfirst
        self._n += 1

    def __iter__(self) -> Iterator[T]:
        """Gibt einen Iterator zurück, der über die Elemente in diesem Beutel
        in beliebiger Reihenfolge iteriert.

        :returns: Ein Iterator, der über die Elemente in diesem Beutel in beliebiger Reihenfolge iteriert

        """
        current = self._first
        while current is not None:
            assert current.item is not None
            yield current.item
            current = current.next

    def contains(self, item: T) -> bool:
        """Prüft, ob ein Element im Beutel enthalten ist.

        :param item: Das zu suchende Element
        :returns: True, wenn das Element im Beutel enthalten ist,
                  False andernfalls

        Zeitkomplexität: O(n), wobei n die Anzahl der Elemente im Beutel ist
        """
        current = self._first
        while current is not None:
            if current.item == item:
                return True
            current = current.next
        return False

    def __contains__(self, item: T) -> bool:
        """Implementiert den 'in'-Operator für den Beutel.

        :param item: Das zu suchende Element
        :returns: True, wenn das Element im Beutel enthalten ist,
                  False andernfalls
        """
        return self.contains(item)

    def remove(self, item: T) -> bool:
        """Entfernt ein Element aus dem Beutel, falls vorhanden.

        :param item: Das zu entfernende Element
        :returns: True, wenn das Element gefunden und entfernt wurde,
                  False andernfalls

        Zeitkomplexität: O(n), wobei n die Anzahl der Elemente im Beutel ist
        """
        if self.is_empty():
            return False

        # Sonderfall: Das erste Element ist das zu entfernende
        if self._first is not None and self._first.item == item:
            self._first = self._first.next
            self._n -= 1
            return True

        # Suche nach dem Element in der Liste
        current = self._first
        while current is not None and current.next is not None:
            if current.next.item == item:
                current.next = current.next.next
                self._n -= 1
                return True
            current = current.next

        return False

    def remove_all(self, item: T) -> int:
        """Entfernt alle Vorkommen eines Elements aus dem Beutel.

        :param item: Das zu entfernende Element
        :returns: Die Anzahl der entfernten Elemente

        Zeitkomplexität: O(n), wobei n die Anzahl der Elemente im Beutel ist
        """
        if self.is_empty():
            return 0

        count = 0

        # Entferne alle Vorkommen am Anfang der Liste
        while self._first is not None and self._first.item == item:
            self._first = self._first.next
            self._n -= 1
            count += 1

        # Entferne alle weiteren Vorkommen
        if self._first is not None:
            current = self._first
            while current.next is not None:
                if current.next.item == item:
                    current.next = current.next.next
                    self._n -= 1
                    count += 1
                else:
                    current = current.next

        return count

    def clear(self) -> None:
        """Entfernt alle Elemente aus dem Beutel.

        Zeitkomplexität: O(1)
        """
        self._first = None
        self._n = 0

    def peek(self) -> T | None:
        """Gibt das erste Element des Beutels zurück, ohne es zu entfernen.

        :returns: Das erste Element des Beutels oder None, wenn der Beutel leer ist

        Zeitkomplexität: O(1)
        """
        if self.is_empty():
            return None
        assert self._first is not None and self._first.item is not None
        return self._first.item

    def to_list(self) -> list[T]:
        """Konvertiert den Beutel in eine Liste.

        :returns: Eine Liste mit allen Elementen des Beutels

        Zeitkomplexität: O(n), wobei n die Anzahl der Elemente im Beutel ist
        """
        result = []
        for item in self:
            result.append(item)
        return result

    def __repr__(self) -> str:
        """Gibt eine String-Repräsentation des Beutels zurück.

        :returns: Eine String-Repräsentation des Beutels
        """
        if self.is_empty():
            return "{}"

        out = "{"
        items = list(self)
        for i, elem in enumerate(items):
            out += f"{elem}"
            if i < len(items) - 1:
                out += ", "
        return out + "}"
