#!/usr/bin/python3
def matrix_divided(matrix, div):
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    for leN in matrix:
        lenRow = len(leN)

    new_matrix = []
    for row in matrix:
        if len(row) is not lenRow:
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) is not list:
            raise TypeError(msg)
        new_row = []
        for column in row:
            if type(column) is not int and type(column) is not float:
                raise TypeError(msg)
            new_row.append(round(column/div, 2))
        new_matrix.append(new_row)
    return new_matrix
