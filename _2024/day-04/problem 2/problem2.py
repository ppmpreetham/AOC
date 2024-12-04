import numpy as np

def diagonals(grid):
    pattern_count = 0
    rows, cols = grid.shape
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            if grid[y, x] == 'A':
                top_left = grid[y - 1, x - 1] + grid[y + 1, x + 1]
                top_right = grid[y - 1, x + 1] + grid[y + 1, x - 1]
                if all(pair in ("MS", "SM") for pair in [top_left, top_right]):
                    pattern_count += 1
    return pattern_count

with open("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2024/day-04/problem 2/input.txt") as sample:
    grid = [list(line) for line in sample.read().splitlines()]

print(diagonals(np.array([list(row) for row in grid])))