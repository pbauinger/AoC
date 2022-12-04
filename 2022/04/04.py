from pathlib import Path

input = Path("input.txt").read_text()
pairs = [x.split(',') for x in input.splitlines()]


def overlaps(sec1, sec2, fully=False):
    s1_start, s1_end = [int(x) for x in sec1.split('-')]
    s2_start, s2_end = [int(x) for x in sec2.split('-')]

    s1_range = set(range(s1_start, s1_end+1))
    s2_range = set(range(s2_start, s2_end+1))

    if fully:
        return len(s1_range & s2_range) in (len(s1_range), len(s2_range))
    return len(s1_range & s2_range) != 0


contained_part1 = 0
contained_part2 = 0
for section1, section2 in pairs:
    contained_part1 += overlaps(section1, section2, fully=True)
    contained_part2 += overlaps(section1, section2, fully=False)


print("Part1", contained_part1)
print("Part2", contained_part2)
