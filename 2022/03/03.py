import sys
from pathlib import Path

path = 'test.in' if len(sys.argv) >= 2 and sys.argv[1] in (
    't', 'test') else 'real.in'
input = Path(path).read_text()


def calc_prio(r):
    if r.isupper():
        return ord(r) - ord('A') + 27
    else:
        return ord(r) - ord('a') + 1


rucksacks = input.splitlines()
prios = 0
for rucksack in rucksacks:
    length = len(rucksack)
    r1, r2 = rucksack[0:length//2], rucksack[length//2:]
    overlap = (set(r1) & set(r2)).pop()
    prios += calc_prio(overlap)

print("Part1", prios)

prios = 0
for i in range(len(rucksacks))[::3]:
    r1, r2, r3 = rucksacks[i:i+3]

    overlap = (set(r1) & set(r2) & set(r3)).pop()
    prios += calc_prio(overlap)

print("Part2", prios)
