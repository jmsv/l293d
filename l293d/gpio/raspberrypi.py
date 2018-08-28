from RPi.GPIO import GPIO


def pins_are_valid(pins, pin_numbering, force_selection=False):
    """
    Check the pins specified are valid for pin numbering in use
    """
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
        if pin_int not in valid_pins and force_selection is False:
            err_str = (
                    "GPIO pin number must be from list of valid pins: %s"
                    "\nTo use selected pins anyway, set force_selection=True "
                    "in function call." % str(valid_pins))
            raise ValueError(err_str)
        if pin in pins_in_use:
            raise ValueError('GPIO pin {} already in use.'.format(pin))
    return True


