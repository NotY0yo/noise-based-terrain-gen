import random
import numpy as np

class PerlinNoise:
    def __init__(self):
        pass
    def get_val_at_cord(self) -> float:
        pass

    def _interpolate(self, a, b, t):
        # Interpolating between the two values using the interpolation factor.
        return a + (b - a) * t
    def _smoothstep(self, t):
        # Applying the smoothstep function to the input.
        return t ** 2 * (3 - 2 * t)