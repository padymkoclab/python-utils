
import re

# https://validators.readthedocs.io/en/latest/

re_uuid = re.compile(r'^[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}$')
re_slug = re.compile(r'^[a-z0-9-]+$')


def url(value, domains=None, protocols=None):

    re.compile(r'', re.IGNORECASE | re.UNICODE)

    if protocols is None:
        protocols = ['http', 'https']


def uuid(value):

    if isinstance(value, str) and re_uuid.match(value):
        return True
    return False


def slug(value):

    if isinstance(value, str) and re_slug.match(value):
        return True
    return False


def email(value):
    pass


def id_address(value):
    pass


def domain(value):
    pass


def ipv6(value):
    pass


def ipv4(value):
    pass
