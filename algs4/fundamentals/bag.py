from typing import Generic, Iterator, Optional, TypeVar

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
            self.next: Optional[Bag.Node[T]] = None
            self.item: Optional[S] = None

    def __init__(self) -> None:
        """Initialisiert einen leeren Beutel."""
        self._first: Optional[Bag.Node[T]] = None  # Anfang des Beutels
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

    def __repr__(self) -> str:
        out = "{"
        for elem in self:
            out += "{}, ".format(elem)
        return out + "}"
