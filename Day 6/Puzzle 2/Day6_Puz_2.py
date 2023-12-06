import re
with open("Day 6/Puzzle 1/Day6_Puz1.txt") as file:
    contents = file.read()
ans=0
time = int(''.join(re.findall(r'\d+', contents.strip().split('\n')[0])).replace(" ", ""))
distance=int(''.join(re.findall(r'\d+', contents.strip().split('\n')[1])).replace(" ", ""))
for x in range(time):
    if (time-x)*x>distance:
        ans+=1
print(ans)