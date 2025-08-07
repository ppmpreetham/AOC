with open(r"C:\Users\ppmpr\OneDrive\Documents\GitHub\AOC\_2021\_day-01\input.txt",'r') as file:
    inps = file.read()
    
inps = list(map(lambda x: int(x), inps.splitlines()))

n = len(inps)
count = 0

for i in range(n-3):
    if inps[i+3] > inps[i]:
        count += 1

print(count)
