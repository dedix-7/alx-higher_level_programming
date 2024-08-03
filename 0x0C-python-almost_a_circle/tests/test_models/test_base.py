#!/usr/bin/python3
""" A module to test the base module and class
"""
import unittest
from models.base import Base


class TestbaseClass(unittest.TestCase):
    """ The class to test the base class
    """

    def setUp(self):
        """make objects of the base class to be used for all the tests
        in this class
        """

        self.base1 = Base()
        self.baseid = Base(9)
        self.base3 = Base(None)
        self.basef = Base(7.8)
        self.bases = Base('string')
        self.based = Base({'key':'value','key2':'value'})
        self.baseb = Base(True)
        self.basecom = Base(complex(6, 7))


    def tearDyown(self):
        """Destroy the objects of the Base class after the tests
        """
        pass

    def test_objectnumb(self):
        """ test to see the object numbers are updating as needed
        """

        self.assertEqual(self.baseid.id, 9)
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base3.id, self.base3._Base__nb_objects)
        self.assertEqual(self.basef.id, 7.8)
        self.assertEqual(self.bases.id, 'string')
        self.assertEqual(self.based.id, {'key':'value','key2':'value'})
        self.assertEqual(self.baseb.id, True)
        self.assertEqual(self.basecom.id, complex(6,7))
