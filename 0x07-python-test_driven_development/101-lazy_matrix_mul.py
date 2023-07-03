#!/usr/bin/python3
"""
    Module containing ``lazy_matrix_mul`` function
"""
import numpy as np


def lazy_matrix_mul(m_x, m_y):
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

    return np.matmul(m_x, m_y)
