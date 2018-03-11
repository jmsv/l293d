#!/usr/bin/env python
import io
import re
from setuptools import setup

with io.open('l293d/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

repo = 'https://github.com/jamesevickery/l293d'

setup(
    name='l293d',
    packages=['l293d'],
    version=version,
    author='James Vickery',
    author_email='dev@jamesvickery.net',
    description=('A Python module to drive motors using '
                 'an L293D via Raspberry Pi GPIO'),
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux'
    ],
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    keywords=['raspberry', 'pi', 'gpio', 'l293d', 'chip', 'motor', 'driver'],
    url=repo,
    download_url='%s/archive/v%s.tar.gz' % (repo, version),
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    }
)
