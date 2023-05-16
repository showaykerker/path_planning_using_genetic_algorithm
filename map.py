import numpy as np
from typing import List

<<<<<<< HEAD
=======

class Point:
	def __init__(self, x: float, y: float, mean: np.ndarray= None, extend: int=1):
		if mean is not None:
			self._bound_direction = np.sign([x-mean[0], y-mean[1]])
			# Make it discrete
			if x > mean[0]: x = np.ceil(x) + extend
			if x < mean[0]: x = np.floor(x) - extend
			if y > mean[1]: y = np.ceil(y) + extend
			if y < mean[1]: y = np.floor(y) - extend
		else:
			self._bound_direction = None
		self.x, self.y = x, y

class Line:
	def __init__(self, p1: Point, p2: Point):
		self.points = np.array([
			[p1.x, p1.y],
			[p2.x, p2.y]])

	def matches(self, x, y):
		p1 = Point(*self.points[0])
		p2 = Point(*self.points[1])
		if p1.x - p2.x != 0:
			slope = (p2.y-p1.y) / (p2.x-p1.x)
			b = p1.y - p1.x * slope
			return slope * x + b == y
		else:
			return True

	def on_line_segment(self, p: Point):
		on_line = self.matches(p.x, p.y)
		between_points = \
			(self.points[:, 0].min() <= p.x <= self.points[:, 0].max()) and\
			(self.points[:, 1].min() <= p.y <= self.points[:, 1].max())
		return on_line and between_points

class Obstacle:

	def __init__(self, poly: np.ndarray):
		"""
		Args
			poly: al.;/ n*2 array that represent the point of a convex hull
				each set of element is a set of (x, y) coordinate.
				The order of points should be clock-wised.
				The first point should be repeated as the last.
		"""
		self._center = np.mean(poly, axis=0)
		self._lines = []
		self._n = len(poly)
		self._poly = poly
		self._points = [Point(p[0], p[1], self._center) for p in poly]
		for i, p in enumerate(self._points[:-1]):
			n_p = self._points[i+1]
			self._lines.append(Line(p, n_p))

	def contains(self, px: float, py: float) -> bool:
		point = Point(px, py)
		for line in self._lines:
			if line.on_line_segment(point):
				return True
		vector_directions = self.get_vertexs_to_point_direction_vectors(point)
		# If a point is outside,
		# either 1 of the x or y axis of the vectors will have same direction.
		outside = (np.all(vector_directions[:, 0] == vector_directions[0, 0])) or\
			(np.all(vector_directions[:, 1] == vector_directions[0, 1]))
		return not outside


	def get_vertexs_to_point_direction_vectors(self, p: Point) -> np.ndarray:
		return np.sign(self._poly - np.array([[p.x, p.y]]))



>>>>>>> wip
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
<<<<<<< HEAD
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
		

=======
		obstacle = Obstacle(poly)
		self._obstacle_list.append(obstacle)
		self._fill_map(obstacle)

	def _fill_map(self, obstacle: Obstacle):
		for l in range(self.data.shape[0]):
			for w in range(self.data.shape[1]):
				self.data[l, w] =\
					int(obstacle.contains(l, w)) or self.data[l, w]
>>>>>>> wip



if __name__ == '__main__':
<<<<<<< HEAD
=======
	import sys
	import numpy
	numpy.set_printoptions(threshold=sys.maxsize)
>>>>>>> wip
	m = Map(4, 5, 0.1)
	print(m.data)