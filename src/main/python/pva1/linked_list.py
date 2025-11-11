# noinspection PyUnusedLocal
class Node:

    def __init__(self, data):
        pass


# noinspection PyUnresolvedReferences
class DoublyLinkedList:

    def __init__(self):
        pass

    def append(self, element):
        """
        Fügt ein Element am Ende der Liste hinzu.
        
        >>> dl = DoublyLinkedList()
        >>> dl.append(1)
        >>> dl.append(2)
        >>> str(dl)
        '[1, 2]'
        """
        pass

    def insert(self, index, element):
        """
        Fügt ein Element an der angegebenen Position ein.
        
        >>> dl = DoublyLinkedList()
        >>> dl.append(1)
        >>> dl.append(3)
        >>> dl.insert(1, 2)
        >>> str(dl)
        '[1, 2, 3]'
        """
        pass

    def pop(self, index=-1):
        """
        Entfernt und gibt das Element an der angegebenen Position zurück.
        
        >>> dl = DoublyLinkedList()
        >>> dl.append(1)
        >>> dl.append(2)
        >>> dl.append(3)
        >>> dl.pop()
        3
        >>> str(dl)
        '[1, 2]'
        >>> dl.pop(0)
        1
        >>> str(dl)
        '[2]'
        """
        pass

    def __str__(self):
        """
        Gibt eine String-Repräsentation der Liste zurück.
        
        >>> dl = DoublyLinkedList()
        >>> dl.append(1)
        >>> dl.append(2)
        >>> str(dl)
        '[1, 2]'
        """
        pass

    def __repr__(self):
        """
        Gibt eine offizielle String-Repräsentation der Liste zurück.
        
        >>> dl = DoublyLinkedList()
        >>> dl.append(1)
        >>> dl.append(2)
        >>> repr(dl)
        'DoublyLinkedList([1, 2])'
        """
        pass

    def __getitem__(self, index):
        """
        Gibt das Element an der angegebenen Position zurück.
        
        >>> dl = DoublyLinkedList()
        >>> dl.append(1)
        >>> dl.append(2)
        >>> dl[1]
        2
        """
        pass

    def __setitem__(self, index, element):
        """
        Setzt das Element an der angegebenen Position.
        
        >>> dl = DoublyLinkedList()
        >>> dl.append(1)
        >>> dl.append(2)
        >>> dl[1] = 3
        >>> str(dl)
        '[1, 3]'
        """
        pass

    def __contains__(self, element):
        """
        Prüft, ob ein Element in der Liste vorhanden ist.
        
        >>> dl = DoublyLinkedList()
        >>> dl.append(1)
        >>> dl.append(2)
        >>> 2 in dl
        True
        >>> 3 in dl
        False
        """
        pass

    def __len__(self):
        """
        Gibt die Anzahl der Elemente in der Liste zurück.
        
        >>> dl = DoublyLinkedList()
        >>> dl.append(1)
        >>> dl.append(2)
        >>> len(dl)
        2
        """
        return 0

    def __iter__(self):
        """
        Gibt einen Iterator für die Liste zurück.
        
        >>> dl = DoublyLinkedList()
        >>> dl.append(1)
        >>> dl.append(2)
        >>> [x for x in dl]
        [1, 2]
        """
        pass


class DoublyLinkedListIterator:
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
