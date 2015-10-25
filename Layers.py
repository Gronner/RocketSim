import Formula


class Layer(object):

    def __init__(self, width_layer, temp_gradient, temp_low, pressure_low):
        """
        Setup of an object to describe a layer of an atmosphere
        :param width_layer: Height the layer is spanning over (Double) [m]
        :param temp_gradient: Change in temperature over distance in the layer (Double) [K/m]
        :param temp_low: Temperature at the lower end of the layer (Double) [K]
        :param pressure_low: Pressure at the lower end of the layer (Double) [Pa]
        """
        self.width_layer = width_layer
        self.temp_gradient = temp_gradient
        self.temp_low = temp_low
        self.pressure_low = pressure_low

    def get_width(self):
        return self.width_layer

    def set_width(self, new_width_layer):
        self.width_layer = new_width_layer

    def get_temp_gradient(self):
        return self.temp_gradient

    def set_temp_gradient(self, new_temp_gradient):
        self.temp_gradient = new_temp_gradient

    def get_temp_low(self):
        return self.temp_low

    def set_temp_low(self, new_temp_low):
        self.temp_low = new_temp_low

    def get_pressure_low(self):
        return self.pressure_low

    def set_pressure_low(self, new_pressure_low):
        self.pressure_low = new_pressure_low

    def get_pressure_now(self, height_rocket, height_layer_below):
        """
        Calculates the pressure at the height the rocket currently is
        :param height_rocket: Height of the rocket above the planets surface (Double)
        :param height_layer_below: Accumulated height of the atmospheric layers beneath the current layer (Double)
        :return: Pressure at the current height in the layer (Double) [Pa]
        """
        return Formula.pressure(self.pressure_low, self.temp_gradient, height_rocket, height_layer_below, self.temp_low)