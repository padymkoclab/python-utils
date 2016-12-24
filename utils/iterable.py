"""Collections utils for sequence, list, tuple, set."""


def flatten(sequence):
    """
    Flat sequence to single-dimension sequence.

    >>> tuple(flatten([[4,5, [2, [3]]], [1,[2, [1, [2]]],3], [1,[2,3]]]))
    (4, 5, 2, 3, 1, 2, 1, 2, 3, 1, 2, 3)
    >>> tuple(flatten([[[[[[[[1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]]]]]]]]]))
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    >>> tuple(flatten(('aaa', 'ddd', ('bbbb', ('ccc', ('ddd', 'e', 'f'))))))
    ('aaa', 'ddd', 'bbbb', 'ccc', 'ddd', 'e', 'f')
    """
    for i in sequence:
        if isinstance(i, (list, tuple)):
            yield from flatten(i)
        else:
            yield i


def splitSequenceToChunks(sequence, length, no_rest=False):
    """Split sequence to chunks same length."""
    if length < 1:
        raise ValueError("Length subsequence must be at least 1")

    chuncks = list()
    for i in range(0, len(sequence), length):
        chuncks.append(sequence[i: i + length])

    if no_rest is True and len(chuncks[-1]) < length and len(chuncks) > 1:
        chuncks[-2].extend(chuncks[-1])
        chuncks = chuncks[:-1]

    return chuncks
