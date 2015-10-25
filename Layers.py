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
        """
        :return: The width (vertical) of the atmospheric layer (Double) [m]
        """
        return self.width_layer

    def set_width(self, new_width_layer):
        """
        Allows to set the width of the current layer
        :param new_width_layer: New width of the atmospheric layer (Double) [m]
        """
        self.width_layer = new_width_layer

    def get_temp_gradient(self):
        """
        :return: The temperature gradient of the current atmospheric layer (Double) [K/m]
        """
        return self.temp_gradient

    def set_temp_gradient(self, new_temp_gradient):
        """
        Allows to set the temperature gradient of the atmospheric layer (Double)
        :param new_temp_gradient: New temperature gradient of the atmospheric layer (Double) [K/m]
        """
        self.temp_gradient = new_temp_gradient

    def get_temp_low(self):
        """
        :return: The temperature at the lower end of the layer (Double) [K]
        """
        return self.temp_low

    def set_temp_low(self, new_temp_low):
        """
        Allows to set the temperature at the lower end of the atmospheric layer
        :param new_temp_low: New temperature at the lower end of the layer (Double) [K]
        """
        self.temp_low = new_temp_low

    def get_pressure_low(self):
        """
        :return: The pressure at the lower end of the layer (Double) [Pa]
        """
        return self.pressure_low

    def set_pressure_low(self, new_pressure_low):
        """
        Allows to set the pressure at the lower end of the atmospheric layer
        :param new_pressure_low: New pressure at the lower end of the atmospheric layer (Double) [Pa]
        """
        self.pressure_low = new_pressure_low

    def get_pressure_now(self, height_rocket, height_layer_below):
        """
        Calculates the pressure at the height the rocket currently is in
        :param height_rocket: Height of the rocket above the planets surface (Double)
        :param height_layer_below: Accumulated height of the atmospheric layers beneath the current layer (Double)
        :return: Pressure at the current height in the layer (Double) [Pa]
        """
        return Formula.pressure(self.pressure_low, self.temp_gradient, height_rocket, height_layer_below, self.temp_low)

    def get_temperature_now(self, height_rocket, height_layer_below):
        """
        Calculates the temperature at the height the rocket currently is in
        :param height_rocket: Height of the rocket above the planets surface (Double)
        :param height_layer_below: Accumulated height of the atmospheric layers beneath the current layer (Double)
        :return: Temperature at the current height in the layer (Double) [K]
        """
        return Formula.temperature(self.temp_low, self.temp_gradient, height_layer_below, height_rocket)

    def get_density_now(self, height_rocket, height_layer_below):
        """
        Calculates the density of the medium at the height the rocket is currently in
        :param height_rocket: Height of the rocket above the planets surface (Double)
        :param height_layer_below: Accumulated height of the atmospheric layers beneath the current layer (Double)
        :return: Density of the medium the rocket is in at a given height (Double) [kg/m^3]
        """
        temperature_now = self.get_temperature_now(height_rocket, height_layer_below)
        pressure_now = self.get_pressure_now(height_rocket, height_layer_below)
        return Formula.density(pressure_now, temperature_now)
