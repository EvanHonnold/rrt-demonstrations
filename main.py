#!/usr/bin/env python3

from shapely.geometry import Polygon
from matplotlib import pyplot

from helpers.drawing import clear_output_dir, save_current_figure, draw_environment

from helpers.serialization import deserialize_environment

clear_output_dir()
draw_environment(deserialize_environment())
save_current_figure()
