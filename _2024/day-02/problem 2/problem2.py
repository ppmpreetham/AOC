data = [[int(n) for n in line.split()] for line in open("c:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2024/day-02/problem 1/input.txt").read().splitlines()]

def isok(lst):
    diff = [x - y for x, y in zip(lst, lst[1:])]
    return all(-3 <= i <= -1 for i in diff) or all(1 <= i <= 3 for i in diff)

def trimmed(line):
    return [line[:i] + line[i+1:] for i in range(len(line))]

print(sum(any(isok(c) for c in [line, *trimmed(line)]) for line in data))