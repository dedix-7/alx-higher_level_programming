#!/usr/bin/python3
""" A repetition of the matrix multiplication function
"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """ This function uses the numpy module to multip[ly 2 matrices
    """


    one = numpy.array(m_a)
    two = numpy.array(m_b)
    return (numpy.dot(one, two))
