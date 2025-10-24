import operator
from itertools import product

# Define data and operations
data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

ops = ['+', '*']
operations = {
    '+': operator.add,
    '*': operator.mul,
}

Match = 0
for line in data.split("\n"):
    target, *arr = map(int, line.replace(":", "").split(" "))
    
    op_combinations = product(ops, repeat=len(arr) - 1)
    
    # print(f"Target: {target}, Array: {arr}")
    for op_comb in op_combinations:
        result = arr[0]
        expr = str(arr[0])
        for i, op in enumerate(op_comb):
            result = operations[op](result, arr[i + 1])
            expr += f" {op} {arr[i + 1]}"
        if result == target:
            Match+=result
            print(f"{expr} = {Match}")

# print(Match)