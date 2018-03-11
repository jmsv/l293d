#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from collections import namedtuple
from threading import Thread
from time import sleep

from l293d.config import Config


def v_print(string):
    """
    Print if verbose
    :param string: Text to print if verbose
    :return: True if printed, otherwise False
    """
    if Config.get_verbose():
        print("[l293d]: %s" % str(string))
        return True
    return False


# Import GPIO
try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None
    Config.test_mode = True
    v_print(
        "Can't import RPi.GPIO; test mode has been enabled:\n"
        "http://l293d.rtfd.io/en/latest/user-guide/configuration/#test-mode")

if not Config.test_mode:
    GPIO.setwarnings(False)

# Set GPIO mode
if not Config.test_mode:
    pin_num = Config.pin_numbering
    v_print('Setting GPIO mode: {}'.format(pin_num))
    GPIO.setmode(getattr(GPIO, pin_num))

pins_in_use = Config.pins_in_use  # Lists pins in use (all motors)


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

        self.pwm = None

        self.pin_numbering = Config.pin_numbering

        self.reversed = False

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
            if not Config.test_mode:
                GPIO.setup(pin, GPIO.OUT)

    def drive_motor(self, direction=1, duration=None, wait=True, speed=100):
        """
        Method called by other functions to drive L293D via GPIO
        """
        self.check()

        if isinstance(speed, int):
            # If speed is an integer, change it to a tuple
            speed = (speed, speed)
        # Unpack speed into PWM, this works even if a PWM tuple was passed in
        speed = PWM(*speed)

        if self.reversed:
            direction *= -1
        if not Config.test_mode:
            if direction == 0:  # Then stop motor
                self.pwm.stop()
            else:  # Spin motor
                # Create a PWM object to control the 'enable pin' for the chip
                self.pwm = GPIO.PWM(self.motor_pins[0], speed.freq)
                # Set first direction GPIO level
                GPIO.output(self.motor_pins[direction], GPIO.HIGH)
                # Set second direction GPIO level
                GPIO.output(self.motor_pins[direction * -1], GPIO.LOW)
                # Start PWM on the 'enable pin'
                self.pwm.start(speed.cycle)
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

    def __move_motor(self, direction, duration, wait, action, speed):
        """
        Uses drive_motor to spin the motor in `direction`
        """
        self.check()
        if Config.verbose:
            v_print('{action} {reversed}motor at '
                    '{pin_nums} pins {pin_str}'.format(
                action=action,
                reversed='reversed' if self.reversed else '',
                pin_nums=self.pin_numbering,
                pin_str=self.pins_string_list()))

        self.drive_motor(direction=direction, duration=duration,
                         wait=wait, speed=speed)

    def clockwise(self, duration=None, wait=True, speed=100):
        """
        Spin the motor clockwise
        """
        self.__move_motor(1, duration, wait, 'spinning clockwise', speed)

    def anticlockwise(self, duration=None, wait=True, speed=100):
        """
        Spin the motor anticlockwise
        """
        self.__move_motor(-1, duration, wait, 'spinning anticlockwise', speed)

    def stop(self, after=0):
        """
        Stop the motor. If 'after' is specified, sleep for amount of time
        """
        if after > 0:
            sleep(after)
        self.__move_motor(0, after, True, 'stopping', None)

    def remove(self):
        """
        Remove motor
        """
        if self.exists:
            for m_pin in self.motor_pins:
                if m_pin in pins_in_use:
                    pins_in_use.remove(m_pin)
            self.exists = False
        else:
            v_print('Motor has already been removed')

    def check(self):
        """
        Check the motor exists. If not, an exception is raised
        """
        if not self.exists:
            raise ValueError('Motor has been removed. '
                             'If you wish to use this motor again, '
                             'you must redefine it.')


PWM = namedtuple("PWM", ["freq", "cycle"])


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
    if Config.pin_numbering == 'BOARD':  # Set valid pins for BOARD
        valid_pins = [
            7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 36, 37
        ]
    elif Config.pin_numbering == 'BCM':  # Set valid pins for BCM
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
    if not Config.test_mode:
        try:
            GPIO.cleanup()
            v_print('GPIO cleanup successful.')
        except Exception:
            v_print('GPIO cleanup failed.')
    else:
        # Skip GPIO cleanup if GPIO calls are not being made (test_mode)
        v_print('Cleanup not needed when test_mode is enabled.')
