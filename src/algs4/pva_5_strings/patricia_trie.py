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
from typing import Generic, TypeVar

from src.algs4.pva_1_fundamentals.queue import Queue

V = TypeVar("V")  # Value type


class _PatriciaNode(Generic[V]):
    """Knoten im Patricia-Trie.

    Attributes:
        val: Wert des Knotens (None wenn Knoten keinen Schlüssel repräsentiert)
        children: Dictionary von Kantenbeschriftungen zu Kind-Knoten
        prefix: Gemeinsamer Präfix, der in diesem Knoten gespeichert ist
    """

    def __init__(self, prefix: str = "") -> None:
        """Initialisiert einen neuen Knoten.

        Args:
            prefix: Gemeinsamer Präfix für diesen Knoten
        """
        self.val: V | None = None
        self.children: dict[str, _PatriciaNode[V]] = {}
        self.prefix: str = prefix


class PatriciaTrie(Generic[V]):
    """Patricia Trie - Kompakter String-basierter Symbol-Table.

    Ein platzsparender Symbol-Table für String-Schlüssel, bei dem Knoten
    mit nur einem Kind verschmolzen werden. Die Kanten speichern Strings
    statt einzelner Zeichen.

    Diese Implementierung ist eine vereinfachte Version, die das Konzept
    der Pfadkompression demonstriert.
    """

    def __init__(self) -> None:
        """Initialisiert einen leeren Patricia-Trie."""
        self._root: _PatriciaNode[V] | None = None
        self._n: int = 0  # Anzahl der Schlüssel-Wert-Paare

    def size(self) -> int:
        """Gibt die Anzahl der Schlüssel-Wert-Paare zurück.

        Returns:
            int: Anzahl der Schlüssel-Wert-Paare
        """
        return self._n

    def __len__(self) -> int:
        """Gibt die Anzahl der Schlüssel-Wert-Paare zurück.

        Returns:
            int: Anzahl der Schlüssel-Wert-Paare
        """
        return self._n

    def is_empty(self) -> bool:
        """Prüft, ob der Patricia-Trie leer ist.

        Returns:
            bool: True wenn leer, False sonst
        """
        return self._n == 0

    def contains(self, key: str) -> bool:
        """Prüft, ob der Patricia-Trie den Schlüssel enthält.

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
        """Fügt ein Schlüssel-Wert-Paar ein.

        Args:
            key: Der Schlüssel
            val: Der zu speichernde Wert

        Raises:
            ValueError: Wenn der Schlüssel None ist
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
        """Hilfsmethode für put.

        Args:
            node: Aktueller Knoten
            key: Der Schlüssel
            val: Der zu speichernde Wert

        Returns:
            _PatriciaNode[V]: Der aktualisierte Knoten
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

    def keys(self) -> Iterator[str]:
        """Gibt alle Schlüssel zurück.

        Returns:
            Iterator[str]: Iterator über alle Schlüssel
        """
        queue: Queue[str] = Queue()
        if self._root is not None:
            self._collect(self._root, "", queue)
        return iter(queue)

    def _collect(self, node: _PatriciaNode[V], prefix: str, queue: Queue[str]) -> None:
        """Sammelt alle Schlüssel im Teilbaum.

        Args:
            node: Wurzel des Teilbaums
            prefix: Aktueller Präfix
            queue: Queue zum Sammeln der Schlüssel
        """
        current_key = prefix + node.prefix

        if node.val is not None:
            queue.enqueue(current_key)

        for char in sorted(node.children.keys()):
            self._collect(node.children[char], current_key, queue)

    def __iter__(self) -> Iterator[str]:
        """Gibt einen Iterator über alle Schlüssel zurück.

        Returns:
            Iterator[str]: Iterator über alle Schlüssel
        """
        return self.keys()

    def __repr__(self) -> str:
        """Gibt eine String-Repräsentation zurück.

        Returns:
            str: String-Repräsentation
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
