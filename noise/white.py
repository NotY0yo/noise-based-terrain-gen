import random
import numpy as np

class WhiteNoise:
    def __init__(self):
        self.map_size = [100,100]

    def get_val_at_cord(self, X, Y):
        pass

    @property
    def map(self):
        noise_map = np.random.random(size=self.map_size)
        return noise_map
