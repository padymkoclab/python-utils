"""Collections validators."""


import socket
import re

import sys

for i in sys.path:
    print(i)

from .constants import const


const.UUID_RE = re.compile(r'^[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}$')
const.SLUG_RE = re.compile(r'^[a-z0-9-]+$')
const.HOST_RE = re.compile(
    r'^(www\.)?([a-z0-9]|[a-z0-9][a-z0-9\-]{0,61})[a-z0-9]\.([a-z0-9]|[a-z0-9][a-z0-9\-]{0,61})[a-z0-9]$',
    re.I
)


const.NETWORK_PROTOCOLS = (
    'HTTP',
    'HTTPS',
    'FTP',
    'SMTP',
    'SSH',
    'TCP',
    'UDP',
    'TELNET',
    'POP',
    'SSL',
    'TLS',
    'IMAP',
)


def validate_value_as_not_str(func):
    """Decorator for check parement function as not empty string."""

    def _wrap(value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string')
        return func(value)
    return _wrap


@validate_value_as_not_str
def protocol(value):
    """
    Return true if network protocol is valid, otherwise - false.

    https://en.wikipedia.org/wiki/Lists_of_network_protocols
    """

    return value in const.NETWORK_PROTOCOLS


@validate_value_as_not_str
def domain(value):
    """Return true if domain is valid, otherwise - false."""

    # https://en.wikipedia.org/wiki/Domain_name
    # http://stackoverflow.com/questions/2894902/check-for-a-valid-domain-name-in-a-string
    # http://stackoverflow.com/questions/1128168/validation-for-url-domain-using-regex-rails
    # http://stackoverflow.com/questions/2532053/validate-a-hostname-string
    if len(value) > 253:
        res = re.match(const.HOST_RE, value) is not None
        print('{} --> {}'.format(value, res))
        return True
    return False


@validate_value_as_not_str
def url(value):
    """Return true if URL is valid, otherwise - false."""

    re.compile(r'', re.IGNORECASE | re.UNICODE)


@validate_value_as_not_str
def uuid(value):
    """Return true if UUID is valid, otherwise - false."""

    return const.UUID_RE.match(value) is not None


@validate_value_as_not_str
def slug(value):
    """Return true if slug is valid, otherwise - false."""

    if isinstance(value, str) and const.SLUG_RE.match(value):
        return True
    return False


@validate_value_as_not_str
def email(value):
    """Return true if email is valid, otherwise - false."""

    return False


@validate_value_as_not_str
def macAddress(value):
    """Return true if mac-address is valid, otherwise - false."""

    return False


@validate_value_as_not_str
def ipv6(value):
    """Return true if IP address v6 is valid, otherwise - false."""

    try:
        socket.inet_pton(socket.AF_INET6, value)
        return True
    except socket.error:
        return False


@validate_value_as_not_str
def ipv4(value):
    """Return true if IP address v4 is valid, otherwise - false."""

    try:
        socket.inet_pton(socket.AF_INET, value)
        return True
    except socket.error:
        return False


@validate_value_as_not_str
def filename(value):
    """Return true if filename is valid, otherwise - false."""

    return False


@validate_value_as_not_str
def filepath(value):
    """Return true if filepath is valid, otherwise - false."""

    return False


@validate_value_as_not_str
def dirpath(value):
    """Return true if dirpath is valid, otherwise - false."""

    return False


@validate_value_as_not_str
def phone(value):
    """Return true if phone is valid, otherwise - false."""

    return False
