
import collections
import re


"""[summary]

[description]
"""


def findall_words(text):
    """
    Find and return words in text.

    >>> findall_words('')
    []
    >>> findall_words('text')
    ['text']
    >>> findall_words('No problem, provided that the traceback is the only output.')
    ['No', 'problem', 'provided', 'that', 'the', 'traceback', 'is', 'the', 'only', 'output']
    >>> findall_words('A number of option flags control various aspects of doctest’s behavior.')
    ['A', 'number', 'of', 'option', 'flags', 'control', 'various', 'aspects', 'of', 'doctest’s', 'behavior']
    """

    if not isinstance(text, str):
        raise TypeError('Must be passed string, not {0}'.format(type(text)))
    if text:
        # complile basic chars of punctuation for removing it from string
        basic_chars_punctuation = re.compile('[{0}]'.format('!"#$%&\()*+,/:;<=>?@[\\]^_`{|}~'))
        # clean basic chars of punctuation from text
        text = basic_chars_punctuation.sub(' ', text)
        # remove ending point (in sentence)
        text = re.sub(r' *\. *$', '', text)
        # remove point in endgin nested sentence, if it have
        # or remove point in sentence break as paragraph
        text = re.sub(r'(\. )|(\.\n)', ' ', text)
        # remove char ' on sides words
        text = re.sub(r'(\' )|( \')', ' ', text)
        # remove dash
        text = re.sub(r'\W-\W', ' ', text)
        # getting words by split string and return it
        words = text.split()
        return words
    return []


def count_words(text):
    """Return count words in text."""

    if not isinstance(text, str):
        raise TypeError('Must be passed string, not {0}'.format(type(text)))
    if text:
        words = findall_words(text)
        len(words)
    return 0


def counter_words(text, ignorecase=False):
    """Count words in text with register and without it."""

    if not isinstance(text, str):
        raise TypeError('Must be passed string, not {0}'.format(type(text)))
    if text:
        words = findall_words(text)
        if ignorecase is True:
            words = (word.lower() for word in words)
        return collections.Counter(words)
    return 0
