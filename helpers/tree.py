import numpy as np
import math
from typing import Tuple, Dict, Set, List
from helpers.search.uniform_cost import uniform_cost_search, SearchGraphEdge

class Tree:

    def __init__(self, root):
        self.root = root

        # This dictionary serves to keep track of the nodes as well.
        # Internally, this class ensures that if a node is in the tree,
        # it will be a key in the dict (even if it is a leaf node).
        self.children:Dict[List] = {root: list()}

        # Second lookup table to expedite computation of cost from goal:
        self.parents:Dict = dict()
    
    def __iter__(self):
        return iter(self.children.keys())

    def dist(self, a,b):
        """ Temporary distance function. TODO: allow constructor to supply others """
        return np.linalg.norm(np.array(a) - np.array(b))

    def add(self, new_node, parent)->None:
        assert parent in self.children.keys()
        assert new_node not in self.children.keys()
        assert new_node not in self.children[parent]

        self.children[parent].append(new_node)
        self.children[new_node] = list()
        self.parents[new_node] = parent

    def change_parent(self, node, new_parent)->None:
        old_parent = self.parents[node]
        self.children[old_parent].remove(node)
        self.parents[node] = new_parent
        self.children[new_parent].append(node)

    def nearest_neighbor(self, point:Tuple)->Tuple:

        closest_neighbor = self.root
        closest_neighbor_dist = self.dist(point, closest_neighbor)
        
        for possible_neighbor in self:
            distance = self.dist(point, possible_neighbor)
            if distance < closest_neighbor_dist:
                closest_neighbor = possible_neighbor
                closest_neighbor_dist = distance

        return closest_neighbor

    def nearest_neighbor_list(self, point, num_neighbors:int)->List:

        distance_node_pairs = [(self.dist(node, point), node) for node in self]

        # order by increasing distance
        distance_node_pairs.sort(key=lambda pair: pair[0]) 
        sorted_neighbors = [neighbor for _, neighbor in distance_node_pairs]

        # special case: few nodes in the tree
        if len(sorted_neighbors) <= num_neighbors:
            return sorted_neighbors

        closest_neighbors = sorted_neighbors[:num_neighbors]

        # exclude the point used for the query:
        if closest_neighbors[0] == point:
            closest_neighbors.append(sorted_neighbors[num_neighbors])

        return closest_neighbors

    def shortest_path_from_root(self, point: Tuple)->List[Tuple]:
        """ Uses Djikstra's algorithm to find the shortest path
            from the root to the given point."""
        
        goal = self.nearest_neighbor(point)
        start = self.root

        def successors(node):
            s = []
            for child in self.children[node]:
                edge = SearchGraphEdge(child, weight=self.dist(node, child))
                s.append(edge)
            return s

        return uniform_cost_search(start, goal, successors)
        
    def shortest_path_to_root_cost(self, point: Tuple)->float:
        current = point
        cost = 0
        while current != self.root:
            parent = self.parents[current]
            cost += self.dist(current, parent)
            current = parent
        return cost

    def validate(self):
        """ For testing purposes """ 
        for node, children in self.children.items():
            for child in children:
                assert self.parents[child] == node

        for node, parent in self.parents.items():
            assert node in self.children[parent]