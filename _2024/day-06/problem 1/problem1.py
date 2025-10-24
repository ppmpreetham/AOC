with open("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2024/day-06/problem 1/input.txt", 'r') as file:
    data = file.read()

tokens = [list(line) for line in data.split("\n")]

def find_player(tokens):
    for r, row in enumerate(tokens):
        if "^" in row:
            return (r, row.index('^'))
    return None

def move_up(tokens, playerindex):
    for r in range(playerindex[0], -1, -1):
        if tokens[r][playerindex[1]] == '#':
            break
        tokens[r][playerindex[1]] = 'x'
    tokens[r + 1][playerindex[1]] = '^'

def move_down(tokens, playerindex):
    for r in range(playerindex[0], len(tokens)):
        if tokens[r][playerindex[1]] == '#':
            break
        tokens[r][playerindex[1]] = 'x'
    tokens[r - 1][playerindex[1]] = '^'

def move_left(tokens, playerindex):
    for c in range(playerindex[1], -1, -1):
        if tokens[playerindex[0]][c] == '#':
            break
        tokens[playerindex[0]][c] = 'x'
    tokens[playerindex[0]][c + 1] = '^'

def move_right(tokens, playerindex):
    for c in range(playerindex[1], len(tokens[0])):
        if tokens[playerindex[0]][c] == '#':
            break
        tokens[playerindex[0]][c] = 'x'
    tokens[playerindex[0]][c - 1] = '^'

# Find the position of '^'
playerindex = find_player(tokens)
print(f"Found ^ at row {playerindex[0]}, column {playerindex[1]}")

# Example usage of the functions

for line in tokens:
    print(line)
print("\n")
for i in range(10):
    playerindex = find_player(tokens)  # Update player position
    move_up(tokens, playerindex)
    playerindex = find_player(tokens)  # Update player position
    move_right(tokens, playerindex)
    playerindex = find_player(tokens)  # Update player position
    move_down(tokens, playerindex)
    playerindex = find_player(tokens)  # Update player position
    move_left(tokens, playerindex)

# Print the modified grid
for line in tokens:
    print(line)
    
flattened_tokens = [item for sublist in tokens for item in sublist]
print(flattened_tokens.count('x')+1)