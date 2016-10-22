#!/usr/bin/env python
from l293d import version

try:
    import yaml
except:
    raise ImportError('Please install python-yaml (sudo apt-get install python-yaml)')

from distutils.core import setup,Extension

setup(
    name = 'l293d',
    version = version.num,
    author = 'James Vickery',
    author_email = 'jamesevickery.dev@gmail.com',
    description = ('A Python module to drive motors using an L293D via Raspberry Pi GPIO'),
    license = 'MIT',
    keywords = 'raspberry pi gpio l293d chip motor driver',
    url = 'https://github.com/jamesevickery/l293d',
    download_url = 'https://github.com/jamesevickery/l293d/tarball/master',
    packages = ['l293d'],
    install_requires = ['python-dev', 'python-pip', 'python-yaml']
)