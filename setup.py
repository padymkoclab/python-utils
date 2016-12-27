"""Install as python module."""

import re
import pathlib

from setuptools import setup

BASE_DIR = pathlib.Path(__file__).absolute().parent


def get_README():
    """Read and return content README file."""

    files = [
        path for path in pathlib.Path('.').iterdir()
        if path.match('README') or
        any(path.match('README.{}'.format(i)) for i in ['txt', 'md', 'rst'])
    ]

    count_files = len(files)
    if count_files == 0:
        raise FileNotFoundError('Not found file README, README.txt, README.md or README.rst')
    elif count_files > 1:
        raise OSError('Found several files for README')
    return files[0].read_text()


def get_version_package():
    """Return current version of package."""

    content = pathlib.Path('utils/__init__.py').read_text()
    version = re.findall(r'__version__\W*=\W*\'(\d+\.\d+\.\d+)\'', content)

    if len(version) != 1:
        raise ValueError('Not found value of version of this package')

    return version[0]


def get_dependencies(environment):
    """Return list dependencies for determined environment."""

    DIR_REQUIREMENTS = 'requirements'
    ALLOW_ENV = ['dev', 'test', 'base']

    if environment not in ALLOW_ENV:
        raise ValueError('Unknown environment "{}". Allowed: {}'.format(environment, ', '.join(ALLOW_ENV)))

    dir_requirements = pathlib.Path(DIR_REQUIREMENTS)

    if not dir_requirements.exists():
        raise NotADirectoryError(DIR_REQUIREMENTS)

    filename = '{}.txt'.format(environment)

    file_base_dependencies = dir_requirements.joinpath(filename)

    if not file_base_dependencies.exists():
        raise FileNotFoundError(filename)

    content = file_base_dependencies.read_text()

    return re.findall(r'(\w+\W*==\W*[\.\w]+)\n', content)


setup(
    name='python-utils',
    version=get_version_package(),
    description='Utils for python programming language',
    long_description=get_README(),
    url='https://github.com/setivolkylany/python-utils',
    author='seti volkylany',
    author_email='setivolkylany@gmail.com',
    license='BSD-3-clause',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU GPLv3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    install_requirements=get_dependencies('base'),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    keywords='python utils',
    extras_require={
        'dev': get_dependencies('dev'),
        'test': get_dependencies('test'),
    },
    packages=['utils'],
)
