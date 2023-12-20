import re
#seed-->soil--->fertilizer-->water-->light-->temperature-->humidity-->location
with open("Day 5/Puzzle 1/Day5_Puz1.txt") as file:
    contents = file.read()

ex='''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

para ="""
50 98 2
52 50 48
"""
def mapper(para):
    finalmap={}
    for line in para.strip().split('\n'):
        start = int(line.split(' ')[0])-1
        end = int(line.split(' ')[1])-1
        keymap = {}
        for i in range(int(line.split(' ')[2])):
            start += 1
            end += 1
            keymap[start] = end
        
        finalmap.update(keymap)
        #edit: for I in range(end):
        # if I in set, ignore, else add to set
    return finalmap

def finder(dict1, dict2):
    dict3 = {}
    for key, value in dict1.items():
        if value in dict2:
            dict3[key] = dict2[value]
    return dict3

seeds = list(map(int, re.findall(r'\d+', ex.split('\n')[0])))

seed_to_soil = mapper('\n'.join(ex.split('\n\n')[1].split('\n')[1:]))
soil_to_fertilizer = mapper('\n'.join(ex.split('\n\n')[2].split('\n')[1:]))
fertilizer_to_water = mapper('\n'.join(ex.split('\n\n')[3].split('\n')[1:]))
water_to_light = mapper('\n'.join(ex.split('\n\n')[4].split('\n')[1:]))
light_to_temperature = mapper('\n'.join(ex.split('\n\n')[5].split('\n')[1:]))
temperature_to_humidity = mapper('\n'.join(ex.split('\n\n')[6].split('\n')[1:]))
humidity_to_location = mapper('\n'.join(ex.split('\n\n')[7].split('\n')[1:]))
# print(seed_to_soil,soil_to_fertilizer)
# print(finder(seed_to_soil, soil_to_fertilizer))