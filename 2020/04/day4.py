import sys
import re
from pathlib import Path


required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

input = Path("input.txt").read_text()
data = [x.replace("\n", " ").split(" ") for x in input.split("\n\n")]


# Part 1
valid = 0
for entry in data:
    intersect = required - set([x.split(":")[0] for x in entry])
    if len(intersect) == 0:
        valid += 1

print("Part 1:", valid)


# Part 2
valid = 0
for entry in data:
    cnt = 0
    for fld, val in (x.split(":") for x in entry):
        if fld == "byr" and val.isdigit() and 1920 <= int(val) <= 2002: cnt += 1
        if fld == "iyr" and val.isdigit() and 2010 <= int(val) <= 2020: cnt += 1
        if fld == "eyr" and val.isdigit() and 2020 <= int(val) <= 2030: cnt += 1
        if fld == "hcl" and re.fullmatch(r"#[0-9a-fA-F]{6}", val): cnt += 1
        if fld == "ecl" and re.fullmatch(r"amb|blu|brn|gry|grn|hzl|oth", val): cnt += 1
        if fld == "pid" and re.fullmatch(r"[0-9]{9}", val): cnt+= 1
        if fld == "hgt":
            match = re.fullmatch(r"(\d+)(cm|in)", val)
            if match:
                height, unit = int(match[1]), match[2]
                if unit == "cm" and 150 <= height <= 193: cnt += 1
                if unit == "in" and 59 <= height <= 76: cnt += 1

    if cnt == 7:
        valid += 1

print("Part 2:", valid)
