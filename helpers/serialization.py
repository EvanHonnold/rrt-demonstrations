from shapely.geometry import Polygon, mapping, shape
import json

class Environment:
    def __init__(self, obstacles, goal):
        self.obstacles = obstacles
        self.goal = goal

def deserialize_environment()->Environment:
    polygons = list()
    goal = None
    with open("Serialized Environments/two_walls.json", "r") as f:
        data = json.load(f)
        for item in data:
            if item["type"] == "Polygon":
                polygons.append(Polygon(shape(item)))
            if item["type"] == "Goal":
                goal = item["coordinates"]
    return Environment(polygons, goal)

# NOTE: should only have to be done once or twice;
# afterwards, can edit .json by hand:
def serialize_polygons():
    p1 = Polygon([(1, 1), (4, 1), (3, 3), (2, 4)])
    p2 = Polygon([(7, 1), (9, 1), (8, 2)])
    mappings = [mapping(p) for p in [p1, p2]]
    with open("Serialized Environments/simple_polygons.json", "w") as f:
        json.dump(mappings, f)
