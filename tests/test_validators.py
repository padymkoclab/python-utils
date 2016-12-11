
import unittest

from ..validators import uuid, slug, ipv4, ipv6


class ValidatorTest(unittest.TestCase):

    def test_uuid(self):

        assert uuid('2bc1c94f-0deb-43e9-92a1-4775189ec9f8') is True
        assert uuid('bd9deaf6-b21e-11e6-9a15-9c2a7053c949') is True
        assert uuid('14c0ed8a-206f-4523-a672-921c7cbd209f') is True
        assert uuid('c9d00794-cfa8-46df-90a1-a1bfdaf249f4') is True
        assert uuid('14c0ed8a_206f-4523-a672-921c7cbd209f') is False
        assert uuid('14c0ed8-206f-4523-a672-921c7cbd209f') is False
        assert uuid('114c0ed8a-206f-4523-a672-921c7cbd209f') is False
        assert uuid('') is False
        assert uuid(0) is False
        assert uuid(None) is False
        assert uuid([]) is False
        assert uuid('2bc1c94f 0deb-43e9-92a1-4775189ec9f8') is False
        assert uuid('123e4567-e89b-12d3-a456-426655440000') is True
        assert uuid('886313e1-3b8a-5372-9b90-0c9aee199e5d') is True
        assert uuid('a8098c1a-f86e-11da-bd1a-00112444be1e') is True

    def test_slug(self):

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
        assert slug(()) is False
        assert slug(0) is False
        assert slug(None) is False

    def test_idv4(self):

        assert ipv4('69.89.31.226') is True
        assert ipv4('19.117.63.126') is True
        assert ipv4('127.0.0.1') is True
        assert ipv6('900.200.100.75') is False
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
        assert ipv4([]) is False
        assert ipv4('') is False
        assert ipv4(None) is False
        assert ipv4(0) is False
        assert ipv4('12.12.12.12') is True

    def test_idv6(self):

        assert ipv6('69.89.31.226') is False
