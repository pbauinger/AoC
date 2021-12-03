from pathlib import Path

input = Path("real.in").read_text()
input = [x for x in input.splitlines()]


def calcuateCnt(arr, bit):
    res0 = 0
    res1 = 0
    for x in arr:
        if x[bit] == "1":
            res1 += 1
        else:
            res0 += 1
    return res0, res1


def filterData(arr, bit, value):
    return [x for x in arr if x[bit] == value]


# Part1
gamma = ""
eps = ""
for bit in range(len(input[0])):
    res0, res1 = calcuateCnt(input, bit)
    if res0 > res1:
        gamma += "0"
        eps += "1"
    else:
        gamma += "1"
        eps += "0"
result = int(gamma, base=2) * int(eps, base=2)
print("Part1", result)


# Part2
ox = input
co2 = ox

bit = 0
while len(ox) > 1:
    res0, res1 = calcuateCnt(ox, bit)
    if res0 > res1:
        ox = filterData(ox, bit, "0")
    else:
        ox = filterData(ox, bit, "1")
    bit += 1


bit = 0
while len(co2) > 1:
    res0, res1 = calcuateCnt(co2, bit)
    if res0 > res1:
        co2 = filterData(co2, bit, "1")
    else:
        co2 = filterData(co2, bit, "0")
    bit += 1

result = int(co2[0], base=2) * int(ox[0], base=2)
print("Part2", result)
