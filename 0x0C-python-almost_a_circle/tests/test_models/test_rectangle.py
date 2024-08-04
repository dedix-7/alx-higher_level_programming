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
        self.rec44 = Rectangle(4, 4)
        self.rec56 = Rectangle(5, 6)

    def tearDown(self):
        """ dfunctionm to run after each test is execuited
        """

        del self.rec34
        del self.rec44
        del self.rec56

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
        """ Test the instantiation with two arguments
        """
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
        r._Rectangle__x = 7
        self.assertEqual(r.x, 7)

    def test_y_getter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        self.assertEqual(r.y, 4)

    def test_y_setter(self):
        r = Rectangle(4, 5, 5, 4, 1)
        r.y = 7
        self.assertEqual(r.y, 7)

class TestRectangleWidth(unittest.TestCase):
    """this class test for initiaization of rectangle width"""

    def test_None_width(self):
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.4, 3)

    def test_string_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("4", 4)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((complex(4, 9)), 4)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"x": 4, "y": 6}, 6)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 7)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 3), 3)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3, 4}, 5)

    def test_frozen_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 5)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(7), 5)

    def test_infinite_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 5)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 4)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 6)
class TestRectangleHeight(unittest.TestCase):
    """This class represent testing initialization for
        height attribute of the rectangle
    """

    def test_None_height(self):
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 3.4)

    def test_string_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "4")

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, complex(4))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {"x": 4, "y": 6})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [1, 2, 3])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (1, 3))

    def test_set_heigh(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {1, 2, 3, 4})

    def test_frozen_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, frozenset({1, 2, 3}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, range(7))

    def test_infinite_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('inf'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -4)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, 0)


class TestRectangle_x(unittest.TestCase):
    """This class represents unittest for initializing
        x attribute
    """

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, None)

    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, "3", 4)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, complex(4))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, {"x": 4, "y": 6})

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, [1, 2, 3])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 5, (1, 3))

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 6, {1, 2, 3, 4})

    def test_frozen_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 8, frozenset({1, 2, 3}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 7, range(7))

    def test_infinite_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, float('inf'))

    def test_zero_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 4, -6)


class TestRectangle_y(unittest.TestCase):
    """unittests for testing initialization of Rectangle x attribute"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 3, None)

    def test_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 3, "4")

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 5, complex(4))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 5, {"x": 4, "y": 6})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 3, [1, 2, 3])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 5, (1, 3))

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 6, 6, {1, 2, 3, 4})

    def test_frozen_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 8, 8, frozenset({1, 2, 3}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 7, 7, range(7))

    def test_infinite_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 4, float('inf'))

    def test_zero_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 4, 6, -6)


class TestRectangleArea(unittest.TestCase):
    """This unittest tests for area of the rectangle"""

    def test_small_area(self):
        r = Rectangle(12, 3, 0, 0, 7)
        self.assertEqual(r.area(), 36)

    def test_large_area(self):
        r = Rectangle(999999, 999999, 0, 0, 4)
        self.assertEqual(r.area(), 999998000001)

    def test_changed_attribute(self):
        r = Rectangle(4, 7, 2, 2, 6)
        r.width = 8
        r.height = 10
        self.assertEqual(r.area(), 80)

    def test_one_arg(self):
        r = Rectangle(10, 23, 0, 0, 4)
        with self.assertRaises(TypeError):
            r.area(3)
