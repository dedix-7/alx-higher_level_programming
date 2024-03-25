#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda innerlist: map(lambda el: el**2), innerlist), matrix))
