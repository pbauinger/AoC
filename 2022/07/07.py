import sys
from pathlib import Path

path = 'test.in' if len(sys.argv) >= 2 and sys.argv[1] in (
    't', 'test') else 'real.in'
input = Path(path).read_text().splitlines()


root = [0, {}]
curr_location = root
location_stack = []
for line in input:
    parts = line.split()
    if (line[0] == '$'):
        if (parts[1] == 'cd'):
            if (parts[2] == '/'):
                curr_location = root
            elif (parts[2] == '..'):
                curr_location = location_stack.pop()
            else:
                location_stack.append(curr_location)
                curr_location = curr_location[1][parts[2]]
    elif (parts[0] == 'dir'):
        curr_location[1][parts[1]] = [0, {}]
    else:
        curr_location[1][parts[1]] = [int(parts[0]), {}]

total = 0
def calculate_size(curr):
    global total

    for child in curr[1].values():
        curr[0] += calculate_size(child)

    if (curr[0] <= 100_000 and curr[1]):
        total += curr[0]
    return curr[0]

calculate_size(root)
print('Part1', total)

free = 70000000 - root[0]
needed = 30000000 - free
min = float('inf')
def find_smallest(curr):
    global min
    size = curr[0]
    if curr[1] and size >= needed and size < min:
        min = size
    for child in curr[1].values():
        find_smallest(child)

find_smallest(root)
print('Part2', min)
