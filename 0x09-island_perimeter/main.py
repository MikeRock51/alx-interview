#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

    # Test case 2: Island along the border
    grid2 = [
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0]
    ]
    # Expected result: 14
    print(island_perimeter(grid2))

    # Test case 3: Empty grid
    grid3 = []
    # Expected result: 0
    print(island_perimeter(grid3))

    # Test case 4: Grid with water only
    grid4 = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Expected result: 0
    print(island_perimeter(grid4))
