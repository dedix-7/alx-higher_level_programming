#!/usr/bin/python3
""" A module to divide a matrixxx
"""


def matrix_divided(matrix, div):
    """ A function to divide a lists of lists with a div
    div must be above zero,
    Args:
         div must be zero
         matrix: must be a lists of lists of integers or floats
    """

    tre = "matrix must be a matrix (list of lists) of integers/floats"
    if (type(matrix) is not list):
        raise TypeError(tre)
    mess = "matrix must be a matrix (list of lists) of integers/floats"
    if (type(div) not in [int, float]):
        raise TypeError('div must be a number')
    for i in range(len(matrix)):
        if (type(matrix[i]) is not list):
            raise TypeError(mess)
        for j in (matrix[i]):
            if (type(j) not in [int, float]):
                raise TypeError(mess)
        size = len(matrix[0])
        if (len(matrix[i]) != size):
            raise TypeError('Each row of the matrix must have the same size')
    treys = [[round((j / div), 2) for j in x] for x in matrix]
    return (treys)
