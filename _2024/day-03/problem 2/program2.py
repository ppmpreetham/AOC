import re, math
with open("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2024/day-03/problem 1/input.txt", "r") as file:
    data = file.read()
    
s = 1
ans = 0

for mul in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data):
    match mul:
        case "do()":
            s = 1
        case "don't()":
            s = 0
    
    if(not s):
        continue
    
    nums = re.findall(r"\d+,\d+", mul)
    if nums:
        ans += math.prod(map(int, nums[0].split(",")))
print(ans)