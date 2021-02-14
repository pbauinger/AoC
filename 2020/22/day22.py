import sys
from pathlib import Path

path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = Path(path).read_text().split("\n\n")

player1 = [int(x) for x in data[0].splitlines()[1:]]
player2 = [int(x) for x in data[1].splitlines()[1:]]


def calc_result(winner):
    total = 0
    for position, card in enumerate(reversed(winner), 1):
        total += card * position

    return total


def part1(player1, player2):
    winner = None
    while player1 and player2:
        pl1_card = player1.pop(0)
        pl2_card = player2.pop(0)

        if pl1_card > pl2_card:
            player1.extend([pl1_card, pl2_card])
            winner = player1

        else:
            player2.extend([pl2_card, pl1_card])
            winner = player2

    return winner


print("Part1", calc_result(part1(player1[:], player2[:])))


def encode_deck(deck):
    return "".join(str(x) for x in deck)


def part2(player1, player2):
    visited = set()
    winner = None
    while player1 and player2:
        encoding = encode_deck(player1) + "|" + encode_deck(player2)
        if encoding in visited:
            return 1, player1
        visited.add(encoding)

        pl1_card = player1.pop(0)
        pl2_card = player2.pop(0)

        if len(player1) >= pl1_card and len(player2) >= pl2_card:
            player_nr, _ = part2(player1[:pl1_card], player2[:pl2_card])
        elif pl1_card > pl2_card:
            player_nr = 1
        else:
            player_nr = 2

        if player_nr == 1:
            player1.extend([pl1_card, pl2_card])
            winner = (1, player1)
        else:
            player2.extend([pl2_card, pl1_card])
            winner = (2, player2)

    return winner


print("Part2", calc_result(part2(player1, player2)[1]))
