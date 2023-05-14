#!/usr/bin/python3
"""0-rotate_sd_matrix"""


def rotate_2d_matrix(matrix):
    """rotate an nxn matrix 90 degrees clockwise
    return nothing
    """
    length = len(matrix[0])
    for i in range(length // 2):
        for j in range(i, length - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[length - 1 - j][i]
            matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
            matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
            matrix[j][length - 1 - i] = temp
