import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

from RocketParts import RocketPart
from RocketParts import Tank

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


class GetThrustTest(unittest.TestCase):

    def test_GetThrustZero(self):
        self.rocket_part = RocketPart(0.0, 0.0, 0.0)
        self.assertEqual(self.rocket_part.get_thrust(), 0.0)


# ----- Unit tests for Tank ----- #

class InitTankTest(unittest.TestCase):

    def test_InitTankZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.mass_part, 0.0)
        self.assertEqual(self.tank.surface_part, 0.0)
        self.assertEqual(self.tank.drag_coefficient_part, 0.0)
        self.assertEqual(self.tank.mass_propellant, 0.0)
        self.assertEqual(self.tank.mass_change_tank, 0.0)
        self.assertEqual(self.tank.velocity_exhaust_tank, 0.0)
        self.assertEqual(self.tank.surface_nozzle, 0.0)
        self.assertEqual(self.tank.pressure_nozzle, 0.0)

    def test_InitTankPositive(self):
        self.tank = Tank(130000.0, 134.0, 0.34, 100000.0, 0.23, 369.2, 2.2, 10023.2)
        self.assertEqual(self.tank.mass_part, 130000.0)
        self.assertEqual(self.tank.surface_part, 134.0)
        self.assertEqual(self.tank.drag_coefficient_part, 0.34)
        self.assertEqual(self.tank.mass_propellant, 100000.0)
        self.assertEqual(self.tank.mass_change_tank, 0.23)
        self.assertEqual(self.tank.velocity_exhaust_tank, 369.2)
        self.assertEqual(self.tank.surface_nozzle, 2.2)
        self.assertEqual(self.tank.pressure_nozzle, 10023.2)

    def test_InitTankMassNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(-110.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def test_InitTankSurfaceNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(0.0, -1100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def test_InitTankDragCoefficientNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(0.0, 0.0, -1000.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    def test_InitTankPropMassNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(0.0, 0.0, 0.0, -130000.0, 0.0, 0.0, 0.0, 0.0)

    def test_InitTankMassChangeNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(0.0, 0.0, 0.0, 0.0, -20000.0, 0.0, 0.0, 0.0)

    def test_InitTankVeNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, -6450.0, 0.0, 0.0)

    def test_InitTankSurfaceNozzleNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -123.2, 0.0)

    def test_InitTankPressureNozzleNegative(self):
        with self.assertRaises(ValueError):
            self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0, -242.3)

    def test_InitTankFalseNonZero(self):
        self.tank = Tank(15.0, 2341.2, 94830.1, 0.23, 0.23, 1002.2, 4.2, 8.23)
        self.assertNotEqual(self.tank.drag_coefficient_part, 130000.0)
        self.assertNotEqual(self.tank.mass_part, 134.0)
        self.assertNotEqual(self.tank.surface_part, 0.34)
        self.assertNotEqual(self.tank.mass_propellant, 100000.0)
        self.assertNotEqual(self.tank.mass_change_tank, 666.0)
        self.assertNotEqual(self.tank.velocity_exhaust_tank, 369.2)
        self.assertNotEqual(self.tank.surface_nozzle, 2.2)
        self.assertNotEqual(self.tank.pressure_nozzle, 10023.2)


class GetThrustLevelTankTest(unittest.TestCase):

    def test_GetThrustLevelZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.tank.thrust_level_tank = 0.0
        self.assertEqual(self.tank.get_thrust_level(), 0.0)

    def test_GetThrustLevelPositiveSubZero(self):
        self.tank = Tank(15.0, 2341.2, 94830.1, 0.23, 0.23, 1002.2, 0.0, 0.0)
        self.tank.thrust_level_tank = 0.23
        self.assertEqual(self.tank.get_thrust_level(), 0.23)

    def test_GetThrustLevelPositiveAboveZero(self):
        self.tank = Tank(15.0, 2341.2, 94830.1, 0.23, 0.23, 1002.2, 0.0, 0.0)
        self.tank.thrust_level_tank = 1.23
        with self.assertRaises(ValueError):
            self.tank.get_thrust_level()

    def test_GetThrustLevelNegative(self):
        self.tank = Tank(15.0, 2341.2, 94830.1, 0.23, 0.23, 1002.2, 0.0, 0.0)
        self.tank.thrust_level_tank = -10003.2
        with self.assertRaises(ValueError):
            self.tank.get_thrust_level()

    def test_GetThrustLevelFalseNonZero(self):
        self.tank = Tank(15.0, 2341.2, 94830.1, 0.23, 0.23, 1002.2, 0.0, 0.0)
        self.assertNotEqual(self.tank.get_thrust_level, 0.23)


class SetThrustTankTest(unittest.TestCase):

    def test_SetThrustZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.23, 0.0, 0.0, 0.0)
        self.tank.set_thrust_level(0.0)
        self.assertEqual(self.tank.get_thrust_level(), 0.0)

    def test_SetThrustPositiveSubOne(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.85, 0.0, 0.0, 0.0)
        self.tank.set_thrust_level(0.23)
        self.assertEqual(self.tank.get_thrust_level(), 0.23)

    def test_SetThrustPositiveAboveOne(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.85, 0.0, 0.0, 0.0)
        with self.assertRaises(ValueError):
            self.tank.set_thrust_level(1.23)

    def test_SetThrustNegative(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.85, 0.0, 0.0, 0.0)
        with self.assertRaises(ValueError):
            self.tank.set_thrust_level(-0.23)

    def test_SetThrustFalseNonZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.85, 0.0, 0.0, 0.0)
        self.tank.set_thrust_level(0.75)
        self.assertNotEqual(self.tank.get_thrust_level(), 0.85)


class GetVelocityExhaustTest(unittest.TestCase):

    def test_GetVelocityExhaustZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.get_velocity_exhaust(), 0.0)

    def test_GetVelocityExhaustPositive(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 123.0, 0.0, 0.0)
        self.assertEqual(self.tank.get_velocity_exhaust(), 123.0)

    def test_GetVelocityExhaustNegative(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.tank.velocity_exhaust_tank = -123.0
        with self.assertRaises(ValueError):
            self.tank.get_velocity_exhaust()

    def test_GetVelocityExhaustFalseNonZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 234.0, 0.0, 0.0)
        self.assertNotEqual(self.tank.get_velocity_exhaust(), 123.0)


class GetMassTest(unittest.TestCase):

    def test_GetMassZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.get_mass(), 0.0)

    def test_GetMassPartZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 1000.2, 0.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.get_mass(), 1000.2)

    def test_GetMassPropZero(self):
        self.tank = Tank(123.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.get_mass(), 123.4)

    def test_GetMassPositive(self):
        self.tank = Tank(123.4, 0.0, 0.0, 1000.2, 0.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.get_mass(), 123.4+1000.2)

    def test_GetMassNegative(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.tank.mass_propellant = -100.2
        with self.assertRaises(ValueError):
            self.tank.get_mass()

    def test_GetMassFalseNonZero(self):
        self.tank = Tank(567.8, 0.0, 0.0, 901.3, 0.0, 0.0, 0.0, 0.0)
        self.assertNotEqual(self.tank.get_mass(), 123.4+1000.2)


class SetMassPropellantTest(unittest.TestCase):

    def test_SetMassPropellantZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 999.0, 0.0, 0.0, 0.0, 0.0)
        self.tank.set_mass_propellant(0.0)
        self.assertEqual(self.tank.mass_propellant, 0.0)

    def test_SetMassPropellantPositive(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.tank.set_mass_propellant(999.0)
        self.assertEqual(self.tank.mass_propellant, 999.0)

    def test_SetMassPropellantNegative(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        with self.assertRaises(ValueError):
            self.tank.set_mass_propellant(-232.2)

    def test_SetMassPropellantFalseNonZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.tank.set_mass_propellant(232.2)
        self.assertNotEqual(self.tank.mass_propellant, 999.0)


class GetMassChangeTest(unittest.TestCase):

    def test_GetMassChangeZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.get_mass_change(), 0.0)

    def test_GetMassChangePositive(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 230.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.get_mass_change(), 230.0)

    def test_GetMassChangePositiveReducedThrustLevel(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 230.0, 0.0, 0.0, 0.0)
        self.tank.set_thrust_level(0.5)
        self.assertEqual(self.tank.get_mass_change(), 230.0*0.5)

    def test_GetMassChangeNegative(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 230.0, 0.0, 0.0, 0.0)
        self.tank.thrust_level_tank = -0.5
        with self.assertRaises(ValueError):
            self.tank.get_mass_change()


class GetSurfaceNozzleTest(unittest.TestCase):

    def test_GetSurfaceNozzleZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.get_surface_nozzle(), 0.0)

    def test_GetSurfaceNozzlePositive(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 123.2, 0.0)
        self.assertEqual(self.tank.get_surface_nozzle(), 123.2)

    def test_GetSurfaceNozzleNegative(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.tank.surface_nozzle = -23.2
        with self.assertRaises(ValueError):
            self.tank.get_surface_nozzle()

    def test_GetSurfaceNozzleFalseNonZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 472.5, 0.0)
        self.assertNotEqual(self.tank.get_surface_nozzle(), 123.2)


class GetPressureNozzleTest(unittest.TestCase):

    def test_GetPressureNozzleZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.assertEqual(self.tank.get_pressure_nozzle(), 0.0)

    def test_GetPressureNozzlePositive(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 123.2, 123.2)
        self.assertEqual(self.tank.get_pressure_nozzle(), 123.2)

    def test_GetPressureNozzleNegative(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        self.tank.pressure_nozzle = -23.2
        with self.assertRaises(ValueError):
            self.tank.get_pressure_nozzle()

    def test_GetPressureNozzleFalseNonZero(self):
        self.tank = Tank(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 472.5, 823.3)
        self.assertNotEqual(self.tank.get_pressure_nozzle(), 123.2)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
