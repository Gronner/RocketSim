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
