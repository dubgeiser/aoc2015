#!/usr/bin/env python3


data = open("input").readlines()
answer = 0
for each in data:
    l, w, h = map(int, each.split('x'))
    t = [l, w, h]
    t.sort()
    t.reverse()
    answer += 2*t[-1] + 2*t[-2] + l*w*h
print(f"{answer = }")
