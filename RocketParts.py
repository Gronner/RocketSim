"""
Author:         Felix Braeunling
Description:    Those classes are used to describe rocket parts in general and different variants of rocket parts
"""


class RocketPart(object):
    """
    Base class for rocket parts with their attributes mass_part, surface_part and drag_coefficient_part
    """

    def __init__(self, mass_part, surface_part, drag_coefficient_part):
        """
        Sets up a rocket part with value validation
        :param mass_part: Mass of the part (Not negative Double) [kg]
        :param surface_part: Surface area of the part (Not negative Double) [m^2]
        :param drag_coefficient_part: Drag coefficient of the part (Not negative Double) [1]
        """
        if mass_part < 0:
            raise ValueError
        else:
            self.mass_part = mass_part
        if surface_part < 0:
            raise ValueError
        else:
            self.surface_part = surface_part
        if drag_coefficient_part < 0:
            raise ValueError
        else:
            self.drag_coefficient_part = drag_coefficient_part

    def get_mass(self):
        """
        :return: Mass of the part (Not Negative Double) [kg]
        """
        if self.mass_part < 0:
            raise ValueError
        return self.mass_part

    def get_surface(self):
        """
        :return: Surface area of the part (Not Negative Double) [m^2]
        """
        if self.surface_part < 0:
            raise ValueError
        return self.surface_part

    def get_drag_coefficient(self):
        """
        :return: Drag coefficient of the part (Not Negative Double) [1]
        """
        if self.drag_coefficient_part < 0:
            raise ValueError
        return self.drag_coefficient_part

    def set_mass(self, new_mass_part):
        """
        Changes the mass of the object and validates the value
        :param new_mass_part: New Mass of the part (Not negative Double) [kg]
        """
        if new_mass_part < 0:
            raise ValueError
        self.mass_part = new_mass_part


class Tank(RocketPart):
    """
    Class to describe rocket tanks with connected engine
    """

    def __init__(self, mass_part, surface_part, drag_coefficient_part, mass_propellant, thrust_tank,
                 velocity_exhaust_tank):
        """
        Setup for a tank with value validation
        :param mass_part: Mass of the tank (without propellant!) (Double) [kg]
        :param surface_part: Surface of the tank (Double) [m^2]
        :param drag_coefficient_part: Drag coefficient of the tank (Double) [1]
        :param mass_propellant: Mass of the propellant stored in the tank (Double) [kg]
        :param thrust_tank: Thrust Level the tank is generating, scales mass flow of the propellant (Double) [%]
        :param velocity_exhaust_tank: Velocity of the propellant at the nozzle [m/s]
        """
        RocketPart.__init__(self, mass_part, surface_part, drag_coefficient_part)
        if mass_propellant < 0:
            raise ValueError
        else:
            self.mass_propellant = mass_propellant
        if thrust_tank < 0 or thrust_tank > 1:
            raise ValueError
        else:
            self.thrust_tank = thrust_tank
        if velocity_exhaust_tank < 0:
            raise ValueError
        else:
            self.velocity_exhaust_tank = velocity_exhaust_tank

    def get_thrust(self):
        """
        :return: Thrust level of the engine, scales the mass of propellant flow (Double) [%]
        """
        if self.thrust_tank < 0 or self.thrust_tank > 1:
            raise ValueError
        return self.thrust_tank

    def set_thrust(self, new_thrust_tank):
        """
        Allows to change the thrust level of the engine
        :param new_thrust_tank: New thrust level of the engine
        """
        if new_thrust_tank < 0 or new_thrust_tank > 1:
            raise ValueError
        else:
            self.thrust_tank = new_thrust_tank

    def get_velocity_exhaust(self):
        """
        :return: Velocity of the propellant exhaust at the nozzle (Double) [m/s]
        """
        if self.velocity_exhaust_tank < 0:
            raise ValueError
        else:
            return self.velocity_exhaust_tank
