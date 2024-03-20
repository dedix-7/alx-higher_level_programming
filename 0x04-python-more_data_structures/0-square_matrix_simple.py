#!/usr/bin/python3
# A script to create a list from another lists
# It creates a list of squaring elems of another list

def square_matrix_simple(matrix=[]):
    return ([[r**2 for r in i] for i in matrix])
