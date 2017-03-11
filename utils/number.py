"""Utils for numbers."""

import math


def get_count_digits(number: int):
    """Return number of digits in a number."""

    if number == 0:
        return 1

    number = abs(number)

    if number <= 999999999999997:
        return math.floor(math.log10(number)) + 1

    count = 0
    while number:
        count += 1
        number //= 10
    return count


def get_digits_from_right_to_left(number):
    """Return digits of an integer excluding the sign."""

    number = abs(number)

    if number < 10:
        return (number, )

    lst = list()

    while number:
        number, digit = divmod(number, 10)
        lst.insert(0, digit)

    return tuple(lst)


def get_digits_from_left_to_right(number, lst=None):
    """Return digits of an integer excluding the sign."""

    if lst is None:
        lst = list()

    number = abs(number)

    if number < 10:
        lst.append(number)
        return tuple(lst)

    get_digits_from_left_to_right(number // 10, lst)
    lst.append(number % 10)

    return tuple(lst)


def sum_digits(number):
    """Return sum digits of number."""

    return sum(get_digits_from_right_to_left(number))


assert get_digits_from_right_to_left(-64517643246567536423) == (6, 4, 5, 1, 7, 6, 4, 3, 2, 4, 6, 5, 6, 7, 5, 3, 6, 4, 2, 3)
assert get_digits_from_right_to_left(-3245214012321021213) == (3, 2, 4, 5, 2, 1, 4, 0, 1, 2, 3, 2, 1, 0, 2, 1, 2, 1, 3)
assert get_digits_from_right_to_left(-40932403024902304) == (4, 0, 9, 3, 2, 4, 0, 3, 0, 2, 4, 9, 0, 2, 3, 0, 4)
assert get_digits_from_right_to_left(-1302132101032132) == (1, 3, 0, 2, 1, 3, 2, 1, 0, 1, 0, 3, 2, 1, 3, 2)
assert get_digits_from_right_to_left(-9999999999999) == (9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
assert get_digits_from_right_to_left(-100000000000) == (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert get_digits_from_right_to_left(-123456789) == (1, 2, 3, 4, 5, 6, 7, 8, 9)
assert get_digits_from_right_to_left(-9651454) == (9, 6, 5, 1, 4, 5, 4)
assert get_digits_from_right_to_left(-1000) == (1, 0, 0, 0)
assert get_digits_from_right_to_left(-129) == (1, 2, 9)
assert get_digits_from_right_to_left(-10) == (1, 0)
assert get_digits_from_right_to_left(-9) == (9, )
assert get_digits_from_right_to_left(0) == (0, )
assert get_digits_from_right_to_left(9) == (9, )
assert get_digits_from_right_to_left(10) == (1, 0)
assert get_digits_from_right_to_left(129) == (1, 2, 9)
assert get_digits_from_right_to_left(100) == (1, 0, 0)
assert get_digits_from_right_to_left(10101) == (1, 0, 1, 0, 1)
assert get_digits_from_right_to_left(54678904) == (5, 4, 6, 7, 8, 9, 0, 4)
assert get_digits_from_right_to_left(9651454) == (9, 6, 5, 1, 4, 5, 4)
assert get_digits_from_right_to_left(123456789) == (1, 2, 3, 4, 5, 6, 7, 8, 9)
assert get_digits_from_right_to_left(2394928349) == (2, 3, 9, 4, 9, 2, 8, 3, 4, 9)
assert get_digits_from_right_to_left(100000000000000) == (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert get_digits_from_right_to_left(9999999999999999) == (9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
assert get_digits_from_right_to_left(123012312312321312312312) == (1, 2, 3, 0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2)


assert get_digits_from_left_to_right(-64517643246567536423) == (6, 4, 5, 1, 7, 6, 4, 3, 2, 4, 6, 5, 6, 7, 5, 3, 6, 4, 2, 3)
assert get_digits_from_left_to_right(-3245214012321021213) == (3, 2, 4, 5, 2, 1, 4, 0, 1, 2, 3, 2, 1, 0, 2, 1, 2, 1, 3)
assert get_digits_from_left_to_right(-40932403024902304) == (4, 0, 9, 3, 2, 4, 0, 3, 0, 2, 4, 9, 0, 2, 3, 0, 4)
assert get_digits_from_left_to_right(-1302132101032132) == (1, 3, 0, 2, 1, 3, 2, 1, 0, 1, 0, 3, 2, 1, 3, 2)
assert get_digits_from_left_to_right(-9999999999999) == (9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
assert get_digits_from_left_to_right(-100000000000) == (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert get_digits_from_left_to_right(-123456789) == (1, 2, 3, 4, 5, 6, 7, 8, 9)
assert get_digits_from_left_to_right(-9651454) == (9, 6, 5, 1, 4, 5, 4)
assert get_digits_from_left_to_right(-1000) == (1, 0, 0, 0)
assert get_digits_from_left_to_right(-129) == (1, 2, 9)
assert get_digits_from_left_to_right(-10) == (1, 0)
assert get_digits_from_left_to_right(-9) == (9, )
assert get_digits_from_left_to_right(0) == (0, )
assert get_digits_from_left_to_right(9) == (9, )
assert get_digits_from_left_to_right(10) == (1, 0)
assert get_digits_from_left_to_right(129) == (1, 2, 9)
assert get_digits_from_left_to_right(100) == (1, 0, 0)
assert get_digits_from_left_to_right(10101) == (1, 0, 1, 0, 1)
assert get_digits_from_left_to_right(54678904) == (5, 4, 6, 7, 8, 9, 0, 4)
assert get_digits_from_left_to_right(9651454) == (9, 6, 5, 1, 4, 5, 4)
assert get_digits_from_left_to_right(123456789) == (1, 2, 3, 4, 5, 6, 7, 8, 9)
assert get_digits_from_left_to_right(2394928349) == (2, 3, 9, 4, 9, 2, 8, 3, 4, 9)
assert get_digits_from_left_to_right(100000000000000) == (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
assert get_digits_from_left_to_right(9999999999999999) == (9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
assert get_digits_from_left_to_right(123012312312321312312312) == (1, 2, 3, 0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 2, 1, 3, 1, 2, 3, 1, 2, 3, 1, 2)


assert 0 == sum_digits(0)
assert 1 == sum_digits(1)
assert 1 == sum_digits(-1)
assert 9 == sum_digits(9)
assert 9 == sum_digits(-9)
assert 1 == sum_digits(10)
assert 1 == sum_digits(-10)
assert 1 == sum_digits(100000)
assert 1 == sum_digits(-100000)
assert 28 == sum_digits(1234567)
assert 28 == sum_digits(-1234567)
assert 28 == sum_digits(100200304056700)
assert 28 == sum_digits(-100200304056700)
assert 45 == sum_digits(-123456789)
assert 45 == sum_digits(123456789)


assert get_count_digits(-99999999999999999999) == 20
assert get_count_digits(-10000000000000000000) == 20
assert get_count_digits(-9999999999999999999) == 19
assert get_count_digits(-1000000000000000000) == 19
assert get_count_digits(-999999999999999999) == 18
assert get_count_digits(-100000000000000000) == 18
assert get_count_digits(-99999999999999999) == 17
assert get_count_digits(-10000000000000000) == 17
assert get_count_digits(-9999999999999999) == 16
assert get_count_digits(-1000000000000000) == 16
assert get_count_digits(-999999999999999) == 15
assert get_count_digits(-100000000000000) == 15
assert get_count_digits(-99999999999999) == 14
assert get_count_digits(-10000000000000) == 14
assert get_count_digits(-9999999999999) == 13
assert get_count_digits(-1000000000000) == 13
assert get_count_digits(-999999999999) == 12
assert get_count_digits(-100000000000) == 12
assert get_count_digits(-99999999999) == 11
assert get_count_digits(-10000000000) == 11
assert get_count_digits(-9999999999) == 10
assert get_count_digits(-1000000000) == 10
assert get_count_digits(-999999999) == 9
assert get_count_digits(-100000000) == 9
assert get_count_digits(-99999999) == 8
assert get_count_digits(-10000000) == 8
assert get_count_digits(-9999999) == 7
assert get_count_digits(-1000000) == 7
assert get_count_digits(-999999) == 6
assert get_count_digits(-100000) == 6
assert get_count_digits(-99999) == 5
assert get_count_digits(-10000) == 5
assert get_count_digits(-9999) == 4
assert get_count_digits(-1000) == 4
assert get_count_digits(-999) == 3
assert get_count_digits(-100) == 3
assert get_count_digits(-99) == 2
assert get_count_digits(-10) == 2
assert get_count_digits(-9) == 1
assert get_count_digits(-1) == 1
assert get_count_digits(0) == 1
assert get_count_digits(1) == 1
assert get_count_digits(9) == 1
assert get_count_digits(10) == 2
assert get_count_digits(99) == 2
assert get_count_digits(100) == 3
assert get_count_digits(999) == 3
assert get_count_digits(1000) == 4
assert get_count_digits(9999) == 4
assert get_count_digits(10000) == 5
assert get_count_digits(99999) == 5
assert get_count_digits(100000) == 6
assert get_count_digits(999999) == 6
assert get_count_digits(1000000) == 7
assert get_count_digits(9999999) == 7
assert get_count_digits(10000000) == 8
assert get_count_digits(99999999) == 8
assert get_count_digits(100000000) == 9
assert get_count_digits(999999999) == 9
assert get_count_digits(1000000000) == 10
assert get_count_digits(9999999999) == 10
assert get_count_digits(10000000000) == 11
assert get_count_digits(99999999999) == 11
assert get_count_digits(100000000000) == 12
assert get_count_digits(999999999999) == 12
assert get_count_digits(1000000000000) == 13
assert get_count_digits(9999999999999) == 13
assert get_count_digits(10000000000000) == 14
assert get_count_digits(99999999999999) == 14
assert get_count_digits(100000000000000) == 15
assert get_count_digits(999999999999999) == 15
assert get_count_digits(1000000000000000) == 16
assert get_count_digits(9999999999999999) == 16
assert get_count_digits(10000000000000000) == 17
assert get_count_digits(99999999999999999) == 17
assert get_count_digits(100000000000000000) == 18
assert get_count_digits(999999999999999999) == 18
assert get_count_digits(1000000000000000000) == 19
assert get_count_digits(9999999999999999999) == 19
assert get_count_digits(10000000000000000000) == 20
assert get_count_digits(99999999999999999999) == 20
