with open("c:/Users/ppmpr/OneDrive/Documents/GitHub/AOC24/day 1/problem 2/input.txt", 'r') as file:
    data = file.read()

# data = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""

list_1 = []
list_2 = []

for i in data.split("\n"):
    parts = i.split()
    if len(parts) >= 2:
        list_1.append(int(parts[0]))
        list_2.append(int(parts[1]))

counter_list = [0]*(max(list_2) + 1)

for i in list_2:
    counter_list[i] += 1

final_list = []
for i in range(len(list_1)):
    if list_1[i] < len(counter_list):
        final_list.append(list_1[i]*counter_list[list_1[i]])

print(sum(final_list))