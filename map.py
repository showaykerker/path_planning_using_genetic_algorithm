import numpy as np
from typing import List

class Map:
	def __init__(self, length: float, width: float, resolution: float):
		"""
		Args
			length: in meter
			width: in meter
			resolution: in meter, the edge length for rectangle grid.
		"""
		self._length = length
		self._width = width
		self._resolution = resolution
		self._obstacle_list = []
		self._init_map()

	def _init_map(self):
		grid_amount_length = int(np.ceil(self._length / self._resolution))
		grid_amount_width = int(np.ceil(self._width / self._resolution))
		self._grid_number = grid_amount_length * grid_amount_width
		self.data = np.zeros((grid_amount_length, grid_amount_width))

	def set_obstacle(self, poly:np.ndarray) -> None:
		"""
		Args
			poly: a n*2 array that represent the point of a convex hull
				each set of element is a set of (x, y) coordinate.
				The order of points should be clock-wised.
				The first point should be repeated as the last.
		"""
		self._obstacle_list.append(Obstacle(poly))


class Obstacle:
	def __init__(self, poly: np.ndarray):
		"""
		Args
			poly: a n*2 array that represent the point of a convex hull
				each set of element is a set of (x, y) coordinate.
				The order of points should be clock-wised.
				The first point should be repeated as the last.
		"""
		self._lines = []
		self._poly = poly
		for i, p in enumerate(poly[:-1]):
			n_p = poly[i+1]
			slope = (n_p[1] - p[1]) / (n_p[0] - p[0])
			b = p[1] - p[0] * slope
			self._lines.append(lambda x: slope * x + b)

	def is_inside(self, px, py):
		




if __name__ == '__main__':
	m = Map(4, 5, 0.1)
	print(m.data)