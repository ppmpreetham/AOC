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

rows=len(example.strip().split('\n')[1])
dot_row='.'*rows
example=example.replace(dot_row,f'{dot_row}\n{dot_row}')
lines=example.strip().split('\n')
columns=len(lines)

lst=[]
for index in range(rows):
    flag=0
    for line in lines:
        if line[index]=='.':
            flag+=1
    lst.append(flag)
print(lst)

