from functools import cache
import itertools as it


# Part 1
p = [4, 5]
s = [0, 0]
cur = dice = rolls = 0
while True:
    for _ in range(3):
        dice = (dice % 100) + 1
        p[cur] = (p[cur] + dice) % 10
        rolls += 1
    s[cur] += p[cur] + 1
    if(s[cur] >= 1000):
        print(s[cur ^ 1] * rolls)
        break
    cur ^= 1


@cache
def part2(cur, p1_p, p2_p, p1_s, p2_s):
    if p1_s >= 21:
        return (1, 0)
    elif p2_s >= 21:
        return (0, 1)
    
    p1_wins = p2_wins = 0
    for rolls in it.product([1,2,3], repeat=3):
        if cur == 0:
            pos = (p1_p + sum(rolls)) % 10
            p1_win, p2_win = part2(cur^1, pos, p2_p, p1_s + pos + 1, p2_s)
        else:
            pos = (p2_p + sum(rolls)) % 10
            p1_win, p2_win = part2(cur^1, p1_p, pos, p1_s, p2_s + pos + 1)
        p1_wins += p1_win
        p2_wins += p2_win
        
    return (p1_wins, p2_wins)

cnt = part2(0, 4, 5, 0, 0)
print(max(cnt))