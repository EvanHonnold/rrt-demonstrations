import numpy as np
import math
from typing import Tuple, Dict, Set

class Tree:

    def __init__(self, root):
        self.root = root

        # This dictionary serves to keep track of the nodes as well.
        # Internally, this class ensures that if a node is in the tree,
        # it will be a key in the dict.
        self.children:Dict[List] = {root: list()}
    
    def __iter__(self):
        return iter(self.children.keys())

    def add(self, new_node, parent)->None:
        assert parent in self.children
        assert new_node not in self.children
        assert new_node not in self.children[parent]

        self.children[parent].append(new_node)
        self.children[new_node] = list()

    def nearest_neighbor(self, point:Tuple)->Tuple:

        def dist(a,b):
            return np.linalg.norm(np.array(a) - np.array(b))

        closest_neighbor = self.root
        closest_neighbor_dist = dist(point, closest_neighbor)
        
        for possible_neighbor in self:
            distance = dist(point, possible_neighbor)
            if distance < closest_neighbor_dist:
                closest_neighbor = possible_neighbor
                closest_neighbor_dist = distance

        return closest_neighbor