#!/usr/bin/env python3


data = open("input").read()
answer = 0
for c in data:
    if c == '(':
        answer += 1
    elif c == ')':
        answer -= 1
print(f"{answer = }")
