"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
import math
from circle import Circle


class CircleTest(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(3)
        self.c2 = Circle(4)
        self.c3 = Circle(5)

    def test_add_area_with_typical_values(self):
        """test for add_area method by creating new circle from existing circle"""
        new_circle = self.c1.add_area(self.c2)
        self.assertEqual(new_circle.get_radius(), self.c3.get_radius())
        new_area = math.pi * (new_circle.get_radius()**2)
        self.assertEqual(new_circle.get_area(), new_area)

    def test_add_area_edge_case(self):
        """test for add area method where some circle has radius 0"""
        # create new circle that radius is 0
        cZero = Circle(0)
        new_circle = self.c1.add_area(cZero)
        self.assertEqual(new_circle.get_radius(), self.c1.get_radius())
        new_area = math.pi * (new_circle.get_radius() ** 2)
        self.assertEqual(new_circle.get_area(), new_area)

    def test_create_circle_with_negative_radius(self):
        """test for circle constructor with negative radius"""
        with self.assertRaises(ValueError):
            c_temp1 = Circle(-1)
        with self.assertRaises(ValueError):
            c_temp2 = Circle(-100)
