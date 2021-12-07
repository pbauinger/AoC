from pathlib import Path


def calc_fuel(data, func):
    min_fuel = float("inf")
    for pos in range(min(data), max(data) + 1):
        fuel = 0
        for crab_pos in data:
            fuel += func(abs(pos - crab_pos))
        min_fuel = min(min_fuel, fuel)
    return min_fuel


data = [int(x) for x in Path("real.in").read_text().split(",")]

print("Part 1", calc_fuel(data, lambda x: x))
print("Part 1", calc_fuel(data, lambda x: x * (x + 1) // 2))
