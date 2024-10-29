import random
import numpy as np

class Noise:
    def __init__(self, max_val:float=1.0, min_val:float=0.0):
        self.max:float = max_val
        self.min:float = min_val