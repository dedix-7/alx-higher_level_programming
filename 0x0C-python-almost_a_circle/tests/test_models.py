#!/usr/bin/python3
import unittest
import sys
from models.base import Base

""" import the unittest module for use in tests
    also import the base module for the base class
"""

class TestMethods(unittest.TestCase, Base):
    """ The class to use for testing
    """

    def test_base(self):
        """ A function to test the base class
        """

        self.assertEqual(Base.nb_objects, 0)
        obj = Base(56)
        self.assertEqual(obj.nb_objects, 1)
        self.assertEqual(obj.id, 56)
        obj2 = Base()
        self.assertEqual(obj.nb_objects, 2)
        self.assertEqual(obj2.id, None)

    def test_rects(self):
        """ Test the rectangle class
        """


if __name__ == "__main__":
    unittest.main()
