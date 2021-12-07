from pathlib import Path
from functools import cache


@cache
def calc_fish(fish, curr, remaining):
    total = 1
    for day in range(curr + fish, remaining + 1, 7):
        total += calc_fish(9, day, remaining)
    return total


def calc(days):
    data = [int(x) for x in Path("real.in").read_text().split(",")]
    total = 0
    for fish in data:
        total += calc_fish(fish, 1, days)
    return total


print("Part 1", calc(80))
print("Part 2", calc(256))
