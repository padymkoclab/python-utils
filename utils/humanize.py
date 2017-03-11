
import sys
import itertools


def intword(number):

    return


def intcomma(number, locale='en_US'):
    """ """

    if -999 < number < 999:
        return str(number)

    result = str()

    print(number)
    while number:
        number, digit = divmod(number, 10)
        print(digit, end=' ')
    print()

    return result


# intcomma(123)
# intcomma(1234)
# intcomma(12345)
# intcomma(123456)
# intcomma(1234567)
