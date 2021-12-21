from pathlib import Path
from collections import Counter


def run(iterations):
    input, rules = Path("real.in").read_text().split("\n\n")

    mappings = {}
    for line in rules.splitlines():
        pair, value = line.split(" -> ")
        mappings[pair] = value

    pairs = Counter()
    for idx in range(1, len(input)):
        pair = input[idx-1] + input[idx]
        pairs[pair] += 1

    char_cnt = Counter(input)
    for _ in range(iterations):
        new_pairs = Counter()
        for p, v in pairs.items():
            map_to = mappings[p]
            char_cnt[map_to] += v
            new_pairs[p[0] + map_to] += v
            new_pairs[map_to + p[1]] += v
        pairs = new_pairs
        
    return char_cnt.most_common()[0][1] - char_cnt.most_common()[-1][1]


print("Part 1: ", run(10))
print("Part 2: ", run(40))