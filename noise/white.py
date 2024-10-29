import random
import numpy as np

class WhiteNoise:
    def __init__(self, max_val:float=1.0, min_val:float=0.0):
        self.max:float = max_val
        self.min:float = min_val

    def get_val_at_cord(self, X, Y) -> float:
        val = random.uniform(self.min, self.max)
        return val

    @property
    def map(self, size:tuple = (100,100)):
        noise_map = np.zeros(size)
        for row in range(len(noise_map)):
            for col in range(len(noise_map[row])):
                noise_map[row, col] = self.get_val_at_cord(row, col)
        return noise_map
