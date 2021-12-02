import more_itertools as mit
from pathlib import Path


def part1(arr):
    prev = arr[0]
    cnt = 0
    for curr in arr[1:]:
        if curr > prev:
            cnt += 1
        prev = curr
    return cnt


def part2(arr):
    prev = float("inf")
    cnt = 0
    for curr in mit.windowed(arr, 3):
        if sum(curr) > prev:
            cnt += 1
        prev = sum(curr)
    return cnt


input = Path("real.in").read_text()
input = [int(x) for x in input.splitlines()]
print(part1(input))
print(part2(input))
