import sys
from pathlib import Path

path = 'test.in' if len(sys.argv) >= 2 and sys.argv[1] in (
    't', 'test') else 'real.in'
input = Path(path).read_text()


def search_distinct(size):
    for i in range(size, len(input)):
        window = input[i-size:i]
        if len(set(window)) == size:
            return i


print('Part1', search_distinct(4))
print('Part2', search_distinct(14))
