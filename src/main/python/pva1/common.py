#!/usr/bin/env python
# -*- encoding:UTF-8 -*-


class Node(object):
    """
        A class representing a node in a linked list.

        Attributes:
            _val (Any): The value stored in the node.
            _next_node (Node or None): Reference to the next node in the list.

        Methods:
            __init__(self, val): Initializes a node with a given value and no next node.
            val (Any): Property that gets or sets the value of the node.
            next_node (Node or None): Property that gets or sets the reference to the next node.
    """
    def __init__(self, val):
        self._val = val
        self._next_node = None

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        self._val = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node


class DoubleNode(object):
    """
        DoubleNode class represents a node in a doubly linked list.

        Methods
        -------
        __init__(self, val):
            Initializes a DoubleNode with a given value.

        prev(self):
            Gets the previous node.

        prev(self, node):
            Sets the previous node.

        next(self):
            Gets the next node.

        next(self, node):
            Sets the next node.

        val(self):
            Gets the value of the node.

        val(self, value):
            Sets the value of the node.
    """
    def __init__(self, val):
        self._val = val
        self._prev = self._next = None

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node):
        self._prev = node

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        self._val = value
