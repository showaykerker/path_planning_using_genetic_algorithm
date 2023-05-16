import numpy as np
import unittest
from map import Map, Obstacle
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

class TestMap(unittest.TestCase):
    def test_set_obstacle(self):
        m = Map(4, 5, 0.1)
        obstacle_poly = np.array([[1, 1], [1, 2], [2, 2], [2, 1], [1, 1]])
        m.set_obstacle(obstacle_poly)
        print(m.data)
        self.assertEqual(np.sum(m.data), 4)  # Four grid cells should be filled
        
        # Check specific grid cells if they are filled
        self.assertEqual(m.data[10, 10], 1)
        self.assertEqual(m.data[10, 11], 1)
        self.assertEqual(m.data[11, 10], 1)
        self.assertEqual(m.data[11, 11], 1)
        
    def test_obstacle_contains(self):
        obstacle_poly = np.array([[1, 1], [1, 2], [2, 2], [2, 1], [1, 1]])
        obstacle = Obstacle(obstacle_poly)
        
        # Points inside the obstacle
        self.assertTrue(obstacle.contains(1.5, 1.5))
        self.assertTrue(obstacle.contains(1.1, 1.1))
        
        # Points on the boundary of the obstacle
        self.assertTrue(obstacle.contains(1, 1))
        self.assertTrue(obstacle.contains(1, 2))
        self.assertTrue(obstacle.contains(2, 2))
        self.assertTrue(obstacle.contains(2, 1))
        
        # Points outside the obstacle
        self.assertFalse(obstacle.contains(0.5, 1.5))
        self.assertFalse(obstacle.contains(1.5, 2.5))
        self.assertFalse(obstacle.contains(2.5, 1.5))
        self.assertFalse(obstacle.contains(1.5, 0.5))
        
if __name__ == '__main__':
    unittest.main()
