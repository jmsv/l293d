To install the Python library:

These instructions assume you're using Linux bash, although the library can also be installed in other environments for testing.

## [PyPI](https://pypi.python.org/pypi/l293d/)

    pip install l293d

l293d is installable via PyPI, using the above command.
However, this might not be always the very latest (development) version.
If you're happy using the version on the Python Package Index,
run the `pip install l293d` command and skip to instruction [5](#5-test).
To install the latest version, follow the below instructions.

Remember to prefix the pip install command with `sudo` if you wish to install this package globally.


## From GitHub


#### 1. Clone code from GitHub

    $ git clone https://github.com/jamesevickery/l293d.git

#### 2. Navigate to the l293d folder

    $ cd l293d/

#### 3. Install dependencies

Python 2:

    $ sudo apt-get install python-dev python-pip

Python 3:

    $ sudo apt-get install python3-pip

Install RPi.GPIO (Pi only):

    $ sudo pip install RPi.GPIO

Also installable via `apt-get`, although `pip` (as above) is recommended:

    $ sudo apt-get install RPi.GPIO

Installing `RPi.GPIO` is required to drive motors on the Raspberry Pi, although in other environments, [test mode](#test-mode) is automatically enabled if `RPi.GPIO` isn't found.

#### 4. Install the library

    $ sudo python setup.py install
    
Or for use with Python 3, swap `python` for `python3` in the command above.

#### 5. Test

    $ python
    >>> import l293d

Again, `python3` may be used instead of `python`, although remember that installations for different Python versions are independent.

Once l293d has been successfully installed, it can be used to drive motors. See [Python Scripts](python-scripts.md) for more info.


## Virtualenv

l293d can be installed in a virtualenv, like you can with other packages:

#### 1. Install

    pip install virtualenv
   
#### 2. Create virtualenv

    virtualenv venv_name

#### 3. Activate virtualenv

    source venv_name/bin/activate

#### 4. Install l293d

Install using one of the methods above: from [PyPI](#pypi) or from [GitHub](#from-github).
You don't need to use `sudo`, as l293d should install within the virtualenv.

#### 5. Deactivate

Once you've finished using the virtualenv:

    deactivate

To learn more about virtualenv, I found [this site](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) useful.
