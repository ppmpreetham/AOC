import re, math
with open("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2024/day-03/problem 1/input.txt", "r") as file:
    data = file.read()

ans = 0
for mul in re.findall("mul\(\d+,\d+\)", data):
    ans += math.prod(map(int,re.findall("\d+,\d+", mul)[0].split(",")))
print(ans)