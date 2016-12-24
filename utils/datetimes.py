"""Utils for working with date and time."""

import datetime


def get_filename_with_datetime(name, extension):
    """Return filename with determined name, current datetime in internation format and extension."""
    now = datetime.datetime.now()

    # truncated version datetime ISO format (withput microseconds and and timezone)
    datetime_ISO_format = now.strftime('%Y-%m-%d %H:%M:%S')

    return '{0} {1}.{2}'.format(name, datetime_ISO_format, extension)
