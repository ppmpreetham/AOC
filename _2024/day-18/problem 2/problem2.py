with open(r"C:\Users\ppmpr\OneDrive\Documents\GitHub\AOC\_2024\day-18\problem 1\input.txt",'r') as file:
    inps = file.read()
length = 71

mem = ""
no_bytes = 2952

filter_inps = [list(map(int,line.split(','))) for line in inps.rstrip().split("\n")[:no_bytes]]
# print(filter_inps)
for j in range(length):
    for i in range(length):
        if [i,j] in filter_inps:
            mem += '#'
        else:
            mem += '.'
    mem+= '\n'

print(mem)

def create_adjacency_list(grid_str):
    grid = [list(row) for row in grid_str.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    adj_list = {}
    
    # up, right, down, left
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':
                adj_list[(r,c)] = []
                # all 4 directions
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (0 <= new_r < rows and 
                        0 <= new_c < cols and 
                        grid[new_r][new_c] == '.'):
                        adj_list[(r,c)].append((new_r, new_c))
    
    return adj_list

adj_list = create_adjacency_list(mem)
# print("Adjacency List:")
# for node in adj_list:
#     print(f"Node {node}: {adj_list[node]}")

from collections import deque

def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None

while(True):
    path = bfs_path(adj_list, (0,0), (length-1,length-1))

    if path is not None:
        # print("BFS Path:", path)
        print("Path length:", len(path)-1)
        print(no_bytes)
        no_bytes+=1
        
    else:
        print("No path found")
        print(no_bytes)
        break
    
print(inps.split("\n")[2952])