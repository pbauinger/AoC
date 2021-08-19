import sys
import re
from pathlib import Path


path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = Path(path).read_text().lower().splitlines()
data = [re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", x).groups() for x in data]

# Part 1
valid = 0
for lo, hi, letter, word in data:
    if int(lo) <= word.count(letter) <= int(hi):
        valid += 1
print("Part1:", valid)


# Part 2
valid = 0
for pos1, pos2, letter, word in data:
    if (word[int(pos1)-1] == letter) ^ (word[int(pos2)-1] == letter):
        valid += 1
print("Part2:", valid)
