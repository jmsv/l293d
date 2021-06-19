raspberry_pi, micropython = True, True

try:
    from l293d.gpio.raspberrypi import GPIO, pins_are_valid
except ImportError:
    raspberry_pi = False

try:
    from l293d.gpio.micropython import GPIO, pins_are_valid
except ImportError:
    micropython = False

if not raspberry_pi and not micropython:
    print(
        "Can't import a GPIO controller; test mode has been enabled:\n"
        "http://l293d.rtfd.io/en/latest/user-guide/configuration/#test-mode")
    from l293d.gpio.testgpio import GPIO, pins_are_valid
