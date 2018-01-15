#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ConfigMeta(type):

    def __getattr__(cls, attr):
        """
        Try and call get_`attr` on the cls.
        """
        try:
            return cls.__dict__["get_" + attr].__func__(cls)
        except KeyError:
            raise AttributeError(
                "object '{}' has no attribute '{}'".format(
                    cls.__name__, attr))

    def __setattr__(cls, attr, value):
        """
        Try and call set_`attr` on the cls.
        """
        if cls.__name__ not in attr:
            # First try calling the set_ method. This will allow the set_
            # method to perform it's checks, then recursively call this method.
            try:
                cls.__dict__["set_" + attr].__func__(cls, value)
            except KeyError:
                raise AttributeError(
                    "object '{}' has no attribute '{}'".format(
                        cls.__name__, attr))
        else:
            # Now that the set_ method has done it's checks, we can use super()
            # to actually set the value.
            super(ConfigMeta, cls).__setattr__(attr, value)


def with_metaclass(mcls):
    """
    Allows compatibility for metaclass in python2 and python3
    """
    def decorator(cls):
        body = vars(cls).copy()
        body.pop("__dict__", None)
        body.pop("__weakref__", None)
        return mcls(cls.__name__, cls.__bases__, body)
    return decorator


@with_metaclass(ConfigMeta)
class Config(object):
    __verbose = True
    __test_mode = False
    __pin_numbering = 'BOARD'
    pins_in_use = []

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
