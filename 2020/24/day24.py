import re
from pathlib import Path
from collections import defaultdict
import itertools
import sys

flatten = itertools.chain.from_iterable

BLACK, WHITE = 1, 0

mapping = {
    "e": 1 + 0j,
    "se": 0 + 1j,
    "sw": -1 + 1j,
    "w": -1 + 0j,
    "nw": 0 - 1j,
    "ne": 1 - 1j
}

def place_tile(moves):
    return sum(mapping[move] for move in moves)

def init_tile(moves):
    return place_tile(re.findall(r"e|se|sw|w|nw|ne", moves))

def get_adj(t):
    return [t + x for x in mapping.values()]

def get_black_adj_cnt(t):
    return sum(floor[x] for x in get_adj(t))

def get_black_tiles():
    return [key for key, value in floor.items() if value == BLACK]

def get_white_tiles():
    black_tiles = set(get_black_tiles())
    return set(flatten([get_adj(x) for x in black_tiles])) - black_tiles

path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
input = Path(path).read_text()
floor = defaultdict(lambda: WHITE)

# Part 1
for line in input.splitlines():
    tile = init_tile(line)
    floor[tile] = floor[tile] ^ 1
print("Part1:", sum(floor.values()))

# Part 2
for _ in range(100):
    to_white = [x for x in get_black_tiles() if get_black_adj_cnt(x) == 0 or get_black_adj_cnt(x) > 2]
    to_black = [x for x in get_white_tiles() if get_black_adj_cnt(x) == 2]

    for x in to_black:
        floor[x] = BLACK

    for x in to_white:
        floor[x] = WHITE
print("Part2:", sum(floor.values()))
