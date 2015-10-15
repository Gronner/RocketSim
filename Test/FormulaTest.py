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
            Formula.pressure(0.0, 0.0, 0.0, 0.0, 0.0)

    def testPressurePositive(self):
        self.assertTrue(Formula.pressure(1013.25, 0.0065, 100.0, 0.0, 24.0) == 877.0988519626972, "[!] Positive test failed!")

    def testPressureNegative(self):
        self.assertTrue(Formula.pressure(-1013.25, 0.0065, 100.0, 0.0, 24.0) == -877.0988519626972, "\
        [!] Negative test failed!")

    def testPressureFalseNonZero(self):
        self.assertFalse(Formula.pressure(-1013.25, 0.0065, 100.0, 0.0, 24.0) == -87.098852, "\
        [!] False non-zero test failed!")


class TemperatureTest(unittest.TestCase):

    def test_TemperatureZero(self):
        self.assertTrue(Formula.temperature(0.0, 0.0, 0.0, 0.0) == 0.0, "[!] Zero test failed!")

    def test_TemperaturePositive(self):
        self.assertTrue(Formula.temperature(12.0, 3.0, 0.0, 100.0) == -3588, "[!] Positive Test failed!")

    def test_TemperatureNegative(self):
        self.assertTrue(Formula.temperature(12.0, -3.0, 0.0, 100.0) == 3612.0, "[!] Negative Test failed!")

    def test_TemperatureFalseNonZero(self):
        self.assertFalse(Formula.temperature(12.0, 3.0, 0.0, -100) == 300.0, "[!] False non-zero Test failed!")


class DensityTest(unittest.TestCase):

    def test_DensityZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.density(0.0, 0.0)

    def test_DensityPositive(self):
        self.assertTrue(Formula.density(10.0, 10.0) == 0.0034832812124127974, "[!] Positive test failed!")

    def test_DensityNegative(self):
        self.assertTrue(Formula.density(10.0, -10.0) == -0.0034832812124127974, "[!] Negative test failed!")

    def test_DensityFalseNonZero(self):
        self.assertFalse(Formula.density(10.0, 10.0) == 33.0, "[!] False non-zero test failed")


class ResultingForceTest(unittest.TestCase):

    def test_ResultingForceZero(self):
        self.assertTrue(Formula.resultingforce(0.0, 0.0, 0.0) == 0.0, "[!] Zero test failed")

    def test_ResultingForcePositive(self):
        self.assertTrue(Formula.resultingforce(100.0, 10.0, 1000.0) == 1110.0, "[!] Positive test failed!")

    def test_ResultingForceNegative(self):
        self.assertTrue(Formula.resultingforce(-100.0, -10.0, -1000.0) == -1110.0, "[!] Negative test failed")

    def test_ResultingForceFalseNonZero(self):
        self.assertFalse(Formula.resultingforce(-100.0, 10.0, -1000.0) == -1110.0, "[!] False non-zero test failed")


def main():
    unittest.main()

if __name__ == "__main__":
    main()