data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# with open("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2024/day-05/problem 1/input.txt", 'r') as file:
#     data = file.read()

mapp = data.split("\n\n")[0]
nums = data.split("\n\n")[1]

maplst = [list(map(int, mapk.split("|"))) for mapk in mapp.split("\n")]
numlst = [list(map(int, filter(None, num.split(",")))) for num in nums.split("\n")]

mapmap = {}
for line in maplst:
    if line[0] not in mapmap:
        mapmap[line[0]] = []
    mapmap[line[0]].append(line[1])
# print(mapmap)

nodes = sorted(set(mapmap.keys()).union(set(dest for dests in mapmap.values() for dest in dests)))
adj_matrix = [[0] * len(nodes) for _ in range(len(nodes))]

node_index = {node: idx for idx, node in enumerate(nodes)}

for src in mapmap:
    for dest in mapmap[src]:
        adj_matrix[node_index[src]][node_index[dest]] = 1

print("Nodes:", nodes)
print("Adjacency Matrix:")
print("   ", " ".join(f"{node:2}" for node in nodes))
for idx, row in enumerate(adj_matrix):
    print(f"{nodes[idx]:2} ", " ".join(map(str, row)))

def find_path(line, mapmap):
    def find_longest_path(start_node, line, mapmap):
        path = [start_node]
        remaining_nodes = set(line) - {start_node}
        while remaining_nodes:
            next_node = None
            for node in remaining_nodes:
                if node in mapmap.get(path[-1], []):
                    next_node = node
                    break
            if next_node:
                path.append(next_node)
                remaining_nodes.remove(next_node)
            else:
                break
        return path

    longest_paths = []
    for start_node in line:
        path = find_longest_path(start_node, line, mapmap)
        longest_paths.append(path)

    longest_paths.sort(key=len, reverse=True)
    return longest_paths[0]

for line in numlst:
    path = find_path(line, mapmap)
    print(f"Reordered path for {line}: {path}")