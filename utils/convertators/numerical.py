"""

http://stackoverflow.com/questions/4296249/how-do-i-convert-a-hex-triplet-to-an-rgb-tuple-and-back/4296263#4296263
https://pymotw.com/3/struct/

import struct
import binascii


fmt = 'I s f'


s = struct.Struct(fmt)
p = s.pack(1, b'text', 321.21)

s2 = struct.Struct(fmt)
print(s2.unpack(p))

"""


import weakref


def bin_from_float(number: float):
    """Return binary from float value.

    >>> bin_from_float(446.15625)
    0b110111110.00101
    """

    integer = int(number)
    fractional = abs(number) % 1

    count = len(str(fractional)[2:])

    binary = []
    while (count > 0):
        # print(number, integer, fractional)
        fractional = fractional * 2
        if fractional >= 1:
            fractional = fractional - 1
            binary.append('1')
        else:
            binary.append('0')
        count -= 1

    if binary:
        return '{}.{}'.format(bin(integer), ''.join(binary))

    return bin(integer)


def bin_to_float(string: str):
    """Convert a string in binary to a float, if it possible."""

    if string.startswith('0b'):
        string = string[2:]

    integer, fractional = string.split('.')

    integer = int(integer, 2) if integer else 0

    if fractional:
        fractional = sum(int(bit) * 2 ** (-i) for i, bit in enumerate(fractional))
    else:
        fractional = 0

    return integer + fractional


def number_to_roman(number: int):
    """Convert number from arabic to roman."""

    return


def number_from_roman(string: str):
    """Convert number from roman to arabic."""

    return


# print(bin_from_float(-455.375))
# print(bin_from_float(446.15625))
# print(bin_from_float(0.15625))
# print(bin_from_float(446))
# print(bin_to_float("0b110111110.00101"))
# print(bin_to_float(".01101101"))

