import sys
import re
from pathlib import Path
import networkx as nx

path = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
data = Path(path).read_text()

G = nx.DiGraph()

for line in data.splitlines():
    source, targets = re.search(r"(.*?) bags? contain (.*).", line).groups()

    if targets == "no other bags":
        continue

    for target in [x.strip() for x in targets.split(",")]:
        w, to = re.search(r"(\d+) (.*?) bags?", target).groups()
        G.add_edge(source, to, weight=int(w))


print("Part 1:", len(nx.ancestors(G, "shiny gold")))

def count_bags (graph, curr):
    sum = 0
    for c, w in graph[curr].items():
        sum += w["weight"] + w["weight"] * count_bags(graph, c)

    return sum

print("Part 2:", count_bags(G, "shiny gold"))
