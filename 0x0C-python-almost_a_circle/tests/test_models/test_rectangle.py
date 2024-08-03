#!/usr/bin/python
""" A module to test the Rectangle class
"""

from models.base import Base
from models.rectangle import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
    """ A class to test the rectangle tests
    it checks for each building block that was added
    """

    def setUp(self):
        """ make this objects before running each test
        """

        self.rec34 = Rectangle(3, 4)
        self.rec00 = Rectangle(0, 0)
        self.rec44 = Rectangle(4, 4)
        self.rec56 = Rectangle(5, 6)

    def tearDown(self):
        """ dfunctionm to run after each test is execuited
        """

        del(self.rec34)
        del(self.rec00)
        del(self.rec44)
        del(self.rec56)

    def test_ionit(self):
        """ testing the constructor works as expected
        """

        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(9)

    def test_instance(self):
        """ test if the objects are instances of the Base class
        """

        self.assertIsInstance(self.rec56, Base)

        def test_two_args(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 3)
        r2 = Rectangle(3, 3, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(Rectangle(10, 3, 0, 0, 12).id, 12)

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 3).__width)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 3).__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 3).__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 0, 0, 3).__y)

    def test_width_getter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        self.assertEqual(r.width, 4)

    def test_width_setter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        r.width = 7
        self.assertEqual(r.width, 7)

    def test_height_getter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        self.assertEqual(r.height, 5)

    def test_height_setter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        r.height = 7
        self.assertEqual(r.height, 7)

    def test_x_getter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        self.assertEqual(r.x, 5)

    def test_x_setter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        r.x = 7
        self.assertEqual(r.x, 7)

    def test_y_getter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        self.assertEqual(r.y, 4)

    def test_y_setter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        r.y = 7
        self.assertEqual(r.y, 7)
