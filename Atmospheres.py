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

    def calc_height_below(self, layer_index):
        """
        Calculates the accumulated height of the layers below the indexed layer
        :param layer_index: Index of the layer the height below is calculated (Integer)
        :return: Accumulated height of the layers below the indexed one (Double) [m]
        """
        height_below = 0
        for i in range(0, layer_index):
            height_below += self.layers[i].get_width()
        return height_below

    def get_layer(self, height_rocket):
        """
        Returns the layer the rocket is at the moment.
        :param height_rocket: Height of the rocket above the planets surface (Double)
        :return: The Layer the rocket currently is into (Layer)
        """
        current_layer = self.layers[0]
        for i in range(0, len(self.layers)):
            height_below = self.calc_height_below(i)
            if height_below > height_rocket:
                break
            current_layer = self.layers[i]
        return current_layer

    def get_layers(self):
        """
        Returns a list of the layers of this atmosphere object
        :return: Layers of this atmosphere (List)
        """
        return self.layers
