#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            aux = j + 1
            if aux == len(matrix):
                print("{}".format(matrix[i][j]), end="")
            else:
                print("{}".format(matrix[i][j]), end=" ")
        print()
