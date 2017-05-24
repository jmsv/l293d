# Installation

To install the Python library:

1. ### Clone code from GitHub

        $ git clone https://github.com/jamesevickery/l293d.git

2. ### Navigate to the l293d folder

        $ cd l293d/

3. ### Install dependencies

    Python 2:

        $ sudo apt-get install python-dev python-pip
   
    Python 3:

        $ sudo apt-get install python3-pip
    
    Install RPi.GPIO (Pi only):

        $ sudo apt-get install RPi.GPIO

    Installing `RPi.GPIO` is required to drive motors on the Raspberry Pi, although in other environments, [test mode](#test-mode) is automatically enabled if `RPi.GPIO` isn't found.

4. ### Install the library

        $ sudo python setup.py install
        
    Or for use with Python 3, swap `python` for `python3` in the command above.

5. ### Test

        $ python
        >>> import l293d
    
    Again, `python3` may be used instead of `python`, although remember that installations for different Python versions are independent.
