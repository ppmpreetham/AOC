import numpy as np

def grid_entropy(grid):
    flat_grid = [char for row in grid for char in row]
    total = len(flat_grid)
    
    star_count = flat_grid.count('*')
    space_count = flat_grid.count(' ')
    
    p_star = star_count / total
    p_space = space_count / total
    
    probabilities = [p for p in [p_star, p_space] if p > 0]
    
    entropy = -sum(p * np.log2(p) for p in probabilities)
    return entropy

# Example usage:
grid = [
    "   *   ",
    "  ***  ",
    " ***** ",
    "*******",
    " ***** ",
    "  ***  ",
    "   *   ",
]


# Call function with the grid
result = grid_entropy(grid)
print(f"Grid Entropy: {result}")
