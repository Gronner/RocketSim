"""
Author: Felix Braeunling

Description: This file contains the Flight class, that describes a setup flight and also contains
"""
import Formula
from Atmospheres import Atmosphere
from Datas import Data
from Layers import Layer
from Planets import Planet
from RocketParts import RocketPart, Tank


class Flight(object):

    def __init__(self, time_delta, planet, rocket, atmosphere, data):
        """
        Setup of a flight with it's parameters
        :param time_delta: Size of the time step the simulation use
        :param planet: Planet the flight will take place
        :param rocket: Rocket the flight will use
        :param atmosphere: Atmosphere of the planet
        :param data: Data object gained values will be saved in.
        :return:
        """
        self.time_delta = time_delta
        self.planet = planet
        self.rocket = rocket
        self.atmosphere = atmosphere
        self.data = data

    def __lt__(self, other):
        max_self = max(self.data.pos_rocket)
        max_other = max(other.data.pos_rocket)
        return Formula.vector_addition(max_self) < Formula.vector_addition(max_other)
