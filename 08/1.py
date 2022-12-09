#!/usr/bin/env python3

def len_mem(l: str) -> int:
    l = eval(l)
    return len(l)


with open("input") as data:
    lines = [x.strip() for x in data]
size_code = 0
size_memory = 0
for l in lines:
    size_code += len(l)
    size_memory += len_mem(l)
print(f"\n{size_code - size_memory}")
