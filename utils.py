"""
[summary]

[description]
"""

import datetime
import io
import base64
from IPython.core import display as JupyterDisplay
import inspect
import subprocess


def open_in_sublime(object_):

    path = inspect.getfile(object_)
    subprocess.call(['subl', path])


class staticmethod_(object):
    """Pure the Python implementation of decorator staticmethod."""

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, objtype=None):
        return self.method


class classmethod_(object):
    """Pure the Python implementation of decorator classmethod."""

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, objtype=None):

        objtype = type(obj) if objtype is None else objtype

        return lambda *args, **kwargs: self.method(objtype, *args, **kwargs)


class staticclassmethod(object):

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, objtype=None):

        objtype = type(obj) if objtype is None else objtype

        def method(*args, **kwargs):
            return self.method(*args, **kwargs)

        return method


class classproperty(object):

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, objtype=None):
        objtype = type(obj) if objtype is None else objtype
        return self.method(objtype)


def check_method_of_object(obj, method):
    """ """

    try:
        attr = getattr(obj, method)
    except AttributeError:
        raise Exception('Object has not method "{}"'.format(method))
    else:
        if not callable(attr):
            raise Exception('Attribute {} of the object is not callable'.format(method))


def split_sequence_to_chunks(sequence, n):
    """ """

    if n < 1:
        raise ValueError()

    chuncks = list()
    for i in range(0, len(sequence), n):
        chuncks.append(sequence[i: i + n])
    return chuncks


def flatten(sequence):
    """
    Make an iterable, arbitrary-nested object as flatten
    and return it as generator.

    >>> tuple(flatten([[4,5, [2, [3]]], [1,[2, [1, [2]]],3], [1,[2,3]]]))
    (4, 5, 2, 3, 1, 2, 1, 2, 3, 1, 2, 3)
    >>> tuple(flatten([[[[[[[[1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]]]]]]]]]))
    (1, 2, 3, 4, 5, 6, 7, 8, 9)
    >>> tuple(flatten(('aaa', 'ddd', ('bbbb', ('ccc', ('ddd', 'e', 'f'))))))
    ('aaa', 'ddd', 'bbbb', 'ccc', 'ddd', 'e', 'f')
    """

    for i in sequence:
        if isinstance(i, (list, tuple)):
            yield from flatten(i)
        else:
            yield i


def run_video_in_jupyter(path):
    """
    path = "/media/wlysenko/66ABF2AC3D03BAAA/Light/Video/Сборка/Пришло время! Пора просыпаться!.mp4"

    """

    video = io.open(path, 'r+b').read()
    encoded = base64.b64encode(video)
    JupyterDisplay.Video(data="""
        <video alt="test" controls>
            <source src="data:video/mp4;base64,{0}" type="video/mp4" />
        </video>
        """.format(encoded.decode('ascii')))


def rgb_to_hex(*args):

    if len(args) != 3:
        raise ValueError()

    return '#{0:X}{1:X}{2:X}'.format(*args)


def hex_to_rgb(val):

    val = val.lstrip('#')

    lv = len(val)

    if lv == 3:
        val = ''.join(i * 2 for i in val)
        lv = 6

    return tuple(int(val[i: i + lv // 3], 16) for i in range(0, lv, lv // 3))


def get_filename_with_datetime(name, extension):
    """Return filename with determined name, current datetime in internation format and extension."""

    now = datetime.datetime.now()

    # truncated version datetime ISO format (withput microseconds and and timezone)
    datetime_ISO_format = now.strftime('%Y-%m-%d %H:%M:%S')

    return '{0} {1}.{2}'.format(name, datetime_ISO_format, extension)


def generate_captcha(request):
    raise NotImplementedError
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    img = Image.new('RGBA', (160, 80), color)
    imgDrawer = ImageDraw.Draw(img)
    textImg = Image.new('RGBA', (160, 80))
    tmpDraw = ImageDraw.Draw(textImg)
    font = ImageFont.truetype("resources/UbuntuMono-RI.ttf", 26)
    i = 15
    key = []
    for x in xrange(1, 7):
        r = str(random.randint(0, 9))
        key.append(r)
        tmpDraw.text((i, random.randint(20, 30)), r,
                     font=font, fill=(0, 0, 0))
        i += 22
    request.session['captcha'] = ''.join(key)
    for o in xrange((80 * 160) / 500):
        imgDrawer.line((random.randint(0, 160), random.randint(0, 80), random.randint(0, 160), random.randint(0, 80)),
                       fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    output = StringIO.StringIO()
    textImg = textImg.rotate(random.randint(-20, 20))
    mask = Image.new('RGBA', (160, 80), (0, 0, 0))
    mask.paste(textImg, (0, 0))
    img.paste(textImg, (0, 0), mask)
    img.save(output, format='png')
    return StreamingHttpResponse([output.getvalue()], content_type="image/png")


def partial(func, *oldargs, **oldkwargs):
    """
    def a(a, b, c, d):
        return a + b + c + d
    assert partial(a, 5, c=0)(8, d=2) == 15
    """

    def wrap(*newargs, **newkwargs):
        newkwargs.update(oldkwargs)
        return func(*(oldargs + newargs), **newkwargs)
    return wrap
