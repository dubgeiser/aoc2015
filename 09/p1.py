#!/usr/bin/env python3

from itertools import permutations


# TSP with 8 cities -> 8 -> (8 - 1)! = 40320 permutations to go through...
sample = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
with open("input") as data:
    cities = set()
    travel_distances = {}
    for l in data:
        l = l.strip()
        route, distance = l.split(" = ")
        city_from, city_to = route.split(" to ")
        travel_distances[(city_from, city_to)] = int(distance)
        travel_distances[(city_to, city_from)] = int(distance)
        cities.add(city_from)
        cities.add(city_to)

min_distance = -1
for full_route in permutations(cities):
    distance = 0
    for i in range(len(full_route) - 1):
        city_from = full_route[i]
        city_to = full_route[i + 1]
        distance += travel_distances[(city_from, city_to)]
    if min_distance == -1 or distance < min_distance:
        min_distance = distance

print(f"\n{min_distance}")
