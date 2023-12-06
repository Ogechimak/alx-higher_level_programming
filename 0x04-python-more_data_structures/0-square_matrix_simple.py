#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix == []:
        return []
    new = []
    for row in matrix:
        new.append([item**2 for item in row])
    return new
