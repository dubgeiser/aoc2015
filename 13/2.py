#!/usr/bin/env python3

from collections import defaultdict
from itertools import permutations

hconf = defaultdict(int)
people = set()
people.add("me")
with open("input") as data:
    for l in data:
        parts = l.strip().split()
        n1 = parts[0].strip()
        n2 = parts[-1].rstrip(".")
        people.add(n1)
        people.add(n2)
        hconf[(n1, n2)] = int({'lose': '-', 'gain': ''}[parts[2]] + parts[3])

optimal = 0
for seating in permutations(people):
    total = hconf[(seating[0], seating[-1])] + hconf[(seating[-1], seating[0])]
    for i in range(len(seating) - 1):
        total += hconf[(seating[i], seating[i + 1])]
        total += hconf[(seating[i + 1], seating[i])]
    optimal = max(total, optimal)
print()
print(optimal)
