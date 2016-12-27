# -*- coding: utf-8 -*-
# /usr/bin/python3.5

"""Implementation stack - LIFO."""


class StackEmptyError(Exception):
    """Exception if stack is empty."""

    pass


class Stack(object):
    """Implementation stack."""

    def __init__(self):
        self.stack = list()

    def pop(self):
        """Remove and return a latest item of a stack."""

        if self.length == 0:
            raise StackEmptyError("Stack is empty")
        return self.stack.pop()

    def push(self, value):
        """Remove and return a latest item of a stack."""

        self.stack.append(value)

    @property
    def length(self):
        """Remove and return a latest item of a stack."""

        return len(self.stack)

    def clear(self):
        """Remove and return a latest item of a stack."""

        self.stack.clear()

    @property
    def isEmpty(self):
        """Remove and return a latest item of a stack."""

        return len(self.stack) == 0

    @property
    def head(self):
        """Return head of a stack (latest added)."""

        if self.length == 0:
            raise StackEmptyError("Stack is empty")
        return self.stack[self.length - 1]

    @property
    def tail(self):
        """Return tail of a stack (earliest added)."""

        if self.length == 0:
            raise StackEmptyError("Stack is empty")
        return self.stack[0]

    def __repr__(self):
        return '{0}({1!r})'.format(self.__class__.__name__, self.stack)

    def __str__(self):
        return str(self.stack)
