
import decimal
import uuid
import datetime
import unittest

from utils.constants import Constant


class TestConstant(unittest.TestCase):
    """
    Test for implementation constants in the Python
    """

    def setUp(self):

        self.const = Constant()

    def tearDown(self):

        del self.const

    def test_create_constant_with_different_variants_of_name(self):

        self.const.CONSTANT = 1
        self.assertEqual(self.const.CONSTANT, 1)
        self.const.Constant = 2
        self.assertEqual(self.const.Constant, 2)
        self.const.ConStAnT = 3
        self.assertEqual(self.const.ConStAnT, 3)
        self.const.constant = 4
        self.assertEqual(self.const.constant, 4)
        self.const.co_ns_ta_nt = 5
        self.assertEqual(self.const.co_ns_ta_nt, 5)
        self.const.constant1111 = 6
        self.assertEqual(self.const.constant1111, 6)

    def test_create_and_change_integer_constant(self):

        self.const.INT = 1234
        self.assertEqual(self.const.INT, 1234)
        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.INT = .211

    def test_create_and_change_float_constant(self):

        self.const.FLOAT = .1234
        self.assertEqual(self.const.FLOAT, .1234)
        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.FLOAT = .211

    def test_create_and_change_list_constant_but_saved_as_tuple(self):

        self.const.LIST = [1, .2, None, True, datetime.date.today(), [], {}]
        self.assertEqual(self.const.LIST, (1, .2, None, True, datetime.date.today(), [], {}))

        self.assertTrue(isinstance(self.const.LIST, tuple))

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.LIST = .211

    def test_create_and_change_none_constant(self):

        self.const.NONE = None
        self.assertEqual(self.const.NONE, None)
        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.NONE = .211

    def test_create_and_change_boolean_constant(self):

        self.const.BOOLEAN = True
        self.assertEqual(self.const.BOOLEAN, True)
        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.BOOLEAN = False

    def test_create_and_change_string_constant(self):

        self.const.STRING = "Text"
        self.assertEqual(self.const.STRING, "Text")

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.STRING += '...'

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.STRING = 'TEst1'

    def test_create_dict_constant(self):

        with self.assertRaisesRegexp(TypeError, 'dict can not be used as constant'):
            self.const.DICT = {}

    def test_create_and_change_tuple_constant(self):

        self.const.TUPLE = (1, .2, None, True, datetime.date.today(), [], {})
        self.assertEqual(self.const.TUPLE, (1, .2, None, True, datetime.date.today(), [], {}))

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.TUPLE = 'TEst1'

    def test_create_and_change_set_constant(self):

        self.const.SET = {1, .2, None, True, datetime.date.today()}
        self.assertEqual(self.const.SET, {1, .2, None, True, datetime.date.today()})

        self.assertTrue(isinstance(self.const.SET, frozenset))

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.SET = 3212

    def test_create_and_change_frozenset_constant(self):

        self.const.FROZENSET = frozenset({1, .2, None, True, datetime.date.today()})
        self.assertEqual(self.const.FROZENSET, frozenset({1, .2, None, True, datetime.date.today()}))

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.FROZENSET = True

    def test_create_and_change_date_constant(self):

        self.const.DATE = datetime.date(1111, 11, 11)
        self.assertEqual(self.const.DATE, datetime.date(1111, 11, 11))

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.DATE = True

    def test_create_and_change_datetime_constant(self):

        self.const.DATETIME = datetime.datetime(2000, 10, 10, 10, 10)
        self.assertEqual(self.const.DATETIME, datetime.datetime(2000, 10, 10, 10, 10))

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.DATETIME = None

    def test_create_and_change_decimal_constant(self):

        self.const.DECIMAL = decimal.Decimal(13123.12312312321)
        self.assertEqual(self.const.DECIMAL, decimal.Decimal(13123.12312312321))

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.DECIMAL = None

    def test_create_and_change_timedelta_constant(self):

        self.const.TIMEDELTA = datetime.timedelta(days=45)
        self.assertEqual(self.const.TIMEDELTA, datetime.timedelta(days=45))

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.TIMEDELTA = 1

    def test_create_and_change_uuid_constant(self):

        value = uuid.uuid4()
        self.const.UUID = value
        self.assertEqual(self.const.UUID, value)

        with self.assertRaisesRegexp(TypeError, 'Constanst can not be changed'):
            self.const.UUID = []

    def test_try_delete_defined_const(self):

        self.const.VERSION = '0.0.1'
        with self.assertRaisesRegexp(TypeError, 'Constanst can not be deleted'):
            del self.const.VERSION

    def test_try_delete_undefined_const(self):

        with self.assertRaisesRegexp(NameError, "name 'UNDEFINED' is not defined"):
            del self.const.UNDEFINED

    def test_get_all_defined_constants(self):

        self.assertDictEqual(self.const(), {})

        self.const.A = 1
        self.assertDictEqual(self.const(), {'A': 1})

        self.const.B = "Text"
        self.assertDictEqual(self.const(), {'A': 1, 'B': "Text"})
