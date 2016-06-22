#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep

#GPIO.setmode(GPIO.BOARD)

class motor(object):
    """
    A motor wired to the L293D chip where
    pin1 or pin9   : On or off
    pin2 or pin10  : Anticlockwise positive
    pin7 or pin15  : Clockwise positive
    """
    
    def spin_clockwise(self, time=None):
        print('spinning {} clockwise'.format(str(self)))
        if time is not None:
            sleep(time)
            self.stop()
    
    
    def stop(self):
        print('stopping {}'.format(str(self)))

