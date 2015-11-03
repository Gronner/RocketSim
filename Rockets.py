"""
Author:         Felix Braeunling
Description:    This class describes the assambled rocket with its position and pyhsical attributes
"""

from RocketParts import RocketPart
from RocketParts import Tank


class Rocket(object):

    def __init__(self, pos, velocity, acceleration):
        """
        Set up of a rocket
        :param pos: Position of the rocket as x and y coordinates (Tuple -> (Double, Double)
        :param velocity: Velocity of the rocket in x and y direction (Tuple -> (Double, Double)
        :param acceleration: Acceleration of the rocket in x and y direction (Tuple -> (Double, Double)
        """
        self.rocket_parts = []
        self.pos = pos
        self.velocity = velocity
        self.acceleration = acceleration
        self.mass = 0.0
        self.surface = 0.0
        self.angle = 0.0

    def get_pos(self):
        """
        :return: The position of the rocket as x and y coordinates (Tuple -> (Double, Double)) ([m], [m])
        """
        return self.pos

    def get_velocity(self):
        """
        :return: The velocity of the rocket in x and y direction (Tuple -> (Double, Double)) ([m/s], [m/s])
        """
        return self.velocity

    def get_acceleration(self):
        """
        :return: The acceleration of the rocket in x and y direction (Tuple -> (Double, Double)) ([m/s^2], [m/s^2])
        """
        return self.acceleration

    def set_pos(self, pos_x, pos_y):
        """
        Allows to set the position of the rocket as x and y coordinates
        :param pos_x: X-position of the rocket (Double)
        :param pos_y: Y-position of the rocket (Double)
        """
        self.pos = [pos_x, pos_y]

    def set_velocity(self, velocity_x, velocity_y):
        """
        Allows to set the velocity of the rocket in x and y direction
        :param velocity_x: Velocity in X direction of the rocket (Double)
        :param velocity_y: Velocity in Y direction of the rocket (Double)
        """
        self.velocity = [velocity_x, velocity_y]

    def set_acceleration(self, acceleration_x, acceleration_y):
        """
        Allows to set the acceleration of the rocket in x and y direction
        :param acceleration_x: Acceleration in X direction of the rocket (Double)
        :param acceleration_y: Acceleration in Y direction of the rocket (Double)
        """
        self.acceleration = [acceleration_x, acceleration_y]
