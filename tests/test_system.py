
import re
import subprocess

from ..system import get_screen_dimensions


def test_get_screen_dimensions_test():

    popen = subprocess.Popen('xrandr | grep "*"', shell=True, stdout=subprocess.PIPE)
    output = popen.communicate()[0]
    output = output.decode().strip()
    dimension = re.match(r'(\d+x\d+)', output).group(1)

    width, height = tuple(map(int, dimension.split('x')))

    assert get_screen_dimensions() == dict(width=width, height=height)
