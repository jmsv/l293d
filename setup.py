#!/usr/bin/env python
import re
from codecs import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(here, 'l293d/__init__.py'), encoding='utf8') as f:
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
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux'
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.2.*, <4',
    keywords=['raspberry', 'pi', 'gpio', 'l293d', 'chip', 'motor', 'driver'],
    url=repo,
    project_urls={
        'Bug Reports': '%s/issues' % repo,
        'Source': repo
    },
    download_url='%s/archive/v%s.tar.gz' % (repo, version),
)
