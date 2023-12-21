#half code only, lost the full code

from collections import Counter
# lst=['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]
# print(lst[::-1])

card = "ABEBF"
ex="""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
def hand(line):
    repeat = sorted(Counter(line).values(), reverse=True)[0]
    secrepeat = sorted(Counter(line).values(), reverse=True)[1]
    return 6 if repeat == 5 else 5 if repeat == 4 else 4 if repeat == 3 and secrepeat == 2 else 3 if repeat == 3 else 2 if repeat == 2 and secrepeat == 2 else 1 if repeat == 2 else 0

for i in ex.strip().split('\n'):
    print(i.split(' ')[0],hand(i))
