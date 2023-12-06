import re
with open("Day 4/Puzzle 1/Day4_Puz1.txt") as file:
    contents = file.read()
add=0
example="""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
document=example.strip().split('\n')
# for line in document:
#    flag=0
#     win=re.findall(r'\d+', line.split(' | ')[0])[1:]
    # user=re.findall(r'\d+', line.split(' | ')[1])
    # for j in range(len(win)):
#         if win[j] in user:
#             flag+=1
#             document.insert(i+1,)
#     print(flag)
# print(add)
for line in range(len(document)):
    flag=0
    win=re.findall(r'\d+', document[line].split(' | ')[0])[1:]
    user=re.findall(r'\d+', document[line].split(' | ')[1])
    for j in range(len(win)):
        if win[j] in user:
            flag+=1
            document.insert(line+1,document[j])
print(document)