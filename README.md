# L293D driver
*Python module to drive DC motors from a Raspberry Pi using the L293D chip*

__The master branch is being used for ongoing development. For the lastest stable version, see the [v0.1.7 branch](https://github.com/jamesevickery/l293d/tree/v0.1.7).__

[![Build Status](https://travis-ci.org/jamesevickery/l293d.svg?branch=master)](https://travis-ci.org/jamesevickery/l293d)


## Contents:
1. [Installation](#installation)
2. [Hardware Setup](#hardware-setup)
3. [Python Scripts](#python-scripts)
4. [Test mode](#test-mode)
5. [Verbosity](#verbosity)
6. [Sources](#sources)
7. [License](#license)


## Installation

To install the Python library:

1. ### Clone code from GitHub
        $ git clone https://github.com/jamesevickery/l293d.git

2. ### Navigate to the l293d folder

        $ cd l293d/

3. ### Install the library:

        $ sudo apt-get install python-dev python-pip python-yaml
        $ sudo python setup.py install

4. ### Test

        $ python
        >>> import l293d.driver

   If importing the library forces [test mode](#test-mode), try to install RPi.GPIO:

        $ sudo apt-get install RPi.GPIO

   This should only work on a Raspberry Pi, however other devices may be used to [test the functionality](#test-mode) of this library.


## Hardware Setup

You will need:

- Raspberry Pi
- L293D chip(s)
- DC motor(s)
- Power-pack (4x AA or similar)
- Breadboard and wires

The L293D driver chips are very cheap to buy: I bought a bag of five [from Amazon](http://www.amazon.co.uk/dp/B008KYMVVY). Unless you intend to use more than two motors, only one driver chip is required; each L293D can drive up to two motors.

1. ### Powering the L293D chip

   Power and ground setup - the chip should bridge the middle of the breadboard:
   
   - The Pi's 5V → L293D pin 16 (see below image for numbering format)
   - An empty power rail → L293D pin 8
   - The Pi's ground (GND) → Breadboard ground rail(s)
   - Ground rail(s) → L293D pins 4, 5, 12, and 13 pins (the middle ones)
   
   ![pin numbering image](http://i.imgur.com/RLGyWst.png?2)

   The circuit should look like this:

   ![power pins image](http://i.imgur.com/awtfujg.png?1)
   
2. ### Data wires

   The GPIO pins used in this example can be substitued for other valid pins, as long as continuity is maintained when [setting up a Python script](#python-scripts).
   
   The Pi's GPIO needs to be wired to the L293D's data pins via the breadboard, as follows:
   
   - GPIO 25 (pin 22) → L293D pin 1
   - GPIO 24 (pin 18) → L293D pin 2
   - GPIO 23 (pin 16) → L293D pin 7
   
   Your circuit should now look something like this:

   ![data pins image](http://i.imgur.com/h5OQFZT.png?1)

3. ### Adding a motor

   - Motor wire 1 → L293D pin 3
   - Motor wire 2 → L293D pin 6
   
   ![one motor image](http://i.imgur.com/0PWp7vN.png?1)

   You will also need to connect the battery pack to the power rail and the common ground rail - the one that connects to the L293D's pin 8.
   
   _Note: It doesn't matter which motor wire is connected to 3 or 6, although this will affect the direction. When you've set up a [Python script](#python-scripts), if `clockwise()` makes the motor spin anti-clockwise, the two motor wires should be swapped._

4. ### Adding another motor (optional)

   This is similar to how the first motor was connected, but the other side of the chip is used.
   
   Data wires:
   
   - GPIO 11 (pin 23) → L293D pin 9
   - GPIO 9 (pin 21) → L293D pin 10
   - GPIO 10 (pin 19) → L293D pin 15
   
   Motor wires:
   
   - Motor wire 1 → L293D pin 11
   - Motor wire 2 → L293D pin 14
   
   The circuit should now look something like this:
   
   ![two motors image](http://i.imgur.com/ryYQOr4.png?1)
   
   More motors can be used with additional L293Ds. Just set up another chip as demonstrated above - each chip can drive a maximum of 2 motors.


## Python Scripts

1. ### Import the module
   
   ```import l293d.driver as l293d```

2. ### Define motors
   
   In this example, the GPIO pin numbers will be the same as listed in [Hardware Setup](#hardware-setup).
   
   ```motor1 = l293d.motor(22, 18, 16)```
   
   'motor1' is what we're calling the motor. You can call it whatever you want, for example `wheel_motor`, `london_eye` or `evil_avocado`.
   
   The numbers correspond to which GPIO pins are connected to L293D pins 1, 2 and 7 repectively: the pins we set up in [Hardware Setup](#hardware-setup).

3. ### Control motors
   
   The statements to make the motor(s) spin are as follows:
   
   - `motor1.clockwise()`
   - `motor1.anticlockwise()`
   - `motor1.stop()`
   
   If, `clockwise()` and `anticlockwise()` spin the motor the wrong way, swap the two motor connections to the L293D chip, as explained in [Hardware Setup: Adding a motor](#adding-a-motor).

4. ### Cleanup
   
   I recommend that at the end of your script, you include the line: `l293d.cleanup()`, to cleanup the GPIO pins being used by the l293d library. This avoids damage to the GPIO pins; see [here](http://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi).

   I also recommend that you set up '`try` `catch`' around motor calls to cleanup if any exceptions are encountered during use of this library.

## Test Mode

Test mode (`test_mode`) is a paramter of the l293d config. By default it's off (False) although if there is a problem importing `RPi.GPIO` when `l293d.driver` is imported, test mode is enabled. You'll see something like the image below, if you have [verbosity](#verbosity) enabled.

![l293d-import-test-mode](http://i.imgur.com/6aZnUiv.png?1)


## Verbosity

Verbosity is another True/False config value. l293d only prints textual output when `verbose` is True; which it is, by default.

The only thing that you should see as output from l293d when `verbose` is `False` is when an exception is raised.


## Sources

- The l293d library is based on [this tutorial](https://business.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051) - The circuit diagrams in the README are from here.
- Some helpful information about the driver chip can be found [here](http://www.rakeshmondal.info/L293D-Motor-Driver).
- You can buy L293D driver chips cheaply online - I bought a [pack of 5 on Amazon](https://www.amazon.co.uk/dp/B008KYMVVY)


## Support

If you have any ideas that would make this library even more beautiful, please [submit an issue](https://github.com/jamesevickery/l293d/issues) - or if you're feeling particularly helpful then I would be delighted if you'd fork and submit a pull request! If you want to contribute but don't have an idea, the [issues page](https://github.com/jamesevickery/l293d/issues) is rarely empty and help would be very much appreciated - especially if the issue is tagged as '[help wanted](https://github.com/jamesevickery/l293d/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)'.

Feel free to contact me if you have any questions about use or development of `l293d`. Either [submit an issue](https://github.com/jamesevickery/l293d/issues), email me at jamesevickery.dev@gmail.com or tweet/DM me [on Twitter](https://twitter.com/jamesevickery).

If you'd like to support my open-source development while I'm a poor university student, please click the button below:

[![donate](https://www.paypalobjects.com/en_GB/i/btn/btn_donate_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=US7C2KB9YZUBJ)

(Even if you only give me 75p or something - I can probably find a bag of pasta for that much)


## License

#### The MIT License (MIT)

*Copyright (c) 2016 James Vickery*

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
