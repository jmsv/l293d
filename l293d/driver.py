#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from time import sleep
from threading import Thread

__version__ = '0.2.7'


class Config(object):
    __verbose = True
    __test_mode = False
    __pin_numbering = 'BOARD'

    @staticmethod
    def set_verbose(value):
        if type(value) == bool:
            Config.__verbose = value
        else:
            raise TypeError('verbose must be either True or False')

    @staticmethod
    def get_verbose():
        return Config.__verbose

    @staticmethod
    def set_test_mode(value):
        if type(value) == bool:
            Config.__test_mode = value
        else:
            raise TypeError('test_mode must be either True or False')

    @staticmethod
    def get_test_mode():
        return Config.__test_mode

    @staticmethod
    def set_pin_numbering(value):
        if type(value) != str:
            raise TypeError('pin_numbering must be a string:'
                            '\'BOARD\' or \'BCM\'')
        value = str(value).upper()
        if pins_in_use:
            raise ValueError('Pin numbering format cannot be changed '
                             'if motors already exist. Set this at '
                             'the start of your script.')
        if not (value == 'BOARD' or value == 'BCM'):
            raise ValueError(
                'Pin numbering format must be \'BOARD\' or \'BCM\'')
        Config.__pin_numbering = value
        print("Pin numbering format set: " + value)
        return value

    @staticmethod
    def get_pin_numbering():
        return Config.__pin_numbering


# Print version
if Config.get_verbose():
    print('L293D driver version ' + __version__)

# Import GPIO
try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None
    print("Can't import RPi.GPIO. Please (re)install.")
    Config.set_test_mode(True)
    print('Test mode has been enabled. Please view README for more info.')

# Set GPIO warnings based on verbose value
if not Config.get_test_mode():
    if Config.get_verbose():
        GPIO.setwarnings(True)
    else:
        GPIO.setwarnings(False)

# Set GPIO mode
if not Config.get_test_mode():
    if Config.get_pin_numbering() == 'BOARD':
        if Config.get_verbose():
            print('Setting GPIO mode: BOARD')
        GPIO.setmode(GPIO.BOARD)
    elif Config.get_pin_numbering() == 'BCM':
        if Config.get_verbose():
            print('Setting GPIO mode: BCM')
        GPIO.setmode(GPIO.BCM)
    else:
        print("pin_numbering must be either 'BOARD' or 'BCM'.")
        raise ValueError("pin_numbering must be either 'BOARD' or 'BCM'.")

pins_in_use = []  # Lists pins in use (all motors)


class DC(object):
    """
    A class for a motor wired to the L293D chip where
    motor_pins[0] is pinA is L293D pin1 or pin9  : On or off
    motor_pins[1] is pinB is L293D pin2 or pin10 : Anticlockwise positive
    motor_pins[2] is pinC is L293D pin7 or pin15 : Clockwise positive
    """

    def __init__(self, pin_a=0, pin_b=0, pin_c=0):
        # Assign parameters to list
        self.motor_pins = [0 for x in range(3)]
        self.motor_pins[0] = pin_a
        self.motor_pins[1] = pin_b
        self.motor_pins[2] = pin_c

        self.pin_numbering = Config.get_pin_numbering()

        # Check pins are valid
        if pins_are_valid(self.motor_pins):
            self.exists = True
        # Append to global list of pins in use
        for pin in self.motor_pins:
            pins_in_use.append(pin)
        # Set up GPIO mode for pins
        self.gpio_setup()

    def gpio_setup(self):
        """
        Set GPIO.OUT for each pin in use
        """
        for pin in self.motor_pins:
            if not Config.get_test_mode():
                GPIO.setup(pin, GPIO.OUT)

    def drive_motor(self, direction=1, duration=None, wait=True):
        """
        Method called by other functions to drive L293D via GPIO
        """
        self.check()
        if not Config.get_test_mode():
            if direction == 0:  # Then stop motor
                GPIO.output(self.motor_pins[0], GPIO.LOW)
            else:  # Spin motor
                # Set first direction GPIO level
                GPIO.output(self.motor_pins[direction], GPIO.HIGH)
                # Set second direction GPIO level
                GPIO.output(self.motor_pins[direction * -1], GPIO.LOW)
                # Turn the motor on
                GPIO.output(self.motor_pins[0], GPIO.HIGH)
        # If duration has been specified, sleep then stop
        if duration is not None and direction != 0:
            stop_thread = Thread(target=self.stop, args=(duration,))
            # Sleep in thread
            stop_thread.start()
            if wait:
                # If wait is true, the main thread is blocked
                stop_thread.join()

    def pins_string_list(self):
        """
        Return readable list of pins
        """
        return '[{}, {} and {}]'.format(*self.motor_pins)

    def spin_clockwise(self, duration=None, wait=True):
        """
        Uses drive_motor to spin motor clockwise
        """
        self.check()
        if Config.get_verbose():
            print('spinning motor at {0} pins {1} clockwise.'.format(
                self.pin_numbering, self.pins_string_list()))
        self.drive_motor(direction=1, duration=duration, wait=wait)

    def spin_anticlockwise(self, duration=None, wait=True):
        """
        Uses drive_motor to spin motor anticlockwise
        """
        self.check()
        if Config.get_verbose():
            print('spinning motor at {0} pins {1} anticlockwise.'.format(
                self.pin_numbering, self.pins_string_list()))
        self.drive_motor(direction=-1, duration=duration, wait=wait)

    def clockwise(self, duration=None, wait=True):
        """
        Calls spin_clockwise
        """
        self.check()
        self.spin_clockwise(duration, wait)

    def anticlockwise(self, duration=None, wait=True):
        """
        Calls spin_anticlockwise
        """
        self.check()
        self.spin_anticlockwise(duration, wait)

    def stop(self, after=0):
        """
        If 'after' is specified, sleep for amount of time
        """
        self.check()
        if after > 0:
            sleep(after)
        # Verbose output
        if Config.get_verbose():
            print('stopping motor at {0} pins {1}.'.format(
                self.pin_numbering, self.pins_string_list()))
        # Call drive_motor to stop motor after sleep
        if not Config.get_test_mode():
            self.drive_motor(direction=0, duration=after, wait=True)

    def remove(self):
        """
        Remove motor
        """
        if self.exists:
            global pins_in_use
            for m_pin in self.motor_pins:
                if m_pin in pins_in_use:
                    pins_in_use.remove(m_pin)
            self.exists = False
        else:
            if Config.get_verbose():
                print('Motor has already been removed')

    def check(self):
        """
        Check the motor exists. If not, an exception is raised
        """
        if not self.exists:
            raise ValueError('Motor has been removed. '
                             'If you wish to use this motor again, '
                             'you must redefine it.')


class Motor(object):
    def __init__(self, pin_a=0, pin_b=0, pin_c=0):
        raise DeprecationWarning('The Motor class has been deprecated. '
                                 'Please use \'DC\' or \'Stepper\' instead.')


class Stepper(object):
    def __init__(self):
        raise FutureWarning('Stepper motors are not yet supported. Go to '
                            'https://github.com/jamesevickery/l293d/issues/20 '
                            'for more info')


def pins_are_valid(pins, force_selection=False):
    """
    Check the pins specified are valid for pin numbering in use
    """
    # Pin numbering, used below, should be
    # a parameter of this function (future)
    if Config.get_pin_numbering() == 'BOARD':  # Set valid pins for BOARD
        valid_pins = [
            7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 36, 37
        ]
    elif Config.get_pin_numbering() == 'BCM':  # Set valid pins for BCM
        valid_pins = [
            4, 5, 6, 12, 13, 16, 17, 18, 22, 23, 24, 25, 26, 27
        ]
    else:  # pin_numbering value invalid
        raise ValueError("pin_numbering must be either 'BOARD' or 'BCM'.")
    for pin in pins:
        pin_int = int(pin)
        if pin_int not in valid_pins and force_selection is False:
            err_str = (
                "GPIO pin number must be from list of valid pins: %s"
                "\nTo use selected pins anyway, set force_selection=True "
                "in function call." % str(valid_pins))
            raise ValueError(err_str)
        if pin in pins_in_use:
            raise ValueError('GPIO pin {} already in use.'.format(pin))
    return True


def cleanup():
    """
    Call GPIO cleanup method
    """
    if not Config.get_test_mode():
        try:
            GPIO.cleanup()
            if Config.get_verbose():
                print('GPIO cleanup successful.')
        except:
            if Config.get_verbose():
                print('GPIO cleanup failed.')
    else:
        # Skip GPIO cleanup if GPIO calls are not being made (test_mode)
        if Config.get_verbose():
            print('Cleanup not needed when test_mode is enabled.')
