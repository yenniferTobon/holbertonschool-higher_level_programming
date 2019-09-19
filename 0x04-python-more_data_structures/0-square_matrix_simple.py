#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    lenMatrix = len(matrix)
    new_matrix = []
    new_row = []
    for i in range(lenMatrix):
        for j in range(lenMatrix):
            new_row.append(matrix[i][j] * matrix[i][j])
    new_matrix.append(new_row)
    return (new_matrix)
    # for row in matrix:
    #     new_matrix = map(lambda x: x * x, l)
