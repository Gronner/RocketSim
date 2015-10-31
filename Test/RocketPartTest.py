import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

from RocketParts import RocketPart

# ----- Unit tests for RocketParts ----- #


class InitRocketPartTest(unittest.TestCase):

    def test_InitRocketPartZero(self):
        self.rocket_part = RocketPart(0.0, 0.0, 0.0)
        self.assertEqual(self.rocket_part.mass_part, 0.0, 0.0)
        self.assertEqual(self.rocket_part.surface_part, 0.0, 0.0)

    def test_InitRocketPartPositive(self):
        self.rocket_part = RocketPart(100.2, 234.50, 145.2)
        self.assertEqual(self.rocket_part.mass_part, 100.2)
        self.assertEqual(self.rocket_part.surface_part, 234.5)
        self.assertEqual(self.rocket_part.drag_coefficient_part, 145.2)

    def test_InitRocketPartMassNegative(self):
        with self.assertRaises(ValueError):
            self.rocket_part = RocketPart(-110.0, 0.0, 0.0)

    def test_InitRocketPartSurfaceNegative(self):
        with self.assertRaises(ValueError):
            self.rocket_part = RocketPart(0.0, -1100.0, 0.0)

    def test_InitRocketPartDragCoefficientNegative(self):
        with self.assertRaises(ValueError):
            self.rocket_part = RocketPart(0.0, 0.0, -1000.0)

    def test_InitRockPartFalseNonZero(self):
        self.rocket_part = RocketPart(100.2, 234.50, 234.5)
        self.assertNotEqual(self.rocket_part.mass_part, 235.2)
        self.assertNotEqual(self.rocket_part.surface_part, 1234.5)
        self.assertEqual(self.rocket_part.drag_coefficient_part, 234.5)


class GetMassTest(unittest.TestCase):

    def test_GetMassZero(self):
        self.rocket_part = RocketPart(0.0, 0.0, 0.0)
        self.assertEqual(self.rocket_part.get_mass(), 0.0, 0.0)

    def test_GetMassPositive(self):
        self.rocket_part = RocketPart(1000.2, 123.0, 543.2)
        self.assertEqual(self.rocket_part.get_mass(), 1000.2)

    def test_GetMassNegative(self):
        with self.assertRaises(ValueError):
            self.rocket_part = RocketPart(0.0, 123.0, 543.2)
            self.rocket_part.mass_part = -10000
            self.rocket_part.get_mass()

    def test_GetMassFalseNonZero(self):
        self.rocket_part = RocketPart(1312.0, 123.0, 543.2)
        self.assertNotEqual(self.rocket_part.get_mass(), 1000.0)


class GetSurfaceTest(unittest.TestCase):

    def test_GetSurfaceZero(self):
        self.rocket_part = RocketPart(0.0, 0.0, 0.0)
        self.assertEqual(self.rocket_part.get_surface(), 0.0)

    def test_GetSurfacePositive(self):
        self.rocket_part = RocketPart(1000.2, 123.0, 543.2)
        self.assertEqual(self.rocket_part.get_surface(), 123.0)

    def test_GetSurfaceNegative(self):
        with self.assertRaises(ValueError):
            self.rocket_part = RocketPart(0.0, 0.0, 543.2)
            self.rocket_part.surface_part = -10000
            self.rocket_part.get_surface()

    def test_GetMassFalseNonZero(self):
        self.rocket_part = RocketPart(1312.0, 123.0, 543.2)
        self.assertNotEqual(self.rocket_part.get_surface(), 1000.0)


class GetDragCoefficientTest(unittest.TestCase):

    def test_GetDragCoefficientZero(self):
        self.rocket_part = RocketPart(0.0, 0.0, 0.0)
        self.assertEqual(self.rocket_part.get_drag_coefficient(), 0.0)

    def test_GetDragCoefficientPositive(self):
        self.rocket_part = RocketPart(1000.2, 123.0, 543.2)
        self.assertEqual(self.rocket_part.get_drag_coefficient(), 543.2)

    def test_GetDragCoefficientNegative(self):
        with self.assertRaises(ValueError):
            self.rocket_part = RocketPart(0.0, 0.0, 543.2)
            self.rocket_part.drag_coefficient_part = -10000
            self.rocket_part.get_drag_coefficient()

    def test_GetDragCoefficientFalseNonZero(self):
        self.rocket_part = RocketPart(1312.0, 123.0, 543.2)
        self.assertNotEqual(self.rocket_part.get_drag_coefficient(), 1000.0)


class SetMassTest(unittest.TestCase):

    def test_SetMassZero(self):
        self.rocket_part = RocketPart(100.0, 0.0, 0.0)
        self.rocket_part.set_mass(0.0)
        self.assertEqual(self.rocket_part.get_mass(), 0.0)

    def test_SetMassPositive(self):
        self.rocket_part = RocketPart(100.0, 0.0, 0.0)
        self.rocket_part.set_mass(3000.2)
        self.assertEqual(self.rocket_part.get_mass(), 3000.2)

    def test_SetMassNegative(self):
        self.rocket_part = RocketPart(100.0, 0.0, 0.0)
        with self.assertRaises(ValueError):
            self.rocket_part.set_mass(-1000.2)

    def test_SetMassFalseNonZero(self):
        self.rocket_part = RocketPart(1234.0, 0.0, 0.0)
        self.rocket_part.set_mass(567.8)
        self.assertNotEqual(self.rocket_part.get_mass(), 1234.0)


# ----- Unit tests for Tank ----- #

class InitTankTest(unittest.TestCase):

    def test_InitTankZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.mass_part, 0.0)
        self.assertEqual(self.tank.surface_part, 0.0)
        self.assertEqual(self.tank.drag_coefficient, 0.0)
        self.assertEqual(self.mass_propellant, 0.0)

    def test_InitTankPositive(self):
        self.tank = Tank(130000.0, 134.0, 0.34, 100000.0)
        self.assertEqual(self.tank.mass_part, 130000.0)
        self.assertEqual(self.tank.surface_part, 134.0)
        self.assertEqual(self.tank.drag_coefficient, 0.34)
        self.assertEqual(self.mass_propellant, 100000.0)

    def test_InitTankMassNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(-110.0, 0.0, 0.0, 0.0)

    def test_InitTankSurfaceNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(0.0, -1100.0, 0.0, 0.0)

    def test_InitTankDragCoefficientNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(0.0, 0.0, -1000.0, 0.0)

    def test_InitTankPropMassNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(0.0, 0.0, 0.0, -130000.0)

    def test_InitTankFalseNonZero(self):
        self.tank = Tank(130000.0, 134.0, 0.34, 100000.0)
        self.assertNotEqual(self.tank.drag_coefficient, 12345.6)
        self.assertNotEqual(self.tank.mass_part, 10495.23)
        self.assertNotEqual(self.tank.surface_part, 0.32)
        self.assertNotEqual(self.tank.mass_propellant)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
