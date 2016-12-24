
import logging as pylogging


def create_logger_by_filename(name):
    """Return a logger for with passed name."""

    # create log
    logger = pylogging.getLogger(name)
    logger.setLevel(pylogging.DEBUG)

    # create handler for terminal
    terminalHandler = pylogging.StreamHandler()

    # set level messages for handler
    terminalHandler.setLevel(pylogging.DEBUG)

    # create formatter for handler
    fmt = pylogging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter for handler
    terminalHandler.setFormatter(fmt)

    # add handler to logger
    logger.addHandler(terminalHandler)

    return logger
