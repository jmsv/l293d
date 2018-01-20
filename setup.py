#!/usr/bin/env python
from distutils.core import setup

l293d_version = '0.3.0'
repo = 'https://github.com/jamesevickery/l293d'

setup(
    name='l293d',
    packages=['l293d'],
    version=l293d_version,
    author='James Vickery',
    author_email='jamesevickery.dev@gmail.com',
    description=('A Python module to drive motors using '
                 'an L293D via Raspberry Pi GPIO'),
    license='MIT',
    keywords=['raspberry', 'pi', 'gpio', 'l293d', 'chip', 'motor', 'driver'],
    url=repo,
    download_url='%s/archive/v%s.tar.gz' % (repo, l293d_version)
)
