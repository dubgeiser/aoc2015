#!/usr/bin/env python3

import math

NAME = 0
SPEED = 1
DURATION = 2
REST = 3

reindeers = []
with open("input") as data:
    for line in data:
        parts = line.strip().split()
        name = parts[0]
        speed =int(parts[3])
        duration = int(parts[6])
        rest = int(parts[-2])
        reindeers.append((name, speed, duration, rest))

distances = [0 for _ in reindeers]
S = 2503
for i, r in enumerate(reindeers):
    distances[i] = math.ceil(S / (r[DURATION] + r[REST])) * (r[SPEED] * r[DURATION])

print()
print(max(distances))
