import sys
import itertools as it
from pathlib import Path
from math import prod


def xSum(data, cnt, target):
    for x in it.combinations(data, cnt):
        if sum(x) == target:
            return x

path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
input = Path(path).read_text()
data = [int(x) for x in input.splitlines()]

print("Part1:", prod(xSum(data, 2, 2020)))
print("Part2:", prod(xSum(data, 3, 2020)))
