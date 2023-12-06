import re
with open("Day 4/Puzzle 1/Day4_Puz1.txt") as file:
    contents = file.read()
add=0
for i in contents.strip().split('\n'):
    flag=0
    win=re.findall(r'\d+', i.split(' | ')[0])[1:]
    user=re.findall(r'\d+', i.split(' | ')[1])
    for j in range(len(win)):
        if win[j] in user:
            flag+=1
    if flag==0:
        add+=(0)
    else:
        add+=(2**(flag-1))
print(add)