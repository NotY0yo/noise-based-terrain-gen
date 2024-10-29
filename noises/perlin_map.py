import numpy as np
import matplotlib.pyplot as plt

"""
code from site:
https://codepal.ai/code-generator/query/5pIVmmBb/perlin-noise-map-python
"""



class PerlinNoiseMap:
    """
    A class to generate and display Perlin noises maps using customizable parameters.

    Perlin noises is a type of gradient noises used in computer graphics and procedural generation.
    This class provides a way to generate Perlin noises maps and visualize them using matplotlib.

    Attributes:
    - width (int): The width of the generated noises map.
    - height (int): The height of the generated noises map.
    - scale (float): The scale of the noises map, which affects the frequency of the noises.
    - octaves (int): The number of octaves used to generate the noises map, which affects the level of detail.
    - persistence (float): The persistence of the noises map, which affects the amplitude of each octave.
    """

    def __init__(self, width: int, height: int, scale: float, octaves: int, persistence: float):
        """
        Constructs a new PerlinNoiseMap instance.

        Parameters:
        - width (int): The width of the generated noises map.
        - height (int): The height of the generated noises map.
        - scale (float): The scale of the noises map, which affects the frequency of the noises.
        - octaves (int): The number of octaves used to generate the noises map, which affects the level of detail.
        - persistence (float): The persistence of the noises map, which affects the amplitude of each octave.

        Raises:
        - ValueError: If any of the parameters (width, height, scale, octaves, persistence) is invalid.
        """

        # Verifying that the parameters are valid.
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if scale <= 0:
            raise ValueError("Scale must be a positive float.")
        if octaves <= 0:
            raise ValueError("Octaves must be a positive integer.")
        if persistence <= 0 or persistence > 1:
            raise ValueError("Persistence must be a float between 0 and 1.")

        # Assigning the parameters to the instance variables.
        self.width = width
        self.height = height
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence

    def generate_noise_map(self):
        """
        Generates a Perlin noises map using the specified parameters.

        Returns:
        numpy.ndarray: A 2D numpy array representing the generated noises map.

        Raises:
        None.
        """

        # Generating an empty 2D array of zeros with the specified width and height.
        noise_map = np.zeros((self.height, self.width))

        # Generating random gradients for each point in the noises map.
        gradients = np.random.randn(self.height, self.width, 2)

        # Generating the noises map by combining multiple octaves of Perlin noises.
        for octave in range(self.octaves):
            # Calculating the frequency and amplitude for the current octave.
            frequency = 2 ** octave
            amplitude = self.persistence ** octave

            # Calculating the coordinates of the sample points for the current octave.
            sample_x = np.arange(0, self.width) / self.scale * frequency
            sample_y = np.arange(0, self.height) / self.scale * frequency

            # Generating a grid of coordinates for the sample points.
            sample_grid_x, sample_grid_y = np.meshgrid(sample_x, sample_y)

            # Calculating the integer coordinates of the four surrounding grid points.
            sample_x0 = np.floor(sample_grid_x).astype(int)
            sample_x1 = sample_x0 + 1
            sample_y0 = np.floor(sample_grid_y).astype(int)
            sample_y1 = sample_y0 + 1

            # Calculating the fractional coordinates within each grid cell.
            sample_dx = sample_grid_x - sample_x0
            sample_dy = sample_grid_y - sample_y0

            # Calculating the dot products between the gradients and the distance vectors.
            dot_product_top_left = np.einsum('ijk,ijk->ij', gradients[sample_y0, sample_x0],
                                             np.stack([sample_dx, sample_dy], axis=2))
            dot_product_top_right = np.einsum('ijk,ijk->ij', gradients[sample_y0, sample_x1],
                                              np.stack([sample_dx - 1, sample_dy], axis=2))
            dot_product_bottom_left = np.einsum('ijk,ijk->ij', gradients[sample_y1, sample_x0],
                                                np.stack([sample_dx, sample_dy - 1], axis=2))
            dot_product_bottom_right = np.einsum('ijk,ijk->ij', gradients[sample_y1, sample_x1],
                                                 np.stack([sample_dx - 1, sample_dy - 1], axis=2))

            # Interpolating the dot products using smoothstep interpolation.
            weight_x = self._smoothstep(sample_dx)
            weight_y = self._smoothstep(sample_dy)
            interpolated_top = self._interpolate(dot_product_top_left, dot_product_top_right, weight_x)
            interpolated_bottom = self._interpolate(dot_product_bottom_left, dot_product_bottom_right, weight_x)
            interpolated = self._interpolate(interpolated_top, interpolated_bottom, weight_y)

            # Adding the interpolated values to the noises map.
            noise_map += interpolated * amplitude

        # Normalizing the noises map to the range [0, 1].
        noise_map = (noise_map - np.min(noise_map)) / (np.max(noise_map) - np.min(noise_map))

        # Returning the generated noises map.
        return noise_map

    def display_noise_map(self, noise_map):
        """
        Displays the given noises map using matplotlib.

        Parameters:
        - noise_map (numpy.ndarray): A 2D numpy array representing the noises map to be displayed.

        Returns:
        None.

        Raises:
        None.
        """

        # Creating a figure and axis for the plot.
        fig, ax = plt.subplots()

        # Displaying the noises map as an image.
        ax.imshow(noise_map, cmap='gray', origin='lower')

        # Adding a colorbar to the plot.
        cbar = plt.colorbar(ax.imshow(noise_map, cmap='gray', origin='lower'))
        cbar.set_label('Noise Value')

        # Setting the title and labels for the plot.
        ax.set_title('Perlin Noise Map')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        # Displaying the plot.
        plt.show()

    def display_multi_map(self, noise_maps):
        fig, ax = plt.subplots(figsize=(5, 5))
        for i in range(0, 5):
            for j in range(0, 5):
                temp = ax.imshow(noise_maps[i, j], cmap='gray', origin='lower')
                ax[i, j] = temp

        plt.show()

    def _smoothstep(self, t):
        """
        Applies the smoothstep function to the given input.

        The smoothstep function is a sigmoid-like interpolation function that
        maps the input from the range [0, 1] to the range [0, 1] smoothly.

        Parameters:
        - t (numpy.ndarray): The input values to be smoothed.

        Returns:
        numpy.ndarray: The smoothed output values.

        Raises:
        None.
        """

        # Applying the smoothstep function to the input.
        return t ** 2 * (3 - 2 * t)

    def _interpolate(self, a, b, t):
        """
        Interpolates between two values using the given interpolation factor.

        Parameters:
        - a (numpy.ndarray): The first value to interpolate from.
        - b (numpy.ndarray): The second value to interpolate to.
        - t (numpy.ndarray): The interpolation factor.

        Returns:
        numpy.ndarray: The interpolated values.

        Raises:
        None.
        """

        # Interpolating between the two values using the interpolation factor.
        return a + (b - a) * t


if __name__ == '__main__':
    # Example usage of the PerlinNoiseMap class:

    # Creating a PerlinNoiseMap instance with custom parameters
    perlin_map = PerlinNoiseMap(width=100, height=100, scale=10, octaves=4, persistence=0.5)

    # Generating a noises map
    noise_map = perlin_map.generate_noise_map()

    # Displaying the noises map
    perlin_map.display_noise_map(noise_map)