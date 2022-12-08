import sys
from pathlib import Path

path = 'test.in' if len(sys.argv) >= 2 and sys.argv[1] in (
    't', 'test') else 'real.in'
input = Path(path).read_text().splitlines()

grid = [list(x) for x in input]


def border(x, y):
    return x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid[0]) - 1


def is_visible(x, y, dx, dy):
    xn, yn = x, y
    while not border(xn, yn):
        xn = xn+dx
        yn = yn+dy
        if grid[x][y] <= grid[xn][yn]:
            return False

    return True


visible = set()
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if (is_visible(x, y, +1, 0) or is_visible(x, y, -1, 0) or
                is_visible(x, y, 0, +1) or is_visible(x, y, 0, -1)):
            visible.add((x, y))
print("Part1", len(visible))


def scenic_score(x, y, dx, dy):
    xn, yn = x, y
    score = 0
    while not border(xn, yn):
        xn = xn+dx
        yn = yn+dy
        score += 1
        if grid[x][y] <= grid[xn][yn]:
            return score

    return score


scores = set()
for x in range(len(grid)):
    for y in range(len(grid[0])):
        scores.add(
            scenic_score(x, y, +1, 0) *
            scenic_score(x, y, -1, 0) *
            scenic_score(x, y, 0, +1) *
            scenic_score(x, y, 0, -1)
        )
print("Part2", max(scores))
