import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

from Planets import Planet


class GetMassTest(unittest.TestCase):

    def test_GetMassZero(self):
        self.planet = Planet(0.0, 6000.0, (0, 0))
        self.assertEqual(self.planet.get_mass(), 0.0)

    def test_GetMassNonZero(self):
        self.planet = Planet(100000000.0, 6000.0, (0, 0))
        self.assertEqual(self.planet.get_mass(), 100000000.0)

    def test_GetMassFalseNonZero(self):
        self.planet = Planet(6000.0, 100000000.0, (0, 0))
        self.assertNotEqual(self.planet.get_mass(), 131231.0)


def main():
    unittest.main()

if __name__ == "__main__":
    main()