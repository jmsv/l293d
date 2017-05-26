#!/usr/bin/env python
from distutils.core import setup

setup(
    name='l293d',
    packages=['l293d'],
    version='0.2.4',
    author='James Vickery',
    author_email='jamesevickery.dev@gmail.com',
    description=('A Python module to drive motors using '
                 'an L293D via Raspberry Pi GPIO'),
    license='MIT',
    keywords=['raspberry', 'pi', 'gpio', 'l293d', 'chip', 'motor', 'driver'],
    url='https://github.com/jamesevickery/l293d',
    download_url='https://github.com/jamesevickery/l293d/archive/v0.2.4.tar.gz'
)
