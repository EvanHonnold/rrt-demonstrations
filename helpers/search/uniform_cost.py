
from helpers.search.easy_priority_queue import EasyPriorityQueue
import math

from typing import List, Tuple, Set, Dict

class SearchGraphEdge:
    def __init__(self, end_node, weight: float):
        self.end_node = end_node
        self.weight:float = weight

def construct_path(start, goal, parents:Dict):
    assert isinstance(parents, dict)
    path = [goal]
    current = goal
    while current != start:
        current = parents[current]
        if current in path:
            raise Exception("Found a loop:", current, "already in path", path)
        assert current not in path # checking for loops
        path.append(current)
    path.reverse()
    return path

def uniform_cost_search(start, goal, successors)->List:
    """ successors: a function that takes a node and returns 
        a SearchGraphEdge for each neighbor. 
        
        Source: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Practical_optimizations_and_infinite_graphs """
    
    queue = EasyPriorityQueue()
    explored:Set = set()
    cost:Dict = dict()  # NOTE: this is technically unnecessary, but used here for the sanity check assert
    parents:Dict = dict()

    queue.push(start, priority=0)
    cost[start] = 0

    while len(queue) > 0:
        
        current_node = queue.pop()
        explored.add(current_node)

        if current_node == goal:
            return construct_path(start, goal, parents)

        for edge in successors(current_node):
            assert isinstance(edge, SearchGraphEdge)

            if edge.end_node not in explored:

                cost_from_current = cost[current_node] + edge.weight
                
                # sanity-check: uniform cost search should not discover shortcuts,
                # since those paths should have been expanded first:
                if edge.end_node in cost.keys():
                    assert cost[edge.end_node] > cost_from_current
                else:
                    cost[edge.end_node] = cost_from_current 
                    parents[edge.end_node] = current_node
                    queue.push(edge.end_node, priority=cost_from_current)

    return []
    
    