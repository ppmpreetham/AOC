with open(r"C:\Users\ppmpr\OneDrive\Documents\GitHub\AOC\_2021\_day-02\input.txt",'r') as file:
    inps = file.read()
    
position, depth  = 0, 0

for line in inps.splitlines():
    dir = line.split(" ")[0]
    val = int(line.split(" ")[1])
    
    match dir:
        case "forward":
            position += val
        case "down":
            depth += val
        case "up":
            depth -= val

print(position*depth)