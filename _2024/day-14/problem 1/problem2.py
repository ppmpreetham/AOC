with open("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2024/day-14/problem 1/input.txt", "r") as file:
    inps = file.read()


bounds = (101,103)
x_half = (bounds[0]-1)/2
y_half = (bounds[1]-1)/2

q_1 = 0
q_2 = 0
q_3 = 0
q_4 = 0

def loc(old_loc, vel, iter, bound):
    return (old_loc + vel * iter) % bound

locations = []
iteration = 15

for line in inps.split("\n"):
    if(line == ""):
        continue
    locn = (loc(int(line.split(" ")[0][2:].split(',')[0]), int(line.split(" ")[1][2:].split(",")[0]), iteration, bounds[0]), loc(int(line.split(" ")[0][2:].split(',')[1]), int(line.split(" ")[1][2:].split(",")[1]), iteration, bounds[1]))
    locations.append(locn)

for i in range(bounds[0]):
    for j in range(bounds[1]):
        if (i,j) in locations:
            print("*", end='')
        else:
            print(" ", end='')
    print("\n")