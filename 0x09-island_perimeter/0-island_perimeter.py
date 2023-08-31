#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island defined in grid"""
    gridHeight = len(grid)
    gridWidth = len(grid[0])
    perimeter = 0

    for i in range(1, gridHeight - 1):
        for j in range(1, gridWidth - 1):
            if grid[i][j] == 1:
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter
