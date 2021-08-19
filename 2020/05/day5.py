import sys
from pathlib import Path

def get_seat_nr(seat):
    return int(seat.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0"), base=2)

seats = [get_seat_nr(x) for x in Path("input.txt").read_text().splitlines()]
print("Part1:", max(seats))

missing = set(range(min(seats), max(seats)+1)) - set(seats)
print("Part2:", min(missing))
