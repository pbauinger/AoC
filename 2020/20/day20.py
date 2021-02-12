import numpy as np
from math import prod
from pathlib import Path


class Tile:
    up = None
    down = None
    left = None
    right = None

    def __init__(self, id, data):
        self.id = id
        self.data = data

    def used_ids(self):
        return [x.id for x in [self.up, self.down, self.left, self.right] if x is not None]

    def rot(self):
        return Tile(self.id, np.rot90(self.data))

    def flip(self):
        return Tile(self.id, np.flipud(self.data))

    def deg(self):
        return len(self.used_ids())

    def add_to_neighbours(self, other):
        if self.id == other.id or other.id in self.used_ids():
            return
        if self.is_other_up(other):
            self.up = other
        if self.is_other_down(other):
            self.down = other
        if self.is_other_left(other):
            self.left = other
        if self.is_other_right(other):
            self.right = other

    def is_other_up(self, other):
        return all(self.data[0] == other.data[-1])

    def is_other_down(self, other):
        return all(self.data[-1] == other.data[0])

    def is_other_right(self, other):
        return all(self.data[:, -1] == other.data[:, 0])

    def is_other_left(self, other):
        return all(self.data[:, 0] == other.data[:, -1])


# read tiles
tiles_txt = Path("input.txt").read_text().split("\n\n")
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
    for b in tiles:
        a.add_to_neighbours(b)
print("Part1", prod(set([x.id for x in tiles if x.deg() == 2])))


# Init gamefield
curr = [x for x in tiles if x.deg() == 2 and x.up is None and x.left is None][0]
rows = []
while curr is not None:
    temp = curr
    row = []
    while temp is not None:
        row.append(temp.data[1:-1, 1:-1])
        temp = temp.right
    rows.append(np.hstack(row))
    curr = curr.down
grid = np.vstack(rows)


# Init sea monster
monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
monster = np.array([list(x) for x in monster.splitlines()[1:]])
monster_height, monster_width = monster.shape
monster_size = (monster == '#').sum()


# Find sea monsters
monster_cnt = 0
for _ in range(2):
    for _ in range(4):
        for row in range(grid.shape[0]):
            for col in range(grid.shape[0]):
                window = grid[row:row + monster_height,
                              col:col + monster_width]
                if window.shape != (monster_height, monster_width):
                    continue
                compare = window == monster
                if compare.sum() == monster_size:
                    monster_cnt += 1
        grid = np.rot90(grid)
    grid = np.flipud(grid)
print("Part2:", (grid == '#').sum() - monster_cnt * monster_size)
