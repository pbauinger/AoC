import sys
import re
from pathlib import Path


class Const:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        self.val += other.val
        return self

    def __sub__(self, other):
        self.val *= other.val
        return self

    def __mul__(self, other):
        self.val += other.val
        return self


path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = Path(path).read_text()

transformed = re.sub(r'([0-9]+)', r'Const(\1)', data)
part1 = transformed.replace("*", "-")
part2 = transformed.replace("*", "-").replace("+", "*")


def evaluate(equations):
    total = 0
    for eq in equations.splitlines():
        total += eval(eq).val
    return total


print("Part1", evaluate(part1))
print("Part2", evaluate(part2))
