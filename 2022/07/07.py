import sys
from pathlib import Path

path = 'test.in' if len(sys.argv) >= 2 and sys.argv[1] in (
    't', 'test') else 'real.in'
input = Path(path).read_text().splitlines()


filesystem = {
    '/': [0, {}]
}
curr_location = filesystem['/']
location_stack = []
for line in input:
    parts = line.split()
    if (line[0] == '$'):
        if (parts[1] == 'cd'):
            if (parts[2] == '/'):
                curr_location = filesystem['/']
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
    size = curr[0]
    for child in curr[1].values():
        size += calculate_size(child)

    curr[0] = size
    if (size <= 100_000 and curr[1]):
        total += size
    return size


calculate_size(filesystem['/'])
print('Part1', total)

free = 70000000 - filesystem['/'][0]
needed = 30000000 - free
min = float('inf')
def find_smallest(curr):
    global min
    size = curr[0]
    if curr[1] and size >= needed and size < min:
        min = size

    for child in curr[1].values():
        find_smallest(child)


find_smallest(filesystem['/'])
print('Part2', min)