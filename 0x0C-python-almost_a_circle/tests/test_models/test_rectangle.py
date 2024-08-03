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
    def test_Noneid(self):
        """ test the super call works when assigning ids
        """

        pass
