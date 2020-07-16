import numpy
from collections import namedtuple
from typing import List, Tuple

# Tower vectors
T_NORTH = numpy.array([0.00, 0.43, 0.00])
T_WEST = numpy.array([-0.50, -0.43, 0.00])
T_EAST = numpy.array([0.50, -0.43, 0.00])

# distance_to_towers is a list/tuple/array of floats to each tower (N, W, E)
Plane = namedtuple('Plane', ['horiz_angle',
                             'vert_angle', 'signal_strength'])


class Collision:
    """
    A collision between 2 aircraft

    In all honesty, this can probably just be a named tuple
    rather than a class
    """
    
    def __init__(
                 self,
                 p1_pos: Tuple[int, int, int],  # these should be numpy arrays
                 p2_pos: Tuple[int,int,int],  # type hints don't support them
                 coll_point: Tuple[int, int, int],  # you hate to see it
                 d: float
                ):
        self.p1_pos = numpy.array(p1_pos)
        self.p2_pos = numpy.array(p2_pos)
        self.coll_point = coll_point
        self.distance_between_planes = self.d

    def __str__(self) -> str:
        return f'Crash Imminent between plane at {self.p1_pos} \
                 and {self.p2_pos}.\nCollision will occur at \
                 position ({self.coll_point}).\n\
                 Current distance between planes: {self.distance} km.'

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
