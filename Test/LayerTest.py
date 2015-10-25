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


class TempGradientTest(unittest.TestCase):

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


class TempLowTest(unittest.TestCase):

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


class PressureLowTest(unittest.TestCase):

    def test_GetPressureLow(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer = Layer(self.width_layer, self.temp_gradient, self.temp_low, self.pressure_low)
        self.assertEqual(self.layer.get_pressure_low(), self.pressure_low)

    def test_SetPressureLow(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer_set = Layer(0.0, 0.0, 0.0, 0.0)
        self.layer_set.set_pressure_low(self.pressure_low)
        self.assertEqual(self.layer_set.get_pressure_low(), self.pressure_low)


class CalculationTest(unittest.TestCase):

    def test_GetPressureNow(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer = Layer(self.width_layer, self.temp_gradient, self.temp_low, self.pressure_low)
        self.height_rocket = 12000.0  # [m]
        self.height_layer_below = 0.0  # [m]
        self.assertEqual(self.layer.get_pressure_now(self.height_rocket, self.height_layer_below), 21139.080525291483)

    def test_GetTemperatureNow(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer = Layer(self.width_layer, self.temp_gradient, self.temp_low, self.pressure_low)
        self.height_rocket = 12000.0  # [m]
        self.height_layer_below = 0.0  # [m]
        self.assertEqual(self.layer.get_temperature_now(self.height_rocket, self.height_layer_below), 380.5)

    def test_GetDensityNow(self):
        self.width_layer = 18000.0  # [m]
        self.temp_gradient = 6.5 / 1000.0  # [K/m]
        self.temp_low = 30.0 + 272.5  # [K]
        self.pressure_low = 101325.0  # [Pa]
        self.layer = Layer(self.width_layer, self.temp_gradient, self.temp_low, self.pressure_low)
        self.height_rocket = 12000.0  # [m]
        self.height_layer_below = 0.0  # [m]
        self.assertEqual(self.layer.get_density_now(self.height_rocket, self.height_layer_below), 0.19351737724422885)


def main():
    unittest.main()

if __name__ == "__main__":
    main()