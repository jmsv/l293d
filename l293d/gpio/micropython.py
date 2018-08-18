
from l293d.driver import v_print


class GPIO(object):
    __pins = {}

    IN = 0
    OUT = 1
    LOW = 0
    HIGH = 1

    BOARD = "BOARD"
    BCM = "BCM"

    class PWM(object):
        def __init__(self, pin_num, freq):
            self.pin = GPIO._GPIO__pins[pin_num]
            self.pwm = machine.PWM(self.pin)
            self.pwm.freq(freq)

        def start(self, duty):
            self.pwm.duty(duty)

        def stop(self):
            self.pwn.deinit()
    
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

