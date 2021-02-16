import sys
from pathlib import Path
from functools import cache

path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = [int(x) for x in Path(path).read_text().splitlines()]
data.append(0)
data.sort()
data.append(data[-1] + 3)


@cache
def arrangements(pos):
    if pos == data[-1]:
        return 1
    if pos not in data:
        return 0

    return arrangements(pos + 1) + arrangements(pos + 2) + \
        arrangements(pos + 3)


print("Part2", arrangements(0))
