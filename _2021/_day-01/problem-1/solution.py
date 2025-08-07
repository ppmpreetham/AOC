with open(r"C:\Users\ppmpr\OneDrive\Documents\GitHub\AOC\_2021\_day-01\input.txt",'r') as file:
    inps = file.read()
    
inps = list(map(lambda x: int(x), inps.splitlines()))

count = 0 
for i in range(len(inps) - 1):
    if inps[i+1] > inps[i]:
        count += 1

print(count)