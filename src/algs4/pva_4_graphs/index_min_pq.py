"""Indexed Min Priority Queue.

Dieses Modul enthält die IndexMinPQ-Klasse, eine Indexed Min Priority Queue
Implementierung basierend auf einem Min-Heap. Sie ermöglicht es, Elemente
mit Indizes zu verwalten und deren Prioritäten zu ändern.

Beispiele:
    >>> pq = IndexMinPQ(5)
    >>> pq.insert(0, 1.0)
    >>> pq.insert(1, 0.5)
    >>> pq.del_min()
    1
    >>> pq.size()
    1
"""


class IndexMinPQ:
    """Indexed Min Priority Queue basierend auf einem Min-Heap.

    Diese Klasse implementiert eine Priority Queue, bei der jedes Element
    einen Index hat und dessen Priorität geändert werden kann. Sie wird
    häufig in Graphen-Algorithmen wie Dijkstra verwendet.

    Attribute:
        pq (list): Der Min-Heap (enthält Indizes)
        qp (list): Inverse Abbildung (Index -> Position im Heap)
        keys (list): Die Prioritäten (Schlüssel) für jeden Index
    """

    def __init__(self, n: int) -> None:
        """Initialisiert eine neue IndexMinPQ mit Kapazität n.

        Args:
            n: Die maximale Anzahl von Elementen
        """
        self.pq = []
        self.qp = [-1] * n
        self.keys = [None] * n

    def insert(self, i, item):
        self.pq.append(i)
        n = len(self.pq) - 1
        self.qp[i] = n
        self.keys[i] = item
        self.swim(n)

    def change(self, i, item):
        self.keys[i] = item
        self.sink(self.qp[i])
        self.swim(self.qp[i])

    def contains(self, index: int) -> bool:
        """Überprüft, ob ein Index in der PQ vorhanden ist.

        Args:
            index: Der zu überprüfende Index

        Returns:
            True, wenn der Index in der PQ ist, False sonst
        """
        return self.qp[index] != -1

    def delete(self, i):
        index = self.qp[i]
        item = self.pq[index]
        self.pq[index], self.pq[-1] = self.pq[-1], self.pq[index]
        self.swim(index)
        self.sink(index)
        self.keys[i] = None
        self.qp[i] = -1
        return item

    def decrease_key(self, i, key):
        if self.keys[i] <= key:
            raise Exception("calling decrease key with invalid value")
        self.keys[i] = key
        self.swim(self.qp[i])

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def min(self):
        return self.keys[self.pq[0]]

    def del_min(self) -> int:
        """Entfernt und gibt das Element mit kleinster Priorität zurück.

        Returns:
            Der Index des Elements mit kleinster Priorität
        """
        m = self.pq[0]
        self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
        self.qp[self.pq[0]] = 0
        self.pq = self.pq[:-1]
        if len(self.pq) > 0:
            self.sink(0)

        self.qp[m] = -1
        return m

    def is_empty(
        self,
    ):
        return not self.pq

    def size(
        self,
    ):
        return len(self.pq)

    def swim(self, k: int) -> None:
        """Hebt einen Knoten im Heap nach oben.

        Args:
            k: Der Index des Knotens
        """
        while k > 0 and self.greater((k - 1) // 2, k):
            parent = (k - 1) // 2
            self.pq[k], self.pq[parent] = self.pq[parent], self.pq[k]
            self.qp[self.pq[k]] = k
            self.qp[self.pq[parent]] = parent
            k = parent

    def sink(self, k: int) -> None:
        """Senkt einen Knoten im Heap nach unten.

        Args:
            k: Der Index des Knotens
        """
        N = len(self.pq)

        while 2 * k + 1 < N:
            j = 2 * k + 1
            if j + 1 < N and self.greater(j, j + 1):
                j += 1

            if not self.greater(k, j):
                break

            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            self.qp[self.pq[k]] = k
            self.qp[self.pq[j]] = j
            k = j
