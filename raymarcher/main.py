"""Somewhat wonky ray marcher!
"""

import sys
import matplotlib.cm as cm
from raymarcher.scene_objects import *
import numpy as np


ORIGIN = np.array([0., 0., 0.])
HIT_DIST = 2 ** -4
EDGE_DIST = 2 ** -3


if __name__ == '__main__':
    dim = 512  # half of width of image
    size = (dim * 2) ** 2  # number of pixels
    out = np.zeros((dim * 2, dim * 2))  # output image array
    max_dist = 10  # total distance for each ray to march

    camera_pos = np.copy(ORIGIN)  # camera position

    scene = [Sphere(np.array([-3, -1, 5]), 2),
             Cube(np.array([3, 3, 5]), 2)]

    count = 0
    for x in np.arange(-dim, dim, 1):      # for loops sweep through 90 degree
        for y in np.arange(-dim, dim, 1):  # field of vision in x, y directions
            sys.stdout.write(f'\r{100 * count / size} %')  # print progress

            direction = np.array([x, y, dim]) / dim  # ray direction vector
            direction /= np.linalg.norm(direction)  # normalize direction

            pos = np.copy(camera_pos)  # start ray at camera

            scene_dist = min(x.sdf(pos) for x in scene)  # initialize scene_dist

            while np.linalg.norm(pos - camera_pos) < max_dist:
                old_scene_dist = scene_dist  # scene_dist for previous pos
                scene_dist = min(x.sdf(pos) for x in scene)

                # march forward!
                pos += direction * scene_dist

                if scene_dist <= HIT_DIST:
                    out[y + dim][x + dim] = 1 / np.dot(pos - camera_pos,
                                                       pos - camera_pos)
                    break
                    # if we hit an object, output the ray's brightness as a
                    # function of how far we are from the hit,
                    # then stop marching
                elif scene_dist <= EDGE_DIST and old_scene_dist <= EDGE_DIST:
                    out[y + dim][x + dim] = -1
                    # break
                    # if we're close to an object, light up, but don't stop
                    # (in case we actually hit the object later)
            count += 1
    # normalize image array
    out /= np.max(out)
    out[out < 0] = 1  # make edges bright again

    # this block is for saving an image
    from PIL import Image
    img = Image.fromarray(out * 255)
    img = img.convert('RGB')
    img.save('raymarcher.png')
    img.show()

    # this block is for displaying with matplotlib
    from matplotlib import pyplot as plt
    plt.imshow(out, cmap=cm.gray)
    plt.show()
