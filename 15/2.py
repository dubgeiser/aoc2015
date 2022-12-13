#!/usr/bin/env python3

from itertools import permutations
import re

sample = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories) -> None:
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

    def __str__(self) -> str:
        return f"{self.name}: {self.capacity}, {self.durability}, {self.flavor}, {self.texture}, {self.calories}"


regex = re.compile(r"(\S+): capacity (-?\d), durability (-?\d), flavor (-?\d), texture (-?\d), calories (-?\d)")
I = []
with open("input") as data:
    [I.append(Ingredient(*regex.findall(l.strip())[0])) for l in data]
T = 100
P = permutations(range(1, T + 1), len(I))
best = -1
for p in P:
    if sum(p) != T: continue
    capacity = durability = flavor = texture = calories = 0
    for i, ingredient in enumerate(I):
        capacity += ingredient.capacity * p[i]
        durability += ingredient.durability * p[i]
        flavor += ingredient.flavor * p[i]
        texture += ingredient.texture * p[i]
        calories += ingredient.calories * p[i]
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0 or calories != 500: continue
    else: best = max(best, capacity*durability*flavor*texture)

print()
# print(len(P))
print(f"{best = }")
