from noise import *
import numpy as np
import matplotlib.pyplot as plt

def display_noise_map(noise_map):
    """
    Displays the given noise map using matplotlib.
from .
    Parameters:
    - noise_map (numpy.ndarray): A 2D numpy array representing the noise map to be displayed.

    Returns:
    None.

    Raises:
    None.
    """

    # Creating a figure and axis for the plot.
    fig, ax = plt.subplots()

    # Displaying the noise map as an image.
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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example usage of the PerlinNoiseMap class:

    # Creating a PerlinNoiseMap instance with custom parameters
    perlin_map = perlin.PerlinNoiseMap(width=100, height=100, scale=10, octaves=4, persistence=0.5)

    # Generating a noise map
    noise_map = perlin_map.generate_noise_map()

    # Displaying the noise map
    display_noise_map(noise_map)


