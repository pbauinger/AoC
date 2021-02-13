import sys
import cmath
import numpy as np
from pathlib import Path

directions = {
    "N": +1j,
    "S": -1j,
    "E": +1,
    "W": -1
}

rotations = {
    "R": -1j,
    "L": +1j
}


path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = Path(path).read_text().splitlines()
data = [(x[0], int(x[1:])) for x in data]


def part1(data):
    curr = complex(0, 0)
    facing = complex(1, 0)

    for action, val in data:
        if action in directions:
            curr += directions[action] * val
        elif action in rotations:
            facing *= rotations[action] ** (val//90)
        elif action == "F":
            curr += facing * val
    return int(abs(curr.imag) + abs(curr.real))


def part2(data):
    curr = complex(0, 0)
    waypoint = complex(10, 1)

    for action, val in data:
        if action in directions:
            waypoint += directions[action] * val
        elif action in rotations:
            waypoint *= rotations[action] ** (val//90)
        elif action == "F":
            curr += (waypoint * val)
    return int(abs(curr.imag) + abs(curr.real))


print("Part1: ", part1(data))
print("Part2: ", part2(data))
