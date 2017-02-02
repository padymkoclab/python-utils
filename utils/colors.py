"""Utils for working with colors."""

import textwrap


def rgb_to_hex(value1, value2, value3):
    """
    Convert RGB value (as three numbers each ranges from 0 to 255) to hex format.

    >>> rgb_to_hex(235, 244, 66)
    '#EBF442'
    >>> rgb_to_hex(56, 28, 26)
    '#381C1A'
    >>> rgb_to_hex(255, 255, 255)
    '#FFFFFF'
    >>> rgb_to_hex(0, 0, 0)
    '#000000'
    >>> rgb_to_hex(203, 244, 66)
    '#CBF442'
    >>> rgb_to_hex(53, 17, 8)
    '#351108'
    """

    for value in (value1, value2, value3):
        if not 0 <= value <= 255:
            raise ValueError('Value each slider must be ranges from 0 to 255')
    return '#{0:02X}{1:02X}{2:02X}'.format(value1, value2, value3)


def hex_to_rgb(value):
    """
    Convert color`s value in hex format to RGB format.

    >>> hex_to_rgb('fff')
    (255, 255, 255)
    >>> hex_to_rgb('ffffff')
    (255, 255, 255)
    >>> hex_to_rgb('#EBF442')
    (235, 244, 66)
    >>> hex_to_rgb('#000000')
    (0, 0, 0)
    >>> hex_to_rgb('#000')
    (0, 0, 0)
    >>> hex_to_rgb('#54433f')
    (84, 67, 63)
    >>> hex_to_rgb('#f7efed')
    (247, 239, 237)
    >>> hex_to_rgb('#191616')
    (25, 22, 22)
    """

    if value[0] == '#':
        value = value[1:]

    len_value = len(value)

    if len_value not in [3, 6]:
        raise ValueError('Incorect a value hex {}'.format(value))

    if len_value == 3:
        value = ''.join(i * 2 for i in value)
    return tuple(int(i, 16) for i in textwrap.wrap(value, 2))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
