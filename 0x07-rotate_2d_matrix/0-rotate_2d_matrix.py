#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(n):
        for j in range(0, n // 2):
            forward = j
            backward = n - 1 - j

            tmp = matrix[i][forward]
            matrix[i][forward] = matrix[i][backward]
            matrix[i][backward] = tmp
            backward

    print(matrix)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]
rotate_2d_matrix(matrix)
rotate_2d_matrix(matrix2)
