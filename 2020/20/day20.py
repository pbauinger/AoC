import sys
import numpy as np
from math import prod
from pathlib import Path


class Tile:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.deg = 0
        self.neighbours_expanded = False

    def rot(self):
        return Tile(self.id, np.rot90(self.data))

    def flip(self):
        return Tile(self.id, np.flipud(self.data))

    def expand_neighbours(self, tiles):
        if self.neighbours_expanded:
            return

        for other in tiles:
            self.add_to_neighbours(other)
            if self.deg == 4:
                break
        self.neighbours_expanded = True

    def add_to_neighbours(self, other):
        if self.id == other.id:
            return
        if not self.up and self.is_other_up(other):
            self.up = other
            self.deg += 1
        if not self.down and self.is_other_down(other):
            self.down = other
            self.deg += 1
        if not self.left and self.is_other_left(other):
            self.left = other
            self.deg += 1
        if not self.right and self.is_other_right(other):
            self.right = other
            self.deg += 1

    def is_other_up(self, other):
        return all(self.data[0] == other.data[-1])

    def is_other_down(self, other):
        return all(self.data[-1] == other.data[0])

    def is_other_right(self, other):
        return all(self.data[:, -1] == other.data[:, 0])

    def is_other_left(self, other):
        return all(self.data[:, 0] == other.data[:, -1])


# read tiles
path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
tiles_txt = Path(path).read_text().split("\n\n")
tiles = []
for tile_txt in tiles_txt:
    id = int(tile_txt.splitlines()[0].split(" ")[1][:-1])
    tile_array = np.array([list(x) for x in tile_txt.splitlines()[1:]])
    tile = Tile(id, tile_array)

    for _ in range(2):
        for _ in range(4):
            tiles.append(tile)
            tile = tile.rot()
        tile = tile.flip()


# calculate neighbours
for a in tiles:
    a.expand_neighbours(tiles)
    if a.deg == 2 and a.left is None and a.up is None:
        break  # we have a startpoint and now can expand further


# Init gamefield
curr = [x for x in tiles if x.deg == 2 and x.up is None and x.left is None][0]
rows = []
while curr is not None:
    curr.expand_neighbours(tiles)
    temp = curr
    row = []
    while temp is not None:
        temp.expand_neighbours(tiles)
        row.append(temp.data[1:-1, 1:-1])
        temp = temp.right
    rows.append(np.hstack(row))
    curr = curr.down
grid = np.vstack(rows)


print("Part1", prod(set([x.id for x in tiles if x.deg == 2])))


# Init sea monster
monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
monster = np.array([list(x) for x in monster.splitlines()[1:]])
monster_height, monster_width = monster.shape
monster_size = (monster == "#").sum()


# Find sea monsters
monster_cnt = 0
for _ in range(2):
    for _ in range(4):
        for row in range(grid.shape[0]):
            for col in range(grid.shape[0]):
                window = grid[row: row + monster_height,
                              col: col + monster_width]
                if window.shape != (monster_height, monster_width):
                    continue
                compare = window == monster
                if compare.sum() == monster_size:
                    monster_cnt += 1
        grid = np.rot90(grid)
    grid = np.flipud(grid)
print("Part2:", (grid == "#").sum() - monster_cnt * monster_size)
