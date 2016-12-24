
import time
import functools
import inspect
import copy
import collections


class frozendict(collections.Mapping):
    """
    Immutable dictionary
    """

    def __init__(self, **kwargs):

        self.__dict = dict(**kwargs)

    def __getitem__(self, key):

        return self.__dict[key]

    def __len__(self):

        return len(self.__dict)

    def __iter__(self):

        return iter(self.__dict)

    def __hash__(self):

        return hash(tuple(self.__dict.keys()))

    def copy(self):

        return copy.copy(self.__dict)

    @classmethod
    def fromkeys(cls, seq, value=None):

        return dict.fromkeys(seq, value)

    def __repr__(self):

        return "<{} {}>".format(self.__class__.__name__, self.__dict)

    def __str__(self):

        return str(self.__dict)


class Immutable(object):
    """

    """

    __slots__ = ['x']

    def __init__(self, x):
        self.x = x

    def __setattr__(self, name, value):
        pass


raise Not
# @functools.total_ordering
class A:

    def __init__(self, n):
        self.n = n

    # def __eq__(self, other):

    #     return self.n == other.n

    def __lt__(self, other):

        return self.n < other.n

    # def __gt__(self, other):

    #     return self.n > other.n

    def __ge__(self, other):

        return self.n >= other.n

    # def __le__(self, other):

    #     return self.n <= other.n

"""
A1 = A(4)
A2 = A(3)
assert A1 > A2
assert not A1 < A2
assert not A1 == A2
assert A1 >= A2
assert not A1 <= A2
"""
