#!/bin/bash

# To be run as ./tests/local-tests.sh

# Abort on errors
set -e

# Flake8 code linting (config in setup.cfg)
flake8

# Run tests in Python 2
py.test tests/

