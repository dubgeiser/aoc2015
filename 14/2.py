#!/usr/bin/env python3

import math


class Reindeer:
    def __init__(self, name:str, speed: int, duration: int, rest: int) -> None:
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest
        self.distance = 0
        self.elapsed = 0

    def update(self) -> None:
        self.elapsed += 1
        # Flying
        if self.elapsed <= self.duration:
            self.distance += self.speed
        elif self.elapsed == self.duration + self.rest:
            self.elapsed = 0

    def __str__(self) -> str:
        return f"{self.name} {self.speed = } {self.duration = } {self.rest = } {self.distance = } {self.elapsed = }"


reindeers = []
with open("input") as data:
    for line in data:
        parts = line.strip().split()
        name = parts[0]
        speed =int(parts[3])
        duration = int(parts[6])
        rest = int(parts[-2])
        reindeers.append(Reindeer(name, speed, duration, rest))

scores = [0 for _ in reindeers]
max_distance = -1
S = 2503
for _ in range(S):
    for i, r in enumerate(reindeers):
        r.update()
        max_distance = max(max_distance, r.distance)
    si = [i for i, r in enumerate(reindeers) if r.distance == max_distance]
    for i in si:
        scores[i] += 1

print()
print(max(scores))
