#!/usr/bin/python3

"""Island perimeter code"""

def island_perimeter(grid):
"""calculates perimeter of island described in grid
Arguments:
grid (int) : list of lists
Return: perimeter of island
"""
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 to the perimeter

                # Check adjacent cells to subtract shared edges
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for each shared edge between adjacent land cells
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for each shared edge between adjacent land cells

    return perimeter

