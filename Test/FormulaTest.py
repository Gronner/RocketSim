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


class AngleTest(unittest.TestCase):

    def test_AngleZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.angle(0.0, 0.0, 0.0, 0.0)

    def test_AnglePositive(self):
        self.assertTrue(Formula.angle(10.0, 3.0, 1000.0, 400.0) == 65.16541251029841, "[!] Positive test failed!")

    def test_AngleNegative(self):
        self.assertTrue(Formula.angle(-10.0, 3.0, 1000.0, 400.0) == 114.83458748970159, "[!] Negative test failed!")

    def testAngleFalseNonZero(self):
        self.assertFalse(Formula.angle(10.0, 3.0, 1000.0, 400.0) == 14.0, "[!] False non-zero failed!")


class AccelerationTest(unittest.TestCase):

    def test_AccelerationZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.acceleration(0.0, 0.0)

    def test_AccelerationPositive(self):
        self.assertTrue(Formula.acceleration(100.0, 10.0) == 10.0, "[!] Positive test failed!")

    def test_AccelerationNegative(self):
        self.assertTrue(Formula.acceleration(100.0, -10.0) == -10.0, "[!] Negative test failed!")

    def test_AccelerationFalseNonZero(self):
        self.assertFalse(Formula.acceleration(100.0, 10.0) == 23.0, "[!] False non-zero test failed!")


class VelocityTest(unittest.TestCase):

    def test_VelocityZero(self):
        self.assertTrue(Formula.velocity(0.0, 0.0, 0.0) == 0.0, "[!] Zero test failed!")

    def test_VelocityPositive(self):
        self.assertTrue(Formula.velocity(10.0, 1.0, 9.81) == 19.810000000000002, "[!] Positive test failed!")

    def test_VelocityNegative(self):
        self.assertTrue(Formula.velocity(-10.0, 1.0, -9.81) == -19.810000000000002, "[!] Negative test failed!")

    def test_VelocityFalseNonZero(self):
        self.assertFalse(Formula.velocity(10.0, 1.0, 9.81) == 14.03, "[!] False non-zero test failed!")


class ResFxTest(unittest.TestCase):

    def test_ResFxZero(self):
        self.assertTrue(Formula.resfx(0.0, 0.0) == 0.0, "[!] Zero test failed!")

    def test_ResFxPositive(self):
        self.assertTrue(Formula.resfx(10.0, 20.0) == 9.396926207859085, "[!] Positive test failed!")

    def test_ResFxNegative(self):
        self.assertTrue(Formula.resfx(10.0, -20.0) == 9.396926207859085, "[!] Negative test failed!")

    def test_ResFxFalseNonZero(self):
        self.assertFalse(Formula.resfx(10.0, 20.0) == 14.1334, "[!] False non-zero test failed!")


class ResFyTest(unittest.TestCase):

    def test_ResFyZero(self):
        self.assertTrue(Formula.resfy(0.0, 0.0) == 0.0, "[!] Zero test failed!")

    def test_ResFyPositive(self):
        self.assertTrue(Formula.resfy(10.0, 20.0) == 3.420201433256687, "[!] Positive test failed!")

    def test_ResFyNegative(self):
        self.assertTrue(Formula.resfy(10.0, -20.0) == -3.420201433256687, "[!] Negative test failed!")

    def test_ResFyFalseNonZero(self):
        self.assertFalse(Formula.resfy(10.0, 20.0) == 14.1334, "[!] False non-zero test failed!")


class WayTest(unittest.TestCase):

    def test_WayZero(self):
        self.assertTrue(Formula.way(0.0, 0.0, 0.0, 0.0) == 0.0, "[!] Zero test failed!")

    def test_WayPositive(self):
        self.assertTrue(Formula.way(10.0, 1.0, 10.0, 9.81) == 24.905, "[!] Positive test failed!")

    def test_WayNegative(self):
        self.assertTrue(Formula.way(-10.0, -1.0, 10.0, 9.81) == -24.905, "[!] Positive test failed!")

    def test_WayFalseNonZero(self):
        self.assertFalse(Formula.way(10.0, 1.0, 10.0, 9.81) == 12.032, "[!] False non-zero test failed!")


def main():
    unittest.main()

if __name__ == "__main__":
    main()