"""Highly inefficient ray marcher.
"""


import matplotlib.cm as cm
import numpy as np


ORIGIN = np.array([0., 0., 0.])
SPHERE_CENTRE = np.array([-3, 0, 5])
CUBE_CENTRE = np.array([3, 0, 5])


def sphere(point: np.array) -> float:
    """Return how far <point> is from the surface of the sphere.
    """
    centre = SPHERE_CENTRE
    r = 2
    return np.linalg.norm(point - centre) - r


def cube(point: np.array) -> bool:
    """Return how far <point> is from the surface of the cube.
    Concretely, this means return how far the farthest coordinate in <point> is
    from the cube's surface.
    """
    centre = CUBE_CENTRE
    r = 2
    return np.max(np.abs(point - centre)) - r


if __name__ == '__main__':
    dim = 64  # half of width of image
    out = np.zeros((2 * dim, 2 * dim))  # output image array
    dist = 8  # total distance for each ray to march
    steps = 10  # number of steps per unit distance of marching

    position = np.copy(ORIGIN)  # camera position

    for x in np.arange(-dim, dim, 1):      # for loops sweep through 90 degree
        for y in np.arange(-dim, dim, 1):  # field of vision in x, y directions
            direction = np.array([x, y, dim]) / dim  # ray direction vector
            direction /= np.linalg.norm(direction)  # normalize direction
            pos = np.copy(position)  # start ray at camera
            for cur_dist in np.arange(0, dist, 1 / steps):
                pos += direction / steps
                # march forward!
                if sphere(pos) <= 0 or cube(pos) <= 0:
                    out[y + dim][x + dim] = (dist - cur_dist) / dist
                    break
                    # if we hit an object, output the ray's brightness as a
                    # function of how far we are from the hit,
                    # then stop marching
                elif sphere(pos) < 0.03125 or cube(pos) < 0.03125:
                    out[y + dim][x + dim] = 1
                    # if we're close to an object, light up, but don't stop
                    # (in case we actually hit the object later)

    # this block is for saving an image
    # from PIL import Image
    # img = Image.fromarray(out * 255)
    # img = img.convert('RGB')
    # img.save('raymarcher.png')
    # img.show()

    # this block is for displaying with matplotlib
    from matplotlib import pyplot as plt
    plt.imshow(out, cmap=cm.gray)
    plt.show()
