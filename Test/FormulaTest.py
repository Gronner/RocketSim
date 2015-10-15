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
        self.assertTrue(Formula.thrust(-10.0, 12.0, -15.0, 10.0, 3.0) == -225.0, "[!] Negative test failed")

    def test_ThrustFalseNoneZero(self):
        self.assertFalse(Formula.thrust(10.0, 12.0, 15.0, 10.0, 3.0) == 10.0, "[!] False none-zero test failed")


class DragTest(unittest.TestCase):

    def test_DragZero(self):
        self.assertTrue(Formula.drag(0.0, 0.0, 0.0, 0.0) == 0, "[!] Zero test failed!")

    def test_DragPositive(self):
        self.assertTrue(Formula.drag(10.0, 12.0, 15.0, 10.0) == 108000.0, "[!] Positive test failed!")

    def test_DragNegative(self):
        self.assertTrue(Formula.drag(-10.0, 12.0, 15.0, 10.0) == -108000.0, "[!] Negative test failed!")

    def test_DragNegativeSquare(self):
        self.assertTrue(Formula.drag(10.0, -12.0, 15.0, 10.0) == 108000.0, "[!] Negative square test failed!")

    def test_DragFalseNoneZero(self):
        self.assertFalse(Formula.drag(10.0, 12.0, 15.0, 10.0) == 15, "[!] False none-zero test failed!")

class GravityTest(unittest.TestCase):

    def test_GravityZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.gravity(0.0, 0.0, 0.0)

    def test_GravityPositve(self):
        self.assertTrue(Formula.gravity(10.0, 12.0, 15.0) == 3.559509333333333e-10, "[!] Positive test failed!")

    def test_GravityNegative(self):
        with self.assertRaises(ValueError):
            Formula.gravity(-10.0, 12.0, 15.0)

    def test_GravityFalseNoneZero(self):
        self.assertFalse(Formula.gravity(10.0, 12.0, 15.0) == 10, "[!] False none-zero test failed!")

def main():
    unittest.main()

if __name__ == "__main__":
    main()