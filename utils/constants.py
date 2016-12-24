# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
Constants for Python programming language
"""

import collections


__all__ = ('const', )


RUSSIAN_LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРТУФХЦЧШЩЫЭЮЯабвгдеёжзийклмнопрстуфхцчшщыьэюя'

CHOICES_LEXERS = [
    ('awk', 'Awk'),
    # ('base_makefile', 'Base Makefile'),
    ('bash', 'Bash'),
    ('coffeescript', 'CoffeeScript'),
    ('css', 'CSS'),
    ('css_django_jinja', 'CSS+Django/Jinja'),
    ('django_jinja', 'Django/Jinja'),
    ('html', 'HTML'),
    ('html_django_jinja', 'HTML+Django/Jinja'),
    ('ipython3', 'IPython'),
    ('javascript', 'JavaScript'),
    ('javascript_django_jinja', 'JavaScript+Django/Jinja'),
    ('json', 'JSON'),
    # ('lesscss', 'LessCss'),
    # ('makefile', 'Makefile'),
    ('mysql', 'MySQL'),
    ('numpy', 'NumPy'),
    ('postgresql_console', 'PostgreSQL'),
    # ('python2', 'Python 2'),
    ('python3', 'Python'),
    ('restructuredtext', 'reStructuredText'),
    # ('sass', 'Sass'),
    ('sql', 'SQL'),
    ('xml', 'XML'),
    ('yaml', 'YAML'),
]


class Constant(object):
    """
    Implementation strict constants in Python 3.

    A constant can be set up, but can not be changed or deleted.
    Value of constant may any immutable type, as well as list or set.
    Besides if value of a constant is list or set, it will be converted in an immutable type as next:
        list -> tuple
        set -> frozenset
    Dict as value of a constant has no support.

    >>> const = Constant()
    >>> del const.temp
    Traceback (most recent call last):
    NameError: name 'temp' is not defined
    >>> const.temp = 1
    >>> const.temp = 88
    Traceback (most recent call last):
        ...
    TypeError: Constanst can not be changed
    >>> del const.temp
    Traceback (most recent call last):
        ...
    TypeError: Constanst can not be deleted
    >>> const.I = ['a', 1, 1.2]
    >>> print(const.I)
    ('a', 1, 1.2)
    >>> const.F = {1.2}
    >>> print(const.F)
    frozenset({1.2})
    >>> const.D = dict()
    Traceback (most recent call last):
        ...
    TypeError: dict can not be used as constant
    >>> del const.UNDEFINED
    Traceback (most recent call last):
        ...
    NameError: name 'UNDEFINED' is not defined
    >>> d = const()
    >>> d['I'] == ('a', 1, 1.2)
    True
    >>> d['temp'] == 1
    True
    >>> d['F'] == frozenset({1.2})
    True
    """
    def __setattr__(self, name, value):
        """Declaration a constant with value. If mutable - it will be converted to immutable, if possible.
        If the constant already exists, then made prevent againt change it."""

        if name in self.__dict__:
            raise TypeError('Constanst can not be changed')

        if not isinstance(value, collections.Hashable):
            if isinstance(value, list):
                value = tuple(value)
            elif isinstance(value, set):
                value = frozenset(value)
            elif isinstance(value, dict):
                raise TypeError('dict can not be used as constant')
            else:
                raise ValueError('Muttable or custom type is not supported')
        self.__dict__[name] = value

    def __delattr__(self, name):
        """Deny against deleting a declared constant."""

        if name in self.__dict__:
            raise TypeError('Constanst can not be deleted')
        raise NameError("name '%s' is not defined" % name)

    def __call__(self):
        """Return all constans."""

        return self.__dict__


const = Constant()


if __name__ == '__main__':
    import doctest
    doctest.testmod()