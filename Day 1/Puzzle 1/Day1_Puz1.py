with open("Day 1/Puzzle 1/Day1_Puz1.txt") as file:
    contents = file.read()
summ=0
for i in contents.split("\n"):
    fwd=bwd=0
    for j in i:
        if j.isdigit():
            fwd=j
            if bwd==0:
                bwd=j
    summ += int(fwd+bwd)
print(summ)
