import numpy
from collections import namedtuple
from typing import List

# Tower vectors
T_NORTH = numpy.array([0.00, 0.43, 0.00])
T_WEST = numpy.array([-0.50, -0.43, 0.00])
T_EAST = numpy.array([0.50, -0.43, 0.00])
Plane = namedtuple('Plane', ['tail_num', 'x', 'y', 'z', 'horiz_angle',
                             'vert_angle', 'speed'])

class Collision:
    """
    A collision between 2 aircraft

    In all honesty, this can probably just be a named tuple
    rather than a class
    """
    
    def __init__(self, p1: Plane, p2: Plane,
                 coll_point: List[int, int, int], d: float):
        self.p1 = p1
        self.p2 = p2
        self.coll_point = coll_point
        self.distance_between_planes = self.d
    
    def __str__(self) -> str:
        return f'Crash Imminent between {self.p1.tail_num} \
                 and {self.p2.tail_num}.\nCollision will occur at \
                 position ({self.coll_point[0]}, {self.coll_point[1]}, \
                 {self.coll_point[2]}).\nCurrent distance between planes: \
                 {self.distance} km.'

    def __lt__(self, other: Collision) -> bool:
        return self.distance_between_planes < other.distance_between_planes

    def __le__(self, other: Collision) -> bool:
        return self.distance_between_planes <= other.distance_between_planes

    def __eq__(self, other: Collision) -> bool:
        return self.distance_between_planes == other.distance_between_planes

    def __gt__(self, other: Collision) -> bool:
        return self.distance_between_planes > other.distance_between_planes

    def __ge__(self, other: Collision) -> bool:
        return self.distance_between_planes >= other.distance_between_planes


def determine_collisions(planes: List[Plane]) -> List[Collision]:
    """Find all collisions in a given airspace 

    Args:
        planes (List[Plane]): The planes to be evaluated for collisions

    Returns:
        List[Collision]: A list of collisions sorted by distance
    """
    collisions = []
    pairs = set()
    for pos, plane in enumerate(planes):
        pass
    return sorted(collisions, key=lambda c: c.distance_between_planes)
