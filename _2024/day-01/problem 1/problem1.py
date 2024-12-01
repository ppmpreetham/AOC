with open("c:/Users/ppmpr/OneDrive/Documents/GitHub/AOC24/day 1/problem1/input.txt", 'r') as file:
    data = file.read()

list_1 = []
list_2 = []

for i in data.split("\n"):
    parts = i.split()
    if len(parts) >= 2:
        list_1.append(parts[0])
        list_2.append(parts[1])

list_1.sort()
list_2.sort()

new_list = []
for i in range(len(list_1)):
    new_list.append(abs(int(list_1[i])-int(list_2[i])))

print(sum(new_list))