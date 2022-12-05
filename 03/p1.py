#!/usr/bin/env python3


data = open("input").read().strip()
row = col = 0
visited = ["0,0"]
answer = 0
for c in data:
    if c == '>':
        col += 1
    elif c == '<':
        col -= 1
    elif c == '^':
        row -= 1
    elif c == 'v':
        row += 1
    pos = f"{row},{col}"
    if pos not in visited:
        visited.append(pos)

print(f"{len(visited) = }")
