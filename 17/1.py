#!/usr/bin/env python3

from itertools import permutations


def count_sums(l: list[int], target, i: int=0, sum_=0):
    global counter
    if sum_ == target:
        counter += 1
        return
    if sum_ < target and i < len(l):
        # Try to add the current element and already move our index to the next
        # element if it would succeed.
        count_sums(l, target, i + 1, sum_ + l[i])

        # If the adding above did not work, we'll come here and just move to
        # the next element.
        count_sums(l, target, i + 1, sum_)

with open("input") as data:
    containers = [int(c.strip()) for c in data]
eggnog = 150
counter = 0
count_sums(containers, eggnog)
print()
print(counter)
