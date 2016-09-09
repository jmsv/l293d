
# L293D driver
*Python module to drive motors from a Raspberry Pi using the L293D chip*


## Contents:
1. [Installation](#installation)
2. [Hardware Setup](#hardware-setup)
3. [Python Scripts](#python-scripts)
4. [Test mode](#test-mode)
5. [Verbosity](#verbosity)
6. [License](#license)


## Installation

To install the Python library:

1. #### Clone code from GitHub
        $ git clone https://github.com/jamesevickery/l293d.git

2. #### Navigate to the l293d folder

        $ cd l293d/

3. #### Install the library:

        $ sudo apt-get install python-dev python-pip
        $ sudo python setup.py install

4. #### Test

        $ python
        >>> import l293d.l293d as l293d

   If importing the library forces [test mode](#test-mode), try to install RPi.GPIO:

        $ sudo apt-get install RPi.GPIO

   This should only work on a Raspberry Pi, however other devices may be used to [test the functionality](#test-mode) of this library.


## Hardware Setup

*to be added: information on how to physically set up motors for use with this library*


## Python Scripts

*to be added: how to create scripts with this library to set up and control motors*


## Test Mode

*to be added: what is test mode? what's it for? what is the meaning of life? etc.*


## Verbosity

*to be added: how to enable/disable verbosity, what it does and whatever*


## License

#### The MIT License (MIT)

*Copyright (c) 2016 James Vickery*

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
