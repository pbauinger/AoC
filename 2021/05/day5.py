from pathlib import Path
from collections import defaultdict


def solve(diagonals=False, threshold=2):
    input = Path("real.in").read_text().splitlines()
    grid = defaultdict(lambda: 0)
    for row in input:
        start, target = [x.strip() for x in row.split("->")]
        x1, y1 = [int(x) for x in start.split(",")]
        x2, y2 = [int(x) for x in target.split(",")]
        if x1 == x2:
            sy, ey = min(y1, y2), max(y1, y2)
            for y in range(sy, ey+1):
                grid[(x1, y)] += 1
        if y1 == y2:
            sx, ex = min(x1, x2), max(x1, x2)
            for x in range(sx, ex+1):
                grid[(x, y1)] += 1
        elif diagonals:
            if x1 < x2 and y1 < y2:
                while x1 <= x2 and y1 <= y2:
                    grid[(x1, y1)] += 1
                    x1 += 1
                    y1 += 1
            elif x1 > x2 and y1 > y2:
                while x1 >= x2 and y1 >= y2:
                    grid[(x1, y1)] += 1
                    x1 -= 1
                    y1 -= 1
            elif x1 > x2 and y1 < y2:
                while x1 >= x2 and y1 <= y2:
                    grid[(x1, y1)] += 1
                    x1 -= 1
                    y1 += 1
            elif x1 < x2 and y1 > y2:
                while x1 <= x2 and y1 >= y2:
                    grid[(x1, y1)] += 1
                    x1 += 1
                    y1 -= 1
    return len([x for x in grid.values() if x >= threshold])


print("Part1", solve())
print("Part2", solve(True))