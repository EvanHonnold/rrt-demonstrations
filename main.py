#!/usr/bin/env python3

from shapely.geometry import Polygon
from matplotlib import pyplot
import numpy as np

from helpers.drawing import clear_output_dir, save_current_figure, draw_environment
from helpers.serialization import deserialize_environment

from typing import List

graph:List = [np.array([0, 0])]


print(np.array([0, 0]).shape)

env = deserialize_environment()

clear_output_dir()
draw_environment(deserialize_environment())
save_current_figure()
