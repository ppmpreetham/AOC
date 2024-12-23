inps="""kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

with open(r"C:\Users\ppmpr\OneDrive\Documents\GitHub\AOC\_2024\day-23\problem 1\input.txt",'r') as file:
    inps = file.read()

filter_inps = [inp.split('-') for inp in inps.strip().split("\n") if inp]

adj_list = {}

for i in range(len(filter_inps)):
    if filter_inps[i][0] not in adj_list:
        adj_list[filter_inps[i][0]] = {filter_inps[i][1]}
    else:
        adj_list[filter_inps[i][0]].add(filter_inps[i][1])

    if filter_inps[i][1] not in adj_list:
        adj_list[filter_inps[i][1]] = {filter_inps[i][0]}
    else:
        adj_list[filter_inps[i][1]].add(filter_inps[i][0])
        

def find_three_cycles(adj_list):
    cycles = set()
    
    for v in adj_list:
        for n1 in adj_list[v]:
            for n2 in adj_list[n1]:
                if n2 != v:
                    if v in adj_list[n2]:
                        cycle = tuple(sorted([v, n1, n2]))
                        cycles.add(cycle)
    
    return cycles

cycles = find_three_cycles(adj_list)
print("Three-vertex cycles found:")

len = 0

for cycle in cycles:
    if any('t' == node[0] for node in cycle):
        print(f"{cycle[0]} -> {cycle[1]} -> {cycle[2]} -> {cycle[0]}")
        len+=1

print(len)