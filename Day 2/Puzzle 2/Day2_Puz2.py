import re
with open("Day 2/Puzzle 1/Day2_Puz2.txt") as file:
    contents = file.read()
flag=0
for i in contents.strip().split('\n'):
    blue_num=max(list(map(int, re.findall(r'(\d+) blue', i))))
    green_num=max(list(map(int,re.findall(r'(\d+) green', i))))
    red_num=max(list(map(int,re.findall(r'(\d+) red', i))))
    flag+=blue_num*green_num*red_num
print(flag)