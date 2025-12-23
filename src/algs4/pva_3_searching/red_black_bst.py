"""Red-Black BST - Rot-Schwarz-Baum (left-leaning)

Ein Rot-Schwarz-Baum ist ein selbstbalancierender binärer Suchbaum, der die
Balance durch Farbmarkierungen (rot/schwarz) der Kanten garantiert. Diese
Implementierung verwendet das "left-leaning" Prinzip von Robert Sedgewick.

Ein Rot-Schwarz-Baum entspricht einem 2-3-Baum:
- Schwarze Kanten: Normale Baum-Kanten
- Rote Kanten: Verbinden 2-Knoten zu 3-Knoten

Invarianten:
1. Rote Kanten sind immer links (left-leaning)
2. Keine zwei aufeinanderfolgenden roten Kanten
3. Perfekte schwarze Balance (gleiche Anzahl schwarzer Kanten zu jedem Blatt)

Zeitkomplexität (garantiert):
- get(key): O(log n)
- put(key, val): O(log n)
- delete(key): O(log n)
- min/max: O(log n)

Beispiele:
    >>> rbt = RedBlackBST()
    >>> rbt.put("S", 0)
    >>> rbt.put("E", 1)
    >>> rbt.put("A", 2)
    >>> rbt.get("E")
    1
    >>> rbt.size()
    3
"""

from collections.abc import Iterator

from src.algs4.pva_1_fundamentals.queue import Queue


class RBNode[K, V]:
    """Knoten im Rot-Schwarz-Baum.

    Attributes:
        key: Schlüssel des Knotens
        val: Wert des Knotens
        left: Linker Kindknoten (kleinere Schlüssel)
        right: Rechter Kindknoten (grössere Schlüssel)
        color: Farbe der Kante zum Elternknoten (True=rot, False=schwarz)
        n: Anzahl der Knoten im Teilbaum (inklusive diesem Knoten)
    """

    def __init__(self, key: K, val: V, color: bool, n: int) -> None:
        """
        Initialize a red–black tree node with the given key, value, color, and subtree size.
        
        Parameters:
            key (K): Node key.
            val (V): Node value.
            color (bool): Color of the link from this node to its parent — `True` = red, `False` = black.
            n (int): Number of nodes in the subtree rooted at this node (including this node).
        """
        self.key: K = key
        self.val: V = val
        self.color: bool = color  # True = rot, False = schwarz
        self.n: int = n
        self.left: RBNode[K, V] | None = None
        self.right: RBNode[K, V] | None = None


class RedBlackBST[K, V]:
    """Red-Black BST - Rot-Schwarz-Baum (left-leaning).

    Ein selbstbalancierender binärer Suchbaum basierend auf 2-3-Bäumen.
    Verwendet Farbmarkierungen statt expliziter 3-Knoten.

    Diese Implementierung folgt dem "left-leaning" Prinzip:
    - Rote Kanten zeigen immer nach links
    - Garantiert logarithmische Höhe
    - Einfacher als Standard-Rot-Schwarz-Bäume
    """

    RED = True
    BLACK = False

    def __init__(self) -> None:
        """Initialisiert einen leeren Rot-Schwarz-Baum."""
        self._root: RBNode[K, V] | None = None

    def _is_red(self, node: RBNode[K, V] | None) -> bool:
        """Prüft ob ein Knoten rot ist.

        Args:
            node: Zu prüfender Knoten

        Returns:
            bool: True wenn Knoten rot, False wenn schwarz oder None
        """
        if node is None:
            return False
        return node.color == self.RED

    def _size(self, node: RBNode[K, V] | None) -> int:
        """Gibt die Anzahl der Knoten im Teilbaum zurück.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            int: Anzahl der Knoten im Teilbaum
        """
        if node is None:
            return 0
        return node.n

    def size(self) -> int:
        """Gibt die Anzahl der Schlüssel-Wert-Paare zurück.

        Returns:
            int: Anzahl der Schlüssel-Wert-Paare
        """
        return self._size(self._root)

    def is_empty(self) -> bool:
        """Prüft, ob der Baum leer ist.

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

    def _height(self, node: RBNode[K, V] | None) -> int:
        """Rekursive Hilfsmethode für height.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            int: Höhe des Teilbaums
        """
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def contains(self, key: K) -> bool:
        """Prüft, ob der Schlüssel vorhanden ist.

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

    def _get(self, node: RBNode[K, V] | None, key: K) -> V | None:
        """Iterative Hilfsmethode für get.

        Args:
            node: Wurzel des Teilbaums
            key: Zu suchender Schlüssel

        Returns:
            V | None: Wert zum Schlüssel, oder None wenn nicht vorhanden
        """
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.val
        return None

    def put(self, key: K, val: V) -> None:
        """Fügt ein Schlüssel-Wert-Paar ein.

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
        self._root.color = self.BLACK  # Wurzel ist immer schwarz

    def _put(self, node: RBNode[K, V] | None, key: K, val: V) -> RBNode[K, V]:
        """Rekursive Hilfsmethode für put mit Balancierung.

        Args:
            node: Wurzel des Teilbaums
            key: Schlüssel
            val: Wert

        Returns:
            RBNode[K, V]: Balancierte Wurzel des Teilbaums
        """
        # Basis: neuen roten Knoten erstellen
        if node is None:
            return RBNode(key, val, self.RED, 1)

        # Rekursiv einfügen
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            # Schlüssel existiert bereits -> Wert aktualisieren
            node.val = val

        # Balancierung: fixiere rechtslastige rote Kanten
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and node.left and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        # Grösse aktualisieren
        node.n = self._size(node.left) + self._size(node.right) + 1
        return node

    def _rotate_left(self, node: RBNode[K, V]) -> RBNode[K, V]:
        """Führt eine Linksrotation durch.

        Macht eine rechtslastige rote Kante zu einer linkslastigen.

          h                x
         / \\(r)          (r)/ \\
        a   x    -->     h   c
           / \\          / \\
          b   c        a   b

        Args:
            node: Wurzel des zu rotierenden Teilbaums

        Returns:
            RBNode[K, V]: Neue Wurzel des Teilbaums
        """
        x = node.right
        assert x is not None

        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        x.n = node.n
        node.n = self._size(node.left) + self._size(node.right) + 1
        return x

    def _rotate_right(self, node: RBNode[K, V]) -> RBNode[K, V]:
        """Führt eine Rechtsrotation durch.

        Balanciert zwei aufeinanderfolgende linkslastige rote Kanten.

            h              x
          (r)/ \\          / \\(r)
           x   c   -->   a   h
          / \\              / \\
         a   b            b   c

        Args:
            node: Wurzel des zu rotierenden Teilbaums

        Returns:
            RBNode[K, V]: Neue Wurzel des Teilbaums
        """
        x = node.left
        assert x is not None

        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = self.RED
        x.n = node.n
        node.n = self._size(node.left) + self._size(node.right) + 1
        return x

    def _flip_colors(self, node: RBNode[K, V]) -> None:
        """Wechselt die Farben eines Knotens und seiner beiden Kinder.

        Spaltet einen temporären 4-Knoten in einen 2-Knoten mit zwei 2-Knoten.

        Args:
            node: Knoten dessen Farben gewechselt werden sollen
        """
        node.color = not node.color
        assert node.left is not None
        assert node.right is not None
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def delete_min(self) -> None:
        """Löscht das Schlüssel-Wert-Paar mit dem kleinsten Schlüssel.

        Raises:
            ValueError: wenn der Baum leer ist
        """
        if self.is_empty():
            raise ValueError("RB-Baum-Unterlauf: Baum ist leer")

        # Wenn beide Kinder der Wurzel schwarz sind, setze Wurzel auf rot
        if not self._is_red(self._root.left) and not self._is_red(self._root.right):
            self._root.color = self.RED

        self._root = self._delete_min(self._root)
        if not self.is_empty():
            self._root.color = self.BLACK

    def _delete_min(self, node: RBNode[K, V]) -> RBNode[K, V] | None:
        """Rekursive Hilfsmethode für delete_min.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            RBNode[K, V] | None: Balancierte Wurzel des Teilbaums
        """
        if node.left is None:
            return None

        if not self._is_red(node.left) and not self._is_red(node.left.left):
            node = self._move_red_left(node)

        node.left = self._delete_min(node.left)
        return self._balance(node)

    def delete_max(self) -> None:
        """Löscht das Schlüssel-Wert-Paar mit dem grössten Schlüssel.

        Raises:
            ValueError: wenn der Baum leer ist
        """
        if self.is_empty():
            raise ValueError("RB-Baum-Unterlauf: Baum ist leer")

        # Wenn beide Kinder der Wurzel schwarz sind, setze Wurzel auf rot
        if not self._is_red(self._root.left) and not self._is_red(self._root.right):
            self._root.color = self.RED

        self._root = self._delete_max(self._root)
        if not self.is_empty():
            self._root.color = self.BLACK

    def _delete_max(self, node: RBNode[K, V]) -> RBNode[K, V] | None:
        """Rekursive Hilfsmethode für delete_max.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            RBNode[K, V] | None: Balancierte Wurzel des Teilbaums
        """
        if self._is_red(node.left):
            node = self._rotate_right(node)

        if node.right is None:
            return None

        if not self._is_red(node.right) and not self._is_red(node.right.left):
            node = self._move_red_right(node)

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

        if not self.contains(key):
            return

        # Wenn beide Kinder der Wurzel schwarz sind, setze Wurzel auf rot
        if not self._is_red(self._root.left) and not self._is_red(self._root.right):
            self._root.color = self.RED

        self._root = self._delete(self._root, key)
        if not self.is_empty():
            self._root.color = self.BLACK

    def _delete(self, node: RBNode[K, V] | None, key: K) -> RBNode[K, V] | None:
        """Rekursive Hilfsmethode für delete.

        Args:
            node: Wurzel des Teilbaums
            key: Zu löschender Schlüssel

        Returns:
            RBNode[K, V] | None: Balancierte Wurzel des Teilbaums
        """
        if node is None:
            return None

        if key < node.key:
            if (
                node.left
                and not self._is_red(node.left)
                and not self._is_red(node.left.left)
            ):
                node = self._move_red_left(node)
            node.left = self._delete(node.left, key)
        else:
            if self._is_red(node.left):
                node = self._rotate_right(node)
            if key == node.key and node.right is None:
                return None
            if (
                node.right
                and not self._is_red(node.right)
                and not self._is_red(node.right.left)
            ):
                node = self._move_red_right(node)

            if key == node.key:
                # Ersetze durch Minimum des rechten Teilbaums
                x = self._min(node.right)
                node.key = x.key
                node.val = x.val
                node.right = self._delete_min(node.right)
            else:
                node.right = self._delete(node.right, key)

        return self._balance(node)

    def _move_red_left(self, node: RBNode[K, V]) -> RBNode[K, V]:
        """Macht node.left oder eines seiner Kinder rot.

        Annahme: node ist rot und beide node.left und node.left.left sind schwarz.

        Args:
            node: Aktueller Knoten

        Returns:
            RBNode[K, V]: Angepasster Knoten
        """
        self._flip_colors(node)
        if node.right and self._is_red(node.right.left):
            node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
            self._flip_colors(node)
        return node

    def _move_red_right(self, node: RBNode[K, V]) -> RBNode[K, V]:
        """Macht node.right oder eines seiner Kinder rot.

        Annahme: node ist rot und beide node.right und node.right.left sind schwarz.

        Args:
            node: Aktueller Knoten

        Returns:
            RBNode[K, V]: Angepasster Knoten
        """
        self._flip_colors(node)
        if node.left and self._is_red(node.left.left):
            node = self._rotate_right(node)
            self._flip_colors(node)
        return node

    def _balance(self, node: RBNode[K, V]) -> RBNode[K, V]:
        """Stellt die Rot-Schwarz-Baum-Invarianten wieder her.

        Args:
            node: Zu balancierender Knoten

        Returns:
            RBNode[K, V]: Balancierter Knoten
        """
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and node.left and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        node.n = self._size(node.left) + self._size(node.right) + 1
        return node

    def min(self) -> K:
        """Gibt den kleinsten Schlüssel zurück.

        Returns:
            K: Kleinster Schlüssel

        Raises:
            ValueError: wenn der Baum leer ist
        """
        if self.is_empty():
            raise ValueError("RB-Baum ist leer")
        return self._min(self._root).key

    def _min(self, node: RBNode[K, V]) -> RBNode[K, V]:
        """Gibt den Knoten mit dem kleinsten Schlüssel zurück.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            RBNode[K, V]: Knoten mit kleinstem Schlüssel
        """
        if node.left is None:
            return node
        return self._min(node.left)

    def max(self) -> K:
        """Gibt den grössten Schlüssel zurück.

        Returns:
            K: Grösster Schlüssel

        Raises:
            ValueError: wenn der Baum leer ist
        """
        if self.is_empty():
            raise ValueError("RB-Baum ist leer")
        return self._max(self._root).key

    def _max(self, node: RBNode[K, V]) -> RBNode[K, V]:
        """Gibt den Knoten mit dem grössten Schlüssel zurück.

        Args:
            node: Wurzel des Teilbaums

        Returns:
            RBNode[K, V]: Knoten mit grösstem Schlüssel
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

    def _floor(self, node: RBNode[K, V] | None, key: K) -> RBNode[K, V] | None:
        """Rekursive Hilfsmethode für floor.

        Args:
            node: Wurzel des Teilbaums
            key: Referenz-Schlüssel

        Returns:
            RBNode[K, V] | None: Knoten mit grösstem Schlüssel <= key
        """
        if node is None:
            return None

        if key == node.key:
            return node
        if key < node.key:
            return self._floor(node.left, key)

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

    def _ceiling(self, node: RBNode[K, V] | None, key: K) -> RBNode[K, V] | None:
        """Rekursive Hilfsmethode für ceiling.

        Args:
            node: Wurzel des Teilbaums
            key: Referenz-Schlüssel

        Returns:
            RBNode[K, V] | None: Knoten mit kleinstem Schlüssel >= key
        """
        if node is None:
            return None

        if key == node.key:
            return node
        if key > node.key:
            return self._ceiling(node.right, key)

        temp = self._ceiling(node.left, key)
        if temp is not None:
            return temp
        else:
            return node

    def select(self, k: int) -> K:
        """Gibt den k-t-kleinsten Schlüssel zurück.

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

    def _select(self, node: RBNode[K, V] | None, k: int) -> RBNode[K, V] | None:
        """Rekursive Hilfsmethode für select.

        Args:
            node: Wurzel des Teilbaums
            k: Rang

        Returns:
            RBNode[K, V] | None: Knoten mit Rang k
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

    def _rank(self, node: RBNode[K, V] | None, key: K) -> int:
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
        """Gibt alle Schlüssel in sortierter Reihenfolge zurück.

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

    def _keys(self, node: RBNode[K, V] | None, queue: Queue[K], lo: K, hi: K) -> None:
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
        queue: Queue[RBNode[K, V] | None] = Queue()

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
        """Gibt eine String-Repräsentation zurück."""
        if self.is_empty():
            return "RedBlackBST()"
        keys = list(self.keys())
        return f"RedBlackBST({keys})"

    def __str__(self) -> str:
        """Gibt eine visuelle Baumdarstellung zurück.

        Returns:
            str: Mehrzeilige String-Repräsentation des Baums mit Farbmarkierungen

        Beispiel:
            >>> rbt = RedBlackBST()
            >>> for key in ["E", "B", "G", "A", "D", "F", "H"]:
            ...     rbt.put(key, key.lower())
            >>> print(rbt)
            E (B)
            ├── B (R)
            │   ├── A (B)
            │   └── D (B)
            └── G (B)
                ├── F (B)
                └── H (B)
        """
        if self.is_empty():
            return "RedBlackBST()"

        lines: list[str] = []
        if self._root is not None:
            color_str = "R" if self._root.color == self.RED else "B"
            lines.append(f"{self._root.key} ({color_str})")
            self._build_tree_children(self._root, "", lines)
        return "\n".join(lines)

    def _build_tree_children(
        self,
        node: RBNode[K, V],
        prefix: str,
        lines: list[str],
    ) -> None:
        """Rekursive Hilfsmethode zum Aufbau der Baumdarstellung.

        Args:
            node: Aktueller Knoten
            prefix: Präfix für die Einrückung
            lines: Liste der Ausgabezeilen
        """
        # Kinder sammeln
        children: list[RBNode[K, V]] = []
        if node.left is not None:
            children.append(node.left)
        if node.right is not None:
            children.append(node.right)

        # Kinder ausgeben
        for i, child in enumerate(children):
            is_last = i == len(children) - 1
            connector = "└── " if is_last else "├── "
            color_str = "R" if child.color == self.RED else "B"
            lines.append(f"{prefix}{connector}{child.key} ({color_str})")

            # Präfix für Enkelkinder
            extension = "    " if is_last else "│   "
            new_prefix = prefix + extension
            self._build_tree_children(child, new_prefix, lines)


if __name__ == "__main__":
    import sys

    # Beispielprogramm: liest Zeichenketten von stdin und gibt sie sortiert aus
    print("Red-Black BST Demo")
    print("Geben Sie Zeichenketten ein (eine pro Zeile), Strg+D zum Beenden:")

    st: RedBlackBST[str, int] = RedBlackBST()
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