#!/usr/bin/env python3


data = open("input").readlines()
answer = 0
for each in data:
    l, w, h = map(int, each.split('x'))
    t = [l, w, h]
    t.sort()
    t.reverse()
    extra = t.pop() * t.pop()
    answer += 2*l*w + 2*w*h + 2*h*l + extra
print(f"{answer = }")
