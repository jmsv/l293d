import unittest

class tests(unittest.TestCase):

    def test_import(self):
        import l293d.driver
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
