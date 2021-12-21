from pathlib import Path
from collections import defaultdict

data = Path("real.in").read_text().splitlines()
graph = defaultdict(list)
for row in data:
    start, end = row.split("-")
    graph[start].append(end)
    graph[end].append(start)


def dfs(curr, visited, double_used):
    cnt = 0
    if curr == "end":
        return 1

    for succ in [x for x in graph[curr] if x != "start"]:
        if succ in visited:
            if not double_used:
                cnt += dfs(succ, visited, True)
            else:
                continue
        elif succ.islower():
            cnt += dfs(succ, visited | {succ}, double_used)
        else:
            cnt += dfs(succ, visited, double_used)
    return cnt


print("Part 1", dfs("start", set(), True))
print("Part 2", dfs("start", set(), False))
