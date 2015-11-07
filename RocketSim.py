"""
Author: Felix Braeunling

Description: This file contains the Flight class, that describes a setup flight and also contains
"""


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