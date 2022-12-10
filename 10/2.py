#!/usr/bin/env python3

def look_and_say(s: str) -> str:
    if len(s) == 1:
        return f"1{s}"
    i = 0
    new = ""
    count = 1
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            count += 1
        else:
            new += f"{count}{s[i]}"
            count = 1
        i += 1
    return new + f"{count}{s[i]}"


input = "1113222113"
for _ in range(50):
    input = look_and_say(input)
print(f"\n{len(input)}")
