#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island defined in grid"""
    gridHeight = len(grid)
    assert (gridHeight > 0)
    gridWidth = len(grid[0])
    perimeter = 0

    assert 1 <= len(grid) <= 100, "Number of rows is out of range"
    assert all(1 <= len(row) <=
               100 for row in grid), "Number of columns is out of range"

    for i in range(1, gridHeight - 1):
        for j in range(1, gridWidth - 1):
            assert grid[i][j] in (
                0, 1), f"Invalid cell value at row {i}, col {j}"
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
