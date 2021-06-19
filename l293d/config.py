#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Config(object):
    __verbose = True
    __test_mode = False
    __pin_numbering = 'BOARD'
    pins_in_use = []

    @classmethod
    def __getattr__(cls, attr):
        """
        Try and call get_`attr` on the cls.
        """
        try:
            return getattr(cls, "get_" + attr)()
        except KeyError:
            raise AttributeError(
                "object '{}' has no attribute '{}'".format(
                    cls.__name__, attr))

    @classmethod
    def __setattr__(cls, attr, value):
        """
        Try and call set_`attr` on the cls.
        """
        if cls.__name__ not in attr:
            # First try calling the set_ method. This will allow the set_
            # method to perform it's checks, then recursively call this method.
            try:
                getattr(cls, "set_" + attr)(value)
            except KeyError:
                raise AttributeError(
                    "object '{}' has no attribute '{}'".format(
                        cls.__name__, attr))

    @classmethod
    def set_verbose(cls, value):
        if type(value) == bool:
            cls.__verbose = value
        else:
            raise TypeError('verbose must be either True or False')

    @classmethod
    def get_verbose(cls):
        return cls.__verbose

    @classmethod
    def set_test_mode(cls, value):
        if type(value) == bool:
            cls.__test_mode = value
        else:
            raise TypeError('test_mode must be either True or False')

    @classmethod
    def get_test_mode(cls):
        return cls.__test_mode

    @classmethod
    def set_pin_numbering(cls, value):
        if type(value) != str:
            raise TypeError('pin_numbering must be a string:'
                            '\'BOARD\' or \'BCM\'')
        value = str(value).upper()
        if cls.pins_in_use:
            raise ValueError('Pin numbering format cannot be changed '
                             'if motors already exist. Set this at '
                             'the start of your script.')
        if not (value == 'BOARD' or value == 'BCM'):
            raise ValueError(
                'Pin numbering format must be \'BOARD\' or \'BCM\'')
        cls.__pin_numbering = value
        print("Pin numbering format set: " + value)
        return value

    @classmethod
    def get_pin_numbering(cls):
        return cls.__pin_numbering
