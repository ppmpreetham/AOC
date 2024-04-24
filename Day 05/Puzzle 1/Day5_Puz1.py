#This Code is incomplete and is not working. I will update it soon.

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
def mapper(para,line_no):
    finalmap={}
    para = para.strip().split('\n\n')[line_no].split('\n')[1:]
    sorted_para = '\n'.join(sorted(para, key=lambda line: int(line.split(' ')[0])))
    for line in sorted_para.strip().split('\n'):
        start = int(line.split(' ')[0])-1
        end = int(line.split(' ')[1])-1
        keymap = {}
        for i in range(int(line.split(' ')[2])):
            start += 1
            end += 1
            keymap[start] = end
        
        finalmap.update(keymap)
    return finalmap

high=list(mapper(ex,1).keys())[-1]
print(high)
def filler(finalmap):
    for i in range(high):
        if i not in finalmap:
            finalmap[i] = i
    finalmap = dict(sorted(finalmap.items()))
    return finalmap


def finder(dict1, dict2):
    dict3 = {}
    for key, value in dict1.items():
        if value in dict2:
            dict3[key] = dict2[value]
    return dict3

seeds = list(map(int, re.findall(r'\d+', ex.split('\n')[0])))

seed_to_soil = filler(mapper(ex,1))
soil_to_fertilizer = filler(mapper(ex,2))
fertilizer_to_water = filler(mapper(ex,3))
water_to_light = filler(mapper(ex,4))
light_to_temperature = filler(mapper(ex,5))
temperature_to_humidity = filler(mapper(ex,6))
humidity_to_location =filler(mapper(ex,7))
 
print(finder(seed_to_soil,soil_to_fertilizer))
