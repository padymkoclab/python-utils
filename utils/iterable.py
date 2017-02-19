"""Collections utils for sequence, list, tuple, set."""


def flatten(sequence):
    """
    Flat a sequence with nested sequences to a single-dimension sequence.

    Arguments:
        a sequence {list or tuple} -- list or tuple

    Yields:
        an object -- any type

    >>> tuple(flatten([[4,5, [2, [3]]], [1,[2, [1, [2]]],3], [1,[2,3]]]))
    (4, 5, 2, 3, 1, 2, 1, 2, 3, 1, 2, 3)
    >>> tuple(flatten([[[[[[[[1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]]]]]]]]]))
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    >>> tuple(flatten(('aaa', 'ddd', ('bbbb', ('ccc', ('ddd', 'e', 'f'))))))
    ('aaa', 'ddd', 'bbbb', 'ccc', 'ddd', 'e', 'f')
    """

    if not isinstance(sequence, (list, tuple)):
        raise TypeError('Support only an instance of list or tuple')

    for i in sequence:
        if isinstance(i, (list, tuple)):
            yield from flatten(i)
        else:
            yield i


def split_on_chunks(sequence, length: int, no_rest=False):
    """
    Split a sequence to chunks same length.

    A length must be more 0.
    If leaved a rest of elements and flag no_rest is False, returns it as a last tuple,
    othewise - appends the rest to the penultimate item, if exists.

    Arguments:
        sequence {any iterable} -- sequence of items
        length: int {more 0} -- length each chunk

    Keyword Arguments:
        no_rest {bool} -- behaviour for rest elements (default: {False})

    Returns:
        [list] -- list of tuples

    Raises:
        ValueError -- if length is less 1
    """

    if not isinstance(sequence, (list, tuple)):
        raise TypeError('Support only an instance of list or tuple')

    sequence_len = len(sequence)

    if length < 1:
        raise ValueError("Length of a chunk must be at least 1")
    elif length >= sequence_len:
        return sequence

    chuncks = list()
    for i in range(0, sequence_len, length):
        chuncks.append(tuple(sequence[i: i + length]))

    if no_rest is True and len(chuncks[-1]) < length and len(chuncks) > 1:
        chuncks[-2] = list(chuncks[-2])
        chuncks[-2].extend(chuncks[-1])
        chuncks[-2] = tuple(chuncks[-2])
        chuncks = chuncks[:-1]

    return chuncks
