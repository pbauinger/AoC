from pathlib import Path
from math import prod


def expand(row, col, prev=float("-inf")):
    if (row < 0 or row >= len(hmap) or col < 0 or col >= len(hmap[0])
            or hmap[row][col] == 9 or hmap[row][col] <= prev):
        return set()
    return ({(row, col)}
            | expand(row - 1, col, hmap[row][col])
            | expand(row + 1, col, hmap[row][col])
            | expand(row, col - 1, hmap[row][col])
            | expand(row, col + 1, hmap[row][col]))


data = Path("real.in").read_text().splitlines()
hmap = []
for line in data:
    hmap.append([int(x) for x in line])


low_points = []
low_corr = []
for row in range(len(hmap)):
    for col in range(len(hmap[0])):
        curr = hmap[row][col]
        low = ((row == 0 or curr < hmap[row-1][col])
               and (row == len(hmap)-1 or curr < hmap[row+1][col])
               and (col == 0 or curr < hmap[row][col-1])
               and (col == len(hmap[0])-1 or curr < hmap[row][col+1]))
        if low:
            low_corr.append((row, col))
            low_points.append(curr)

part1 = sum(x+1 for x in low_points)
print("Part1", part1)


basins = []
for row_low, col_low in low_corr:
    basins.append(len(expand(row_low, col_low)))

part2 = prod(sorted(basins, reverse=True)[:3])
print("Part2", part2)
