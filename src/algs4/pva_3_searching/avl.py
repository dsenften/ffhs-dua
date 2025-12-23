"""AVL Tree - Selbstbalancierender binärer Suchbaum

Ein AVL-Baum ist ein selbstbalancierender binärer Suchbaum, bei dem sich die
Höhen der beiden Kinderbäume jedes Knotens um höchstens eins unterscheiden.
Benannt nach den Erfindern Adelson-Velsky und Landis (1962).

Zeitkomplexität (garantiert):
- get(key): O(log n)
- put(key, val): O(log n)
- delete(key): O(log n)
- min/max: O(log n)

Im Gegensatz zum unbalancierten BST garantiert der AVL-Baum O(log n)
Performance auch im schlechtesten Fall durch automatische Balancierung.

Beispiele:
    >>> avl = AVL()
    >>> avl.put("S", 0)
    >>> avl.put("E", 1)
    >>> avl.put("A", 2)
    >>> avl.get("E")
    1
    >>> avl.size()
    3
"""

from collections.abc import Iterator

from src.algs4.pva_1_fundamentals.queue import Queue


class AVLNode[K, V]:
    """Knoten im AVL-Baum.

    Attributes:
        key: Schlüssel des Knotens
        val: Wert des Knotens
        left: Linker Kindknoten (kleinere Schlüssel)
        right: Rechter Kindknoten (grössere Schlüssel)
        height: Höhe des Teilbaums (Anzahl Kanten zum tiefsten Blatt)
        n: Anzahl der Knoten im Teilbaum (inklusive diesem Knoten)
    """

    def __init__(self, key: K, val: V) -> None:
        """
        Initialize an AVL tree node and its default attributes.
        
        Parameters:
            key (K): The node's key.
            val (V): The node's value.
        
        Notes:
            Sets `height` to 0, `n` (subtree size) to 1, and initializes `left` and `right` to `None`.
        """
        self.key: K = key
        self.val: V = val
        self.height: int = 0  # Blattknoten haben Höhe 0
        self.n: int = 1  # Einzelner Knoten hat Grösse 1
        self.left: AVLNode[K, V] | None = None
        self.right: AVLNode[K, V] | None = None


class AVL[K, V]:
    """AVL Tree - Selbstbalancierender binärer Suchbaum.

    Ein geordneter Symbol-Table, implementiert als AVL-Baum.
    Unterstützt die üblichen put-, get- und delete-Operationen sowie
    geordnete Operationen wie min, max, floor, ceiling und rank.

    Durch automatische Balancierung garantiert dieser Baum O(log n)
    Performance für alle Operationen im schlechtesten Fall.
    """

    def __init__(self) -> None:
        """Initialisiert einen leeren AVL-Baum."""
        self._root: AVLNode[K, V] | None = None

    def _height(self, node: AVLNode[K, V] | None) -> int:
        """Gibt die Höhe des Knotens zurück.

        Args:
            node: Knoten

        Returns:
            int: Höhe des Knotens (-1 für None)
        """
        if node is None:
            return -1
        return node.height

    def _size(self, node: AVLNode[K, V] | None) -> int:
        """Gibt die Anzahl der Knoten im Teilbaum zurück.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            int: Anzahl der Knoten im Teilbaum
        """
        if node is None:
            return 0
        return node.n

    def _update_height(self, node: AVLNode[K, V]) -> None:
        """Aktualisiert die Höhe eines Knotens basierend auf seinen Kindern.

        Args:
            node: Knoten dessen Höhe aktualisiert werden soll
        """
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _update_size(self, node: AVLNode[K, V]) -> None:
        """Aktualisiert die Grösse eines Knotens basierend auf seinen Kindern.

        Args:
            node: Knoten dessen Grösse aktualisiert werden soll
        """
        node.n = 1 + self._size(node.left) + self._size(node.right)

    def _balance_factor(self, node: AVLNode[K, V]) -> int:
        """Berechnet den Balance-Faktor eines Knotens.

        Der Balance-Faktor ist die Differenz zwischen der Höhe des linken
        und rechten Teilbaums. Ein Wert zwischen -1 und 1 bedeutet, dass
        der Baum balanciert ist.

        Args:
            node: Knoten

        Returns:
            int: Balance-Faktor (height(left) - height(right))
        """
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, node: AVLNode[K, V]) -> AVLNode[K, V]:
        """Führt eine Rechtsrotation durch.

        Wird verwendet um einen linkslastigen Baum zu balancieren.

            y                x
           / \\              / \\
          x   C    -->     A   y
         / \\                  / \\
        A   B                B   C

        Args:
            node: Wurzel des zu rotierenden Teilbaums (y)

        Returns:
            AVLNode[K, V]: Neue Wurzel des Teilbaums (x)
        """
        x = node.left
        assert x is not None

        # Rotation durchführen
        node.left = x.right
        x.right = node

        # Höhen und Grössen aktualisieren
        self._update_height(node)
        self._update_size(node)
        self._update_height(x)
        self._update_size(x)

        return x

    def _rotate_left(self, node: AVLNode[K, V]) -> AVLNode[K, V]:
        """Führt eine Linksrotation durch.

        Wird verwendet um einen rechtslastigen Baum zu balancieren.

          x                  y
         / \\                / \\
        A   y      -->     x   C
           / \\            / \\
          B   C          A   B

        Args:
            node: Wurzel des zu rotierenden Teilbaums (x)

        Returns:
            AVLNode[K, V]: Neue Wurzel des Teilbaums (y)
        """
        y = node.right
        assert y is not None

        # Rotation durchführen
        node.right = y.left
        y.left = node

        # Höhen und Grössen aktualisieren
        self._update_height(node)
        self._update_size(node)
        self._update_height(y)
        self._update_size(y)

        return y

    def _balance(self, node: AVLNode[K, V]) -> AVLNode[K, V]:
        """Balanciert einen Knoten falls nötig.

        Prüft den Balance-Faktor und führt die entsprechenden Rotationen durch:
        - Balance-Faktor > 1: Linkslastig -> Rechtsrotation
        - Balance-Faktor < -1: Rechtslastig -> Linksrotation
        - Doppelrotationen für Zig-Zag-Fälle

        Args:
            node: Zu balancierender Knoten

        Returns:
            AVLNode[K, V]: Balancierte Wurzel des Teilbaums
        """
        # Höhe und Grösse aktualisieren
        self._update_height(node)
        self._update_size(node)

        # Balance-Faktor prüfen
        balance = self._balance_factor(node)

        # Fall 1: Linkslastig
        if balance > 1:
            assert node.left is not None
            # Fall 1a: Left-Left (einfache Rechtsrotation)
            if self._balance_factor(node.left) >= 0:
                return self._rotate_right(node)
            # Fall 1b: Left-Right (Doppelrotation)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        # Fall 2: Rechtslastig
        if balance < -1:
            assert node.right is not None
            # Fall 2a: Right-Right (einfache Linksrotation)
            if self._balance_factor(node.right) <= 0:
                return self._rotate_left(node)
            # Fall 2b: Right-Left (Doppelrotation)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        # Bereits balanciert
        return node

    def size(self) -> int:
        """Gibt die Anzahl der Schlüssel-Wert-Paare im AVL-Baum zurück.

        Returns:
            int: Anzahl der Schlüssel-Wert-Paare
        """
        return self._size(self._root)

    def is_empty(self) -> bool:
        """Prüft, ob der AVL-Baum leer ist.

        Returns:
            bool: True wenn leer, False sonst
        """
        return self._root is None

    def __len__(self) -> int:
        """Gibt die Anzahl der Elemente zurück."""
        return self.size()

    def height(self) -> int:
        """Gibt die Höhe des Baums zurück.

        Returns:
            int: Höhe des Baums (-1 für leeren Baum)
        """
        return self._height(self._root)

    def contains(self, key: K) -> bool:
        """Prüft, ob der Schlüssel im AVL-Baum vorhanden ist.

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

    def _get(self, node: AVLNode[K, V] | None, key: K) -> V | None:
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
        """Fügt ein Schlüssel-Wert-Paar in den AVL-Baum ein.

        Wenn der Schlüssel bereits existiert, wird der Wert überschrieben.
        Der Baum wird automatisch balanciert.

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

    def _put(self, node: AVLNode[K, V] | None, key: K, val: V) -> AVLNode[K, V]:
        """Rekursive Hilfsmethode für put mit automatischer Balancierung.

        Args:
            node: Wurzel des Teilbaums
            key: Schlüssel
            val: Wert

        Returns:
            AVLNode[K, V]: Balancierte Wurzel des Teilbaums
        """
        # Basis: neuen Knoten erstellen
        if node is None:
            return AVLNode(key, val)

        # Rekursiv einfügen
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            # Schlüssel existiert bereits -> Wert aktualisieren
            node.val = val
            return node

        # Balancierung durchführen
        return self._balance(node)

    def delete_min(self) -> None:
        """Löscht das Schlüssel-Wert-Paar mit dem kleinsten Schlüssel.

        Raises:
            ValueError: wenn der AVL-Baum leer ist
        """
        if self.is_empty():
            raise ValueError("AVL-Baum-Unterlauf: Baum ist leer")
        self._root = self._delete_min(self._root)

    def _delete_min(self, node: AVLNode[K, V]) -> AVLNode[K, V] | None:
        """Rekursive Hilfsmethode für delete_min mit Balancierung.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            AVLNode[K, V] | None: Balancierte Wurzel des Teilbaums
        """
        if node.left is None:
            return node.right

        node.left = self._delete_min(node.left)
        return self._balance(node)

    def delete_max(self) -> None:
        """Löscht das Schlüssel-Wert-Paar mit dem grössten Schlüssel.

        Raises:
            ValueError: wenn der AVL-Baum leer ist
        """
        if self.is_empty():
            raise ValueError("AVL-Baum-Unterlauf: Baum ist leer")
        self._root = self._delete_max(self._root)

    def _delete_max(self, node: AVLNode[K, V]) -> AVLNode[K, V] | None:
        """Rekursive Hilfsmethode für delete_max mit Balancierung.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            AVLNode[K, V] | None: Balancierte Wurzel des Teilbaums
        """
        if node.right is None:
            return node.left

        node.right = self._delete_max(node.right)
        return self._balance(node)

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

    def _delete(self, node: AVLNode[K, V] | None, key: K) -> AVLNode[K, V] | None:
        """Rekursive Hilfsmethode für delete mit Balancierung.

        Args:
            node: Wurzel des Teilbaums
            key: Zu löschender Schlüssel

        Returns:
            AVLNode[K, V] | None: Balancierte Wurzel des Teilbaums
        """
        if node is None:
            return None

        # Schlüssel suchen
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Knoten gefunden - lösche ihn
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Knoten hat zwei Kinder: ersetze durch Minimum des rechten Teilbaums
            temp = node
            node = self._min(temp.right)
            node.right = self._delete_min(temp.right)
            node.left = temp.left

        # Balancierung durchführen
        return self._balance(node)

    def min(self) -> K:
        """Gibt den kleinsten Schlüssel im AVL-Baum zurück.

        Returns:
            K: Kleinster Schlüssel

        Raises:
            ValueError: wenn der AVL-Baum leer ist
        """
        if self.is_empty():
            raise ValueError("AVL-Baum ist leer")
        return self._min(self._root).key

    def _min(self, node: AVLNode[K, V]) -> AVLNode[K, V]:
        """Gibt den Knoten mit dem kleinsten Schlüssel im Teilbaum zurück.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            AVLNode[K, V]: Knoten mit kleinstem Schlüssel
        """
        if node.left is None:
            return node
        return self._min(node.left)

    def max(self) -> K:
        """Gibt den grössten Schlüssel im AVL-Baum zurück.

        Returns:
            K: Grösster Schlüssel

        Raises:
            ValueError: wenn der AVL-Baum leer ist
        """
        if self.is_empty():
            raise ValueError("AVL-Baum ist leer")
        return self._max(self._root).key

    def _max(self, node: AVLNode[K, V]) -> AVLNode[K, V]:
        """Gibt den Knoten mit dem grössten Schlüssel im Teilbaum zurück.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            AVLNode[K, V]: Knoten mit grösstem Schlüssel
        """
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

    def _floor(self, node: AVLNode[K, V] | None, key: K) -> AVLNode[K, V] | None:
        """Rekursive Hilfsmethode für floor.

        Args:
            node: Wurzel des Teilbaums
            key: Referenz-Schlüssel

        Returns:
            AVLNode[K, V] | None: Knoten mit grösstem Schlüssel <= key
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

    def _ceiling(self, node: AVLNode[K, V] | None, key: K) -> AVLNode[K, V] | None:
        """Rekursive Hilfsmethode für ceiling.

        Args:
            node: Wurzel des Teilbaums
            key: Referenz-Schlüssel

        Returns:
            AVLNode[K, V] | None: Knoten mit kleinstem Schlüssel >= key
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
        """Gibt den k-t-kleinsten Schlüssel im AVL-Baum zurück.

        Args:
            k: Rang (0-basiert)

        Returns:
            K: k-t-kleinster Schlüssel

        Raises:
            ValueError: wenn k ausserhalb des gültigen Bereichs liegt
        """
        if k < 0 or k >= self.size():
            raise ValueError(
                f"Index {k} ist ausserhalb des Bereichs [0, {self.size()})"
            )
        node = self._select(self._root, k)
        assert node is not None
        return node.key

    def _select(self, node: AVLNode[K, V] | None, k: int) -> AVLNode[K, V] | None:
        """Rekursive Hilfsmethode für select.

        Args:
            node: Wurzel des Teilbaums
            k: Rang

        Returns:
            AVLNode[K, V] | None: Knoten mit Rang k
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

    def _rank(self, node: AVLNode[K, V] | None, key: K) -> int:
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
        """Gibt alle Schlüssel im AVL-Baum in sortierter Reihenfolge zurück.

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

    def _keys(self, node: AVLNode[K, V] | None, queue: Queue[K], lo: K, hi: K) -> None:
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
        queue: Queue[AVLNode[K, V] | None] = Queue()

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
        """Gibt eine String-Repräsentation des AVL-Baums zurück."""
        if self.is_empty():
            return "AVL()"
        keys = list(self.keys())
        return f"AVL({keys})"

    def __str__(self) -> str:
        """Gibt eine visuelle Baumdarstellung zurück.

        Returns:
            str: Mehrzeilige String-Repräsentation des Baums

        Beispiel:
            >>> avl = AVL()
            >>> for key in ["E", "B", "G", "A", "D", "F", "H"]:
            ...     avl.put(key, key.lower())
            >>> print(avl)
            E (h:2)
            ├── B (h:1)
            │   ├── A (h:0)
            │   └── D (h:0)
            └── G (h:1)
                ├── F (h:0)
                └── H (h:0)
        """
        if self.is_empty():
            return "AVL()"

        lines: list[str] = []
        if self._root is not None:
            lines.append(f"{self._root.key} (h:{self._root.height})")
            self._build_tree_children(self._root, "", lines)
        return "\n".join(lines)

    def _build_tree_children(
        self,
        node: AVLNode[K, V],
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
        children: list[AVLNode[K, V]] = []
        if node.left is not None:
            children.append(node.left)
        if node.right is not None:
            children.append(node.right)

        # Kinder ausgeben
        for i, child in enumerate(children):
            is_last = i == len(children) - 1
            connector = "└── " if is_last else "├── "
            lines.append(f"{prefix}{connector}{child.key} (h:{child.height})")

            # Präfix für Enkelkinder
            extension = "    " if is_last else "│   "
            new_prefix = prefix + extension
            self._build_tree_children(child, new_prefix, lines)


if __name__ == "__main__":
    import sys

    # Beispielprogramm: liest Zeichenketten von stdin und gibt sie sortiert aus
    print("AVL Tree Demo")
    print("Geben Sie Zeichenketten ein (eine pro Zeile), Strg+D zum Beenden:")

    st: AVL[str, int] = AVL()
    i = 0

    try:
        for line in sys.stdin:
            for key in line.split():
                st.put(key, i)
                i += 1

        if st.is_empty():
            print("\nDer Baum ist leer.")
        else:
            print("\nLevel-Order-Traversierung:")
            for s in st.level_order():
                print(f"{s} {st.get(s)}")

            print("\nSortierte Reihenfolge (In-Order):")
            for s in st.keys():
                print(f"{s} {st.get(s)}")

            print(f"\nGrösse: {st.size()}")
            print(f"Höhe: {st.height()}")
            print(f"Minimum: {st.min()}")
            print(f"Maximum: {st.max()}")

            print("\nVisuelle Baumdarstellung:")
            print(st)

    except KeyboardInterrupt:
        print("\nProgramm beendet")