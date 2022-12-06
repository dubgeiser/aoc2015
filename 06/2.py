#!/usr/bin/env python3


with open("input") as data:
    instructions = [l.strip() for l  in data]

SIZE_C = SIZE_R = 1000
grid = [[0 for _ in range(SIZE_C)] for _ in range(SIZE_R)]

TURN_ON = 1
TURN_OFF = -1 
TOGGLE = 2

instructionmap = {
        'toggle': TOGGLE,
        'turn on': TURN_ON,
        'turn off': TURN_OFF,
        }

def rectext2coords(t):
    coords = []
    rect = t.split(" through ")
    row_l, col_l = (int(i) for i in rect[0].split(','))
    row_r, col_r = (int(i) for i in rect[1].split(','))
    for r in range(row_l, row_r + 1):
        for c in range(col_l, col_r + 1):
            coords.append((r, c))
    return coords


def manipulate_lights(rectangle_text, action):
    coordinates = rectext2coords(rectangle_text)
    for r, c in coordinates:
        grid[r][c] += action
        if grid[r][c] < 0:
            grid[r][c] = 0

for instruction in instructions:
    for actionkey, actionvalue in instructionmap.items():
        if instruction.startswith(actionkey):
            manipulate_lights(instruction.replace(f"{actionkey} ", ""), actionvalue)

total = 0
for r in grid:
    total += sum(r)
print()
print(total)
