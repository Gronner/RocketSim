"""
Author:         Felix Braeunling
Description:    Those classes are used to describe rocket parts in general and different variants of rocket parts
"""

class RocketPart(object):
    """
    Base class for rocket parts with their attributes mass_part and surface_part
    """

    def __init__(self, mass_part, surface_part):
        """
        Sets up a rocket part with value validation
        :param mass_part: Mass of the part (Non negative Double) [kg]
        :param surface_part: Surface of the part (Non negative Double) [m^2]
        """
        if mass_part < 0:
            raise ValueError
        self.mass_part = mass_part
        if surface_part < 0:
            raise ValueError
        self.surface_part = surface_part
