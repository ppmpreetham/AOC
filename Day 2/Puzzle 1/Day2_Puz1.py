with open("Day 2/Puzzle 1/Day2_Puz2.txt") as file:
    contents = file.read()
def get_number(j):
    s=''
    for i in j:
        if i.isdigit():
            s+=i
    return int(s)
def haha(x):
    if 'blue' in x and get_number(x)<=14:
        return 1
    if 'green' in x and get_number(x)<=13:
        return 1
    if 'red' in x and get_number(x)<=12:
        return 1
    return 0
flag=0
for i in contents.strip().replace('; ', ', ').replace(': ',', ').split('\n'):
    k=[haha(x) for x in i.split(', ')[1:len(i.split(', '))]]
    if all(elem == 1 for elem in k):
        flag+=get_number(i.split(', ')[0])
print(flag)