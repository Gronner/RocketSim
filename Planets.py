"""
Author:         Felix Braeunling
Description:    This class describes the planet (or celestial body) the rocket is taking off
"""


class Planet(object):

    def __init__(self, mass_planet, radius_planet, pos_planet):
        """
        Setup of an object that describes a planet (or celestial body)
        :param mass_planet: Mass of the planet (Double) [kg]
        :param radius_planet: Radius of the planet (center to surface) (Double) [m]
        :param pos_planet: Position of the planets center of mass as x and y Coordinates (Tuple -> (Double, Double))
        """
        self.mass_planet = mass_planet
        self.radius_planet = radius_planet
        self.pos_planet = pos_planet

    def get_mass(self):
        """
        :return: Mass of the planet (Double) [kg]
        """
        return self.mass_planet

    def get_radius(self):
        """
        :return: Radius of the planet (Double) [m]
        """
        return self.radius_planet

    def get_pos(self):
        """
        :return: Position of the center of mass of the planet (Tuple -> (Double, Double)
        """
        return self.pos_planet
