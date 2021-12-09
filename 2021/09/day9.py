from pathlib import Path
from math import prod


def expand(row, col):
    curr = hmap[row][col]
    positions = {(row, col)}
    if row != 0 and hmap[row-1][col] != 9 and hmap[row-1][col] > curr:
        positions |= expand(row - 1, col)
    if row != len(hmap)-1 and hmap[row+1][col] != 9 and hmap[row+1][col] > curr:
        positions |= expand(row + 1, col)
    if col != 0 and hmap[row][col-1] != 9 and hmap[row][col-1] > curr:
        positions |= expand(row, col - 1)
    if col != len(hmap[0])-1 and hmap[row][col+1] != 9 and hmap[row][col+1] > curr:
        positions |= expand(row, col + 1)
    return positions


data = Path("real.in").read_text().splitlines()
hmap = []
for line in data:
    hmap.append([int(x) for x in line])


low_points = []
low_corr = []
for row in range(len(hmap)):
    for col in range(len(hmap[0])):
        curr = hmap[row][col]
        low = row == 0 or curr < hmap[row-1][col]
        low &= row == len(hmap)-1 or curr < hmap[row+1][col]
        low &= col == 0 or curr < hmap[row][col-1]
        low &= col == len(hmap[0])-1 or curr < hmap[row][col+1]
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
