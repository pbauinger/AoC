from pathlib import Path

input = Path("input.txt").read_text().split('\n\n')

calories = []
for elf in input:
    calories.append(sum(int(c) for c in elf.split()))

calories.sort()
print("Part1", calories[-1])
print("Part2", sum(calories[-3:]))

