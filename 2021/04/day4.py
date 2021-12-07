from pathlib import Path


def apply_num_to_boards(boards, markings, n):
    for board, marking in zip(boards, markings):
        for idx, value in enumerate(board):
            if(value == num):
                marking[idx] = True


def get_winners(markings, ignore):
    winners = set()
    for board_idx, marking in enumerate(markings):
        if(board_idx in ignore):
            continue
        rows = [0] * 5
        columns = [0] * 5
        for idx, marked in enumerate(marking):
            if marked:
                rows[idx // 5] += 1
                columns[idx % 5] += 1
        if 5 in rows or 5 in columns:
            winners.add(board_idx)
            continue
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

winners = set()
for num in numbers:
    apply_num_to_boards(boards, markings, num)
    new_winners = get_winners(markings, winners)
    
    if new_winners:
        winners |= new_winners
        if len(winners) == 1:
            w_idx = (list(new_winners))[0]
            print("Part1", sum_unmarked(boards[w_idx], markings[w_idx]) * int(num))

        if len(winners) == len(boards):
            w_idx = (list(new_winners))[0]
            print("Part2", sum_unmarked(boards[w_idx], markings[w_idx]) * int(num))
            break