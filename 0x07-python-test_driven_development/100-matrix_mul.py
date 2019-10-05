#!/usr/bin/python3
def all_rows_are_lists(matrix):
    """Check if all elements in a list are lists"""
    return all([type(row) is list for row in matrix])


def all_rows_has_ints_floats(matrix):
    """Check if rows are only filled with ints or floats"""
    check = []
    for row in matrix:
        check.append(all([isinstance(n, (int, float)) for n in row]))
    return all(check)


def all_rows_has_same_size(matrix):
    """Checks if all the lists are the same size"""
    sizes = len(set([len(row) for row in matrix]))
    return True if sizes == 1 else False


def get_dim(matrix):
    """Get the dimension of the matrix"""
    if all_rows_has_same_size(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        return rows, cols
    else:
        return 0, 0


def can_multiplicate(m_a, m_b):
    """Checks if we can multiplicate the matrices"""
    te_list_ma = "m_a must be a list"
    te_list_mb = "m_b must be a list"
    te_listli_ma = "m_a must be a list of lists"
    te_listli_mb = "m_b must be a list of lists"
    ve_empty_ma = "m_a can't be empty"
    ve_empty_mb = "m_b can't be empty"
    te_intf_ma = "m_a should contain only integers or floats"
    te_intf_mb = "m_b should contain only integers or floats"
    te_size_ma = "each row of m_a must be of the same size"
    te_size_mb = "each row of m_b must be of the same size"
    ve_cantmul = "m_a and m_b can't be multiplied"

    if not (type(m_a) is list):
        raise TypeError(te_list_ma)
    elif not (type(m_b) is list):
        raise TypeError(te_list_mb)
    elif not all_rows_are_lists(m_a):
        raise TypeError(te_listli_ma)
    elif not all_rows_are_lists(m_b):
        raise TypeError(te_listli_mb)
    elif not m_a:
        raise ValueError(ve_empty_ma)
    elif not m_b:
        raise ValueError(ve_empty_mb)
    elif not m_a[0]:
        raise ValueError(ve_empty_ma)
    elif not m_b[0]:
        raise ValueError(ve_empty_mb)
    elif not all_rows_has_ints_floats(m_a):
        raise TypeError(te_intf_ma)
    elif not all_rows_has_ints_floats(m_b):
        raise TypeError(te_intf_mb)
    elif not all_rows_has_same_size(m_a):
        raise TypeError(te_size_ma)
    elif not all_rows_has_same_size(m_b):
        raise TypeError(te_size_mb)
    elif ((get_dim(m_a)[1] != get_dim(m_b)[0])
            or (get_dim(m_a)[0] == 0)):
        raise ValueError(ve_cantmul)
    else:
        return True


def zero_matrix(rows, cols):
    answer = []
    for i in range(rows):
        answer.append([0 for x in range(cols)])
    return answer


def dot_product(la, lb):
    return sum([la[n] * lb[n] for n in range(len(la))])


def matrix_mul(m_a, m_b):
    """Matrix multiplication"""
    if can_multiplicate(m_a, m_b):
        ans = zero_matrix(get_dim(m_a)[0], get_dim(m_b)[1])
        for i in range(get_dim(m_a)[0]):
            for j in range(get_dim(m_b)[1]):
                row = m_a[i]
                col = [x[j] for x in m_b]
                ans[i][j] = dot_product(row, col)
        return ans
