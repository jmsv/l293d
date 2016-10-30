#!/usr/bin/env python
from l293d import version

from distutils.core import setup

setup(
    name='l293d',
    version=version.num,
    author='James Vickery',
    author_email='jamesevickery.dev@gmail.com',
    description=('A Python module to drive motors using '
                 'an L293D via Raspberry Pi GPIO'),
    license='MIT',
    keywords='raspberry pi gpio l293d chip motor driver',
    url='https://github.com/jamesevickery/l293d',
    download_url='https://github.com/jamesevickery/l293d/tarball/master',
    packages=['l293d'],
    package_data={'l293d': ['default_l293d_config.ini']}
)
