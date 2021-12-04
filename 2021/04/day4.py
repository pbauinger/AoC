from pathlib import Path


def apply_num_to_boards(boards, markings, n):
    for board, marking in zip(boards, markings):
        for idx, value in enumerate(board):
            if(value == num):
                marking[idx] = True


def get_winners(markings):
    winners = set()
    for board_idx, marking in enumerate(markings):
        rows = [0] * 5
        columns = [0] * 5
        for idx, marked in enumerate(marking):
            if marked:
                rows[idx // 5] += 1
                columns[idx % 5] += 1
        if any(x == 5 for x in rows) or any(x == 5 for x in columns):
            winners.add(board_idx)
    return winners


def sum_unmarked(board, markings):
    return sum(int(val) for val, marking in zip(board, markings) if not marking)


input = Path("real.in").read_text().split("\n\n")
numbers = input[0].split(",")

boards = []
markings = []
for board_raw in input[1:]:
    boards.append(sum([row.split() for row in board_raw.split("\n")], []))
    markings.append([False] * 25)

prev_winners = set()
for num in numbers:
    apply_num_to_boards(boards, markings, num)
    winners = get_winners(markings)
    if winners:
        new_winners = winners - prev_winners
        if len(winners) == 1 and len(new_winners) == 1:
            w_idx = new_winners.pop()
            print("Part1", sum_unmarked(boards[w_idx], markings[w_idx]) * int(num))

        prev_winners = winners
        if len(winners) == len(boards):
            w_idx = new_winners.pop()
            print("Part2", sum_unmarked(boards[w_idx], markings[w_idx]) * int(num))
            break
