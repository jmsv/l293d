# Configuration

## Test Mode:

Test mode (`test_mode`) is a paramter of the l293d config. By default it's off (False) although if there is a problem importing `RPi.GPIO` when `l293d.driver` is imported, test mode is enabled. You'll see something like the image below, if you have [verbosity](#verbosity) enabled.

![l293d-import-test-mode](http://i.imgur.com/6aZnUiv.png?1)

## Verbosity

Verbosity is another True/False config value. l293d only prints textual output when `verbose` is True; which it is, by default.

The only thing that you should see as output from l293d when `verbose` is `False` is when an exception is raised.

## Pin Numbering

Pin numbering (`pin_numbering`) is either BOARD or BCM. These are different ways of numbering the Raspberry Pi's pins. BOARD numbering refers to the physical location of the pins, whereas BCM refers to the Broadcom pin number. A good pinout diagram labelling the pin & BCM numbers can be found at [pinout.xyz](https://pinout.xyz/).
