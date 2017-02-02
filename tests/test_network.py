

from utils.network import convert_ip_v4tov6


def test_convert_ip_v4tov6():

    assert convert_ip_v4tov6('50.94.165.48') == '0:0:0:0:0:ffff:325e:a530'
    assert convert_ip_v4tov6('220.51.107.99') == '0:0:0:0:0:ffff:dc33:6b63'
    assert convert_ip_v4tov6('172.60.91.8') == '0:0:0:0:0:ffff:ac3c:5b08'
    assert convert_ip_v4tov6('95.2.61.251') == '0:0:0:0:0:ffff:5f02:3dfb'
    assert convert_ip_v4tov6('254.17.196.58') == '0:0:0:0:0:ffff:fe11:c43a'
    assert convert_ip_v4tov6('214.3.88.17') == '0:0:0:0:0:ffff:d603:5811'
    assert convert_ip_v4tov6('59.254.123.196') == '0:0:0:0:0:ffff:3bfe:7bc4'
    assert convert_ip_v4tov6('201.9.169.102') == '0:0:0:0:0:ffff:c909:a966'
    assert convert_ip_v4tov6('21.203.172.203') == '0:0:0:0:0:ffff:15cb:accb'
    assert convert_ip_v4tov6('235.173.151.106') == '0:0:0:0:0:ffff:ebad:976a'
    assert convert_ip_v4tov6('18.46.38.234') == '0:0:0:0:0:ffff:122e:26ea'
    assert convert_ip_v4tov6('215.9.4.54') == '0:0:0:0:0:ffff:d709:436'
    assert convert_ip_v4tov6('39.204.223.5') == '0:0:0:0:0:ffff:27cc:df05'
    assert convert_ip_v4tov6('131.31.62.204') == '0:0:0:0:0:ffff:831f:3ecc'
    assert convert_ip_v4tov6('48.183.95.206') == '0:0:0:0:0:ffff:30b7:5fce'
    assert convert_ip_v4tov6('85.217.71.232') == '0:0:0:0:0:ffff:55d9:47e8'
    assert convert_ip_v4tov6('34.111.144.113') == '0:0:0:0:0:ffff:226f:9071'
    assert convert_ip_v4tov6('233.45.60.168') == '0:0:0:0:0:ffff:e92d:3ca8'
    assert convert_ip_v4tov6('239.43.102.54') == '0:0:0:0:0:ffff:ef2b:6636'
    assert convert_ip_v4tov6('52.108.169.243') == '0:0:0:0:0:ffff:346c:a9f3'
