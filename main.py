#!/usr/bin/env python3

import numpy as np

from helpers.drawing import clear_output_dir, save_current_figure, draw_environment, draw_tree
from helpers.serialization import deserialize_environment, Environment
from helpers.geometry import random_point_in_polygon
from helpers.tree import Tree

from typing import List, Dict, Tuple



def drive_from(from_point, target_point)->Tuple:
    """ Local planner. Start at `from_point` and drive a fixed distance towards the target. 
        Returns the location where we stop. """

    MAX_DRIVE_DISTANCE = 1

    from_point = np.array(from_point)
    target_point = np.array(target_point)

    full_vector_between_points = target_point - from_point
    full_distance = np.linalg.norm(full_vector_between_points)

    unit_vector = full_vector_between_points/full_distance

    driving_vector = unit_vector * min(full_distance, MAX_DRIVE_DISTANCE)

    return tuple(from_point + driving_vector)
    
def close_enough_to_goal(point, goal)->bool:
    return np.linalg.norm(np.array(point) - np.array(goal)) < 0.33



env = deserialize_environment()

tree = Tree(root=(0, 0))

for i in range(5000):

    sample = random_point_in_polygon(env.bounds)

    closest_node_on_tree = tree.nearest_neighbor(sample)

    new_node = drive_from(closest_node_on_tree, sample)
    tree.add(new_node, parent=closest_node_on_tree)

    if close_enough_to_goal(new_node, env.goal):
        print(f"Reached the goal! {i} samples required.")
        break
    

draw_tree(tree)
draw_environment(deserialize_environment())
save_current_figure()
 

