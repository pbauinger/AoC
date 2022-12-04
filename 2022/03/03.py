from pathlib import Path

input = Path("input.txt").read_text()


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

i = 0
prios = 0
while i < len(rucksacks):
    r1 = rucksacks[i]
    r2 = rucksacks[i+1]
    r3 = rucksacks[i+2]

    overlap = (set(r1) & set(r2) & set(r3)).pop()
    prios += calc_prio(overlap)
    i+=3

print("Part2", prios)