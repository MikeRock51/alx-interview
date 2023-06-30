#!/usr/bin/python3
"""Contains the pascal's traingle solution"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    """

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal = [[1], [1, 1]]
    if n == 2:
        return pascal

    for row in range(1, n - 1):
        newRow = [1]
        i = 0
        while i < len(pascal[row]) - 1:
            newRow.append(pascal[row][i] + pascal[row][i + 1])
            i += 1
        newRow.append(1)
        pascal.append(newRow)

    return pascal
