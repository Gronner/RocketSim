import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

from RocketParts import RocketPart


class InitRocketPartTest(unittest.TestCase):

    def test_InitRocketPartZero(self):
        self.rocket_part = RocketPart(0.0, 0.0)
        self.assertEqual(self.rocket_part.mass_part, 0.0)
        self.assertEqual(self.rocket_part.surface_part, 0.0)

    def test_InitRocketPartPositive(self):
        self.rocket_part = RocketPart(100.2, 234.50)
        self.assertEqual(self.rocket_part.mass_part, 100.2)
        self.assertEqual(self.rocket_part.surface_part, 234.5)

    def test_InitRocketPartMassNegative(self):
        with self.assertRaises(ValueError):
            self.rocket_part = RocketPart(-110.0, 0.0)

    def test_InitRocketPartSurfaceNegative(self):
        with self.assertRaises(ValueError):
            self.rocket_part = RocketPart(0.0, -1100.0)

    def test_InitRockPartFalseNonZero(self):
        self.rocket_part = RocketPart(100.2, 234.50)
        self.assertEqual(self.rocket_part.mass_part, 235.2)
        self.assertEqual(self.rocket_part.surface_part, 1234.5)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
