#!/usr/bin/env python3

def move(c, row, col):
    if c == '>':
        col += 1
    elif c == '<':
        col -= 1
    elif c == '^':
        row -= 1
    elif c == 'v':
        row += 1
    return row, col, f"{row},{col}"

data = open("input").read().strip()
data = list(data[::-1])
row_santa = col_santa = row_robo = col_robo = 0
visited = ["0,0"]

while len(data) > 0:
    move_santa = data.pop()
    row_santa, col_santa, pos_santa = move(move_santa, row_santa, col_santa)
    if pos_santa not in visited:
        visited.append(pos_santa)

    move_robo = data.pop()
    row_robo, col_robo, pos_robo = move(move_robo, row_robo, col_robo)
    if pos_robo not in visited:
        visited.append(pos_robo)

print(f"{len(visited) = }")
