
import collections
import unittest

from ..extratypes import frozendict


class FrozendictTest(unittest.TestCase):
    """

    """

    @classmethod
    def setUpClass(cls):

        cls.obj = frozendict(
            a=1, b=.5, c=True, d=(1, 2), e=[3, 4], f={5, 6},
            z=frozenset((7, 8)), r={'a': 1}
        )

    @classmethod
    def tearDownClass(cls):

        del cls.obj

    def test_len(self):

        self.assertEqual(len(self.obj), 8)

    def test_getitem(self):

        self.assertEqual(self.obj['a'], 1)
        self.assertEqual(self.obj['e'], [3, 4])

    def test_deny_setitem(self):

        with self.assertRaises(TypeError):
            self.obj['new'] = 1

    def test_deny_delitem(self):

        with self.assertRaises(TypeError):
            del self.obj['a']

    def test_iter(self):

        self.assertTrue(isinstance(self.obj, collections.Iterable))

    def test_hash(self):

        self.assertTrue(isinstance(self.obj, collections.Hashable))
        self.assertTrue(isinstance(hash(self.obj), int))

    def test_copy(self):

        self.assertEqual(self.obj.copy(), self.obj)

    def test_fromkeys(self):

        self.assertDictEqual(frozendict.fromkeys((1, 2, 3), True), {1: True, 2: True, 3: True})
        self.assertDictEqual(frozendict.fromkeys((1, 2, 3)), {1: None, 2: None, 3: None})

    def test_repr(self):

        self.assertRegex(repr(self.obj), r"^<frozendict \{.*\}>$")

    def test_str(self):

        self.assertRegex(str(self.obj), r"^\{.*\}$")
