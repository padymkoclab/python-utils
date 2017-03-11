"""Collections utils for network."""


import ipaddress


def convert_ip_v4tov6(value):
    """Covert ipv4 to ipv6."""

    # http://stackoverflow.com/questions/19750929/converting-ipv4-address-to-a-hex-ipv6-address-in-python
    return '0:0:0:0:0:' + ipaddress.IPv6Address('ffff::' + value).compressed
