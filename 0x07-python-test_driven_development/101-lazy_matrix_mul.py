#!/usr/bin/python3
""" A repetition of the matrix multiplication function
"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """ This function uses the numpy module to multip[ly 2 matrices
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
    if (len(m_a) == 1):
        if (len(m_a[0]) == 0):
            raise ValueError("m_a can't be empty")
    for i in m_a:
        if (len(i) != len(m_a[0])):
            raise TypeError('each row of m_a must be of the same size')
        if not (all(isinstance(d, (int, float)) for d in i)):
            raise TypeError("m_a should contain only integers or floats")
    if (len(m_b) == 0):
        raise ValueError("m_b can't be empty")
    if (len(m_b) == 1):
        if (len(m_b[0]) == 0):
            raise ValueError("m_b can't be empty")

    one = numpy.array(m_a)
    two = numpy.array(m_b)
    return (numpy.dot(one, two))
