import re
with open("Day 6/Puzzle 1/Day6_Puz1.txt") as file:
    contents = file.read()
time = int(''.join(re.findall(r'\d+', contents.strip().split('\n')[0])).replace(" ", ""))
distance=int(''.join(re.findall(r'\d+', contents.strip().split('\n')[1])).replace(" ", ""))
ans=0
for x in range(time):
    if (time-x)*x>distance:
        ans+=1
print(ans)