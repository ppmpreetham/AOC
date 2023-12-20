# with open("") as file:
    # contents = file.read()
example="""
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
lines=example.strip().split('\n')
lst=[]
for i in lines:
    flag=0
    for j in i:
        if j=='.':
            flag+=1
    lst.append(flag)
    for haha in range(len(lst)):
        if lst[haha]==10:
            lines[haha]=lines[haha].
print(lines)