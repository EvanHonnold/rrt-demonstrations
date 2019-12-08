#!/usr/bin/env python3

import numpy as np
from shapely.geometry import LineString, Polygon
import random

from helpers.drawing import clear_output_dir, save_current_figure, draw_environment, draw_tree, draw_path
from helpers.serialization import deserialize_environment, Environment
from helpers.geometry import random_point_in_polygon, path_length
from helpers.tree import Tree

from typing import List, Dict, Tuple



def drive_from(from_point, target_point)->LineString:
    """ Local planner. Start at `from_point` and drive a fixed distance towards the target. 
        Returns the path driven. """

    MAX_DRIVE_DISTANCE = 1

    from_point = np.array(from_point)
    target_point = np.array(target_point)

    full_vector_between_points = target_point - from_point
    full_distance = np.linalg.norm(full_vector_between_points)

    unit_vector = full_vector_between_points/full_distance

    driving_vector = unit_vector * min(full_distance, MAX_DRIVE_DISTANCE)
    
    point_reached = from_point + driving_vector

    return LineString([tuple(from_point), tuple(point_reached)])
    

def collides_with_obstacles(path: LineString, obstacles: List[Polygon])->bool:
    for obstacle in obstacles:
        if path.intersects(obstacle):
            return True
    return False

def close_enough_to_goal(point, goal)->bool:
    return np.linalg.norm(np.array(point) - np.array(goal)) < 0.33

def euclidean_distance(a, b):
    """ Temporary distance function. TODO: allow constructor to supply others """
    return np.linalg.norm(np.array(a) - np.array(b))

random.seed(7)
env = deserialize_environment()

tree = Tree(root=(0, 0))
cost_from_goal:Dict = dict({(0, 0): 0})

for i in range(6000):

    sample = random_point_in_polygon(env.bounds)
    closest_node_on_tree = tree.nearest_neighbor(sample)
    driving_path = drive_from(closest_node_on_tree, sample)
    
    if not collides_with_obstacles(driving_path, env.obstacles):
        new_node = driving_path.coords[-1]

        # RRT-star "re-wiring" step:
        

        tree.add(new_node, parent=closest_node_on_tree)
        cost_from_goal[new_node] = cost_from_goal[closest_node_on_tree] 

        if close_enough_to_goal(new_node, env.goal):
            print(f"Reached the goal! {i} samples required.")
            break
    

path = tree.shortest_path_from_root(env.goal)
print(path_length(path, distance_function=euclidean_distance))
print("Neighbors:", tree.nearest_neighbor_list((10, 4.1), 4))

# draw_tree(tree)
# draw_path(path)
# draw_environment(deserialize_environment())
# save_current_figure()


