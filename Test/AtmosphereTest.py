import unittest
import sys
sys.path.append('/home/felix/Projekte/Studienarbeit/RocketSim')

from Atmospheres import Atmosphere
from Layers import Layer


class AddLayerTest(unittest.TestCase):

    def test_AddLayerInt(self):
        self.atmosphere = Atmosphere()
        with self.assertRaises(ValueError):
            self.atmosphere.add_layer(23)

    def test_AddLayerString(self):
        self.atmosphere = Atmosphere()
        with self.assertRaises(ValueError):
            self.atmosphere.add_layer("test")

    def test_AddLayerTest(self):
        self.atmosphere = Atmosphere()
        self.layer = Layer(0.0, 0.0, 0.0, 0.0)
        try:
            self.atmosphere.add_layer(self.layer)
        except Exception, e:
            self.fail(e)

    def test_AddLayerLayer(self):
        self.atmosphere = Atmosphere()
        self.layer_one = Layer(0.0, 0.0, 0.0, 0.0)
        self.layer_two = Layer(1.0, 1.0, 1.0, 1.0)
        try:
            self.atmosphere.add_layer(self.layer_one)
            self.atmosphere.add_layer(self.layer_two)
        except Exception, e:
            self.fail(e)