#!/usr/bin/python3
# a module to print a matrix of matrices

def print_matrix_integer(matrix=[[]]):
    if (matrix):
        for row in matrix:
            size = len(matrix[row])
            i = 0
            for col in row:
                print("{:d}".format(col))
                i += 1
                if (i < (size - 1)):
                    print(" ")
            print()
