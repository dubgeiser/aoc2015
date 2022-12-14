#!/usr/bin/env python3

from dataclasses import dataclass, field, fields


UNKNOWN = -1

@dataclass
class Sue:
    name: str
    children: int = field(default=UNKNOWN)
    cats: int = field(default=UNKNOWN)
    samoyeds: int = field(default=UNKNOWN)
    pomeranians: int = field(default=UNKNOWN)
    akitas: int = field(default=UNKNOWN)
    vizslas: int = field(default=UNKNOWN)
    goldfish: int = field(default=UNKNOWN)
    trees: int = field(default=UNKNOWN)
    cars: int = field(default=UNKNOWN)
    perfumes: int = field(default=UNKNOWN)

    def match_probability(self, other: "Sue") -> int:
        """Return a number indicating how likely this Sue matches the other.
        Assume other Sue's fields are all known."""
        probability = 0
        probability += self.match_probability_bigger(["cats", "trees"], other)
        probability += self.match_probability_smaller(["pomeranians", "goldfish"], other)
        for f in fields(other):
            if f.name in ["name", "cats", "trees", "pomeranians", "goldfish"]: continue
            if getattr(self, f.name) == getattr(other, f.name): probability += 100
            if getattr(self, f.name) == UNKNOWN: probability += 1
        return probability

    def match_probability_bigger(self, attrs: list[str], other: "Sue") -> int:
        probability = 0
        for attr in attrs:
            if getattr(self, attr) > getattr(other, attr):
                probability += 100
            if getattr(self, attr) == UNKNOWN:
                probability += 1
        return probability

    def match_probability_smaller(self, attrs: list[str], other: "Sue") -> int:
        probability = 0
        for attr in attrs:
            if getattr(self, attr) > UNKNOWN and getattr(self, attr) < getattr(other, attr):
                probability += 100
            if getattr(self, attr) == UNKNOWN:
                probability += 1
        return probability

    @staticmethod
    def from_data(l: str) -> "Sue":
        kwargs = {}
        kwargs["name"] = l[:l.index(":")]
        props = l[l.index(":") + 2:].split(", ") 
        for p in props:
            fname, fvalue = p.split(": ")
            kwargs[fname] = int(fvalue)
        return Sue(**kwargs)


mystery_sue = Sue(name="X", children=3, cats=7, samoyeds=2, pomeranians=3,
                  akitas=0, vizslas=0, goldfish=5, trees=3, cars=2, perfumes=1)
with open("input") as data:
    sues = [Sue.from_data(l.strip()) for l in data]
THE_Sue = None
probability = -1
for s in sues:
    p = s.match_probability(mystery_sue)
    if p > probability:
        probability = p
        THE_Sue = s
print()
print(THE_Sue)
