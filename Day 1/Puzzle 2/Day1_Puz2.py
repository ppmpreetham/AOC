with open("Day 1/Puzzle 1/Day1_Puz1.txt") as file:
    contents = file.read()
summ=0
mapping={
    "one":"o1ne",
    "two":"t2wo",
    "three":"th3re",
    "four":"fo4ur",
    "five":"fi5ve",
    "six":"si6x",
    "seven":"sev7en",
    "eight":"ei8ght",
    "nine":"ni9ne"
}
for i in contents.split("\n"):
    fwd,bwd=0,0
    for key, val in alpa.items():
        i = i.replace(key, str(val))
    for j in i:
        if j.isdigit():
            fwd=j
            if bwd==0:
                bwd=j
    summ += int(bwd+fwd)
print(summ)
