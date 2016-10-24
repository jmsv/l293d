#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from threading import Thread

# Load config
import config

verbose = config.verbose
test_mode = config.test_mode
pin_numbering = config.pin_numbering

# Print version
if verbose:
    import version

    print('L293D driver version ' + version.num)

# Import GPIO
try:
    import RPi.GPIO as GPIO
except Exception as e:
    print("Can't import RPi.GPIO. Please (re)install.")
    test_mode = True
    print('Test mode has been enabled. Please view README for more info.')
# Set GPIO warnings based on verbose value
if not test_mode:
    if verbose:
        GPIO.setwarnings(True)
    else:
        GPIO.setwarnings(False)

# Set GPIO mode
if not test_mode:
    if pin_numbering == 'BOARD':
        if verbose:
            print('Setting GPIO mode: BOARD')
        GPIO.setmode(GPIO.BOARD)
    elif pin_numbering == 'BCM':
        if verbose:
            print('Setting GPIO mode: BCM')
        GPIO.setmode(GPIO.BCM)
    else:
        print("pin_numbering must be either 'BOARD' or 'BCM'.")
        raise ValueError("pin_numbering must be either 'BOARD' or 'BCM'.")

pins_in_use = []  # Lists pins in use (all motors)


class motor(object):
    """
    A class for a motor wired to the L293D chip where
    motor_pins[0] is pinA is L293D pin1 or pin9  : On or off
    motor_pins[1] is pinB is L293D pin2 or pin10 : Anticlockwise positive
    motor_pins[2] is pinC is L293D pin7 or pin15 : Clockwise positive
    """

    # List of pins in use by motor object
    motor_pins = [0 for x in range(3)]

    def __init__(self, pinA=0, pinB=0, pinC=0):
        # Assign parameters to list
        self.motor_pins[0] = pinA
        self.motor_pins[1] = pinB
        self.motor_pins[2] = pinC

        # Check pins are valid
        self.pins_are_valid(self.motor_pins)
        # Append to global list of pins in use
        for pin in self.motor_pins:
            pins_in_use.append(pin)
        # Set up GPIO mode for pins
        self.gpio_setup(self.motor_pins)

    def pins_are_valid(self, pins, force_selection=False):
        '''
        Check the pins specified are valid for pin numbering in use
        '''
        global pin_numbering
        if pin_numbering == 'BOARD':  # Set valid pins for BOARD
            valid_pins = [
                7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 36, 37
            ]
        elif pin_numbering == 'BCM':  # Set valid pins for BCM
            valid_pins = [
              4, 5, 6, 12, 13, 16, 17, 18, 22, 23, 24, 25, 26, 27
            ]
        else:  # pin_numbering value invalid
            raise ValueError("pin_numbering must be either 'BOARD' or 'BCM'.")
        for pin in pins:
            pin_int = int(pin)
            if (pin_int not in valid_pins) and (force_selection is not True):
                errStr = (
                    "GPIO pin number must be from list of valid pins: %s"
                    "\nTo use selected pins anyway, set force_selection=True "
                    "in function call." % str(valid_pins))
                raise ValueError(errStr)
            for pin in pins_in_use:
                if (pin in pins):
                    raise ValueError('GPIO pin {} already in use.'.format(
                        str(pin)))
        self.motor_pins = pins
        return True

    def gpio_setup(self, pins):
        '''
        Set GPIO.OUT for each pin in use
        '''
        for pin in pins:
            if not test_mode:
                GPIO.setup(pin, GPIO.OUT)

    def drive_motor(self, direction=1, duration=None, wait=True):
        '''
        Method called by other functions to drive L293D via GPIO
        '''
        if not test_mode:
            if (direction == 0):  # Then stop motor
                GPIO.output(self.motor_pins[0], GPIO.LOW)
            else:  # Spin motor
                # Set first direction GPIO level
                GPIO.output(self.motor_pins[direction], GPIO.HIGH)
                # Set second direction GPIO level
                GPIO.output(self.motor_pins[direction * -1], GPIO.LOW)
                # Turn the motor on
                GPIO.output(self.motor_pins[0], GPIO.HIGH)
        # If duration has been specified, sleep then stop
        if (duration is not None) and (direction != 0):
            stop_thread = Thread(target=self.stop, args=(duration, ))
            # Sleep in thread
            stop_thread.start()
            if wait:
                # If wait is true, the main thread is blocked
                stop_thread.join()

    def pins_string_list(self):
        '''
        Return readable list of pins
        '''
        return '[{}, {} and {}]'.format(*self.motor_pins)

    def spin_clockwise(self, duration=None, wait=True):
        '''
        Uses drive_motor to spin motor clockwise
        '''
        if verbose:
            print('spinning motor at {0} pins {1} clockwise.'.format(
                pin_numbering, self.pins_string_list()))
        self.drive_motor(direction=1, duration=duration, wait=wait)

    def spin_anticlockwise(self, duration=None, wait=True):
        '''
        Uses drive_motor to spin motor anticlockwise
        '''
        if verbose:
            print('spinning motor at {0} pins {1} anticlockwise.'.format(
                pin_numbering, self.pins_string_list()))
        self.drive_motor(direction=-1, duration=duration, wait=wait)

    def clockwise(self, duration=None, wait=True):
        '''
        Calls spin_clockwise
        '''
        self.spin_clockwise(duration, wait)

    def anticlockwise(self, duration=None, wait=True):
        '''
        Calls spin_anticlockwise
        '''
        self.spin_anticlockwise(duration, wait)

    def stop(self, after=0):
        '''
        If 'after' is specified, sleep for amount of time
        '''
        if after > 0:
            sleep(after)
        # Verbose output
        if verbose:
            print('stopping motor at {0} pins {1}.'.format(
                pin_numbering, self.pins_string_list()))
        # Call drive_motor to stop motor after sleep
        if not test_mode:
            self.drive_motor(direction=0, duration=after, wait=True)


def cleanup():
    '''
    Call GPIO cleanup method
    '''
    if not test_mode:
        try:
            GPIO.cleanup()
            if verbose:
                print('GPIO cleanup successful.')
        except:
            if verbose:
                print('GPIO cleanup failed.')
    else:
        # Skip GPIO cleanup if GPIO calls are not being made (test_mode)
        if verbose:
            print('Cleanup not needed when test_mode is enabled.')
