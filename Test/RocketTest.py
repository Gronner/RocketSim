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
        self.assertNotEqual(self.rocket.mass, 0.0)
        self.assertNotEqual(self.rocket.surface, 0.0)
        self.assertNotEqual(self.rocket.angle, 0.0)
