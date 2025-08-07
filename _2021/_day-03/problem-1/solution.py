with open(r"C:\Users\ppmpr\OneDrive\Documents\GitHub\AOC\_2021\_day-03\input.txt",'r') as file:
    inps = file.read()

total = [0] * len(inps.splitlines()[0])
n = len(inps.splitlines())

for line in inps.splitlines():
    x = int(line, 2)
    nlen = len(line)
    for i in range(nlen):
        total[i] += (x & (1 << (nlen-1 - i))) >> (nlen-1 - i)

gamma = [int(count > n / 2) for count in total]
epsilon = [1 - bit for bit in gamma]  # Inverse of gamma
    
print(int("".join(map(str, gamma)), 2)*int("".join(map(str, epsilon)), 2))
