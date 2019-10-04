#!/usr/bin/python3
def all_rows_are_lists(matrix):
    return all([type(row) is list for row in matrix])


def all_rows_has_ints_floats(matrix):
    check = []
    for row in matrix:
        check.append(all([isinstance(n, (int, float)) for n in row]))
    return all(check)


def all_rows_has_same_size(matrix):
    sizes = len(set([len(row) for row in matrix]))
    return True if sizes == 1 else False


def matrix_divided(matrix, div):
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"
    err_div = "div must be a number"
    err_zero = "division by zero"

    if not (type(matrix) is list):
        raise TypeError(err_matrix)
    elif not matrix or not all_rows_are_lists(matrix):
        raise TypeError(err_matrix)
    elif not all_rows_has_ints_floats(matrix):
        raise TypeError(err_matrix)
    elif not all_rows_has_same_size(matrix):
        raise TypeError(err_size)
    elif not isinstance(div, (int, float)):
        raise TypeError(err_div)
    elif div == 0:
        raise ZeroDivisionError(err_zero)
    else:
        return [list(map(lambda x: round(x / div, 2), k)) for k in matrix]
