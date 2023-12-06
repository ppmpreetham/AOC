import re
with open("Day 6/Puzzle 1/Day6_Puz1.txt") as file:
    contents = file.read()
ans=1
lst=[]
time = list(map(int, re.findall(r'\d+', contents.strip().split('\n')[0])))
distance=list(map(int,re.findall(r'\d+', contents.strip().split('\n')[1])))
for i in range(len(time)):
    flag=0
    t,d=time[i],distance[i]
    for x in range(t):
        if (t-x)*x>d:
            flag+=1
    lst.extend([flag])
for i in lst:
    ans=ans*i
print(ans)