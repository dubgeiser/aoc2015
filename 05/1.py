#!/usr/bin/env python3

with open("input") as data:
    lines = [l.strip() for l in data]


def has_three_vowels(s) -> bool:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    letters = list(s)
    count = 0
    for l in vowels:
        count += letters.count(l)
    return count >= 3


def has_at_least_one_letter_that_appears_twice(s):
    unique = set(s)
    for l in unique:
        if f"{l}{l}" in s:
            return True
    return False


def does_not_have_certain_pairs(s: str) -> bool:
    return 'ab' not in s and 'cd' not in s and 'pq' not in s and 'xy' not in s \


def is_nice(s: str) -> bool:
    return does_not_have_certain_pairs(s) \
            and has_three_vowels(s) \
            and has_at_least_one_letter_that_appears_twice(s)



answer = 0
for l in lines:
    if is_nice(l):
        answer += 1


print(f"{answer = }")
