"""Utils for working with colors."""


def rgb_to_hex(*args):
    """
    Convert RGB to HEX.

    >>> rgb_to_hex(235, 244, 66)
    '#EBF442'
    >>> rgb_to_hex(56, 28, 26)
    '#381C1A'
    >>> rgb_to_hex(255, 255, 255)
    '#FFFFFF'
    >>> rgb_to_hex(0, 0, 0)
    '#000000'
    """

    if len(args) != 3:
        raise ValueError("RGB color must be passed as three number")

    return '#{0:X}{1:X}{2:X}'.format(*args)


def hex_to_rgb(val):
    """Convert HEX to RGB."""

    val = val.lstrip('#')

    lv = len(val)

    if lv == 3:
        val = ''.join(i * 2 for i in val)
        lv = 6

    return tuple(int(val[i: i + lv // 3], 16) for i in range(0, lv, lv // 3))
