"""Binary Search Tree (BST) - Binärer Suchbaum

Ein binärer Suchbaum ist eine Datenstruktur zur effizienten Speicherung und
Suche von Schlüssel-Wert-Paaren. Jeder Knoten hat einen Schlüssel und einen Wert,
wobei alle Schlüssel im linken Teilbaum kleiner und alle Schlüssel im rechten
Teilbaum grösser als der Schlüssel des Knotens sind.

Zeitkomplexität (durchschnittlicher Fall):
- get(key): O(log n)
- put(key, val): O(log n)
- delete(key): O(log n)
- min/max: O(log n)

Zeitkomplexität (schlechtester Fall):
- Alle Operationen: O(n) wenn der Baum degeneriert (unbalanciert)

Beispiele:
    >>> bst = BST()
    >>> bst.put("S", 0)
    >>> bst.put("E", 1)
    >>> bst.put("A", 2)
    >>> bst.get("E")
    1
    >>> bst.size()
    3
"""

from collections.abc import Iterator
from typing import Generic, TypeVar

from src.algs4.pva_1_fundamentals.queue import Queue

K = TypeVar("K")  # Key type (muss vergleichbar sein)
V = TypeVar("V")  # Value type


class Node(Generic[K, V]):
    """Knoten im binären Suchbaum.

    Attributes:
        key: Schlüssel des Knotens
        val: Wert des Knotens
        left: Linker Kindknoten (kleinere Schlüssel)
        right: Rechter Kindknoten (grössere Schlüssel)
        n: Anzahl der Knoten im Teilbaum (inklusive diesem Knoten)
    """

    def __init__(self, key: K, val: V, n: int) -> None:
        """Initialisiert einen neuen Knoten.

        Args:
            key: Schlüssel des Knotens
            val: Wert des Knotens
            n: Anzahl der Knoten im Teilbaum
        """
        self.key: K = key
        self.val: V = val
        self.n: int = n
        self.left: Node[K, V] | None = None
        self.right: Node[K, V] | None = None


class BST(Generic[K, V]):
    """Binary Search Tree - Binärer Suchbaum.

    Ein geordneter Symbol-Table, implementiert als binärer Suchbaum.
    Unterstützt die üblichen put-, get- und delete-Operationen sowie
    geordnete Operationen wie min, max, floor, ceiling und rank.

    Diese Implementierung verwendet keinen Balancierungs-Mechanismus,
    daher kann die Worst-Case-Performance O(n) sein bei degenerierten Bäumen.
    """

    def __init__(self) -> None:
        """Initialisiert einen leeren binären Suchbaum."""
        self._root: Node[K, V] | None = None

    def size(self) -> int:
        """Gibt die Anzahl der Schlüssel-Wert-Paare im BST zurück.

        Returns:
            int: Anzahl der Schlüssel-Wert-Paare
        """
        return self._size(self._root)

    def _size(self, node: Node[K, V] | None) -> int:
        """Gibt die Anzahl der Knoten im Teilbaum zurück.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            int: Anzahl der Knoten im Teilbaum
        """
        if node is None:
            return 0
        return node.n

    def is_empty(self) -> bool:
        """Prüft, ob der BST leer ist.

        Returns:
            bool: True wenn leer, False sonst
        """
        return self._root is None

    def __len__(self) -> int:
        """Gibt die Anzahl der Elemente zurück."""
        return self.size()

    def contains(self, key: K) -> bool:
        """Prüft, ob der Schlüssel im BST vorhanden ist.

        Args:
            key: Zu suchender Schlüssel

        Returns:
            bool: True wenn Schlüssel vorhanden, False sonst

        Raises:
            ValueError: wenn key None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        return self.get(key) is not None

    def get(self, key: K) -> V | None:
        """Gibt den Wert zum Schlüssel zurück.

        Args:
            key: Zu suchender Schlüssel

        Returns:
            V | None: Wert zum Schlüssel, oder None wenn nicht vorhanden

        Raises:
            ValueError: wenn key None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        return self._get(self._root, key)

    def _get(self, node: Node[K, V] | None, key: K) -> V | None:
        """Rekursive Hilfsmethode für get.

        Args:
            node: Wurzel des Teilbaums
            key: Zu suchender Schlüssel

        Returns:
            V | None: Wert zum Schlüssel, oder None wenn nicht vorhanden
        """
        if node is None:
            return None

        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def put(self, key: K, val: V) -> None:
        """Fügt ein Schlüssel-Wert-Paar in den BST ein.

        Wenn der Schlüssel bereits existiert, wird der Wert überschrieben.

        Args:
            key: Schlüssel
            val: Wert

        Raises:
            ValueError: wenn key oder val None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        if val is None:
            raise ValueError("Wert darf nicht None sein")
        self._root = self._put(self._root, key, val)

    def _put(self, node: Node[K, V] | None, key: K, val: V) -> Node[K, V]:
        """Rekursive Hilfsmethode für put.

        Args:
            node: Wurzel des Teilbaums
            key: Schlüssel
            val: Wert

        Returns:
            Node[K, V]: Aktualisierte Wurzel des Teilbaums
        """
        if node is None:
            return Node(key, val, 1)

        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val

        node.n = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete_min(self) -> None:
        """Löscht das Schlüssel-Wert-Paar mit dem kleinsten Schlüssel.

        Raises:
            ValueError: wenn der BST leer ist
        """
        if self.is_empty():
            raise ValueError("BST-Unterlauf: Baum ist leer")
        self._root = self._delete_min(self._root)

    def _delete_min(self, node: Node[K, V] | None) -> Node[K, V] | None:
        """Rekursive Hilfsmethode für delete_min.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            Node[K, V] | None: Aktualisierte Wurzel des Teilbaums
        """
        if node is None:
            return None
        if node.left is None:
            return node.right

        node.left = self._delete_min(node.left)
        node.n = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete_max(self) -> None:
        """Löscht das Schlüssel-Wert-Paar mit dem grössten Schlüssel.

        Raises:
            ValueError: wenn der BST leer ist
        """
        if self.is_empty():
            raise ValueError("BST-Unterlauf: Baum ist leer")
        self._root = self._delete_max(self._root)

    def _delete_max(self, node: Node[K, V] | None) -> Node[K, V] | None:
        """Rekursive Hilfsmethode für delete_max.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            Node[K, V] | None: Aktualisierte Wurzel des Teilbaums
        """
        if node is None:
            return None
        if node.right is None:
            return node.left

        node.right = self._delete_max(node.right)
        node.n = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete(self, key: K) -> None:
        """Löscht das Schlüssel-Wert-Paar mit dem gegebenen Schlüssel.

        Args:
            key: Zu löschender Schlüssel

        Raises:
            ValueError: wenn key None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        self._root = self._delete(self._root, key)

    def _delete(self, node: Node[K, V] | None, key: K) -> Node[K, V] | None:
        """Rekursive Hilfsmethode für delete (Hibbard-Deletion).

        Args:
            node: Wurzel des Teilbaums
            key: Zu löschender Schlüssel

        Returns:
            Node[K, V] | None: Aktualisierte Wurzel des Teilbaums
        """
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Knoten gefunden - lösche ihn
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right

            # Knoten hat zwei Kinder: ersetze durch Minimum des rechten Teilbaums
            temp = node
            node = self._min(temp.right)
            assert node is not None
            node.right = self._delete_min(temp.right)
            node.left = temp.left

        node.n = self._size(node.left) + self._size(node.right) + 1
        return node

    def min(self) -> K:
        """Gibt den kleinsten Schlüssel im BST zurück.

        Returns:
            K: Kleinster Schlüssel

        Raises:
            ValueError: wenn der BST leer ist
        """
        if self.is_empty():
            raise ValueError("BST ist leer")
        return self._min(self._root).key

    def _min(self, node: Node[K, V] | None) -> Node[K, V]:
        """Gibt den Knoten mit dem kleinsten Schlüssel im Teilbaum zurück.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            Node[K, V]: Knoten mit kleinstem Schlüssel

        Raises:
            AssertionError: wenn node None ist
        """
        assert node is not None
        if node.left is None:
            return node
        return self._min(node.left)

    def max(self) -> K:
        """Gibt den grössten Schlüssel im BST zurück.

        Returns:
            K: Grösster Schlüssel

        Raises:
            ValueError: wenn der BST leer ist
        """
        if self.is_empty():
            raise ValueError("BST ist leer")
        return self._max(self._root).key

    def _max(self, node: Node[K, V] | None) -> Node[K, V]:
        """Gibt den Knoten mit dem grössten Schlüssel im Teilbaum zurück.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            Node[K, V]: Knoten mit grösstem Schlüssel

        Raises:
            AssertionError: wenn node None ist
        """
        assert node is not None
        if node.right is None:
            return node
        return self._max(node.right)

    def floor(self, key: K) -> K | None:
        """Gibt den grössten Schlüssel <= key zurück.

        Args:
            key: Referenz-Schlüssel

        Returns:
            K | None: Grösster Schlüssel <= key, oder None wenn keiner existiert

        Raises:
            ValueError: wenn key None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        node = self._floor(self._root, key)
        if node is None:
            return None
        return node.key

    def _floor(self, node: Node[K, V] | None, key: K) -> Node[K, V] | None:
        """Rekursive Hilfsmethode für floor.

        Args:
            node: Wurzel des Teilbaums
            key: Referenz-Schlüssel

        Returns:
            Node[K, V] | None: Knoten mit grösstem Schlüssel <= key
        """
        if node is None:
            return None

        if key == node.key:
            return node
        if key < node.key:
            return self._floor(node.left, key)

        # key > node.key: floor könnte im rechten Teilbaum sein
        temp = self._floor(node.right, key)
        if temp is not None:
            return temp
        else:
            return node

    def ceiling(self, key: K) -> K | None:
        """Gibt den kleinsten Schlüssel >= key zurück.

        Args:
            key: Referenz-Schlüssel

        Returns:
            K | None: Kleinster Schlüssel >= key, oder None wenn keiner existiert

        Raises:
            ValueError: wenn key None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        node = self._ceiling(self._root, key)
        if node is None:
            return None
        return node.key

    def _ceiling(self, node: Node[K, V] | None, key: K) -> Node[K, V] | None:
        """Rekursive Hilfsmethode für ceiling.

        Args:
            node: Wurzel des Teilbaums
            key: Referenz-Schlüssel

        Returns:
            Node[K, V] | None: Knoten mit kleinstem Schlüssel >= key
        """
        if node is None:
            return None

        if key == node.key:
            return node
        if key > node.key:
            return self._ceiling(node.right, key)

        # key < node.key: ceiling könnte im linken Teilbaum sein
        temp = self._ceiling(node.left, key)
        if temp is not None:
            return temp
        else:
            return node

    def select(self, k: int) -> K:
        """Gibt den k-t-kleinsten Schlüssel im BST zurück.

        Args:
            k: Rang (0-basiert)

        Returns:
            K: k-t-kleinster Schlüssel

        Raises:
            ValueError: wenn k ausserhalb des gültigen Bereichs liegt
        """
        if k < 0 or k >= self.size():
            raise ValueError(f"Index {k} ist ausserhalb des Bereichs [0, {self.size()})")
        node = self._select(self._root, k)
        assert node is not None
        return node.key

    def _select(self, node: Node[K, V] | None, k: int) -> Node[K, V] | None:
        """Rekursive Hilfsmethode für select.

        Args:
            node: Wurzel des Teilbaums
            k: Rang

        Returns:
            Node[K, V] | None: Knoten mit Rang k
        """
        if node is None:
            return None

        t = self._size(node.left)
        if t > k:
            return self._select(node.left, k)
        elif t < k:
            return self._select(node.right, k - t - 1)
        else:
            return node

    def rank(self, key: K) -> int:
        """Gibt die Anzahl der Schlüssel < key zurück.

        Args:
            key: Referenz-Schlüssel

        Returns:
            int: Anzahl der Schlüssel < key

        Raises:
            ValueError: wenn key None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        return self._rank(self._root, key)

    def _rank(self, node: Node[K, V] | None, key: K) -> int:
        """Rekursive Hilfsmethode für rank.

        Args:
            node: Wurzel des Teilbaums
            key: Referenz-Schlüssel

        Returns:
            int: Anzahl der Schlüssel < key im Teilbaum
        """
        if node is None:
            return 0

        if key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return 1 + self._size(node.left) + self._rank(node.right, key)
        else:
            return self._size(node.left)

    def keys(self) -> Iterator[K]:
        """Gibt alle Schlüssel im BST in sortierter Reihenfolge zurück.

        Returns:
            Iterator[K]: Iterator über alle Schlüssel
        """
        if self.is_empty():
            return iter([])
        return self.keys_range(self.min(), self.max())

    def keys_range(self, lo: K, hi: K) -> Iterator[K]:
        """Gibt alle Schlüssel im Bereich [lo, hi] in sortierter Reihenfolge zurück.

        Args:
            lo: Untere Grenze
            hi: Obere Grenze

        Returns:
            Iterator[K]: Iterator über Schlüssel im Bereich

        Raises:
            ValueError: wenn lo oder hi None ist
        """
        if lo is None:
            raise ValueError("Untere Grenze darf nicht None sein")
        if hi is None:
            raise ValueError("Obere Grenze darf nicht None sein")

        queue: Queue[K] = Queue()
        self._keys(self._root, queue, lo, hi)
        return iter(queue)

    def _keys(
        self, node: Node[K, V] | None, queue: Queue[K], lo: K, hi: K
    ) -> None:
        """Rekursive Hilfsmethode für keys (In-Order-Traversierung).

        Args:
            node: Wurzel des Teilbaums
            queue: Queue zum Sammeln der Schlüssel
            lo: Untere Grenze
            hi: Obere Grenze
        """
        if node is None:
            return

        if lo < node.key:
            self._keys(node.left, queue, lo, hi)
        if lo <= node.key <= hi:
            queue.enqueue(node.key)
        if node.key < hi:
            self._keys(node.right, queue, lo, hi)

    def level_order(self) -> Iterator[K]:
        """Gibt die Schlüssel in Level-Order-Reihenfolge zurück (Breitensuche).

        Returns:
            Iterator[K]: Iterator über Schlüssel in Level-Order
        """
        keys: Queue[K] = Queue()
        queue: Queue[Node[K, V] | None] = Queue()

        queue.enqueue(self._root)
        while not queue.is_empty():
            node = queue.dequeue()
            if node is None:
                continue

            keys.enqueue(node.key)
            queue.enqueue(node.left)
            queue.enqueue(node.right)

        return iter(keys)

    def __iter__(self) -> Iterator[K]:
        """Iteriert über alle Schlüssel in sortierter Reihenfolge."""
        return self.keys()

    def __repr__(self) -> str:
        """Gibt eine String-Repräsentation des BST zurück."""
        if self.is_empty():
            return "BST()"
        keys = list(self.keys())
        return f"BST({keys})"

    def __str__(self) -> str:
        """Gibt eine visuelle Baumdarstellung zurück.

        Returns:
            str: Mehrzeilige String-Repräsentation des Baums

        Beispiel:
            >>> bst = BST()
            >>> for key in ["E", "B", "G", "A", "D", "F", "H"]:
            ...     bst.put(key, key.lower())
            >>> print(bst)
            E
            ├── B
            │   ├── A
            │   └── D
            └── G
                ├── F
                └── H
        """
        if self.is_empty():
            return "BST()"

        lines: list[str] = []
        if self._root is not None:
            lines.append(str(self._root.key))
            self._build_tree_children(self._root, "", lines)
        return "\n".join(lines)

    def _build_tree_children(
        self,
        node: Node[K, V],
        prefix: str,
        lines: list[str],
    ) -> None:
        """Rekursive Hilfsmethode zum Aufbau der Baumdarstellung für Kindknoten.

        Args:
            node: Aktueller Knoten (dessen Kinder dargestellt werden sollen)
            prefix: Präfix für die Einrückung
            lines: Liste der Ausgabezeilen
        """
        # Kinder sammeln
        children: list[Node[K, V]] = []
        if node.left is not None:
            children.append(node.left)
        if node.right is not None:
            children.append(node.right)

        # Kinder ausgeben
        for i, child in enumerate(children):
            is_last = i == len(children) - 1
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{child.key}")

            # Präfix für Enkelkinder
            extension = "    " if is_last else "│   "
            new_prefix = prefix + extension
            self._build_tree_children(child, new_prefix, lines)


if __name__ == "__main__":
    import sys

    # Beispielprogramm: liest Zeichenketten von stdin und gibt sie sortiert aus
    print("Binary Search Tree Demo")
    print("Geben Sie Zeichenketten ein (eine pro Zeile), Strg+D zum Beenden:")

    st: BST[str, int] = BST()
    i = 0

    try:
        for line in sys.stdin:
            for key in line.split():
                st.put(key, i)
                i += 1

        print("\nLevel-Order-Traversierung:")
        for s in st.level_order():
            print(f"{s} {st.get(s)}")

        print("\nSortierte Reihenfolge (In-Order):")
        for s in st.keys():
            print(f"{s} {st.get(s)}")

        print(f"\nGrösse: {st.size()}")
        print(f"Minimum: {st.min()}")
        print(f"Maximum: {st.max()}")

    except KeyboardInterrupt:
        print("\nProgramm beendet")
