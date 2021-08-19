import sys
from pathlib import Path
from collections import defaultdict


def exec_code(commands):
    pc, acc = 0, 0
    visited = defaultdict(lambda: False)

    while pc < len(commands):
        inst, val = commands[pc]
        if visited[pc]:
            return (acc, False)
        visited[pc] = True

        if inst == "nop":
            pc += 1
        elif inst == "acc":
            acc += int(val)
            pc += 1
        elif inst == "jmp":
            pc += int(val)
    return (acc, True)

path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = Path("input.txt").read_text().splitlines()
commands = [x.split(" ") for x in data]

print("Part1:", exec_code(commands)[0])

# Part 2
for line, cmd in enumerate(commands):
    inst, val = cmd
    if inst in ["jmp", "nop"]:
        changed = commands.copy()
        changed[line] = ("jmp" if inst == "nop" else "nop", val)
        acc, success = exec_code(changed)
        if success:
            print("Part2:", acc)
            break
