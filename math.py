
import math


def count_combinations(n_objects: int, n_sample: int) -> int:
    """
    https://en.wikipedia.org/wiki/Combination
    C(n, r) = n! / r! * (n - r)!
    """

    if not (isinstance(n_objects, int) and isinstance(n_sample, int)):
        raise TypeError('"n_objects" and "n_sample" must be integer')

    if n_objects < n_sample:
        raise ValueError('"n_sample" must be less or equal "n_objects"')
    elif n_objects == n_sample:
        return 1

    if n_sample == 0:
        return 1
    elif n_sample == 1:
        return n_objects

    return math.factorial(n_objects) / (math.factorial(n_sample) * math.factorial(n_objects - n_sample))


def fibonacci(num):
    """ """

    if not isinstance(num, int) or num < 0:
        raise ValueError('Sequence Fibonacci can be determined only for positive integer')

    if num in [0, 1]:
        return num
    elif num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
