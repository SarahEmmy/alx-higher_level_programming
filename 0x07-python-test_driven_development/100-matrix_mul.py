#!/usr/bin/python3
"""
    Module containing matrix multiplication.
"""

def matrix_mul(m_x, m_y):
    """ Multiplies two matrices. Validation of matrices must be done in the
        stated order.

    Args:
        m_x (:obj:`list' of :obj:`list` of int or float): List of lists of
            integers or floats.
        m_y (:obj:`list` of :obj:`list` of int or float): List of lists of
            integers or floats.

    Returns:
        :obj:`list` of :obj:`list` of int or float: Product of two matrices.
    """

    if type(m_x) != list:
        raise TypeError("m_x must be a list")
    if type(m_y)!= list:
        raise TypeError("m_y must be a list")

    x_col_len = 0
    x_row_len = None
    x_matrix = True
    x_i_or_f = True
    x_rect = True
    for row in m_x:
        if type(row) != list:
            x_matrix = False
            break
        for x in row:
            if type(x) != int and type(x) != float:
                x_i_or_f = False
        if x_row_len != None:
            if x_row_len != len(row):
                x_rect = False
        else:
            x_row_len = len(row)
        x_col_len += 1

    y_col_len = 0
    y_row_len = None
    y_matrix = True
    y_i_or_f = True
    y_rect = True
    for row in m_y:
        if type(row) != list:
            y_matrix = False
            break
        for x in row:
            if type(x) != int and type(x) != float:
                y_i_or_f = False
        if y_row_len != None:
            if y_row_len != len(row):
                y_rect = False
        else:
            y_row_len = len(row)
        y_col_len += 1

    if not x_matrix:
        raise TypeError("m_x must be a list of lists")

    if not y_matrix:
        raise TypeError("m_y must be a list of lists")

    if x_col_len == 0 or (x_row_len == 0 and x_rect):
        raise ValueError("m_x can't be empty")

    if y_col_len == 0 or (y_row_len == 0 and y_rect):
        raise ValueError("m_y can't be empty")

    if not x_i_or_f:
        raise TypeError("m_x should contain only integers or floats")

    if not y_i_or_f:
        raise TypeError("m_y should contain only integers or floats")

    if not x_rect:
        raise TypeError("each row of m_x must should be of the same size")

    if not y_rect:
        raise TypeError("each row of m_y must should be of the same size")

    if x_row_len != y_col_len:
        raise ValueError("m_x and m_y can't be multiplied")

    new_matrix = []
    for x_cdx in range(x_col_len):
        new_row = []
        for rdx in range(y_row_len):
            total = 0
            for cdx in range(y_col_len):
                total += m_y[cdx][rdx] * m_x[x_cdx][cdx]
            new_row.append(total)
        new_matrix.append(new_row)

    return new_matrix
