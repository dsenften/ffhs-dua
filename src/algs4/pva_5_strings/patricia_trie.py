"""Patricia Trie - Kompakter Trie für String-Speicherung

Patricia (Practical Algorithm to Retrieve Information Coded in Alphanumeric)
ist eine platzsparende Variante des Trie, bei der Knoten mit nur einem Kind
mit dem Kind verschmolzen werden. Die Kanten speichern Strings statt einzelner
Zeichen.

Zeitkomplexität:
- get(key): O(m), wobei m = Länge des Schlüssels
- put(key, val): O(m), wobei m = Länge des Schlüssels
- delete(key): O(m), wobei m = Länge des Schlüssels

Speicheroptimierung:
- Reduziert die Anzahl der Knoten bei langen gemeinsamen Präfixen
- Besonders effizient bei Daten mit vielen ähnlichen Schlüsseln

Hinweis:
    Dies ist eine vereinfachte Patricia-Trie Implementierung für akademische
    Zwecke. Sie demonstriert das Konzept der Pfadkompression.

Beispiele:
    >>> pt = PatriciaTrie()
    >>> pt.put("test", 1)
    >>> pt.put("testing", 2)
    >>> pt.get("test")
    1
    >>> pt.size()
    2
"""

from collections.abc import Iterator

from src.algs4.pva_1_fundamentals.queue import Queue


class _PatriciaNode[V]:
    """Knoten im Patricia-Trie.

    Attributes:
        val: Wert des Knotens (None wenn Knoten keinen Schlüssel repräsentiert)
        children: Dictionary von Kantenbeschriftungen zu Kind-Knoten
        prefix: Gemeinsamer Präfix, der in diesem Knoten gespeichert ist
    """

    def __init__(self, prefix: str = "") -> None:
        """
        Create a Patricia Trie node with an optional prefix.
        
        Parameters:
            prefix (str): The string prefix stored at this node (defaults to empty string).
        """
        self.val: V | None = None
        self.children: dict[str, _PatriciaNode[V]] = {}
        self.prefix: str = prefix


class PatriciaTrie[V]:
    """Patricia Trie - Kompakter String-basierter Symbol-Table.

    Ein platzsparender Symbol-Table für String-Schlüssel, bei dem Knoten
    mit nur einem Kind verschmolzen werden. Die Kanten speichern Strings
    statt einzelner Zeichen.

    Diese Implementierung ist eine vereinfachte Version, die das Konzept
    der Pfadkompression demonstriert.
    """

    def __init__(self) -> None:
        """
        Create an empty Patricia trie.
        
        Initializes the internal root reference to None and the stored key count to 0.
        """
        self._root: _PatriciaNode[V] | None = None
        self._n: int = 0  # Anzahl der Schlüssel-Wert-Paare

    def size(self) -> int:
        """
        Return the number of key-value pairs stored in the trie.
        
        Returns:
            int: The number of stored key-value pairs.
        """
        return self._n

    def __len__(self) -> int:
        """
        Return the number of stored key-value pairs.
        
        Returns:
            The number of stored key-value pairs.
        """
        return self._n

    def is_empty(self) -> bool:
        """
        Check whether the trie contains no key-value pairs.
        
        Returns:
            bool: `True` if the trie contains no entries, `False` otherwise.
        """
        return self._n == 0

    def contains(self, key: str) -> bool:
        """
        Check whether the trie contains the specified key.
        
        Parameters:
            key (str): The key to look up; must not be None.
        
        Returns:
            True if the key exists in the trie, False otherwise.
        
        Raises:
            ValueError: If `key` is None.
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")
        return self.get(key) is not None

    def get(self, key: str) -> V | None:
        """
        Retrieve the value associated with the given key in the trie.
        
        Parameters:
            key (str): The key to look up; must not be None.
        
        Returns:
            V | None: The value associated with `key`, or `None` if the key is not stored.
        
        Raises:
            ValueError: If `key` is None.
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")

        if self._root is None:
            return None

        node = self._root
        remaining = key

        while True:
            # Prüfe ob Präfix übereinstimmt
            if not remaining.startswith(node.prefix):
                return None

            # Entferne den Präfix
            remaining = remaining[len(node.prefix) :]

            # Wenn nichts mehr übrig ist, sind wir am Ziel
            if not remaining:
                return node.val

            # Suche nach passendem Kind
            first_char = remaining[0]
            if first_char not in node.children:
                return None

            node = node.children[first_char]

    def put(self, key: str, val: V) -> None:
        """
        Insert or update a key-value pair in the trie.
        
        Parameters:
            key (str): The key to insert or update.
            val (V): The value to associate with the key.
        
        Raises:
            ValueError: If `key` is None.
        
        Notes:
            If the key was not previously present, the trie's size is incremented.
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")

        if self._root is None:
            self._root = _PatriciaNode(key)
            self._root.val = val
            self._n += 1
            return

        # Navigiere zum richtigen Knoten und füge ein
        self._root = self._put(self._root, key, val)

    def _put(self, node: _PatriciaNode[V], key: str, val: V) -> _PatriciaNode[V]:
        """
        Insert or update the given key and value into the subtree rooted at the provided node and return the updated subtree root.
        
        Parameters:
            node (_PatriciaNode[V]): Current subtree root whose prefix may be matched, split, or extended.
            key (str): Portion of the key remaining to insert relative to this node.
            val (V): Value to associate with the key.
        
        Returns:
            _PatriciaNode[V]: The updated node representing the root of this subtree.
        
        Notes:
            This method updates the trie's size counter (self._n) when a new key is created.
        """
        # Finde längsten gemeinsamen Präfix
        common_len = 0
        for i in range(min(len(key), len(node.prefix))):
            if key[i] == node.prefix[i]:
                common_len += 1
            else:
                break

        # Fall 1: Schlüssel ist exakt der Präfix
        if common_len == len(key) == len(node.prefix):
            if node.val is None:
                self._n += 1
            node.val = val
            return node

        # Fall 2: Schlüssel ist länger als Präfix
        if common_len == len(node.prefix):
            remaining = key[common_len:]
            first_char = remaining[0]

            if first_char in node.children:
                node.children[first_char] = self._put(
                    node.children[first_char], remaining, val
                )
            else:
                new_node = _PatriciaNode(remaining)
                new_node.val = val
                node.children[first_char] = new_node
                self._n += 1

            return node

        # Fall 3: Knoten muss aufgespalten werden
        # Erstelle neuen Knoten für gemeinsamen Präfix
        split_node = _PatriciaNode(node.prefix[:common_len])

        # Alter Knoten-Präfix wird gekürzt
        old_prefix_remaining = node.prefix[common_len:]
        node.prefix = old_prefix_remaining

        # Neuer Knoten für den Schlüssel
        key_remaining = key[common_len:]

        if not key_remaining:
            # Der Schlüssel endet beim gemeinsamen Präfix
            split_node.val = val
            self._n += 1
            split_node.children[old_prefix_remaining[0]] = node
        else:
            # Beide Zweige fortsetzen
            new_node = _PatriciaNode(key_remaining)
            new_node.val = val
            self._n += 1

            split_node.children[old_prefix_remaining[0]] = node
            split_node.children[key_remaining[0]] = new_node

        return split_node

    def delete(self, key: str) -> None:
        """
        Delete the key and its associated value from the trie, cleaning up nodes and applying path compression.
        
        Removes the stored value at the key's terminal node if present; prunes leaf nodes that become empty and merges nodes that have exactly one child to preserve the Patricia trie’s compressed paths.
        
        Parameters:
            key (str): The key to remove; must not be None.
        
        Raises:
            ValueError: If `key` is None.
        """
        if key is None:
            raise ValueError("Schlüssel darf nicht None sein")

        if self._root is None:
            return  # Nichts zu löschen

        # Versuche zu löschen
        result = self._delete(self._root, key)
        if result is None:
            self._root = None
        else:
            self._root = result

    def _delete(self, node: _PatriciaNode[V], key: str) -> _PatriciaNode[V] | None:
        """
        Recursively removes a key from the subtree rooted at `node`, updating trie structure and size.
        
        Parameters:
            node (_PatriciaNode[V]): The current subtree root being examined.
            key (str): The remaining portion of the key to delete, relative to `node`'s prefix.
        
        Returns:
            _PatriciaNode[V] | None: The updated subtree root after deletion, or `None` if the subtree becomes empty.
        
        Notes:
            - If the key is found, `self._n` is decremented.
            - The method prunes empty nodes and merges single-child nodes with their child to preserve path compression.
            - If the key is not present in this subtree, the original `node` is returned unchanged.
        """
        # Prüfe ob Präfix übereinstimmt
        if not key.startswith(node.prefix):
            return node  # Schlüssel nicht gefunden, nichts ändern

        # Entferne den Präfix
        remaining = key[len(node.prefix) :]

        # Wenn nichts mehr übrig ist, sind wir am Ziel
        if not remaining:
            if node.val is not None:
                node.val = None
                self._n -= 1

                # Aufräumen: Wenn Knoten keine Kinder hat, löschen
                if not node.children:
                    return None

                # Wenn Knoten nur ein Kind hat, verschmelzen
                if len(node.children) == 1:
                    child_char, child = next(iter(node.children.items()))
                    # Verschmelze: Präfixe kombinieren
                    # child.prefix beginnt bereits mit child_char, daher nicht doppelt hinzufügen
                    child.prefix = node.prefix + child.prefix
                    return child

            return node

        # Suche nach passendem Kind
        first_char = remaining[0]
        if first_char not in node.children:
            return node  # Schlüssel nicht gefunden

        # Rekursiv im Kind löschen
        child_result = self._delete(node.children[first_char], remaining)

        if child_result is None:
            # Kind wurde gelöscht
            del node.children[first_char]

            # Aufräumen: Wenn dieser Knoten jetzt leer ist und keinen Wert hat
            if not node.children and node.val is None:
                return None

            # Wenn nur ein Kind übrig ist und dieser Knoten keinen Wert hat, verschmelzen
            if len(node.children) == 1 and node.val is None:
                child_char, child = next(iter(node.children.items()))
                # child.prefix beginnt bereits mit child_char, daher nicht doppelt hinzufügen
                child.prefix = node.prefix + child.prefix
                return child
        else:
            node.children[first_char] = child_result

        return node

    def keys(self) -> Iterator[str]:
        """
        Iterate over all stored keys in sorted order.
        
        Returns:
            Iterator[str]: An iterator over every key contained in the trie, yielded in sorted order.
        """
        queue: Queue[str] = Queue()
        if self._root is not None:
            self._collect(self._root, "", queue)
        return iter(queue)

    def _collect(self, node: _PatriciaNode[V], prefix: str, queue: Queue[str]) -> None:
        """
        Collects all keys in the subtree rooted at `node` and enqueues each full key into `queue` in lexicographic order.
        
        Parameters:
            node (_PatriciaNode[V]): Root of the subtree to traverse.
            prefix (str): Accumulated key prefix that precedes `node.prefix`.
            queue (Queue[str]): Destination queue; each discovered full key is enqueued.
        """
        current_key = prefix + node.prefix

        if node.val is not None:
            queue.enqueue(current_key)

        for char in sorted(node.children.keys()):
            self._collect(node.children[char], current_key, queue)

    def __iter__(self) -> Iterator[str]:
        """
        Iterate over all stored keys in sorted order.
        
        Returns:
            Iterator[str]: An iterator that yields every key in the trie in sorted order.
        """
        return self.keys()

    def __repr__(self) -> str:
        """
        Return a concise, human-readable string representation of the trie.
        
        The representation is:
        - "PatriciaTrie(empty)" when the trie contains no keys.
        - "PatriciaTrie([...])" listing all keys when there are 10 or fewer keys.
        - "PatriciaTrie([first_10_keys]... N total)" showing the first 10 keys followed by the total count when there are more than 10 keys.
        
        Returns:
            str: The formatted string representation.
        """
        if self.is_empty():
            return "PatriciaTrie(empty)"
        keys_list = list(self.keys())
        if len(keys_list) <= 10:
            return f"PatriciaTrie({keys_list})"
        return f"PatriciaTrie({keys_list[:10]}... {self._n} total)"


if __name__ == "__main__":
    import sys

    # CLI-Interface für Patricia Trie
    pt: PatriciaTrie[int] = PatriciaTrie()
    i = 0

    # Lese Wörter von stdin
    for line in sys.stdin:
        for word in line.split():
            pt.put(word, i)
            i += 1

    # Gebe alle Schlüssel-Wert-Paare aus (wenn weniger als 100)
    if pt.size() < 100:
        print("Alle Schlüssel-Wert-Paare:")
        for key in pt.keys():
            print(f"{key}: {pt.get(key)}")
        print()

    print(f"\nAnzahl der Einträge: {pt.size()}")
    print(f"Repräsentation: {repr(pt)}")