import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

from Atmospheres import Atmosphere
from Layers import Layer


class AddLayerTest(unittest.TestCase):

    def test_AddLayerInt(self):
        self.atmosphere = Atmosphere()
        with self.assertRaises(ValueError):
            self.atmosphere.add_layer(23)

    def test_AddLayerString(self):
        self.atmosphere = Atmosphere()
        with self.assertRaises(ValueError):
            self.atmosphere.add_layer("test")

    def test_AddLayerTest(self):
        self.atmosphere = Atmosphere()
        self.layer = Layer(0.0, 0.0, 0.0, 0.0)
        try:
            self.atmosphere.add_layer(self.layer)
        except Exception, e:
            self.fail(e)

    def test_AddLayerLayer(self):
        self.atmosphere = Atmosphere()
        self.layer_one = Layer(0.0, 0.0, 0.0, 0.0)
        self.layer_two = Layer(1.0, 1.0, 1.0, 1.0)
        try:
            self.atmosphere.add_layer(self.layer_one)
            self.atmosphere.add_layer(self.layer_two)
        except Exception, e:
            self.fail(e)


class GetLayerTest(unittest.TestCase):

    def test_GetLayerNoLayer(self):
        self.atmosphere = Atmosphere()
        self.height_rocket = 10000.0
        with self.assertRaises(IndexError):
            self.atmosphere.get_layer(self.height_rocket)

    def test_GetLayerOneLayer(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer_one = Layer(self.width_layer, self.temp_gradient, self.temp_low, self.pressure_low)
        self.atmosphere = Atmosphere()
        self.height_rocket = 10000.0
        self.atmosphere.add_layer(self.layer_one)
        self.assertEqual(self.atmosphere.get_layer(self.height_rocket), self.layer_one)

    def test_GetLayerNLayer(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer_one = Layer(self.width_layer, self.temp_gradient, self.temp_low, self.pressure_low)
        self.layer_two = Layer(self.width_layer, self.temp_gradient, self.temp_low, self.pressure_low)
        self.atmosphere = Atmosphere()
        self.height_rocket = 10000.0
        self.atmosphere.add_layer(self.layer_one)
        self.atmosphere.add_layer(self.layer_two)
        self.assertEqual(self.atmosphere.get_layer(self.height_rocket), self.layer_one)


def main():
    unittest.main()


if __name__ == "__main__":
    main()