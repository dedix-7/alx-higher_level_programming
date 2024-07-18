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
    for i in m_b:
        if (len(i) != len(m_b[0])):
            raise TypeError('each row of m_b must be of the same size')
        if not (all(isinstance(d, (int, float)) for d in i)):
            raise TypeError("m_b should contain only integers or floats")
    if (len(m_a[0]) != (len(m_b))):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        res = []
        for j in range(len(m_b[0])):
            star = 0
            for k in range(len(m_b)):
                star += m_a[i][k] * m_b[k][j]
            res.append(star)
        result.append(res)
    return (result)
