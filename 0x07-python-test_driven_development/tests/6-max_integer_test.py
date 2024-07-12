#!/usr/bin/python3
import unittest
""" This is a modeule to test the function to find the max integer in a list of ints
"""


max_integer = __import__('6-max_integer').max_integer
class Testmaxint(unittest.TestCase):
    """ The class for the unit tests
    """

    def test_maximum(self):
        """ Test the maximum values for various lists
        """

        self.assertEqual(max_integer([4, 5, 6, 7, 8]), 8)
        self.assertEqual(max_integer([-4, -6, -8, 9, 87]), 87)
        self.assertEqual(max_integer([-5, -6, -7, 0]), 0)
        self.assertEqual(max_integer([98]), 98)
        self.assertEqual(max_integer([87, 85, 76]), 87)
        self.assertEqual(max_integer([-3, -2, -4, -1]), -1)
        self.assertEqual(max_integer([-3.4, 5, -5.6]), 5)
        self.assertEqual(max_integer([]), None)
        # Now the raises check

        with self.assertRaises(TypeError):
            max_integer(['list', 'of'])
            max_integer(34, 56, 78)
            max_integer({56: 'dict'})
            max_integer((56, 78, 89))
            max_integer(['56', 667, 'string', 'mixed', 'with'])
            max_integer()
            max_integer([67, 89, 87], [76, 87, 54])
            max_integer('string1')
