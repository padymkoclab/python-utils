
import unittest

import pytest

from ..math import count_combinations, fibonacci


class MathTest(unittest.TestCase):

    def test_count_combinations(self):

        assert count_combinations(15, 4) == 1365
        assert count_combinations(52, 5) == 2598960
        assert count_combinations(15, 8) == 6435
        assert count_combinations(255, 14) == 39206761937327465798625
        assert count_combinations(78, 3) == 76076
        assert count_combinations(4, 4) == 1
        assert count_combinations(6, 5) == 1
        assert count_combinations(9, 5) == 1
        assert count_combinations(10, 5) == 2
        assert count_combinations(10, 0) == 0
        assert count_combinations(0, 0) == 0
        assert count_combinations(1000, 10) == 263409560461970212832400

    def test_count_combinations_error(self):

        with pytest.raises(ValueError):
            count_combinations(5, 7)
        with pytest.raises(TypeError):
            count_combinations(6, None)
        with pytest.raises(TypeError):
            count_combinations(6, True)
        with pytest.raises(TypeError):
            count_combinations(None, [])
        with pytest.raises(TypeError):
            count_combinations(None, None)
        with pytest.raises(TypeError):
            count_combinations(True, False)

    def test_fibonacci(self):

        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8
        assert fibonacci(7) == 13
        assert fibonacci(8) == 21
        assert fibonacci(9) == 34
        assert fibonacci(10) == 55
        assert fibonacci(11) == 89
        assert fibonacci(12) == 144
        assert fibonacci(13) == 233
        assert fibonacci(14) == 377
        assert fibonacci(15) == 610
        assert fibonacci(16) == 987
        assert fibonacci(17) == 1597
        assert fibonacci(18) == 2584
        assert fibonacci(19) == 4181
        assert fibonacci(20) == 6765
        assert fibonacci(21) == 10946
        assert fibonacci(22) == 17711
        assert fibonacci(23) == 28657
        assert fibonacci(24) == 46368
        assert fibonacci(25) == 75025
        assert fibonacci(26) == 121393
        assert fibonacci(27) == 196418
        assert fibonacci(28) == 317811

    def test_fibonacci_invalid_input(self):

        pytest.raises(ValueError, fibonacci, -1)
        pytest.raises(ValueError, fibonacci, 1.0)
