
def pins_are_valid(pins, pin_numbering, force_selection=False):
    """
    Check the pins specified are valid for pin numbering in use
    """
    # Test mode shouldn't validate pins
    return True


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
            pass

        def start(self, duty):
            pass

        def stop(self):
            pass

    @classmethod
    def setwarnings(cls, warn):
        pass

    @classmethod
    def setmode(cls, mode):
        pass

    @classmethod
    def setup(cls, pin_num, mode):
        pass

    @classmethod
    def output(cls, pin_num, mode):
        pass
