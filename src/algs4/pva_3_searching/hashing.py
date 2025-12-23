"""Hash Tables - Hash-Tabellen mit Separate Chaining und Linear Probing

Hash-Tabellen sind Datenstrukturen zur effizienten Speicherung und Suche von
Schlüssel-Wert-Paaren. Sie verwenden eine Hash-Funktion, um Schlüssel in
Array-Indizes umzuwandeln.

Zwei Hauptstrategien zur Kollisionsbehandlung:
1. Separate Chaining: Jeder Array-Eintrag ist eine verkettete Liste
2. Linear Probing: Bei Kollisionen wird linear nach dem nächsten freien Platz gesucht

Zeitkomplexität (durchschnittlicher Fall):
- get(key): O(1)
- put(key, val): O(1)
- delete(key): O(1)

Zeitkomplexität (schlechtester Fall):
- Separate Chaining: O(n) wenn alle Schlüssel in einer Liste landen
- Linear Probing: O(n) wenn die Tabelle fast voll ist

Beispiele:
    >>> # Separate Chaining
    >>> sc = SeparateChainingHashST()
    >>> sc.put("apple", 1)
    >>> sc.put("banana", 2)
    >>> sc.get("apple")
    1
    >>> sc.size()
    2

    >>> # Linear Probing
    >>> lp = LinearProbingHashST()
    >>> lp.put("apple", 1)
    >>> lp.put("banana", 2)
    >>> lp.get("banana")
    2
    >>> lp.size()
    2
"""

from collections.abc import Iterator


class SequentialSearchNode[K, V]:
    """Knoten für die sequentielle Suche in verketteten Listen.

    Attributes:
        key: Schlüssel des Knotens
        val: Wert des Knotens
        next: Nächster Knoten in der Liste
    """

    def __init__(
        self, key: K, val: V, next_node: "SequentialSearchNode[K, V] | None"
    ) -> None:
        """
        Create a node holding a key, a value, and a reference to the next node in a singly linked list.
        
        Parameters:
            key (K): The node's key.
            val (V): The node's value.
            next_node (SequentialSearchNode[K, V] | None): Reference to the next node in the list, or None if this is the last node.
        """
        self.key: K = key
        self.val: V = val
        self.next: SequentialSearchNode[K, V] | None = next_node


class SeparateChainingHashST[K, V]:
    """Hash Table mit Separate Chaining zur Kollisionsbehandlung.

    Diese Implementierung verwendet ein Array von verketteten Listen.
    Jeder Array-Eintrag (Bucket) enthält eine verkettete Liste von
    Schlüssel-Wert-Paaren, die auf denselben Hash-Wert abgebildet werden.

    Die Tabellengrösse wird dynamisch angepasst, um eine durchschnittliche
    Kettenlänge von etwa 2-8 Elementen zu gewährleisten.

    Attributes:
        INIT_CAPACITY: Initiale Kapazität der Hash-Tabelle
    """

    INIT_CAPACITY: int = 4

    def __init__(self, capacity: int = INIT_CAPACITY) -> None:
        """Initialisiert eine leere Hash-Tabelle.

        Args:
            capacity: Initiale Kapazität der Hash-Tabelle (Standard: 4)
        """
        self._m: int = capacity  # Anzahl der Buckets
        self._n: int = 0  # Anzahl der Schlüssel-Wert-Paare
        self._st: list[SequentialSearchNode[K, V] | None] = [None] * self._m

    def _hash(self, key: K) -> int:
        """Berechnet den Hash-Wert für einen Schlüssel.

        Args:
            key: Schlüssel zum Hashen

        Returns:
            int: Hash-Wert (Index im Array)
        """
        return (hash(key) & 0x7FFFFFFF) % self._m

    def size(self) -> int:
        """Gibt die Anzahl der Schlüssel-Wert-Paare zurück.

        Returns:
            int: Anzahl der Schlüssel-Wert-Paare
        """
        return self._n

    def is_empty(self) -> bool:
        """Prüft, ob die Hash-Tabelle leer ist.

        Returns:
            bool: True wenn leer, sonst False
        """
        return self.size() == 0

    def contains(self, key: K) -> bool:
        """Prüft, ob ein Schlüssel in der Hash-Tabelle vorhanden ist.

        Args:
            key: Zu suchender Schlüssel

        Returns:
            bool: True wenn der Schlüssel vorhanden ist, sonst False

        Raises:
            ValueError: Wenn key None ist
        """
        if key is None:
            raise ValueError("key cannot be None")
        return self.get(key) is not None

    def get(self, key: K) -> V | None:
        """Gibt den Wert für einen Schlüssel zurück.

        Args:
            key: Schlüssel zum Suchen

        Returns:
            V | None: Wert für den Schlüssel, oder None wenn nicht gefunden

        Raises:
            ValueError: Wenn key None ist
        """
        if key is None:
            raise ValueError("key cannot be None")

        i = self._hash(key)
        node = self._st[i]

        # Sequentielle Suche in der verketteten Liste
        while node is not None:
            if key == node.key:
                return node.val
            node = node.next

        return None

    def put(self, key: K, val: V) -> None:
        """Fügt ein Schlüssel-Wert-Paar ein oder aktualisiert einen Wert.

        Wenn der Schlüssel bereits vorhanden ist, wird der Wert aktualisiert.
        Wenn val None ist, wird der Schlüssel gelöscht.

        Args:
            key: Schlüssel zum Einfügen
            val: Wert zum Einfügen

        Raises:
            ValueError: Wenn key None ist
        """
        if key is None:
            raise ValueError("key cannot be None")

        if val is None:
            self.delete(key)
            return

        # Vergrössere die Tabelle, wenn die durchschnittliche Kettenlänge >= 10
        if self._n >= 10 * self._m:
            self._resize(2 * self._m)

        i = self._hash(key)
        node = self._st[i]

        # Suche nach dem Schlüssel in der verketteten Liste
        while node is not None:
            if key == node.key:
                node.val = val
                return
            node = node.next

        # Schlüssel nicht gefunden, füge am Anfang der Liste ein
        self._st[i] = SequentialSearchNode(key, val, self._st[i])
        self._n += 1

    def delete(self, key: K) -> None:
        """Löscht einen Schlüssel und den zugehörigen Wert.

        Args:
            key: Zu löschender Schlüssel

        Raises:
            ValueError: Wenn key None ist
        """
        if key is None:
            raise ValueError("key cannot be None")

        i = self._hash(key)
        node = self._st[i]
        prev: SequentialSearchNode[K, V] | None = None

        # Suche nach dem Schlüssel in der verketteten Liste
        while node is not None:
            if key == node.key:
                if prev is None:
                    # Erster Knoten in der Liste
                    self._st[i] = node.next
                else:
                    # Knoten in der Mitte oder am Ende
                    prev.next = node.next
                self._n -= 1

                # Verkleinere die Tabelle, wenn sie zu leer wird
                if self._m > self.INIT_CAPACITY and self._n <= 2 * self._m:
                    self._resize(self._m // 2)

                return

            prev = node
            node = node.next

    def keys(self) -> Iterator[K]:
        """Gibt einen Iterator über alle Schlüssel zurück.

        Yields:
            K: Schlüssel in der Hash-Tabelle
        """
        for i in range(self._m):
            node = self._st[i]
            while node is not None:
                yield node.key
                node = node.next

    def _resize(self, capacity: int) -> None:
        """
        Resize the hash table to the given number of buckets and rehash all entries.
        
        Rebuilds the table with the specified capacity and reinserts every existing key-value pair so their bucket indices reflect the new capacity.
        
        Parameters:
            capacity (int): Target number of buckets for the resized table.
        """
        temp = SeparateChainingHashST[K, V](capacity)
        for i in range(self._m):
            node = self._st[i]
            while node is not None:
                temp.put(node.key, node.val)
                node = node.next

        self._m = temp._m
        self._n = temp._n
        self._st = temp._st


class LinearProbingHashST[K, V]:
    """Hash Table mit Linear Probing zur Kollisionsbehandlung.

    Diese Implementierung verwendet zwei parallele Arrays für Schlüssel und Werte.
    Bei einer Kollision wird linear nach dem nächsten freien Platz gesucht.

    Die Tabellengrösse wird dynamisch angepasst, um einen Füllgrad (Load Factor)
    zwischen 12.5% und 50% zu gewährleisten.

    Attributes:
        INIT_CAPACITY: Initiale Kapazität der Hash-Tabelle
    """

    INIT_CAPACITY: int = 4

    def __init__(self, capacity: int = INIT_CAPACITY) -> None:
        """Initialisiert eine leere Hash-Tabelle.

        Args:
            capacity: Initiale Kapazität der Hash-Tabelle (Standard: 4)
        """
        self._m: int = capacity  # Grösse der Hash-Tabelle
        self._n: int = 0  # Anzahl der Schlüssel-Wert-Paare
        self._keys: list[K | None] = [None] * self._m
        self._vals: list[V | None] = [None] * self._m

    def _hash(self, key: K) -> int:
        """Berechnet den Hash-Wert für einen Schlüssel.

        Args:
            key: Schlüssel zum Hashen

        Returns:
            int: Hash-Wert (Index im Array)
        """
        return (hash(key) & 0x7FFFFFFF) % self._m

    def size(self) -> int:
        """Gibt die Anzahl der Schlüssel-Wert-Paare zurück.

        Returns:
            int: Anzahl der Schlüssel-Wert-Paare
        """
        return self._n

    def is_empty(self) -> bool:
        """Prüft, ob die Hash-Tabelle leer ist.

        Returns:
            bool: True wenn leer, sonst False
        """
        return self.size() == 0

    def contains(self, key: K) -> bool:
        """Prüft, ob ein Schlüssel in der Hash-Tabelle vorhanden ist.

        Args:
            key: Zu suchender Schlüssel

        Returns:
            bool: True wenn der Schlüssel vorhanden ist, sonst False

        Raises:
            ValueError: Wenn key None ist
        """
        if key is None:
            raise ValueError("key cannot be None")
        return self.get(key) is not None

    def get(self, key: K) -> V | None:
        """Gibt den Wert für einen Schlüssel zurück.

        Args:
            key: Schlüssel zum Suchen

        Returns:
            V | None: Wert für den Schlüssel, oder None wenn nicht gefunden

        Raises:
            ValueError: Wenn key None ist
        """
        if key is None:
            raise ValueError("key cannot be None")

        i = self._hash(key)

        # Linear Probing: Suche nach dem Schlüssel
        while self._keys[i] is not None:
            if self._keys[i] == key:
                return self._vals[i]
            i = (i + 1) % self._m

        return None

    def put(self, key: K, val: V) -> None:
        """Fügt ein Schlüssel-Wert-Paar ein oder aktualisiert einen Wert.

        Wenn der Schlüssel bereits vorhanden ist, wird der Wert aktualisiert.
        Wenn val None ist, wird der Schlüssel gelöscht.

        Args:
            key: Schlüssel zum Einfügen
            val: Wert zum Einfügen

        Raises:
            ValueError: Wenn key None ist
        """
        if key is None:
            raise ValueError("key cannot be None")

        if val is None:
            self.delete(key)
            return

        # Vergrössere die Tabelle, wenn sie halb voll ist
        if self._n >= self._m // 2:
            self._resize(2 * self._m)

        i = self._hash(key)

        # Linear Probing: Suche nach dem Schlüssel oder einem freien Platz
        while self._keys[i] is not None:
            if self._keys[i] == key:
                self._vals[i] = val
                return
            i = (i + 1) % self._m

        # Freier Platz gefunden, füge ein
        self._keys[i] = key
        self._vals[i] = val
        self._n += 1

    def delete(self, key: K) -> None:
        """Löscht einen Schlüssel und den zugehörigen Wert.

        Nach dem Löschen müssen alle Schlüssel im selben Cluster
        neu eingefügt werden, um die Integrität der Hash-Tabelle
        zu gewährleisten.

        Args:
            key: Zu löschender Schlüssel

        Raises:
            ValueError: Wenn key None ist
        """
        if key is None:
            raise ValueError("key cannot be None")

        if not self.contains(key):
            return

        # Finde die Position des Schlüssels
        i = self._hash(key)
        while key != self._keys[i]:
            i = (i + 1) % self._m

        # Lösche den Schlüssel und Wert
        self._keys[i] = None
        self._vals[i] = None

        # Füge alle Schlüssel im selben Cluster neu ein
        i = (i + 1) % self._m
        while self._keys[i] is not None:
            key_to_rehash = self._keys[i]
            val_to_rehash = self._vals[i]
            self._keys[i] = None
            self._vals[i] = None
            self._n -= 1
            self.put(key_to_rehash, val_to_rehash)  # type: ignore
            i = (i + 1) % self._m

        self._n -= 1

        # Verkleinere die Tabelle, wenn sie zu leer wird
        if self._n > 0 and self._n <= self._m // 8:
            self._resize(self._m // 2)

    def keys(self) -> Iterator[K]:
        """Gibt einen Iterator über alle Schlüssel zurück.

        Yields:
            K: Schlüssel in der Hash-Tabelle
        """
        for i in range(self._m):
            if self._keys[i] is not None:
                yield self._keys[i]  # type: ignore

    def _resize(self, capacity: int) -> None:
        """Ändert die Grösse der Hash-Tabelle.

        Args:
            capacity: Neue Kapazität der Hash-Tabelle
        """
        temp = LinearProbingHashST[K, V](capacity)
        for i in range(self._m):
            if self._keys[i] is not None:
                temp.put(self._keys[i], self._vals[i])  # type: ignore

        self._m = temp._m
        self._n = temp._n
        self._keys = temp._keys
        self._vals = temp._vals


def main() -> None:
    """Demonstriert die Verwendung der Hash-Tabellen."""
    print("=== Separate Chaining Hash Table ===")
    sc = SeparateChainingHashST[str, int]()

    # Füge Elemente ein
    words = ["S", "E", "A", "R", "C", "H", "E", "X", "A", "M", "P", "L", "E"]
    for i, word in enumerate(words):
        sc.put(word, i)

    print(f"Size: {sc.size()}")
    print(f"Keys: {list(sc.keys())}")

    # Suche nach Elementen
    print(f"\nget('E'): {sc.get('E')}")
    print(f"get('X'): {sc.get('X')}")
    print(f"contains('A'): {sc.contains('A')}")
    print(f"contains('Z'): {sc.contains('Z')}")

    # Lösche ein Element
    sc.delete("E")
    print("\nAfter deleting 'E':")
    print(f"Size: {sc.size()}")
    print(f"contains('E'): {sc.contains('E')}")

    print("\n=== Linear Probing Hash Table ===")
    lp = LinearProbingHashST[str, int]()

    # Füge Elemente ein
    for i, word in enumerate(words):
        lp.put(word, i)

    print(f"Size: {lp.size()}")
    print(f"Keys: {list(lp.keys())}")

    # Suche nach Elementen
    print(f"\nget('E'): {lp.get('E')}")
    print(f"get('X'): {lp.get('X')}")
    print(f"contains('A'): {lp.contains('A')}")
    print(f"contains('Z'): {lp.contains('Z')}")

    # Lösche ein Element
    lp.delete("E")
    print("\nAfter deleting 'E':")
    print(f"Size: {lp.size()}")
    print(f"contains('E'): {lp.contains('E')}")


if __name__ == "__main__":
    main()