#!/usr/bin/env python3

import json


def process_dict(d: dict) -> int:
    total = 0
    for key in d:
        if d[key] == "red": return 0
        total += FMAP[type(d[key])](d[key])
    return total


def process_list(l: list) -> int:
    total = 0
    for i in l:
        total += FMAP[type(i)](i)
    return total


FMAP = {
        dict: process_dict,
        list: process_list,
        int: lambda x: x,
        str: lambda _: 0,
        }

data = json.loads(open("input").read().strip())
print()
total = 0
for each in data:
    total += FMAP[type(each)](each)
print(total)
