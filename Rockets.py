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
