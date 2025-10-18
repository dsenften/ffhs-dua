"""Queue-Implementierung.

Dieses Modul enthält eine Queue-Implementierung basierend auf einer
verketteten Liste mit First-In-First-Out (FIFO) Verhalten.

Beispiele:
    >>> queue = Queue()
    >>> queue.enqueue(1)
    >>> queue.enqueue(2)
    >>> queue.dequeue()
    1
    >>> queue.size()
    1
"""

from collections.abc import Iterator
from typing import Generic, Optional, TypeVar

from ..errors.errors import NoSuchElementException

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, item: T, next: Optional["Node[T]"]) -> None:
        """Initialisiert einen neuen Knoten.

        :param item: Das Element, das im Knoten gespeichert werden soll
        :param next: Der nächste Knoten in der Queue

        """
        self.item: T = item
        self.next: Node[T] | None = next


class Queue(Generic[T]):
    """Die Queue-Klasse repräsentiert eine First-In-First-Out (FIFO) Warteschlange
    von generischen Elementen.

    Sie unterstützt die üblichen enqueue- und dequeue-Operationen, zusammen mit
    Methoden zum Anzeigen des ersten Elements, zum Testen, ob die Queue leer ist,
    und zum Iterieren durch die Elemente in FIFO-Reihenfolge. Diese
    Implementierung verwendet eine einfach verkettete Liste von Knoten. Die
    enqueue-, dequeue-, peek-, size- und is_empty-Operationen benötigen alle
    konstante Zeit im schlimmsten Fall.

    """

    def __init__(self) -> None:
        """Initialisiert eine leere Queue."""
        self._first: Node[T] | None = None
        self._last: Node[T] | None = None
        self._n: int = 0

    def enqueue(self, item: T) -> None:
        """Fügt das Element zu dieser Queue hinzu.

        :param item: Das Element, das hinzugefügt werden soll

        """
        old_last: Node[T] | None = self._last
        self._last = Node(item, None)
        if self.is_empty():
            self._first = self._last
        else:
            assert old_last is not None
            old_last.next = self._last
        self._n += 1

    def dequeue(self) -> T:
        """
        Entfernt und gibt das Element zurück, das als erstes zur Queue hinzugefügt wurde.
        :return: Das Element, das als erstes zur Queue hinzugefügt wurde.
        :raises NoSuchElementException: Wenn diese Queue leer ist
        """
        if self.is_empty():
            raise NoSuchElementException("Queue-Unterlauf")

        assert self._first is not None
        item = self._first.item
        self._first = self._first.next
        self._n -= 1
        if self.is_empty():
            self._last = None
        return item

    def is_empty(self) -> bool:
        """Gibt True zurück, wenn diese Queue leer ist.

        :return: True, wenn diese Queue leer ist, sonst False
        :rtype: bool

        """
        return self._first is None

    def size(self) -> int:
        """Gibt die Anzahl der Elemente in dieser Queue zurück.

        :return: Die Anzahl der Elemente in dieser Queue
        :rtype: int

        """
        return self._n

    def __len__(self) -> int:
        return self.size()

    def peek(self) -> T:
        """
        Gibt das Element zurück, das als erstes zur Queue hinzugefügt wurde, ohne es zu entfernen.
        :return: Das Element, das als erstes zur Queue hinzugefügt wurde
        :raises NoSuchElementException: Wenn diese Queue leer ist
        """
        if self.is_empty():
            raise NoSuchElementException("Queue-Unterlauf")

        assert self._first is not None
        return self._first.item

    def __iter__(self) -> Iterator[T]:
        """Iteriert über alle Elemente in dieser Queue in FIFO-Reihenfolge."""
        curr = self._first
        while curr is not None:
            yield curr.item
            curr = curr.next

    def __repr__(self) -> str:
        """Gibt eine String-Repräsentation dieser Queue zurück.

        :return: Die Sequenz der Elemente in FIFO-Reihenfolge, durch Leerzeichen getrennt

        """
        s = []
        for item in self:
            s.append(f"{item} ")
        return "".join(s)
