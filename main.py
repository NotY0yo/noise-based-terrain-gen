
from matplotlib import cm
from noise import *
import numpy as np
import matplotlib.pyplot as plt

"""
perlin
temperature
humidity
shifted
base_3d
surface

"""




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
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    plt.style.use('_mpl-gallery')

    # convert 2d arry into x, y, z coords
    x = np.arange(0, noise_map.shape[0])
    y = np.arange(0, noise_map.shape[1])
    x, y = np.meshgrid(x, y)


    # Displaying the noise map as an image.
    ax.plot_surface(X=x, Y=y, Z=noise_map, vmin=noise_map.min() * 2, cmap=cm.Blues)

    # Setting the title and labels for the plot.
    ax.set_zlim(0,noise_map.max()*2)
    ax.set_title('Perlin Noise Map')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Displaying the plot.
    plt.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # Creating a PerlinNoiseMap instance with custom parameters
    perlin_map = perlin.PerlinNoiseMap(width=50, height=50, scale=10, octaves=4, persistence=0.1)

    # Generating a noise map
    noiseMap = perlin_map.generate_noise_map()

    print(f"x:{noiseMap.shape[0]} , y: {noiseMap.shape[1]}")
    # Displaying the noise map
    display_noise_map(noiseMap)
    """
    import matplotlib.pyplot as plt
    import numpy as np

    from matplotlib import cm

    plt.style.use('_mpl-gallery')

    # Make data
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    # Plot the surface
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
           yticklabels=[],
           zticklabels=[])

    plt.show()"""