import os
from shapely.geometry import Polygon
from matplotlib import pyplot

def clear_output_dir()->None:
    files = os.listdir("output")
    for f in files:
        if f.endswith(".png") or f.endswith(".pdf"):
            os.remove(os.path.join("output", f))

def plot_polygon(p: Polygon)->None:
    x, y = p.exterior.xy
    pyplot.plot(x, y)

def save_current_figure()->None:
    extension = ".pdf"
    other_file_count = len([name for name in os.listdir('output') if os.path.isfile(name)])
    pyplot.savefig(f'output/figure_{other_file_count}{extension}')