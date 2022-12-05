#!/usr/bin/env python3


import hashlib

data = 'bgvyzdsv'
i = 0
while True:
    try_input = data + str(i)
    hash = hashlib.md5(try_input.encode('utf-8')).hexdigest()
    if hash.startswith('000000'):
        break
    i += 1

print(i)
