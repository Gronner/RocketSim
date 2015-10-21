import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

from Layers import Layer


class WidthTest(unittest.TestCase):

    def test_GetWidthTestTrue(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer = Layer(self.width_layer, self.temp_gradient, self.temp_low, self.pressure_low)
        self.assertEqual(self.layer.get_width(), self.width_layer)

    def test_SetWidthTest(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer_set = Layer(0.0, 0.0, 0.0, 0.0)
        self.layer_set.set_width(self.width_layer)
        self.assertEqual(self.layer_set.get_width(), self.width_layer)

    def test_GetTempGradient(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer = Layer(self.width_layer, self.temp_gradient, self.temp_low, self.pressure_low)
        self.assertEqual(self.layer.get_temp_gradient(), self.temp_gradient)

    def test_SetTempGradient(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer_set = Layer(0.0, 0.0, 0.0, 0.0)
        self.layer_set.set_temp_gradient(self.temp_gradient)
        self.assertEqual(self.layer_set.get_temp_gradient(), self.temp_gradient)

    def test_GetTempLow(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer = Layer(self.width_layer, self.temp_gradient, self.temp_low, self.pressure_low)
        self.assertEqual(self.layer.get_temp_low(), self.temp_low)

    def test_SetTempLow(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer_set = Layer(0.0, 0.0, 0.0, 0.0)
        self.layer_set.set_temp_low(self.temp_low)
        self.assertEqual(self.layer_set.get_temp_low(), self.temp_low)


def main():
    unittest.main()

if __name__ == "__main__":
    main()