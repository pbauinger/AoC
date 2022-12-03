from pathlib import Path

points = {
    'A': 1,
    'B': 2,
    'C': 3
}

beats = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

loses = {v: k for k, v in beats.items()}

input = Path("input.txt").read_text()
rounds = [x.split() for x in input.splitlines()]
p = 0
for opp, me in rounds:
    me = chr(ord(me) - ord('X') + ord('A'))
    if opp == me:
        p += 3
    if beats[me] == opp:
        p += 6
    p += points[me]
print("Part1", p)

p = 0
for opp, result in rounds:
    if result == 'Y':
        p += 3
        p += points[opp]
    if result == 'Z':
        p += 6
        p += points[loses[opp]]
    if result == 'X':
        p += points[beats[opp]]

print("Part2", p)