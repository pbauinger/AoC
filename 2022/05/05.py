import sys
from pathlib import Path
import re

path = 'test.in' if len(sys.argv) >= 2 and sys.argv[1] in (
    't', 'test') else 'real.in'
input = Path(path).read_text().split('\n\n')


def process(part1=True):
    stacks_str = input[0].splitlines()
    moves = input[1].splitlines()

    nr_of_stacks = int(stacks_str[-1].split()[-1])
    stacks = [[] for _ in range(nr_of_stacks)]
    for stack_str in stacks_str[:-1]:
        for s in range(nr_of_stacks):
            if stack_str[1 + 4 * s] != ' ':
                stacks[s].insert(0, stack_str[1 + 4 * s])

    for move in moves:
        amount, dest, target = [int(x) for x in re.fullmatch(
            "move (\d+) from (\d+) to (\d+)", move).groups()]
        dest -= 1
        target -= 1

        temp = []
        for _ in range(amount):
            temp.append(stacks[dest].pop())
        
        if (not part1):
            temp.reverse()
        
        stacks[target].extend(temp)


    return "".join([s[-1] for s in stacks])


print("Part1", process(part1=True))
print("Part1", process(part1=False))
