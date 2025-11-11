class UnionFind:
    def __init__(self, n: int):
        """
        Initializes a union-find data structure with `n` elements.
        :param n: The number of elements in the union-find structure.
        >>> uf = UnionFind(5)
        >>> uf.parent
        [0, 1, 2, 3, 4]
        """
        self.parent = list(range(n))

    def find(self, x):
        """
        Returns the root element of the set to which the element `x` belongs.
        Runs in constant time.
        :param x:
        :return:

        >>> uf = UnionFind(5)
        >>> uf.find(0)
        0
        >>> uf.union(0, 1)
        >>> uf.find(1)
        0
        >>> uf.union(1, 2)
        >>> uf.find(2)
        0
        >>> uf.find(3)
        3
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """
        Merges the sets containing elements `x` and `y`.
        Runs in constant time.
        :param x:
        :param y:

        >>> uf = UnionFind(5)
        >>> uf.union(0, 1)
        >>> uf.find(1)
        0
        >>> uf.union(2, 3)
        >>> uf.find(3)
        2
        >>> uf.union(1, 2)
        >>> uf.find(3)
        0
        >>> uf.union(0, 4)
        >>> uf.find(4)
        0
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

    def is_connected(self, x: int, y: int):
        """
        Returns True if the elements `x` and `y` are in the same set,
        False otherwise. Runs in constant time.
        :param x:
        :param y:

        >>> uf = UnionFind(5)
        >>> uf.union(0, 1)
        >>> uf.union(2, 3)
        >>> uf.union(1, 2)
        >>> uf.is_connected(0, 3)
        True
        >>> uf.is_connected(0, 4)
        False
        """
        return self.find(x) == self.find(y)


# Beispiel-Nutzung
if __name__ == '__main__':
    import doctest

    doctest.testmod()
