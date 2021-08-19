import sys
from pathlib import Path


path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = Path(path).read_text().splitlines()


def check_slope(data, d_col, d_row):
    col_length = len(data[0])
    col = 0
    trees = 0

    for x in data[::d_row]:
        if x[col] == "#":
            trees += 1
        col = (col + d_col) % col_length

    return trees


part1 = check_slope(data, 3, 1)
print("Part1", part1)

part2 = (
    check_slope(data, 1, 1)
    * check_slope(data, 3, 1)
    * check_slope(data, 5, 1)
    * check_slope(data, 7, 1)
    * check_slope(data, 1, 2)
)
print("Part2", part2)
