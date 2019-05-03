import numpy as np


class SceneObject:
    def __init__(self, centre: np.array, scale: float) -> None:
        self.centre = centre
        self.scale = scale

    def sdf(self, point: np.array) -> float:
        """Every scene object must have a signed distance function - a function
        which returns how far away a point is from the surface of the object.
        The returned value is positive if the point is outside the object and
        negative if it is inside.
        """
        raise NotImplementedError


class Sphere(SceneObject):
    def sdf(self, point: np.array) -> float:
        """Return how far <point> is from the surface of the sphere.
        """
        return np.linalg.norm(point - self.centre) - self.scale


class Cube(SceneObject):
    def sdf(self, point: np.array) -> float:
        """Return how far <point> is from the surface of the cube.
        Concretely, this means return how far the farthest coordinate in <point> is
        from the cube's surface.
        """
        return np.max(np.abs(point - self.centre)) - self.scale
