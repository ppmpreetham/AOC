with open(r"C:\Users\ppmpr\OneDrive\Documents\GitHub\AOC\_2021\_day-02\input.txt",'r') as file:
    inps = file.read()
    
aim, position, depth  = 0, 0, 0

for line in inps.splitlines():
    dir = line.split(" ")[0]
    val = int(line.split(" ")[1])
    
    match dir:
        case "forward":
            position += val
            depth += aim*val
        case "down":
            aim += val
        case "up":
            aim -= val

print(position*depth)