import sys
from pathlib import Path

path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = [int(x) for x in Path(path).read_text().splitlines()]
data.append(0)
data.sort()
data.append(data[-1] + 3)


one_gaps = 0
three_gaps = 0

prev = data[0]
for item in data[1:]:
    if item - prev == 1:
        one_gaps += 1
    elif item - prev == 3:
        three_gaps += 1
    prev = item

part1 = one_gaps * three_gaps
print("Part1:", part1)


lookup = {}
def arrangements(pos):
    if pos in lookup:
        return lookup[pos]
    if pos == data[-1]:
        return 1
    if pos not in data:
        return 0

    calc = arrangements(pos + 1) + arrangements(pos + 2) + \
        arrangements(pos + 3)
    lookup[pos] = calc
    return calc


print("Part2", arrangements(0))
