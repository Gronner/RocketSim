import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

from Planets import Planet


class GetMassTest(unittest.TestCase):

    def test_GetMassZero(self):
        self.planet = Planet(0.0, 6000.0, (0.0, 0.0))
        self.assertEqual(self.planet.get_mass(), 0.0)

    def test_GetMassNonZero(self):
        self.planet = Planet(100000000.0, 6000.0, (0.0, 0.0))
        self.assertEqual(self.planet.get_mass(), 100000000.0)

    def test_GetMassFalseNonZero(self):
        self.planet = Planet(6000.0, 100000000.0, (0.0, 0.0))
        self.assertNotEqual(self.planet.get_mass(), 131231.0)


class GetRadiusTest(unittest.TestCase):

    def test_GetRadiusZero(self):
        self.planet = Planet(0.0, 0.0, (0.0, 0.0))
        self.assertEqual(self.planet.get_radius(), 0.0)

    def test_GetRadiusNonZero(self):
        self.planet = Planet(0.0, 6000.0, (0.0, 0.0))
        self.assertEqual(self.planet.get_radius(), 6000.0)

    def test_GetRadiusFalseNonZero(self):
        self.planet = Planet(0.0, 6000.0, (0.0, 0.0))
        self.assertNotEqual(self.planet.get_radius(), 0.0)


class GetPosTest(unittest.TestCase):

    def test_GetPosZero(self):
        self.planet = Planet(0.0, 0.0, (0.0, 0.0))
        self.assertEqual(self.planet.get_pos(), (0.0, 0.0))

    def test_GetPosPositive(self):
        self.planet = Planet(0.0, 0.0, (60.0, 40.6))
        self.assertEqual(self.planet.get_pos(), (60.0, 40.6))

    def test_GetPosNegtive(self):
        self.planet = Planet(0.0, 0.0, (-30.3, -20.0))
        self.assertEqual(self.planet.get_pos(), (-30.3, -20.0))

    def test_GetPosFalseNonZero(self):
        self.planet = Planet(0.0, 0.0, (60.2, 40.0))
        self.assertNotEqual(self.planet.get_pos(), (-20.0, 30.0))


def main():
    unittest.main()

if __name__ == "__main__":
    main()