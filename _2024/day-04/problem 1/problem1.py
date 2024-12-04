def find_word(grid, y, x, word):
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    found = 0
    for dy, dx in directions:
        cur = ""
        for i in range(len(word)):
            ny, nx = y + i * dy, x + i * dx
            if ny not in range(len(grid)) or nx not in range(len(grid[0])):
                break
            cur += grid[ny][nx]
        if cur == word:
            found += 1
    return found

with open("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2024/day-04/problem 1/input.txt") as sample:
    grid = [list(line.strip()) for line in sample.readlines()]

print(sum(find_word(grid, y, x, "XMAS") for y in range(len(grid)) for x in range(len(grid[0]))))