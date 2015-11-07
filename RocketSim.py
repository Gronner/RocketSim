"""
Author: Felix Braeunling

Description: This file contains the Flight class, that describes a setup flight and also contains
"""

class Flight(object):

    def __init__(self, time_delta, planet, rocket, atmosphere, data, filename):
        self.time_delta = time_delta
        self.planet = planet
        self.rocket = rocket
        self.atmosphere = atmosphere
        self.data = data

