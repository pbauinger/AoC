from pathlib import Path
import itertools as it
import sys

preamble_size = 25


def two_sum(nums, target):
    for num_t in it.combinations(nums, 2):
        if sum(num_t) == target:
            return True
    return False


def part1(data):
    for idx, to_check in enumerate(data[preamble_size:]):
        preamble = data[idx:idx+preamble_size]
        if not two_sum(preamble, to_check):
            return to_check


def part2(data, target):
    for i, curr in enumerate(data):
        for j in range(i + 1, len(data)):
            curr += data[j]
            if curr == invalid:
                result = data[i:j+1]
                return min(result) + max(result)

            if curr > invalid:
                break


path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = [int(x) for x in Path(path).read_text().splitlines()]
invalid = part1(data)
print("Part1:", invalid)
print("Part2:", part2(data, invalid))
