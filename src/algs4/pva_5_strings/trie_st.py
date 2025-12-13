"""Trie Symbol Table - String-basierte Symbol-Tabelle

Ein Trie (abgeleitet von "retrieval") ist ein Baum, dessen Kanten mit Zeichen
beschriftet sind. Die Position eines Knotens im Baum bestimmt den Schlüssel,
den er repräsentiert. Die Suchzeit hängt ausschliesslich von der Länge des
Suchschlüssels ab, nicht von der Anzahl der Einträge im Trie.

Zeitkomplexität:
- get(key): O(m), wobei m = Länge des Schlüssels
- put(key, val): O(m), wobei m = Länge des Schlüssels
- delete(key): O(m), wobei m = Länge des Schlüssels
- Alle Operationen sind unabhängig von der Anzahl n der Einträge!

Vorteile:
- Suchzeit unabhängig von der Datenmenge
- Keine teuren String-Vergleiche
- Natürliche Unterstützung für Präfix-Operationen
- Speichereffizient bei gemeinsamen Präfixen

Beispiele:
    >>> st = TrieST()
    >>> st.put("sea", 1)
    >>> st.put("sells", 2)
    >>> st.put("she", 3)
    >>> st.get("sea")
    1
    >>> st.size()
    3
    >>> list(st.keys_with_prefix("se"))
    ['sea', 'sells']
"""

from collections.abc import Iterator

from src.algs4.pva_1_fundamentals.queue import Queue


class _Node[V]:
    """Knoten im Trie.

    Attributes:
        val: Wert des Knotens (None wenn Knoten keinen Schlüssel repräsentiert)
        children: Dictionary von Zeichen zu Kind-Knoten
    """

    def __init__(self) -> None:
        """Initialisiert einen neuen Knoten."""
        self.val: V | None = None
        self.children: dict[str, _Node[V]] = {}


class TrieST[V]:
    """Trie Symbol Table - String-basierte Symbol-Tabelle.

    Ein geordneter Symbol-Table für String-Schlüssel, implementiert als Trie.
    Die Suchzeit hängt nur von der Schlüssellänge ab, nicht von der Anzahl
    der Einträge.

    Diese Implementierung verwendet ein Dictionary für die Kind-Knoten,
    was flexibel für beliebige Zeichen ist (nicht nur ASCII).
    """

    def __init__(self) -> None:
        """Initialisiert einen leeren Trie."""
        self._root: _Node[V] | None = None
        self._n: int = 0  # Anzahl der Schlüssel-Wert-Paare

    def size(self) -> int:
        """Gibt die Anzahl der Schlüssel-Wert-Paare im Trie zurück.

        Returns:
            int: Anzahl der Schlüssel-Wert-Paare
        """
        return self._n

    def __len__(self) -> int:
        """Gibt die Anzahl der Schlüssel-Wert-Paare im Trie zurück.

        Returns:
            int: Anzahl der Schlüssel-Wert-Paare
        """
        return self._n

    def is_empty(self) -> bool:
        """Prüft, ob der Trie leer ist.

        Returns:
            bool: True wenn leer, False sonst
        """
        return self._n == 0

    def contains(self, key: str) -> bool:
        """Prüft, ob der Trie den Schlüssel enthält.

        Args:
            key: Der zu suchende Schlüssel

        Returns:
            bool: True wenn der Schlüssel enthalten ist, False sonst

        Raises:
            ValueError: Wenn der Schlüssel None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        return self.get(key) is not None

    def get(self, key: str) -> V | None:
        """Gibt den Wert zurück, der mit dem Schlüssel verknüpft ist.

        Args:
            key: Der zu suchende Schlüssel

        Returns:
            V | None: Der verknüpfte Wert oder None wenn nicht gefunden

        Raises:
            ValueError: Wenn der Schlüssel None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        node = self._get(self._root, key, 0)
        if node is None:
            return None
        return node.val

    def _get(self, node: _Node[V] | None, key: str, depth: int) -> _Node[V] | None:
        """Hilfsmethode für get - sucht rekursiv nach einem Knoten.

        Args:
            node: Aktueller Knoten
            key: Der zu suchende Schlüssel
            depth: Aktuelle Tiefe im Trie (Index in key)

        Returns:
            _Node[V] | None: Der Knoten mit dem Schlüssel oder None
        """
        if node is None:
            return None
        if depth == len(key):
            return node
        char = key[depth]
        if char not in node.children:
            return None
        return self._get(node.children[char], key, depth + 1)

    def put(self, key: str, val: V) -> None:
        """Fügt ein Schlüssel-Wert-Paar in den Trie ein.

        Überschreibt den alten Wert, wenn der Schlüssel bereits vorhanden ist.

        Args:
            key: Der Schlüssel
            val: Der zu speichernde Wert

        Raises:
            ValueError: Wenn der Schlüssel None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        self._root = self._put(self._root, key, val, 0)

    def _put(self, node: _Node[V] | None, key: str, val: V, depth: int) -> _Node[V]:
        """Hilfsmethode für put - fügt rekursiv einen Schlüssel ein.

        Args:
            node: Aktueller Knoten
            key: Der Schlüssel
            val: Der zu speichernde Wert
            depth: Aktuelle Tiefe im Trie (Index in key)

        Returns:
            _Node[V]: Der aktualisierte Knoten
        """
        if node is None:
            node = _Node()
        if depth == len(key):
            if node.val is None:
                self._n += 1  # Neuer Schlüssel
            node.val = val
            return node
        char = key[depth]
        if char not in node.children:
            node.children[char] = _Node()
        node.children[char] = self._put(node.children[char], key, val, depth + 1)
        return node

    def delete(self, key: str) -> None:
        """Löscht den Schlüssel und den zugehörigen Wert aus dem Trie.

        Args:
            key: Der zu löschende Schlüssel

        Raises:
            ValueError: Wenn der Schlüssel None ist
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        self._root = self._delete(self._root, key, 0)

    def _delete(self, node: _Node[V] | None, key: str, depth: int) -> _Node[V] | None:
        """Hilfsmethode für delete - löscht rekursiv einen Schlüssel.

        Args:
            node: Aktueller Knoten
            key: Der zu löschende Schlüssel
            depth: Aktuelle Tiefe im Trie (Index in key)

        Returns:
            _Node[V] | None: Der aktualisierte Knoten oder None
        """
        if node is None:
            return None

        if depth == len(key):
            if node.val is not None:
                self._n -= 1
            node.val = None
        else:
            char = key[depth]
            if char in node.children:
                node.children[char] = self._delete(node.children[char], key, depth + 1)
                # Entferne leere Kind-Knoten
                if node.children[char] is None:
                    del node.children[char]

        # Wenn Knoten keinen Wert hat und keine Kinder, kann er entfernt werden
        if node.val is None and len(node.children) == 0:
            return None

        return node

    def keys(self) -> Iterator[str]:
        """Gibt alle Schlüssel im Trie zurück.

        Returns:
            Iterator[str]: Iterator über alle Schlüssel in lexikographischer Reihenfolge
        """
        return self.keys_with_prefix("")

    def keys_with_prefix(self, prefix: str) -> Iterator[str]:
        """Gibt alle Schlüssel zurück, die mit dem Präfix beginnen.

        Args:
            prefix: Der Präfix

        Returns:
            Iterator[str]: Iterator über alle Schlüssel mit dem Präfix

        Raises:
            ValueError: Wenn der Präfix None ist
        """
        if prefix is None:
            raise ValueError("Präfix darf nicht None sein")
        queue: Queue[str] = Queue()
        node = self._get(self._root, prefix, 0)
        self._collect(node, prefix, queue)
        return iter(queue)

    def _collect(self, node: _Node[V] | None, prefix: str, queue: Queue[str]) -> None:
        """Sammelt alle Schlüssel im Teilbaum.

        Args:
            node: Wurzel des Teilbaums
            prefix: Aktueller Präfix
            queue: Queue zum Sammeln der Schlüssel
        """
        if node is None:
            return
        if node.val is not None:
            queue.enqueue(prefix)
        for char in sorted(node.children.keys()):
            self._collect(node.children[char], prefix + char, queue)

    def keys_that_match(self, pattern: str) -> Iterator[str]:
        """Gibt alle Schlüssel zurück, die dem Muster entsprechen.

        Das Zeichen '.' im Muster steht für ein beliebiges Zeichen.

        Args:
            pattern: Das Suchmuster (z.B. ".he.l.")

        Returns:
            Iterator[str]: Iterator über alle passenden Schlüssel

        Raises:
            ValueError: Wenn das Muster None ist
        """
        if pattern is None:
            raise ValueError("Muster darf nicht None sein")
        queue: Queue[str] = Queue()
        self._collect_match(self._root, "", pattern, queue)
        return iter(queue)

    def _collect_match(
        self, node: _Node[V] | None, prefix: str, pattern: str, queue: Queue[str]
    ) -> None:
        """Sammelt alle Schlüssel, die dem Muster entsprechen.

        Args:
            node: Aktueller Knoten
            prefix: Aktueller Präfix
            pattern: Das Suchmuster
            queue: Queue zum Sammeln der Schlüssel
        """
        if node is None:
            return

        depth = len(prefix)
        if depth == len(pattern):
            if node.val is not None:
                queue.enqueue(prefix)
            return

        char = pattern[depth]
        if char == ".":
            # Wildcard - durchsuche alle Kinder
            for c in sorted(node.children.keys()):
                self._collect_match(node.children[c], prefix + c, pattern, queue)
        elif char in node.children:
            self._collect_match(node.children[char], prefix + char, pattern, queue)

    def longest_prefix_of(self, query: str) -> str:
        """Gibt den längsten Schlüssel zurück, der ein Präfix von query ist.

        Args:
            query: Die Abfragezeichenfolge

        Returns:
            str: Der längste Präfix-Schlüssel oder "" wenn keiner gefunden

        Raises:
            ValueError: Wenn die Query None ist
        """
        if query is None:
            raise ValueError("Query darf nicht None sein")
        length = self._search(self._root, query, 0, 0)
        return query[:length]

    def _search(
        self, node: _Node[V] | None, query: str, depth: int, length: int
    ) -> int:
        """Hilfsmethode für longest_prefix_of.

        Args:
            node: Aktueller Knoten
            query: Die Abfragezeichenfolge
            depth: Aktuelle Tiefe
            length: Länge des längsten gefundenen Präfix

        Returns:
            int: Länge des längsten Präfix
        """
        if node is None:
            return length
        if node.val is not None:
            length = depth
        if depth == len(query):
            return length
        char = query[depth]
        if char not in node.children:
            return length
        return self._search(node.children[char], query, depth + 1, length)

    def __iter__(self) -> Iterator[str]:
        """Gibt einen Iterator über alle Schlüssel zurück.

        Returns:
            Iterator[str]: Iterator über alle Schlüssel
        """
        return self.keys()

    def __repr__(self) -> str:
        """Gibt eine String-Repräsentation des Tries zurück.

        Returns:
            str: String-Repräsentation
        """
        if self.is_empty():
            return "TrieST(empty)"
        keys_list = list(self.keys())
        if len(keys_list) <= 10:
            return f"TrieST({keys_list})"
        return f"TrieST({keys_list[:10]}... {self._n} total)"


if __name__ == "__main__":
    import sys

    # CLI-Interface für Trie Symbol Table
    st: TrieST[int] = TrieST()
    i = 0

    # Lese Wörter von stdin
    for line in sys.stdin:
        for word in line.split():
            st.put(word, i)
            i += 1

    # Gebe alle Schlüssel-Wert-Paare aus (wenn weniger als 100)
    if st.size() < 100:
        print("Alle Schlüssel-Wert-Paare:")
        for key in st.keys():
            print(f"{key}: {st.get(key)}")
        print()

    # Teste longest_prefix_of
    print('longest_prefix_of("shellsort"):')
    print(st.longest_prefix_of("shellsort"))
    print()

    print('longest_prefix_of("quicksort"):')
    print(st.longest_prefix_of("quicksort"))
    print()

    # Teste keys_with_prefix
    print('keys_with_prefix("shor"):')
    for s in st.keys_with_prefix("shor"):
        print(s)
    print()

    # Teste keys_that_match
    print('keys_that_match(".he.l."):')
    for s in st.keys_that_match(".he.l."):
        print(s)
    print()
