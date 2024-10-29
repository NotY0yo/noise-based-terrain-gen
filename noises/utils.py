import random
import numpy as np
from fontTools.mtiLib import parseSingleSubst


class chunk:
    def __init__(self, chunk_coordinates:list, max_x:int=16, max_y:int=16):
        self.x_size:int = max_x
        self.y_size:int = max_y
        self.data:np.ndarray = np.zeros(shape=(self.x_size, self.y_size), dtype=float)
        self.chunk_coordinate = chunk_coordinates

    def __getattr__(self, item) -> float:
        return self.data[item]

class Noise:
    def __init__(self, seed, max_val:float=1.0, min_val:float=0.0, seed_offset:int=0):
        self.max:float = max_val
        self.min:float = min_val
        random.seed(seed)
        self.seed = seed
        self.seed_offset:int = seed_offset
        self.generated_chunks = []

    def generate_chunk(self) -> chunk:
        pass

    def get_float_from_cord(self) -> float:
        pass
        # convert cords to chunk_cords
        # if chunk_cords in self.generate_chunks
        # chunk = self.generated_chunks[chunk_cords]
        # else generate_chunk
        # then convert cords to cords in this chunk
        # return float value
