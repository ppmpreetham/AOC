with open("Day1_Puz1.txt") as file:
    contents = file.read()
summ=0
for i in contents.strip().split("\n"):
    fwd,bwd=0,0
    for j in i:
        if j.isdigit():
            bwd=j
            if fwd==0:
                fwd=j
    summ += int(fwd+bwd)
print(summ)