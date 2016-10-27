import unittest


class L293DTestCase(unittest.TestCase):
    def test_import(self):
        import l293d.driver
        print(str(l293d.driver))
        self.assertTrue(True)

    def test_pins_string_list(self):
        import l293d.driver as d
        motor = d.Motor(29, 7, 13)
        self.assertEqual(motor.pins_string_list(), '[29, 7 and 13]')

if __name__ == '__main__':
    unittest.main()
