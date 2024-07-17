#!/usr/bin/python3
""" A script to multiply two matrices
It also checks the matrices can actually be multiplied
"""


def matrix_mul(m_a, m_b):
    """ A function to multiply two matrices
        Args: m_a is matrix 1
               m_b is matrix 2
         Raises: Type errior for non matrices and elements not ints or floats
         ValueError for empty matyrices
    """

    if (type(m_a) is not list):
        raise TypeError('m_a must be a list')
    if (type(m_b) is not list):
        raise TypeError('m_b must be a list')
    if not (all(isinstance(x, list) for x in m_a)):
        raise TypeError('m_a must be a list of lists')
    if not (all(isinstance(x, list) for x in m_b)):
        raise TypeError('m_b must be a list of lists')
    if (len(m_a) == 0):
        raise ValueError("m_a can't be empty")
    for i in m_a:
        if not (all(isinstance(c, int
