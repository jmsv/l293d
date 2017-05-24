#!/bin/bash

# to be run as ./tests/local-tests.sh

set -e

# install
echo "   ------------   Installing l293d for Python 2.    ------------"
sudo python2 setup.py install
echo "   ------------   Installing l293d for Python 3.    ------------"
sudo python3 setup.py install

# linting check
flake8 . --exclude __init__.py
echo "   ------------ flake 8 checks passed - returned 0. ------------"

# run tests
py.test tests/
python3 -m pytest tests/

echo "   ------------         All checks passed.          ------------"
