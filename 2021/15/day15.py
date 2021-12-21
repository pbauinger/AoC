from pathlib import Path
from queue import PriorityQueue


def in_bounds(grid, row, col):
    return row >= 0 and col >= 0 and row < len(grid) and col < len(grid)


def expand(grid, row, col):
    expanded = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    return [(row, col) for (row, col) in expanded if in_bounds(grid, row, col)]


def djikstra(grid):
    target = (len(grid) - 1, len(grid[0]) - 1)

    visited = set()
    q = PriorityQueue()
    q.put((0, 0, 0))
    while q:
        cost, cr, cc = q.get()
        if (cr, cc) == target:
            return cost

        if (cr, cc) in visited:
            continue
        visited.add((cr, cc))
        for sr, sc in expand(grid, cr, cc):
            if (sr, sc) in visited:
                continue
            q.put((cost + grid[sr][sc], sr, sc))


grid = [list(l) for l in Path("real.in").read_text().splitlines()]
grid = [list(map(int, x)) for x in grid]
print("Part1:", djikstra(grid))

size = len(grid)
big_grid = [[0]*size*5 for i in range(size * 5)]
for row in range(len(big_grid)):
    for col in range(len(big_grid)):
        v = (grid[row % size][col % size] + row // size + col // size)
        while v > 9:  # if would be enough; v always <= 17
            v -= 9
        big_grid[row][col] = v
print("Part2:", djikstra(big_grid))
