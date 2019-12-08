from shapely.geometry import Polygon
from typing import Tuple
import random

def random_point_in_polygon(p: Polygon)->Tuple[float, float]:
    """ Note: actually samples within the BOUNDING BOX of the polygon. In future, 
        decompose the polygon into triangles and sample from them. """
    min_x, min_y, max_x, max_y = p.bounds
    x = random.uniform(min_x, max_x)
    y = random.uniform(min_y, max_y)
    return (x, y)
