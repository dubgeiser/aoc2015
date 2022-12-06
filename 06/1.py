#!/usr/bin/env python3


with open("input") as data:
    instructions = [l.strip() for l  in data]

SIZE_C = SIZE_R = 1000
grid = [[0 for _ in range(SIZE_C)] for _ in range(SIZE_R)]

TURN_ON = 1
TURN_OFF = 0
TOGGLE = -1

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
        if action == TURN_ON:
            grid[r][c] = 1
        elif action == TURN_OFF:
            grid[r][c] = 0
        elif action == TOGGLE:
            grid[r][c] = { 0 : 1, 1 : 0 }[grid[r][c]]
        else:
            raise Exception(f"Unkown Action: {action}")

for instruction in instructions:
    for actionkey, actionvalue in instructionmap.items():
        if instruction.startswith(actionkey):
            manipulate_lights(instruction.replace(f"{actionkey} ", ""), actionvalue)

total = 0
for r in grid:
    total += sum(r)
print()
print(total)
