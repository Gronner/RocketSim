"""
Author:         Felix Braeunling
Description:    This class describes the atmosphere of a planet consisting of different layers.
"""

from Layers import Layer


class Atmosphere(object):

    def __init__(self):
        self.layers = []

    def add_layer(self, new_layer):
        """
        Adds a new layer to the atmosphere, the new layer gets added at the end of the layer list, this the new layer
        is the highest one.
        :param new_layer: A layer object describing an atmospheric layer (Layer)
        """
        if type(new_layer) != Layer:
            raise ValueError
        self.layers.append(new_layer)



