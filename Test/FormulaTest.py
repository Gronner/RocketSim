import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

import Formula


class ThrustTest(unittest.TestCase):

    def test_ThrustZero(self):
        self.assertEqual(Formula.thrust(0.0, 0.0, 0.0, 0.0, 0.0), 0.0)

    def test_ThrustPositive(self):
        self.assertEqual(Formula.thrust(10.0, 12.0, 15.0, 10.0, 3.0), 225.0)

    def test_ThrustNegative(self):
        self.assertEqual(Formula.thrust(-10.0, 12.0, -15.0, 10.0, 3.0), -225.0)

    def test_ThrustFalseNonZero(self):
        self.assertNotEqual(Formula.thrust(10.0, 12.0, 15.0, 10.0, 3.0), 10.0)


class DragTest(unittest.TestCase):

    def test_DragZero(self):
        self.assertEqual(Formula.drag(0.0, 0.0, 0.0, 0.0), 0.0)

    def test_DragPositive(self):
        self.assertEqual(Formula.drag(10.0, 12.0, 15.0, 10.0), 108000.0)

    def test_DragNegative(self):
        self.assertEqual(Formula.drag(-10.0, 12.0, 15.0, 10.0), -108000.0)

    def test_DragNegativeSquare(self):
        self.assertEqual(Formula.drag(10.0, -12.0, 15.0, 10.0), 108000.0)

    def test_DragFalseNonZero(self):
        self.assertNotEqual(Formula.drag(10.0, 12.0, 15.0, 10.0), 15.0)


class GravityTest(unittest.TestCase):

    def test_GravityZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.gravity(0.0, 0.0, 0.0)

    def test_GravityPositve(self):
        self.assertEqual(Formula.gravity(10.0, 12.0, 15.0), 3.559509333333333e-10)

    def test_GravityNegative(self):
        with self.assertRaises(ValueError):
            Formula.gravity(-10.0, 12.0, 15.0)

    def test_GravityFalseNonZero(self):
        self.assertNotEqual(Formula.gravity(10.0, 12.0, 15.0), 10.0)


class PressureTest(unittest.TestCase):

    def test_PressureZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.pressure(0.0, 0.0, 0.0, 0.0, 0.0)

    def testPressurePositive(self):
        self.assertEqual(Formula.pressure(1013.25, 0.0065, 100.0, 0.0, 24.0), 877.0988519626972)

    def testPressureNegative(self):
        self.assertEqual(Formula.pressure(-1013.25, 0.0065, 100.0, 0.0, 24.0), -877.0988519626972)

    def testPressureFalseNonZero(self):
        self.assertNotEqual(Formula.pressure(-1013.25, 0.0065, 100.0, 0.0, 24.0), -87.098852)


class TemperatureTest(unittest.TestCase):

    def test_TemperatureZero(self):
        self.assertEqual(Formula.temperature(0.0, 0.0, 0.0, 0.0), 0.0)

    def test_TemperaturePositive(self):
        self.assertEqual(Formula.temperature(12.0, 3.0, 0.0, 100.0), 312.0)

    def test_TemperatureNegative(self):
        self.assertEqual(Formula.temperature(12.0, -3.0, 0.0, 100.0), -288.0)

    def test_TemperatureFalseNonZero(self):
        self.assertNotEqual(Formula.temperature(12.0, 3.0, 0.0, -100), 300.0)


class DensityTest(unittest.TestCase):

    def test_DensityZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.density(0.0, 0.0)

    def test_DensityPositive(self):
        self.assertEqual(Formula.density(10.0, 10.0), 0.0034832812124127974)

    def test_DensityNegative(self):
        self.assertEqual(Formula.density(10.0, -10.0), -0.0034832812124127974)

    def test_DensityFalseNonZero(self):
        self.assertNotEqual(Formula.density(10.0, 10.0), 33.0)


class ResultingForceTest(unittest.TestCase):

    def test_ResultingForceZero(self):
        self.assertEqual(Formula.resulting_force(0.0, 0.0, 0.0), 0.0)

    def test_ResultingForcePositive(self):
        self.assertEqual(Formula.resulting_force(100.0, 10.0, 1000.0), 1110.0)

    def test_ResultingForceNegative(self):
        self.assertEqual(Formula.resulting_force(-100.0, -10.0, -1000.0), -1110.0)

    def test_ResultingForceFalseNonZero(self):
        self.assertNotEqual(Formula.resulting_force(-100.0, 10.0, -1000.0), -1110.0)


class AngleTest(unittest.TestCase):

    def test_AngleZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.angle(0.0, 0.0, 0.0, 0.0)

    def test_AnglePositive(self):
        self.assertEqual(Formula.angle(10.0, 3.0, 1000.0, 400.0), 65.16541251029841)

    def test_AngleNegative(self):
        self.assertEqual(Formula.angle(-10.0, 3.0, 1000.0, 400.0), 114.83458748970159)

    def testAngleFalseNonZero(self):
        self.assertNotEqual(Formula.angle(10.0, 3.0, 1000.0, 400.0), 14.0)


class AccelerationTest(unittest.TestCase):

    def test_AccelerationZero(self):
        with self.assertRaises(ZeroDivisionError):
            Formula.acceleration(0.0, 0.0)

    def test_AccelerationPositive(self):
        self.assertEqual(Formula.acceleration(100.0, 10.0), 10.0)

    def test_AccelerationNegative(self):
        self.assertEqual(Formula.acceleration(100.0, -10.0), -10.0)

    def test_AccelerationFalseNonZero(self):
        self.assertNotEqual(Formula.acceleration(100.0, 10.0), 23.0)


class VelocityTest(unittest.TestCase):

    def test_VelocityZero(self):
        self.assertEqual(Formula.velocity(0.0, 0.0, 0.0), 0.0)

    def test_VelocityPositive(self):
        self.assertEqual(Formula.velocity(10.0, 1.0, 9.81), 19.810000000000002)

    def test_VelocityNegative(self):
        self.assertEqual(Formula.velocity(-10.0, 1.0, -9.81), -19.810000000000002)

    def test_VelocityFalseNonZero(self):
        self.assertNotEqual(Formula.velocity(10.0, 1.0, 9.81), 14.03)


class ResXTest(unittest.TestCase):

    def test_ResXZero(self):
        self.assertEqual(Formula.res_x(0.0, 0.0), 0.0)

    def test_ResXPositive(self):
        self.assertEqual(Formula.res_x(10.0, 20.0), 9.396926207859085)

    def test_ResXNegative(self):
        self.assertEqual(Formula.res_x(10.0, -20.0), 9.396926207859085)

    def test_ResXFalseNonZero(self):
        self.assertNotEqual(Formula.res_x(10.0, 20.0), 14.1334)


class ResYTest(unittest.TestCase):

    def test_ResYZero(self):
        self.assertEqual(Formula.res_y(0.0, 0.0), 0.0)

    def test_ResYPositive(self):
        self.assertEqual(Formula.res_y(10.0, 20.0), 3.420201433256687)

    def test_ResYNegative(self):
        self.assertEqual(Formula.res_y(10.0, -20.0), -3.420201433256687)

    def test_ResYFalseNonZero(self):
        self.assertNotEqual(Formula.res_y(10.0, 20.0), 14.1334)


class WayTest(unittest.TestCase):

    def test_WayZero(self):
        self.assertEqual(Formula.way(0.0, 0.0, 0.0), 0.0)

    def test_WayPositive(self):
        self.assertEqual(Formula.way(1.0, 10.0, 9.81), 14.905000000000001)

    def test_WayNegative(self):
        self.assertEqual(Formula.way(-1.0, 10.0, 9.81), -5.095)

    def test_WayFalseNonZero(self):
        self.assertNotEqual(Formula.way(1.0, 10.0, 9.81), 12.032)


class PositionTest(unittest.TestCase):

    def test_PositionZero(self):
        self.assertEqual(Formula.position(0.0, 0.0), 0.0)

    def test_PositionPositive(self):
        self.assertEqual(Formula.position(20.0, 123.0), 143.00)

    def test_PositionNegative(self):
        self.assertEqual(Formula.position(-20.0, -123.0), -143.00)

    def test_PositionFalseNonZero(self):
        self.assertNotEqual(Formula.position(30.0, -44.0), -143.00)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
