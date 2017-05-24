import unittest
from sys import version_info

# Python 2: reload is built-in
if version_info.major == 3:
    if version_info.minor < 4:
        # Python 3.0 - 3.3: deprecated since Python 3.4 in favour of importlib
        from imp import reload
    else:
        # Python 3.4+
        from importlib import reload


class L293DTestCase(unittest.TestCase):
    def test_import(self):
        """
        Import driver module, then assertTrue.
        If the import fails, an exception is
        raised and the assertion is never reached
        """
        import l293d as d
        print(str(d))
        self.assertTrue(True)
        reload(d.driver)  # Revert changes

    def test_pins_string_list(self):
        """
        Test that the list of pins is returned correctly
        """
        import l293d as d
        print(d.pins_in_use)
        motor = d.DC(29, 7, 13)
        self.assertEqual(motor.pins_string_list(), '[29, 7 and 13]')
        reload(d.driver)

    def test_pins_are_valid_board_1(self):
        """
        Test for valid pins when all others are in use
        """
        import l293d as d
        d.pins_in_use = [7, 11, 12, 13, 15, 29, 31, 32, 33, 36, 37]
        self.assertTrue(d.pins_are_valid([22, 18, 16]))
        reload(d.driver)

    def test_pins_are_valid_board_2(self):
        """
        Test for valid pins when a pin is already in use
        """
        import l293d as d
        d.pins_in_use = [7, 11, 12]
        try:
            valid = d.pins_are_valid([31, 36, 11])
            if valid:
                self.assertFalse(True)
        except:
            self.assertFalse(False)
        reload(d.driver)

    def test_motor_can_be_removed(self):
        """
        Test that a motor can be created and removed
        """
        import l293d as d
        original_pins = d.pins_in_use
        motor = d.DC(29, 7, 13)
        motor.remove()
        self.assertEqual(d.pins_in_use, original_pins)
        reload(d.driver)

    def test_pin_numbering_lock(self):
        """"
        Test that pin_numbering can't be changed after a motor's definition
        """
        import l293d as d
        d.Config.set_pin_numbering('BcM')
        m1 = d.DC(4, 5, 6)
        error = 'No error'
        try:
            d.Config.set_pin_numbering('BoaRD')
        except ValueError as e:
            error = str(e)
        self.assertEquals(
            error, 'Pin numbering format cannot be changed '
                   'if motors already exist. Set this at '
                   'the start of your script.')
        m1.remove()
        reload(d.driver)


if __name__ == '__main__':
    unittest.main()
