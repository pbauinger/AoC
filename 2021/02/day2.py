from pathlib import Path


def part1(data):
    hor = 0
    depth = 0
    for x in data:
        direction, amount = x.split()
        amount = int(amount)
        if direction == "forward":
            hor += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount
    return hor * depth


def part2(data):
    hor = 0
    depth = 0
    aim = 0
    for x in data:
        direction, amount = x.split()
        amount = int(amount)
        if direction == "forward":
            hor += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    return hor * depth


input = Path("real.in").read_text().splitlines()
print(part1(input))
print(part2(input))
