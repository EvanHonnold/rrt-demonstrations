#!/usr/bin/env python3

from shapely.geometry import Polygon
from matplotlib import pyplot

from helpers.drawing import clear_output_dir, save_current_figure, plot_polygon

clear_output_dir()

p = Polygon([(1, 1), (3, 1), (2, 2), (1, 2)])
plot_polygon(p)
save_current_figure()
