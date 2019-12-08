from shapely.geometry import Polygon, mapping, shape
import json
from typing import List

class Environment:

    def __init__(self, obstacles, bounds, goal):
        self.obstacles:List[Polygon] = obstacles
        self.bounds: Polygon = bounds
        self.goal = goal

def deserialize_environment()->Environment:
    polygons = list()
    goal = None
    bounds = None
    with open("Serialized Environments/two_walls.json", "r") as f:
        data = json.load(f)
        for item in data:
            if item["type"] == "Polygon":
                polygons.append(Polygon(shape(item)))
            if item["type"] == "Goal":
                goal = item["coordinates"]
            if item["type"] == "Bounds":
                x_min, x_max = item["x_range_exclusive"]
                y_min, y_max = item["y_range_exclusive"]
                bounds = Polygon([(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)])

    return Environment(polygons, bounds, goal)

# NOTE: should only have to be done once or twice;
# afterwards, can edit .json by hand:
def serialize_polygons():
    p1 = Polygon([(1, 1), (4, 1), (3, 3), (2, 4)])
    p2 = Polygon([(7, 1), (9, 1), (8, 2)])
    mappings = [mapping(p) for p in [p1, p2]]
    with open("Serialized Environments/simple_polygons.json", "w") as f:
        json.dump(mappings, f)
