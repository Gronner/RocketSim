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
        new_pos = [0.0, 0.0]
        self.rocket.set_pos(new_pos)
        self.assertEqual(self.rocket.get_pos(), new_pos)

    def test_SetPosPositive(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_pos = [123.4, 5678.9]
        self.rocket.set_pos(new_pos)
        self.assertEqual(self.rocket.get_pos(), new_pos)

    def test_SetPosNegative(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_pos = [-123.4, -5678.9]
        self.rocket.set_pos(new_pos)
        self.assertEqual(self.rocket.get_pos(), new_pos)

    def test_SetPosFalseNonZero(self):
        self.rocket = Rocket([0.0, 0.0], [0.0, 0.0], [0.0, 0.0])
        new_pos = [432.1, 9876.5]
        self.rocket.set_pos(new_pos)
        self.assertNotEqual(self.rocket.get_pos(), [0.0, 0.0])


def main():
    unittest.main()

if __name__ == "__main__":
    main()