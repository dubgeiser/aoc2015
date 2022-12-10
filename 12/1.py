#!/usr/bin/env python3

import re

regex = re.compile(r'-{0,1}\d+')
matches = map(int, regex.findall(open("input").read().strip()))

print()
print(sum(matches))
