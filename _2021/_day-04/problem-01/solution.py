from pprint import pprint

with open(r"C:\Users\ppmpr\OneDrive\Documents\GitHub\AOC\_2021\_day-04\example.txt",'r') as file:
    inps = file.read()

draw = list(map(int, inps.split("\n\n")[0].split(",")))
boards = []
n = len(inps.split("\n\n")[1:])

def findRowOrArray():

for board in inps.split("\n\n")[1:]:
    boardarr = []
    for line in board.split("\n"):
        if line.strip() == "":
            continue
        linearr = []
        for num in line.split(" "):
            if num != "":
                linearr.append(int(num))
        boardarr.append(linearr)
    boards.append(boardarr)



for i, n in enumerate(draw):
    for board in boards:
        for line in board:
            if n in line:
                line[line.index(n)] = -1
                
            # print(line, end="*")
            # if n in line:
            #    line[line.index(n)] = -1
                
pprint(boards)