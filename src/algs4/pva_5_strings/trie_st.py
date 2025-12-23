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
        """
        Create an empty TrieST instance.
        
        Initializes internal state so the trie has no root node and contains zero key-value pairs.
        """
        self._root: _Node[V] | None = None
        self._n: int = 0  # Anzahl der Schlüssel-Wert-Paare

    def size(self) -> int:
        """
        Return the number of key-value pairs stored in the trie.
        
        Returns:
            int: Number of key-value pairs stored.
        """
        return self._n

    def __len__(self) -> int:
        """
        Report the number of key-value pairs stored in the trie.
        
        Returns:
            int: Number of key-value pairs stored in the trie.
        """
        return self._n

    def is_empty(self) -> bool:
        """
        Determine whether the trie contains no key-value pairs.
        
        Returns:
            `true` if the trie contains no key-value pairs, `false` otherwise.
        """
        return self._n == 0

    def contains(self, key: str) -> bool:
        """
        Determine whether the Trie contains the given key.
        
        Parameters:
            key (str): The string key to look up.
        
        Returns:
            `true` if the key exists, `false` otherwise.
        
        Raises:
            ValueError: If `key` is None.
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        return self.get(key) is not None

    def get(self, key: str) -> V | None:
        """
        Retrieve the value associated with the given key.
        
        Parameters:
            key (str): The string key to look up; must not be None.
        
        Returns:
            `V` if the key exists, `None` otherwise.
        
        Raises:
            ValueError: If `key` is None.
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        node = self._get(self._root, key, 0)
        if node is None:
            return None
        return node.val

    def _get(self, node: _Node[V] | None, key: str, depth: int) -> _Node[V] | None:
        """
        Locate the trie node that corresponds to the given key starting from the provided node and depth.
        
        Parameters:
            node (_Node[V] | None): The node from which to start the search.
            key (str): The string key to locate.
            depth (int): The current index in `key` indicating the character to examine.
        
        Returns:
            _Node[V] | None: The node matching the key (when `depth == len(key)`), or `None` if no such path exists.
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
        """
        Insert or update the value associated with the given key in the trie.
        
        If the key already exists, its value is replaced.
        
        Parameters:
            key (str): The key to insert; must not be None.
            val (V): The value to store for the key.
        
        Raises:
            ValueError: If `key` is None.
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        self._root = self._put(self._root, key, val, 0)

    def _put(self, node: _Node[V] | None, key: str, val: V, depth: int) -> _Node[V]:
        """
        Insert or update the value for `key` in the trie and return the node that roots this subtree.
        
        Parameters:
            node (_Node[V] | None): Current node for this subtree (may be None).
            key (str): The string key to insert or update.
            val (V): The value to associate with `key`.
            depth (int): Current index in `key` indicating the position being processed.
        
        Returns:
            _Node[V]: The updated node representing the root of this subtree.
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
        """
        Remove a key and its associated value from the trie.
        
        If the key exists, removes its stored value, prunes any now-empty nodes, and updates the trie size counter.
        
        Args:
            key (str): The key to remove.
        
        Raises:
            ValueError: If `key` is None.
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
        """
        Return an iterator over every key stored in the trie.
        
        Returns:
            Iterator[str]: An iterator yielding all keys in lexicographic order.
        """
        return self.keys_with_prefix("")

    def keys_with_prefix(self, prefix: str) -> Iterator[str]:
        """
        Collects all keys in the trie that start with the given prefix.
        
        Parameters:
            prefix (str): The prefix to match; must not be None.
        
        Returns:
            Iterator[str]: An iterator over keys that begin with `prefix`.
        
        Raises:
            ValueError: If `prefix` is None.
        """
        if prefix is None:
            raise ValueError("Präfix darf nicht None sein")
        queue: Queue[str] = Queue()
        node = self._get(self._root, prefix, 0)
        self._collect(node, prefix, queue)
        return iter(queue)

    def _collect(self, node: _Node[V] | None, prefix: str, queue: Queue[str]) -> None:
        """
        Collect all keys in the subtrie rooted at `node` and enqueue each complete key prefixed by `prefix` into `queue`.
        
        Parameters:
            node (_Node[V] | None): Root of the subtrie to traverse; if None, nothing is enqueued.
            prefix (str): Current key prefix for this subtree.
            queue (Queue[str]): Queue used to collect matching keys; each full key is enqueued as a string.
        """
        if node is None:
            return
        if node.val is not None:
            queue.enqueue(prefix)
        for char in sorted(node.children.keys()):
            self._collect(node.children[char], prefix + char, queue)

    def keys_that_match(self, pattern: str) -> Iterator[str]:
        """
        Finds all keys that match a pattern using '.' as a single-character wildcard.
        
        Parameters:
            pattern (str): Search pattern where '.' matches any single character.
        
        Returns:
            An iterator over keys that match the pattern.
        
        Raises:
            ValueError: If `pattern` is None.
        """
        if pattern is None:
            raise ValueError("Muster darf nicht None sein")
        queue: Queue[str] = Queue()
        self._collect_match(self._root, "", pattern, queue)
        return iter(queue)

    def _collect_match(
        self, node: _Node[V] | None, prefix: str, pattern: str, queue: Queue[str]
    ) -> None:
        """
        Collects keys in the subtrie that match a pattern where '.' matches any single character.
        
        Traverses the subtrie rooted at `node`, extending `prefix` as it descends, and enqueues each key that matches `pattern` into `queue`.
        
        Parameters:
        	node (_Node[V] | None): Subtrie root to search; if None nothing is enqueued.
        	prefix (str): String accumulated from the root to the current node.
        	pattern (str): Pattern to match against; '.' is a wildcard matching any single character.
        	queue (Queue[str]): Queue to receive matching keys.
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
        """
        Return the longest key stored in the trie that is a prefix of the given query.
        
        Parameters:
            query (str): The query string to search for a key-prefix.
        
        Returns:
            str: The longest key in the trie that is a prefix of `query`, or an empty string if no such key exists.
        
        Raises:
            ValueError: If `query` is None.
        """
        if query is None:
            raise ValueError("Query darf nicht None sein")
        length = self._search(self._root, query, 0, 0)
        return query[:length]

    def _search(
        self, node: _Node[V] | None, query: str, depth: int, length: int
    ) -> int:
        """
        Find the length of the longest key in the subtree rooted at `node` that is a prefix of `query`.
        
        Parameters:
            node (_Node[V] | None): Subtrie root to search.
            query (str): Query string whose prefix is being matched.
            depth (int): Current depth in `query` corresponding to `node`.
            length (int): Length of the longest matching key found so far.
        
        Returns:
            int: Number of characters of the longest key in the subtree that is a prefix of `query`.
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
        """
        Provide an iterator over all keys in the trie.
        
        Returns:
            Iterator[str]: An iterator that yields each stored key.
        """
        return self.keys()

    def __repr__(self) -> str:
        """
        Return a concise textual representation of the trie.
        
        The representation is:
        - "TrieST(empty)" when the trie contains no keys.
        - "TrieST([keys])" when the trie contains 10 or fewer keys (shows all keys).
        - "TrieST([first 10 keys]... {n} total)" when the trie contains more than 10 keys (shows the first 10 and the total count).
        
        Returns:
            str: The textual representation of the trie.
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