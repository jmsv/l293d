raspberry_pi, micropython = True, True

try:
    from RPi.GPIO import GPIO
except ImportError:
    raspberry_pi = False

try:
    from machine import Pin
    from l293d.gpio.micropython import GPIO
except ImportError:
    micropython = False

if not raspberry_pi and not micropython:
    print(
        "Can't import a GPIO controller; test mode has been enabled:\n"
        "http://l293d.rtfd.io/en/latest/user-guide/configuration/#test-mode")
    from l293d.gpio.testgpio import GPIO
