"""Utils for working with strings."""

import collections


def getWords(text: str) -> list:
    """
    Return words found in a text as list.

    A word considering if contains at least single digit or letter.
    """
    if not isinstance(text, str):
        raise TypeError('Must be passed string, not {0}'.format(type(text)))
    return list(
        filter(
            lambda string: any((char.isalnum() for char in string)),
            text.split(' ')
        )
    )


def getCountWords(text: str) -> int:
    """
    Return count words in a text.

    A word considering if contains at least single digit or letter.
    """
    return len(getWords(text))


def getCounterWords(text: str, ignorecase=False) -> collections.Counter:
    """Count words in text with register and without it."""
    if not isinstance(text, str):
        raise TypeError('Must be passed string, not {0}'.format(type(text)))
    words = getWords(text)
    if ignorecase is True:
        words = (word.lower() for word in words)
    return collections.Counter(words)
