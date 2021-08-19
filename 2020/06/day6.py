import sys
from pathlib import Path

path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = Path(path).read_text()

groups = [x for x in data.split("\n\n")]

part1 = [set(x.replace("\n", "")) for x in groups]
print("Part1:", sum([len(x) for x in part1]))

total = 0
for group in groups:
    entries = [set(x) for x in group.split("\n")]
    intersection = entries[0]
    for entry in entries[1:]:
        intersection &= entry

    total += len(intersection)
print("Part2:", total)
