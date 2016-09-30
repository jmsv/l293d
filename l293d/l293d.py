#!/usr/bin/env python
# -*- coding: utf-8 -*-

import version
print('L293D driver version ' + version.num)

from time import sleep
from threading import Thread

try:
    import config
    verbose = config.verbose
    test_mode = config.test_mode
    use_BCM = config.use_BCM
except:
    print('Error loading config')

try:
    import RPi.GPIO as GPIO
except Exception as e:
    print("Can't import RPi.GPIO. Please (re)install.")
    test_mode = True
    print('Test mode has been enabled. Please view README for more info.')

if not test_mode:
    try:
        if use_BCM:
            GPIO.setmode(GPIO.BCM)
            if verbose: print('GPIO mode set (GPIO.BCM)')
        else:
            GPIO.setmode(GPIO.BOARD)
            if verbose: print('GPIO mode set (GPIO.BOARD)')
        GPIO.setwarnings(False)
    except Exception as e:
        print("Can't set GPIO mode')

class motor(object):
    """
    A motor wired to the L293D chip where
    motor_pins[0] is pinA is L293D pin1 or pin9  : On or off
    motor_pins[1] is pinB is L293D pin2 or pin10 : Anticlockwise positive
    motor_pins[2] is pinC is L293D pin7 or pin15 : Clockwise positive
    """

    motor_pins = [0 for x in range(3)]

    def __init__(self, pinA=0, pinB=0, pinC=0):
        self.motor_pins[0] = pinA
        self.motor_pins[1] = pinB
        self.motor_pins[2] = pinC

        self.pins_are_valid(self.motor_pins)
        pins_in_use.append(self.motor_pins)
        self.gpio_setup(self.motor_pins)


    def pins_are_valid(self, pins, force_selection=False):
        global use_BCM
        if use_BCM:
            valid_pins = [4, 17, 18, 27, 22, 23, 24, 25, 5, 6, 12, 13, 16, 26]
        else: 
            valid_pins = [7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 36, 37]
        for pin in pins:
            pin_int = int(pin)
            if (pin_int not in valid_pins) and (force_selection is not True):
                errStr =  ("GPIO pin number must be from list of valid pins: %s" 
                    "\nTo use selected pins anyway, set force_selection=True "
                    "in function call." % str(valid_pins))
                raise ValueError(errStr)
            for pin_in_use in pins_in_use:
                if pin_int in pin_in_use:
                    raise ValueError('GPIO pin {} already in use.'.format(pin_int))
        self.motor_pins = pins
        return True


    def gpio_setup(self, pins):
        for pin in pins:
            if not test_mode: GPIO.setup(pin, GPIO.OUT)


    def drive_motor(self, direction=1, duration=None, wait=True):
        if not test_mode:
            if (direction == 0):
                GPIO.output(self.motor_pins[0], GPIO.LOW)
            else:
                GPIO.output(self.motor_pins[direction], GPIO.HIGH)
                GPIO.output(self.motor_pins[direction*-1], GPIO.LOW)
                GPIO.output(self.motor_pins[0], GPIO.HIGH)
        if (duration is not None) and (direction != 0):
            stop_thread = Thread(target=self.stop, args = (duration, ))
            stop_thread.start()
            if wait:
                stop_thread.join()


    def pins_string_list(self):
        return '[{}, {} and {}]'.format(*self.motor_pins)


    def spin_clockwise(self, duration=None, wait=True):
        if verbose: print('spinning motor at pins {} clockwise.'.format(self.pins_string_list()))
        self.drive_motor(direction=1, duration=duration, wait=wait)


    def spin_anticlockwise(self, duration=None, wait=True):
        if verbose: print('spinning motor at pins {} anticlockwise.'.format(self.pins_string_list()))
        self.drive_motor(direction=-1, duration=duration, wait=wait)


    def stop(self, after=0):
        if after > 0: sleep(after)
        if verbose: print('stopping motor at pins {}.'.format(self.pins_string_list()))
        if not test_mode: self.drive_motor(direction=0, duration=after, wait=True)


def cleanup():
    if not test_mode:
        try:
            GPIO.cleanup()
            if verbose: print('GPIO cleanup successful.')
        except:
            if verbose: print('GPIO cleanup failed.')

