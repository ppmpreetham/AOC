# inps = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""

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

location = []
for line in inps.split("\n"):
    if(line == ""):
        continue
    iteration = 100
    locn = (loc(int(line.split(" ")[0][2:].split(',')[0]), int(line.split(" ")[1][2:].split(",")[0]), iteration, bounds[0]), loc(int(line.split(" ")[0][2:].split(',')[1]), int(line.split(" ")[1][2:].split(",")[1]), iteration, bounds[1]))
    
    if(locn[0] < x_half and locn[1] < y_half):
        q_1 += 1
    
    if(locn[0] > x_half and locn[1] < y_half):
        q_2 += 1
        
    if(locn[0] > x_half and locn[1] > y_half):
        q_3 += 1
        
    if(locn[0] < x_half and locn[1] > y_half):
        q_4 += 1

print(q_1*q_2*q_3*q_4)