
import types

import pytest

from utils import iterable


def test_flatten():

    assert isinstance(iterable.flatten([]), types.GeneratorType)
    assert tuple(iterable.flatten([])) == ()
    assert tuple(iterable.flatten(())) == ()

    with pytest.raises(TypeError):
        tuple(iterable.flatten(''))

    assert tuple(iterable.flatten([1, 2, 3, 4])) == (1, 2, 3, 4)
    assert tuple(iterable.flatten((1, 2, 3, 4))) == (1, 2, 3, 4)

    assert tuple(iterable.flatten(([1, 2], [3, 4]))) == (1, 2, 3, 4)
    assert tuple(iterable.flatten(([[], [(), [[[1, ['3', [2.1]], None]], True]]]))) == (1, '3', 2.1, None, True)
    assert tuple(iterable.flatten(((([(), ()])), []))) == ()
    assert tuple(iterable.flatten(((1, 2, ('ext'), ([3.312]), None, []), None))) == (1, 2, 'ext', 3.312, None, None)


def test_split_on_chunks():

    # a length is more a length of sequence
    assert iterable.split_on_chunks([12, 32.12, 'sa'], 4, True) == [12, 32.12, 'sa']

    # a length is equal a length of sequence
    assert iterable.split_on_chunks((True, None, 'sa'), 3, True) == (True, None, 'sa')

    # no support for a string
    with pytest.raises(TypeError):
        iterable.split_on_chunks('text', 20, False)

    # a length is 0
    with pytest.raises(ValueError):
        iterable.split_on_chunks([1, 2.1], 0, False)

    # a length is less 0
    with pytest.raises(ValueError):
        iterable.split_on_chunks([[], None], -10, True)

    assert iterable.split_on_chunks((), 1) == ()

    obj = (1, (2.1, [True, None]), [21, 'str'], '', False, 0)
    assert iterable.split_on_chunks(obj, 1) == \
        [(1, ), ((2.1, [True, None]), ), ([21, 'str'], ), ('', ), (False, ), (0, )]
    assert iterable.split_on_chunks(obj, 2) == [(1, (2.1, [True, None])), ([21, 'str'], ''), (False, 0)]
    assert iterable.split_on_chunks(obj, 3) == [(1, (2.1, [True, None]), [21, 'str']), ('', False, 0)]
    assert iterable.split_on_chunks(obj, 4) == [(1, (2.1, [True, None]), [21, 'str'], ''), (False, 0)]
    assert iterable.split_on_chunks(obj, 4, True) == [(1, (2.1, [True, None]), [21, 'str'], '', False, 0)]
    assert iterable.split_on_chunks(obj, 5) == [(1, (2.1, [True, None]), [21, 'str'], '', False), (0, )]
    assert iterable.split_on_chunks(obj, 5, True) == [(1, (2.1, [True, None]), [21, 'str'], '', False, 0, )]
    assert iterable.split_on_chunks(obj, 6) == (1, (2.1, [True, None]), [21, 'str'], '', False, 0)

    obj = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, True, None, False, '', []]

    assert iterable.split_on_chunks(obj, 1) == [
        (0, ),
        (1, ),
        (2, ),
        (3, ),
        (4, ),
        (5, ),
        (6, ),
        (7, ),
        (8, ),
        (9, ),
        (True, ),
        (None, ),
        (False, ),
        ('', ),
        ([], ),
    ]
    assert iterable.split_on_chunks(obj, 2) == [
        (0, 1),
        (2, 3),
        (4, 5),
        (6, 7),
        (8, 9),
        (True, None),
        (False, ''),
        ([], )
    ]
    assert iterable.split_on_chunks(obj, 2, True) == [
        (0, 1),
        (2, 3),
        (4, 5),
        (6, 7),
        (8, 9),
        (True, None),
        (False, '', []),
    ]
    assert iterable.split_on_chunks(obj, 3) == [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (9, True, None),
        (False, '', []),
    ]
    assert iterable.split_on_chunks(obj, 4) == [
        (0, 1, 2, 3),
        (4, 5, 6, 7),
        (8, 9, True, None),
        (False, '', []),
    ]
    assert iterable.split_on_chunks(obj, 4, True) == [
        (0, 1, 2, 3),
        (4, 5, 6, 7),
        (8, 9, True, None, False, '', []),
    ]
    assert iterable.split_on_chunks(obj, 5) == [
        (0, 1, 2, 3, 4),
        (5, 6, 7, 8, 9),
        (True, None, False, '', []),
    ]
    assert iterable.split_on_chunks(obj, 6) == [
        (0, 1, 2, 3, 4, 5),
        (6, 7, 8, 9, True, None),
        (False, '', []),
    ]
    assert iterable.split_on_chunks(obj, 6, True) == [
        (0, 1, 2, 3, 4, 5),
        (6, 7, 8, 9, True, None, False, '', []),
    ]
    assert iterable.split_on_chunks(obj, 7) == [
        (0, 1, 2, 3, 4, 5, 6),
        (7, 8, 9, True, None, False, ''),
        ([],),
    ]
    assert iterable.split_on_chunks(obj, 7, True) == [
        (0, 1, 2, 3, 4, 5, 6),
        (7, 8, 9, True, None, False, '', []),
    ]
    assert iterable.split_on_chunks(obj, 8) == [
        (0, 1, 2, 3, 4, 5, 6, 7),
        (8, 9, True, None, False, '', []),
    ]
    assert iterable.split_on_chunks(obj, 9) == [
        (0, 1, 2, 3, 4, 5, 6, 7, 8),
        (9, True, None, False, '', []),
    ]
    assert iterable.split_on_chunks(obj, 9, True) == [(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, True, None, False, '', [])]
