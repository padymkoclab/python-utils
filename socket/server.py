
import logging
from logging.config import fileConfig
import socket


fileConfig('utils/python/socket/logging.ini')

logger = logging.getLogger()

HOST = 'localhost'
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logger.info('Socket created')
logger.info('Server started on {}:{}'.format(HOST, PORT))

sock.bind((HOST, PORT))
sock.listen(1)

while True:
    logger.warning('Waiting connection ...')
    connection, client_address = sock.accept()
    logger.warning('Connection from address: {0}:{1}'.format(*client_address))

    try:
        data = connection.recv(16)

        if data:
            logger.info('Received "{}"'.format(data))
            logger.info('Sending data back to the sender')
            connection.sendall(data)
        else:
            logger.info('No more data from {0}:{1}'.format(*client_address))
            break
    finally:
        connection.close()
