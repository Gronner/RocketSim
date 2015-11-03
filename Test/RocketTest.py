import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

from Rockets import Rocket
from RocketParts import RocketPart
from RocketParts import Tank


class InitRocketTest(unittest.TestCase):

    def test_InitRocketZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.assertEqual(self.rocket.rocket_parts, [])
        self.assertEqual(self.rocket.pos, [0.0, 0.0])
        self.assertEqual(self.rocket.velocity, [0.0, 0.0])
        self.assertEqual(self.rocket.acceleration, [0.0, 0.0])
        self.assertEqual(self.rocket.mass, 0.0)
        self.assertEqual(self.rocket.surface, 0.0)
        self.assertEqual(self.rocket.angle, 0.0)

    def test_InitRocketPositive(self):
        self.rocket = Rocket([12.0, 13.2], [192.30, 1235.2], [992.0, 882.0])
        self.nose = RocketPart(1000.2, 231.2, 0.23)
        self.rocket.rocket_parts.append(self.nose)
        self.assertEqual(self.rocket.rocket_parts, [self.nose])
        self.assertEqual(self.rocket.pos, [12.0, 13.2])
        self.assertEqual(self.rocket.velocity, [192.30, 1235.2])
        self.assertEqual(self.rocket.acceleration, [992.0, 882.0])
        self.assertEqual(self.rocket.mass, 0.0)
        self.assertEqual(self.rocket.surface, 0.0)
        self.assertEqual(self.rocket.angle, 0.0)

    def test_InitRocketNegativeMovement(self):
        self.rocket = Rocket([-12.0, -13.2], [-192.30, -1235.2], [-992.0, -882.0])
        self.assertEqual(self.rocket.pos, [-12.0, -13.2])
        self.assertEqual(self.rocket.velocity, [-192.30, -1235.2])
        self.assertEqual(self.rocket.acceleration, [-992.0, -882.0])

    def test_InitRocketFalseNonZero(self):
        self.rocket = Rocket([22.0, 23.2], [292.30, 2235.2], [292.0, 282.0])
        self.assertNotEqual(self.rocket.pos, [12.0, 13.2])
        self.assertNotEqual(self.rocket.velocity, [192.30, 1235.2])
        self.assertNotEqual(self.rocket.acceleration, [992.0, 882.0])
        self.assertNotEqual(self.rocket.mass, 10.0)
        self.assertNotEqual(self.rocket.surface, 20.0)
        self.assertNotEqual(self.rocket.angle, 30.0)


class GetPostTest(unittest.TestCase):

    def test_GetPosZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.assertEqual(self.rocket.get_pos(), [0.0, 0.0])

    def test_GetPosPositive(self):
        self.rocket = self.rocket = Rocket([13.3, 222222.2], [0.0, 0.0], [0.0, 0.0])
        self.assertEqual(self.rocket.get_pos(), [13.3, 222222.2])

    def test_GetPosNegative(self):
        self.rocket = self.rocket = Rocket([-13.3, -222222.2], [0.0, 0.0], [0.0, 0.0])
        self.assertEqual(self.rocket.get_pos(), [-13.3, -222222.2])

    def test_GetPosFalseNonZero(self):
        self.rocket = self.rocket = self.rocket = Rocket([24.2, 1234.5], [0.0, 0.0], [0.0, 0.0])
        self.assertNotEqual(self.rocket.get_pos(), [13.3, 222222.2])


class GetVelocityTest(unittest.TestCase):

    def test_GetVelocityZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.assertEqual(self.rocket.get_velocity(), [0.0, 0.0])

    def test_GetVelocityPositive(self):
        self.rocket = self.rocket = Rocket([0.0, 0.0], [13.3, 222222.2], [0.0, 0.0])
        self.assertEqual(self.rocket.get_velocity(), [13.3, 222222.2])

    def test_GetVelocityNegative(self):
        self.rocket = Rocket([0.0, 0.0], [-13.3, -222222.2], [0.0, 0.0])
        self.assertEqual(self.rocket.get_velocity(), [-13.3, -222222.2])

    def test_GetVelocityFalseNonZero(self):
        self.rocket = Rocket([0.0, 0.0], [24.2, 1234.5], [0.0, 0.0])
        self.assertNotEqual(self.rocket.get_velocity(), [13.3, 222222.2])


class GetAccelerationTest(unittest.TestCase):

    def test_GetAccelerationZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.assertEqual(self.rocket.get_acceleration(), [0.0, 0.0])

    def test_GetAccelerationPositive(self):
        self.rocket = self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [13.3, 222222.2])
        self.assertEqual(self.rocket.get_acceleration(), [13.3, 222222.2])

    def test_GetAccelerationNegative(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [-13.3, -222222.2])
        self.assertEqual(self.rocket.get_acceleration(), [-13.3, -222222.2])

    def test_GetAccelerationFalseNonZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [24.2, 1234.5])
        self.assertNotEqual(self.rocket.get_acceleration(), [13.3, 222222.2])


class SetPosTest(unittest.TestCase):

    def test_SetPosZero(self):
        self.rocket = Rocket([13.3, 222222.2], [0.0, 0.0], [0.0, 0.0])
        self.rocket.set_pos(0.0, 0.0)
        self.assertEqual(self.rocket.get_pos(), [0.0, 0.0])

    def test_SetPosPositive(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_x = 123.4
        new_y = 5678.9
        self.rocket.set_pos(new_x, new_y)
        self.assertEqual(self.rocket.get_pos(), [new_x, new_y])

    def test_SetPosNegative(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_x = 123.4
        new_y = 5678.9
        self.rocket.set_pos(-1*new_x, -1*new_y)
        self.assertEqual(self.rocket.get_pos(), [-1*new_x, -1*new_y])

    def test_SetPosFalseNonZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_x = 123.4
        new_y = 5678.9
        self.rocket.set_pos(432.1, 9876.5)
        self.assertNotEqual(self.rocket.get_pos(), [new_x, new_y])


class SetVelocityTest(unittest.TestCase):

    def test_SetVelocityZero(self):
        self.rocket = Rocket([0.0, 0.0], [13.3, 222222.2], [0.0, 0.0])
        self.rocket.set_velocity(0.0, 0.0)
        self.assertEqual(self.rocket.get_velocity(), [0.0, 0.0])

    def test_SetVelocityPositive(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_x = 123.4
        new_y = 5678.9
        self.rocket.set_velocity(new_x, new_y)
        self.assertEqual(self.rocket.get_velocity(), [new_x, new_y])

    def test_SetVelocityNegative(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_x = 123.4
        new_y = 5678.9
        self.rocket.set_velocity(-1*new_x, -1*new_y)
        self.assertEqual(self.rocket.get_velocity(), [-1*new_x, -1*new_y])

    def test_SetVelocityFalseNonZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_x = 123.4
        new_y = 5678.9
        self.rocket.set_velocity(432.1, 9876.5)
        self.assertNotEqual(self.rocket.get_velocity(), [new_x, new_y])


class SetAccelerationTest(unittest.TestCase):

    def test_SetAccelerationZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [13.3, 222222.2])
        self.rocket.set_acceleration(0.0, 0.0)
        self.assertEqual(self.rocket.get_acceleration(), [0.0, 0.0])

    def test_SetAccelerationPositive(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_x = 123.4
        new_y = 5678.9
        self.rocket.set_acceleration(new_x, new_y)
        self.assertEqual(self.rocket.get_acceleration(), [new_x, new_y])

    def test_SetAccelerationNegative(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_x = 123.4
        new_y = 5678.9
        self.rocket.set_acceleration(-1*new_x, -1*new_y)
        self.assertEqual(self.rocket.get_acceleration(), [-1*new_x, -1*new_y])

    def test_SetAccelerationFalseNonZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_x = 123.4
        new_y = 5678.9
        self.rocket.set_acceleration(432.1, 9876.5)
        self.assertNotEqual(self.rocket.get_acceleration(), [new_x, new_y])


class GetMassTest(unittest.TestCase):

    def test_GetMassZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.assertEqual(self.rocket.get_mass(), 0.0)

    def test_GetMassPositive(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.rocket.mass = 123.4
        self.assertEqual(self.rocket.get_mass(), 123.4)

    def test_GetMassNegative(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.rocket.mass = -123.4
        with self.assertRaises(ValueError):
            self.rocket.get_mass()

    def test_GetMassFalseNonZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.rocket.mass = 56789.0
        self.assertNotEqual(self.rocket.get_mass(), 123.4)


class AppendPartTest(unittest.TestCase):

    def test_AppendPartInt(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        with self.assertRaises(ValueError):
            self.rocket.append_part(123)

    def test_AppendPartString(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        with self.assertRaises(ValueError):
            self.rocket.append_part("test")

    def test_AppendPartRocketPartFirst(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.part_one = RocketPart(1000.0, 2000.0, 0.34)
        self.rocket.append_part(self.part_one)
        self.assertEqual(self.rocket.rocket_parts[0], self.part_one)

    def test_AppendPartTankFirst(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.tank_one = Tank(1000.0, 2000.0, 0.34, 1000.0, 0.5, 100.0)
        with self.assertRaises(ValueError):
            self.rocket.append_part(self.tank_one)

    def test_AppendPartRocketPartThenTank(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        self.part_one = RocketPart(1000.0, 2000.0, 0.34)
        self.tank_one = Tank(1000.0, 2000.0, 0.34, 1000.0, 0.5, 100.0)
        self.rocket.append_part(self.part_one)
        self.rocket.append_part(self.tank_one)
        self.assertEqual(self.rocket.rocket_parts[0], self.part_one)
        self.assertEqual(self.rocket.rocket_parts[1], self.tank_one)


def main():
    unittest.main()

if __name__ == "__main__":
    main()