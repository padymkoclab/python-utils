
# http://danielhnyk.cz/simple-server-client-aplication-python-3/
# https://pymotw.com/2/socket/tcp.html

import logging
from logging.config import fileConfig
import socket

import factory


fileConfig('utils/python/socket/logging.ini')

logger = logging.getLogger()

HOST = 'localhost'
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logger.info('Connecting to a server by address {}:{}'.format(HOST, PORT))


sock.connect((HOST, PORT))


def create_new_msg():
    user = factory.Faker('name').generate(())
    sentence = factory.Faker('sentence').generate(())
    msg = '{}: "{}"'.format(user, sentence)
    return msg.encode()


try:

    msg = create_new_msg()
    logger.info('Sending a data to the server ...')
    sock.sendall(msg)

    amount_received = 0
    amount_expected = len(msg)

    while amount_received < amount_expected:
        data = sock.recv(8000000000)
        amount_received += len(data)
        print(1, len(data), data, amount_received, amount_expected)

finally:
    logger.info('Close the socket to the server.')
    sock.close()
