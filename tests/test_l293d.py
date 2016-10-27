import unittest


class L293DTestCase(unittest.TestCase):
    def test_import(self):
        """
        Import driver module, then assertTrue.
        If the import fails, an exception is
        raised and the assertion is never reached
        """
        import l293d.driver
        print(str(l293d.driver))
        self.assertTrue(True)
        reload(l293d.driver)  # Revert changes

    def test_pins_string_list(self):
        """
        Test that the list of pins is returned correctly
        """
        import l293d.driver as d
        print(d.pins_in_use)
        motor = d.Motor(29, 7, 13)
        self.assertEqual(motor.pins_string_list(), '[29, 7 and 13]')
        reload(d)

    def test_pins_are_valid_board_1(self):
        """
        Test for valid pins when all others are in use
        """
        import l293d.driver as d
        d.pins_in_use = [7, 11, 12, 13, 15, 29, 31, 32, 33, 36, 37]
        self.assertTrue(d.pins_are_valid([22, 18, 16]))
        reload(d)

    def test_pins_are_valid_board_2(self):
        """
        Test for valid pins when a pin is already in use
        """
        import l293d.driver as d
        d.pins_in_use = [7, 11, 12]
        try:
            valid = d.pins_are_valid([31, 36, 11])
            if valid:
                self.assertFalse(True)
        except:
            self.assertFalse(False)
        reload(d)


if __name__ == '__main__':
    unittest.main()
