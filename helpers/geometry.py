from shapely.geometry import Polygon, LineString
from typing import Tuple, List
import random

def random_point_in_polygon(p: Polygon)->Tuple[float, float]:
    """ Note: actually samples within the BOUNDING BOX of the polygon. In future, 
        decompose the polygon into triangles and sample from them. """
    min_x, min_y, max_x, max_y = p.bounds
    x = random.uniform(min_x, max_x)
    y = random.uniform(min_y, max_y)
    return (x, y)

def path_length(path: List, distance_function)->float:
    distance = 0
    for p1, p2 in zip(path, path[1:]):
        distance += distance_function(p1, p2)
    return distance

def line_collides_with_obstacles(path: LineString, obstacles: List[Polygon])->bool:
    for obstacle in obstacles:
        if path.intersects(obstacle):
            return True
    return False