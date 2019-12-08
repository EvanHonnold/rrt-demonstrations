import os
from shapely.geometry import Polygon
from matplotlib import pyplot, patches
from matplotlib.collections import PatchCollection
from typing import List
import numpy as np
from helpers.serialization import Environment
from helpers.tree import Tree

def clear_output_dir()->None:
    files = os.listdir("output")
    for f in files:
        if f.endswith(".png") or f.endswith(".pdf"):
            os.remove(os.path.join("output", f))

def plot_polygons(polygons: List[Polygon])->None:  
    polygon_patches = [patches.Polygon(np.array(p.exterior.xy).transpose()) for p in polygons] 
    collection = PatchCollection(polygon_patches)
    collection.set_color([63/255,81/255,181/255]) # indigo 500 (https://www.materialui.co/colors)
    pyplot.gca().add_collection(collection)

def plot_circle(center, radius=0.25, color="green"):
    pyplot.gca().add_artist(pyplot.Circle(center, radius=radius, color=color))

def save_current_figure()->None:

    # make sure axes are scaled so that everything is visible:
    pyplot.gca().autoscale()
    pyplot.gca().axis('equal')

    extension = ".pdf"
    other_file_count = len([name for name in os.listdir('./output/')])
    pyplot.savefig(f'output/figure_{other_file_count}{extension}')

def draw_environment(e: Environment)->None:

    plot_circle([0, 0]) # start
    plot_circle(e.goal)
    plot_polygons(e.obstacles)

def draw_tree(tree: Tree)->None:

    for node in tree:
        x1, y1 = node
        for child in tree.children[node]:
            x2, y2 = child
            pyplot.plot([x1, x2], [y1, y2], color="black")
            plot_circle(child, radius=0.05, color="black")
            
def draw_path(path: List)->None:

    x_vals = [x for x, _ in path]
    y_vals = [y for _, y in path]
    pyplot.plot(x_vals, y_vals, color="green")
