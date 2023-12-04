#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = 0
        for content in row:
            print("{:d}".format(content), end="")
            count += 1
            if count != len(row):
                print(end=" ")
        print("")
