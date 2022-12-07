#!/usr/bin/env python3

import re


with open("input") as data:
    lines = [l.strip() for l in data]


def contains_non_overlapping_pairs(s: str) -> bool:
    i = 0
    while i < len(s) - 1:
        if s.count(s[i:i+2]) >= 2:
            return True
        i += 1
    return False


def contains_repeating_letter(s: str) -> bool:
    unique = set(s)
    for l in unique:
        r = re.compile(l + '.{1}' + l)
        if len(r.findall(s)) > 0:
            return  True
    return False


def is_nice(s: str) -> bool:
    return contains_non_overlapping_pairs(s) and contains_repeating_letter(s)


answer = 0
for l in lines:
    if is_nice(l):
        answer += 1

print(f"{answer = }")
