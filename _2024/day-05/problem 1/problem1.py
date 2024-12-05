with open("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2024/day-05/problem 1/input.txt", 'r') as file:
    data = file.read()

mapp = data.split("\n\n")[0]
nums = data.split("\n\n")[1]

maplst = [map.split("|") for map in mapp.split("\n")]
numlst = [num.split(",") for num in nums.split("\n")]

sum = 0
for line in numlst:
    count = 0
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if [line[i],line[j]] in maplst:
                count+=1
    if count==len(line)*(len(line)-1)/2 and line[0]!='':
        sum += int(line[int(len(line) / 2)])

print(sum)