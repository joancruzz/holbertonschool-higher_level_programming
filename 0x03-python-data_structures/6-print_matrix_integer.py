#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for idx in list:
            print("{:d}".format(idx), end="")
            if idx != list[-1]:
                print ("".format(), end=" ")
        print()
