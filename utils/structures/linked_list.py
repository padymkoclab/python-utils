"""Implementation singly linked list."""


# http://stackoverflow.com/questions/280243/python-linked-list

class linkedList(object):
    """Linked list of nodes."""

    def __init__(self, cargo=None):
        self._cargo = cargo
        self._next = None

    def __len__(self):

        return 1

    def __add__(self):

        return 1

    def __repr__(self):

        return 1

    def __str__(self):

        return str(self.cargo)

    @property
    def cargo(self):
        """Return value of node."""

        return self._cargo

    @cargo.setter
    def cargo(self, value):
        """Set value of node."""

        self._cargo = value

    @property
    def next(self):
        """Return a next node."""

        return self._next

    @next.setter
    def next(self, node):
        """Set a next node."""

        self._next = node

    def reverse(self):
        pass

    def remove(self):
        pass

    def extend(self):
        pass

    def clear(self):

        self.__init__()


lst = linkedList()
print(lst)

# lst + 213
# lst + 542
# lst + -343

# print(str(lst))
# print(repr(lst))
# lst.clear()
# print(str(lst))
# print(repr(lst))
