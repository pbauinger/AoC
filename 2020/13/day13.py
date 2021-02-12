from pathlib import Path
from math import prod

data = Path("input.txt").read_text().splitlines()

# Part 1
target = int(data[0])
departures = [int(x) for x in data[1].split(',') if x != 'x']

id = 0
wait = float("inf")
for dep in departures:
    temp = dep - (target % dep)
    if temp < wait:
        wait = temp
        id = dep

print("Part1", id * wait)


# Part 2
data = [(int(val), idx)
        for (idx, val) in enumerate(data[1].split(',')) if val != 'x']
found_ids = set()
timestamp = 0
while True:
    finished = True
    for val, offset in data:
        rem = (timestamp + offset) % val
        if rem == 0:
            found_ids.add(val)
        if rem != 0:
            timestamp += prod(found_ids)
            finished = False
            break
    if finished:
        break
    
print("Part2", timestamp)
