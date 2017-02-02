"""Tests for validators."""

import unittest

import pytest

from utils.validators import uuid, slug, ipv4, ipv6, domain


def test_domain(self):
    """Test validator of domain."""

    assert domain('google.com') is True
    assert domain('google.com.ru') is True
    assert domain('icann.org') is True
    assert domain('icann-.org') is False
    assert domain('-icann.org') is False
    assert domain(' google.com') is False
    assert domain('czds.icann.org') is True
    assert domain('i.o') is True
    assert domain('google .com ') is False
    assert domain(' ') is False
    assert domain('xn--stackoverflow.com') is False
    assert domain('stackoverflow.xn--com') is False
    assert domain('stackoverflow.ul.com') is True
    assert domain('stackoverflow.com') is True
    assert domain('roberts-jones.com') is True
    assert domain('fernandez.com') is True
    assert domain('chandler.net') is True
    assert domain('parker.net') is True
    assert domain('ellis.com') is True
    assert domain('bruce-glover.com') is True
    assert domain('baker-luna.info') is True
    assert domain('campbell.net') is True


def test_uuid(self):
    """Test UUID."""

    assert uuid('2bc1c94f-0deb-43e9-92a1-4775189ec9f8') is True
    assert uuid('bd9deaf6-b21e-11e6-9a15-9c2a7053c949') is True
    assert uuid('14c0ed8a-206f-4523-a672-921c7cbd209f') is True
    assert uuid('c9d00794-cfa8-46df-90a1-a1bfdaf249f4') is True
    assert uuid('14c0ed8a_206f-4523-a672-921c7cbd209f') is False
    assert uuid('14c0ed8-206f-4523-a672-921c7cbd209f') is False
    assert uuid('114c0ed8a-206f-4523-a672-921c7cbd209f') is False
    assert uuid('17148075-676f-47a6-861f-c5b189c6f2ce') is True
    assert uuid('2bc1c94f 0deb-43e9-92a1-4775189ec9f8') is False
    assert uuid('123e4567-e89b-12d3-a456-426655440000') is True
    assert uuid('886313e1-3b8a-5372-9b90-0c9aee199e5d') is True
    assert uuid('a8098c1a-f86e-11da-bd1a-00112444be1e') is True
    assert uuid('') is False

    with pytest.raises(ValueError):
        assert uuid(0)
    with pytest.raises(ValueError):
        assert uuid(None) is False
    with pytest.raises(ValueError):
        assert uuid([]) is False


def test_slug(self):
    """Test slug."""

    assert slug('from django.utils.translation import ugettext_lazy') is False
    assert slug('I\'ve been trying to figure out what the best ') is False
    assert slug('знатный-родовитый-благородный-благородных-кровей') is False
    assert slug('не нажимайте на него, попытайтесь воздействовать на него лаской') is False
    assert slug('rem-fuga-sint-atque') is True
    assert slug('dolore-eius') is True
    assert slug('facilis') is True
    assert slug('Laboriosam') is False
    assert slug('laboriosaM') is False
    assert slug('labOriosa') is False
    assert slug('') is False
    assert slug('the-part-of-an-url-which-identifies-a-page-using-human-readable-keywords') is True
    assert slug('121414351434') is True
    assert slug('-') is True
    assert slug('----------') is True

    with pytest.raises(ValueError):
        assert slug(()) is False
    with pytest.raises(ValueError):
        assert slug(0) is False
    with pytest.raises(ValueError):
        assert slug(None) is False


def test_idv4(self):
    """Test ipaddress v4."""

    assert ipv4('69.89.31.226') is True
    assert ipv4('19.117.63.126') is True
    assert ipv4('127.0.0.1') is True
    assert ipv4('900.200.100.75') is False
    assert ipv4('abc.0.0.1') is False
    assert ipv4('1278.0.0.1') is False
    assert ipv4('127.0.0.abc') is False
    assert ipv4('123.5.77.88') is True
    assert ipv4('255.255.255.255') is True
    assert ipv4('0.0.0.0') is True
    assert ipv4('256.255.255.255') is False
    assert ipv4('255.255.255.256') is False
    assert ipv4('255.256.255.255') is False
    assert ipv4('255.255.256.255') is False
    assert ipv4('300.300.256.300') is False
    assert ipv4('-1.0.255.0') is False
    assert ipv4('12.12.12.12') is True
    assert ipv4('') is False
    assert ipv4('53.254.123.44') is True
    assert ipv4('127.175.180.17') is True
    assert ipv4('243.214.151.234') is True
    assert ipv4('32.90.138.94') is True
    assert ipv4('199.250.6.202') is True
    assert ipv4('176.154.222.145') is True
    assert ipv4('38.125.205.216') is True
    assert ipv4('220.228.141.249') is True
    assert ipv4('132.213.221.227') is True
    assert ipv4('225.0.177.164') is True

    with pytest.raises(ValueError):
        assert ipv4([]) is False
    with pytest.raises(ValueError):
        assert ipv4(None) is False
    with pytest.raises(ValueError):
        assert ipv4(0) is False


def test_idv6(self):
    """Test ipaddress v6."""

    assert ipv6('2001:0db8:0000:0000:0000:ff00:0042:8329') is True
    assert ipv6('2001:db8:0:0:0:ff00:42:8329') is True
    assert ipv6('2001:db8::ff00:42:8329') is True
    assert ipv6('0.0.0.0') is False
    assert ipv6('2002::ffff:ffff') is True
    assert ipv6('2002::') is True
    assert ipv6('0') is False
    assert ipv6('69.89.31.226') is False
    assert ipv6('') is False
    assert ipv6('61f5:10ed:47a1:ef5b:416f:bffc:c9c9:1ff0') is True
    assert ipv6('5522:4a59:1c79:a945:3280:13b9:ec3c:b585') is True
    assert ipv6('b40c:a53b:4d79:5f30:9ff1:a9f0:40b6:92e7') is True
    assert ipv6('da0:a56b:cae0:a91b:f8a1:b047:c5ed:5bd') is True
    assert ipv6('13d3:bb4c:736c:26eb:7107:2658:380:2d47') is True
    assert ipv6('5889:f7a5:8c54:94e5:f295:5090:8165:8845') is True
    assert ipv6('35b4:2c66:1111:d532:6a04:14ed:6531:4f10') is True
    assert ipv6('70db:9b18:a7f1:8838:1f8f:8c55:142a:b056') is True
    assert ipv6('7f69:8c56:2ad3:ad48:746d:3c9e:81b3:dd98') is True
    assert ipv6('7d72:198c:1ec0:8948:b8d8:e421:cb10:18c2') is True

    with pytest.raises(ValueError):
        assert ipv6([]) is False
    with pytest.raises(ValueError):
        assert ipv6(None) is False
    with pytest.raises(ValueError):
        assert ipv6(0) is False
