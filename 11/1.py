#!/usr/bin/env python3


def inc_c(c: str) -> str:
    if c == 'z': return 'a'
    else: return chr(ord(c) + 1)


def inc(s: str) -> str:
    ls = list(s)
    i = -1
    while abs(i) <= len(ls):
        l = inc_c(ls[i])
        ls[i] = l
        if l != "a":
            break
        i -= 1
    return "".join(ls)


def has_three_consecutive_letters(s: str) -> bool:
    for i in range(len(s) - 2):
        if ord(s[i]) + 1 == ord(s[i+1]) and ord(s[i+1]) + 1 == ord(s[i+2]):
            return True
    return False


def has_two_different_non_overlapping_pairs(s: str) -> bool:
    found = set()
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            found.add(s[i])
            if len(found) >= 2: return True
    return False

def is_valid(s: str) -> bool:
    return has_three_consecutive_letters(s) \
        and has_two_different_non_overlapping_pairs(s)


def sensible_reset(s: str) -> str:
    banned = ('i', 'o', 'l')
    new = ""
    for i in range(len(s)):
        if s[i] in banned:
            new += "k"
            new += ("a" * (len(s) - i - 1))
            break
        else:
            new += s[i]
    return new

password = "hxbxwxba"
while not is_valid(sensible_reset(password)):
    password = inc(password)
print()
print(password)
