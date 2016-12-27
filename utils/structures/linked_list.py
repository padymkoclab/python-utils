"""Implementation singly linked list."""


# http://stackoverflow.com/questions/280243/python-linked-list

class linkedListNode(object):
    """Node of linked list."""

    def __init__(self, cargo, next_):
        self._cargo = cargo
        self._next = next_

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    def __str__(self):

        return str(self.cargo)


class linkedList(object):
    """Linked list."""

    def __init__(self):
        self.current_node = None

    def __len__(self):
        length = 0
        node = self.current_node
        while node is not None:
            length += 1
            node = node.next
        return length

    def __repr__(self):

        return '{0}({1!s})'.format(self.__class__.__name__, self)

    def __str__(self):

        if self.current_node is None:
            return "()"

        result = list()
        node = self.current_node
        while node is not None:
            result.append(str(node))
            node = node.next
        return ', '.join(result)

    def __add__(self, cargo):
        """Add node."""

        node = linkedListNode(cargo, self.current_node)
        self.current_node = node

    def reverse(self):
        pass

    def remove(self):
        pass

    def extend(self):
        pass

    def clear(self):

        self.__init__()


# lst = linkedList()

# lst + 213
# lst + 542
# lst + -343

# print(str(lst))
# print(repr(lst))
# lst.clear()
# print(str(lst))
# print(repr(lst))
