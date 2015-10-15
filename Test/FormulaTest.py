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

    def test_ThrustFalseNonZero(self):
        self.assertFalse(Formula.thrust(10.0, 12.0, 15.0, 10.0, 3.0) == 10.0, "[!] False non-zero test failed")


class DragTest(unittest.TestCase):

    def test_DragZero(self):
        self.assertTrue(Formula.drag(0.0, 0.0, 0.0, 0.0) == 0, "[!] Zero test failed!")

    def test_DragPositive(self):
        self.assertTrue(Formula.drag(10.0, 12.0, 15.0, 10.0) == 108000.0, "[!] Positive test failed!")

    def test_DragNegative(self):
        self.assertTrue(Formula.drag(-10.0, 12.0, 15.0, 10.0) == -108000.0, "[!] Negative test failed!")

    def test_DragNegativeSquare(self):
        self.assertTrue(Formula.drag(10.0, -12.0, 15.0, 10.0) == 108000.0, "[!] Negative square test failed!")

    def test_DragFalseNonZero(self):
        self.assertFalse(Formula.drag(10.0, 12.0, 15.0, 10.0) == 15, "[!] False non-zero test failed!")

class GravityTest(unittest.TestCase):

    def test_GravityZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.gravity(0.0, 0.0, 0.0)

    def test_GravityPositve(self):
        self.assertTrue(Formula.gravity(10.0, 12.0, 15.0) == 3.559509333333333e-10, "[!] Positive test failed!")

    def test_GravityNegative(self):
        with self.assertRaises(ValueError):
            Formula.gravity(-10.0, 12.0, 15.0)

    def test_GravityFalseNonZero(self):
        self.assertFalse(Formula.gravity(10.0, 12.0, 15.0) == 10, "[!] False non-zero test failed!")

class PressureTest(unittest.TestCase):

    def test_PressureZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.pressure(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def testPressurePositive(self):
        self.assertTrue(Formula.pressure(1013.25, 0.0065, 100.0, 0.0, 24.0) == 877.098852, "[!] Positive test failed!")

    def testPressureNegative(self):
        self.assertTrue(Formula.pressure(-1013.25, 0.0065, 100.0, 0.0, 24.0) == -877.098852, "\
        [!] Negative test failed!")

    def testPressureFalseNonZero(self):
        self.assertFalse(Formula.pressure(-1013.25, 0.0065, 100.0, 0.0, 24.0) == -87.098852, "\
        [!] False non-zero test failed!")

def main():
    unittest.main()

if __name__ == "__main__":
    main()