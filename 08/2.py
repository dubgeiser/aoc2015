#!/usr/bin/env python3


def encode(l: str) -> str:
    marker = "@@@@@@@@@@"
    l = l[1:-1]
    l = l.replace("\\\\", marker)
    l = l.replace('\\"', '\\\\\\"')
    l = l.replace('\\x', '\\\\x')
    l = l.replace(marker, "\\\\\\\\")
    return '"\\"' + l + '\\""'


with open("input") as data:
    lines = [x.strip() for x in data]
size_code = 0
size_encoded = 0
for l in lines:
    size_code += len(l)
    size_encoded += len(encode(l))

print(f"\n{size_encoded - size_code}")
