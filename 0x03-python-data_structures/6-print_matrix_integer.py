#!/usr/bin/python3
# a module to print a matrix of matrices

def print_matrix_integer(matrix=[[]]):
    if (matrix):
        for i in range(len(matrix)):
            size = len(matrix[i])
            for j in range(size):
                if (j != size - 1):
                    endchar = " "
                else:
                    endchar = ""
                print("{:d}".format(matrix[i][j]), end=endchar)
