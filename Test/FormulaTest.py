import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

import Formula


class ThrustTest(unittest.TestCase):

    def test_ThrustZero(self):
        self.assertTrue(Formula.thrust(0.0, 0.0, 0.0, 0.0, 0.0) == 0.0, "[!] Zero test failed!")

    def test_ThrustPositive(self):
        self.assertTrue(Formula.thrust(10.0, 12.0, 15.0, 10.0, 3.0) == 225.0, "[!] Positive test failed")

    def test_ThrustNegative(self):
        self.assertTrue(Formula.thrust(-10.0, 12.0, -15.0, 10.0, 3.0) == -225.0, "[!] Positive test failed")

    def test_ThrustFalseNoneZero(self):
        self.assertFalse(Formula.thrust(10.0, 12.0, 15.0, 10.0, 3.0) == 10.0, "[!] False None-zero test failed")


def main():
    unittest.main()

if __name__ == "__main__":
    main()