#!/usr/bin/env python3


data = open("input").read()
floor = 0
answer = 1
for c in data:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor < 0:
        break
    answer += 1
print(f"{answer = }")
