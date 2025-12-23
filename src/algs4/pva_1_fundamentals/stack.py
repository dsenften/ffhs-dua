"""Stack-Implementierungen.

Dieses Modul enthält verschiedene Stack-Implementierungen:
- Stack: Verkettete Liste mit dynamischer Grösse
- FixedCapacityStack: Feste Array-Grösse
- ResizingArrayStack: Dynamisches Array mit amortisiert O(1) push/pop

Beispiele:
    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.pop()
    2
    >>> stack.size()
    1
"""

from collections.abc import Iterator


class Node[T]:
    # Hilfsklasse für verkettete Liste
    def __init__(self):
        """
        Initialize a linked-list node with empty value and no next reference.
        
        Attributes:
            item (T | None): Stored value for the node, initialized to None.
            next (Node | None): Reference to the next node in the list, initialized to None.
        """
        self.item: T = None
        self.next: Node | None = None


class Stack[T]:
    """Die Stack-Klasse repräsentiert einen Last-In-First-Out (LIFO) Stapel von generischen
    Elementen. Sie unterstützt die üblichen push- und pop-Operationen, zusammen mit Methoden
    zum Anzeigen des obersten Elements, zum Testen, ob der Stack leer ist, und zum Iterieren
    durch die Elemente in LIFO-Reihenfolge.

    Diese Implementierung verwendet eine einfach verkettete Liste mit einer statischen
    verschachtelten Klasse für die Listenknoten. Siehe LinkedStack für die Version aus
    dem Lehrbuch, die eine nicht-statische verschachtelte Klasse verwendet. Siehe
    ResizingArrayStack für eine Version, die ein Array mit dynamischer Grössenanpassung verwendet.
    Die push-, pop-, peek-, size- und is_empty-Operationen benötigen alle konstante
    Zeit im schlimmsten Fall.

    """

    def __init__(self) -> None:
        """Initialisiert einen leeren Stack."""
        self._first: Node[T] | None = None
        self._n: int = 0

    def is_empty(self) -> bool:
        """Gibt True zurück, wenn dieser Stack leer ist.

        :returns: True, wenn dieser Stack leer ist, False andernfalls

        """
        return self._n == 0

    def size(self) -> int:
        """Gibt die Anzahl der Elemente in diesem Stack zurück.

        :returns: Die Anzahl der Elemente in diesem Stack

        """
        return self._n

    def __len__(self) -> int:
        return self.size()

    def push(self, item: T) -> None:
        """Fügt das Element zu diesem Stack hinzu.

        :param item: Das Element, das hinzugefügt werden soll

        """
        oldfirst = self._first
        self._first = Node()
        self._first.item = item
        self._first.next = oldfirst
        self._n += 1

    def pop(self) -> T:
        """Entfernt und gibt das zuletzt hinzugefügte Element dieses Stacks zurück.

        :returns: Das zuletzt hinzugefügte Element
        :raises ValueError: Wenn dieser Stack leer ist

        """
        if self.is_empty():
            raise ValueError("Stack-Unterlauf")
        assert self._first is not None
        item = self._first.item
        assert item is not None
        self._first = self._first.next
        self._n -= 1
        return item

    def peek(self) -> T:
        """Gibt das zuletzt hinzugefügte Element dieses Stacks zurück (ohne es zu entfernen).

        :returns: Das zuletzt hinzugefügte Element dieses Stacks
        :raises ValueError: Wenn dieser Stack leer ist

        """
        if self.is_empty():
            raise ValueError("Stack-Unterlauf")
        assert self._first is not None
        item = self._first.item
        assert item is not None
        return item

    def __repr__(self) -> str:
        """Gibt eine String-Repräsentation dieses Stacks zurück.

        :returns: Die Sequenz der Elemente in diesem Stack in LIFO-Reihenfolge, durch Leerzeichen getrennt

        """
        s = []
        for item in self:
            s.append(item.__repr__())
        return " ".join(s)

    def __iter__(self) -> Iterator[T]:
        """
        Iterate over the stack's elements from top (most recently pushed) to bottom.
        
        Returns:
            Iterator[T]: An iterator that yields the stack's elements in LIFO order.
        """
        current = self._first
        while current is not None:
            item = current.item
            assert item is not None
            yield item
            current = current.next


class FixedCapacityStack[T]:
    """Die FixedCapacityStack-Klasse repräsentiert einen Stack mit fester Kapazität.

    Diese Implementierung verwendet ein Array mit fester Grösse, um die Elemente zu speichern.
    Die push-, pop-, size- und is_empty-Operationen benötigen konstante Zeit.
    """

    def __init__(self, capacity: int):
        """Initialisiert einen leeren Stack mit der angegebenen Kapazität.

        :param capacity: Die maximale Anzahl von Elementen, die dieser Stack aufnehmen kann
        """
        self.a: list[T | None] = [None] * capacity
        self.n: int = 0

    def is_empty(self) -> bool:
        """Gibt True zurück, wenn dieser Stack leer ist.

        :returns: True, wenn dieser Stack leer ist, False andernfalls
        """
        return self.n == 0

    def size(self) -> int:
        return self.n

    def __len__(self) -> int:
        return self.size()

    def push(self, item: T):
        """Fügt das Element zu diesem Stack hinzu.

        :param item: Das Element, das hinzugefügt werden soll
        :raises IndexError: Wenn der Stack bereits voll ist
        """
        self.a[self.n] = item
        self.n += 1

    def pop(self) -> T:
        """
        Remove and return the most recently pushed element from this fixed-capacity stack.
        
        Returns:
            The most recently pushed element.
        
        Raises:
            AssertionError: If the stack is empty.
        """
        self.n -= 1
        item = self.a[self.n]
        assert item is not None
        return item


class ResizingArrayStack[T]:
    """Die ResizingArrayStack-Klasse repräsentiert einen Stack mit dynamischer Grössenanpassung.

    Diese Implementierung verwendet ein Array, dessen Grösse dynamisch angepasst wird,
    um die Elemente zu speichern. Die push- und pop-Operationen benötigen amortisiert
    konstante Zeit. Die size- und is_empty-Operationen benötigen konstante Zeit.
    """

    def __init__(self) -> None:
        """Initialisiert einen leeren Stack mit dynamischer Grössenanpassung."""
        self.a: list[T | None] = [None]
        self.n: int = 0

    def is_empty(self) -> bool:
        """Gibt True zurück, wenn dieser Stack leer ist.

        :returns: True, wenn dieser Stack leer ist, False andernfalls
        """
        return self.n == 0

    def size(self) -> int:
        return self.n

    def __len__(self) -> int:
        return self.size()

    def resize(self, capacity: int) -> None:
        """Passt die Grösse des Arrays an die angegebene Kapazität an.

        :param capacity: Die neue Kapazität des Arrays
        """
        temp: list[T | None] = [None] * capacity
        for i in range(self.n):
            temp[i] = self.a[i]
        self.a = temp

    def push(self, item: T) -> None:
        """Fügt das Element zu diesem Stack hinzu.

        :param item: Das Element, das hinzugefügt werden soll
        """
        if self.n == len(self.a):
            self.resize(2 * len(self.a))
        self.a[self.n] = item
        self.n += 1

    def pop(self) -> T:
        """Entfernt und gibt das zuletzt hinzugefügte Element dieses Stacks zurück.

        :returns: Das zuletzt hinzugefügte Element
        :raises AssertionError: Wenn dieser Stack leer ist
        """
        self.n -= 1
        item = self.a[self.n]
        self.a[self.n] = None
        if self.n > 0 and self.n <= len(self.a) // 4:
            self.resize(len(self.a) // 2)
        assert item is not None
        return item

    def __iter__(self) -> Iterator[T]:
        """Gibt einen Iterator für diesen Stack zurück, der durch die Elemente in
        LIFO-Reihenfolge iteriert.

        :return: Ein Iterator für diesen Stack, der durch die Elemente in LIFO-Reihenfolge iteriert
        """
        i = self.n - 1
        while i >= 0:
            item = self.a[i]
            assert item is not None
            yield item
            i -= 1