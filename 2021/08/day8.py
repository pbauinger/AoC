from pathlib import Path

data = Path("real.in").read_text().splitlines()

part1 = 0
part2 = 0
for x in data:
    signals, result = [y.split() for y in x.split(" | ")]
    signals = ["".join(sorted(x)) for x in signals]
    result = ["".join(sorted(x)) for x in result]
    digit_map = {}
    signal_map = {}

    # Sort by len to reach 1 and 4 first. With 1 and 4 we can deduce the rest 
    for signal in sorted(signals, key=len):
        if len(signal) == 2: digit = 1
        elif len(signal) == 3: digit = 7
        elif len(signal) == 4: digit = 4
        elif len(signal) == 7: digit = 8

        elif len(signal) == 5:
            if set(digit_map[1]) <= set(signal): digit = 3
            elif len(set(signal) & set(digit_map[4])) == 3: digit = 5
            else: digit = 2

        elif len(signal) == 6:
            if not set(digit_map[1]) <= set(signal): digit = 6
            elif set(digit_map[4]) <= set(signal): digit = 9
            else: digit = 0

        digit_map[digit] = signal
        signal_map[signal] = digit

    mul = 1000
    for res in result:
        if res in [digit_map[1], digit_map[4], digit_map[7], digit_map[8]]:
            part1 += 1
        part2 += signal_map[res] * mul
        mul //= 10

print("Part 1", part1)
print("Part 2", part2)
