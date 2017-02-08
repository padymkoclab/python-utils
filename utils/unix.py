"""Utils without category."""

import os


def printANSI():
    """Print in terminal most used ANSI-codes."""
    escape_code = '\033'
    console_width = os.get_terminal_size().columns

    for l in range(0, 10):
        print('-' * console_width)
        for j in range(30, 40):
            for e in (range(30, 38), range(40, 48)):
                for k in e:
                    s = '{};{};{}m'.format(l, j, k)
                    m = '{}[{} {} {}[00m'.format(escape_code, s, s, escape_code)
                    print(m, end='')
            print()
