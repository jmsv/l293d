import machine


def pins_are_valid(pins, force_selection=False):
    """
    Check the pins specified are valid for pin numbering in use
    """
    # Micropython can be run on any number of boards, so don't do any
    #  validation against pin numbers.
    return True


class GPIO(object):
    __pins = {}

    IN = 0
    OUT = 1
    LOW = 0
    HIGH = 1

    BOARD = "BOARD"
    BCM = "BCM"

    class PwmObject(object):
        def __init__(self, pin, freq):
            self.pin = pin
            self.pwm = machine.PWM(self.pin)
            self.pwm.freq(freq)

        def start(self, duty):
            self.pwm.duty(duty)

        def stop(self):
            self.pwm.deinit()

    @classmethod
    def PWM(cls, pin, freq):
        return cls.PwmObject(cls.__pins[pin], freq)

    @classmethod
    def setwarnings(cls, warn):
        pass

    @classmethod
    def setmode(cls, mode):
        pass

    @classmethod
    def setup(cls, pin_num, mode):
        cls.__pins[pin_num] = machine.Pin(pin_num, mode)

    @classmethod
    def output(cls, pin_num, mode):
        cls.__pins[pin_num].value(mode)
