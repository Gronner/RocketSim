import unittest
import Formula


class ThrustTest(unittest.TestCase):

    def test_ThrustZero(self):
        self.assertTrue(Formula.Thrust(0.0, 0.0, 0.0, 0.0, 0.0) == 0, "[!] Zero test failed!")

    def test_ThrustNoneZero(self):
        self.assertTrue(Formula.Thrust(10.0, 12.0, 15.0, 10.0, 3.0) == 15, "[!] None-zero test failed")

    def test_ThrustFalseNoneZero(self):
        self.assertFalse(Formula.Thrust(10.0, 12.0, 15.0, 10.0, 3.0) == 10, "[!] False None-zero test failed")


def main():
    unittest.main()

if __name__ == "__main__":
    main()