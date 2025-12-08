import heapq
from collections import defaultdict


def parse_input(file_path):
    with open(file_path, "r") as f:
        return [tuple(map(int, line.strip().split(","))) for line in f if line.strip()]


def part_1(data):

    distances = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1, z1 = data[i]
            x2, y2, z2 = data[j]
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
            distances.append((dist, i, j))

    heapq.heapify(distances)

    parent = list(range(len(data)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False

    num_connections = 10 if len(data) == 20 else 1000

    connections = 0
    while distances and connections < num_connections:
        _, i, j = heapq.heappop(distances)
        union(i, j)
        connections += 1

    circuit_sizes = defaultdict(int)
    for i in range(len(data)):
        circuit_sizes[find(i)] += 1

    largest = sorted(circuit_sizes.values(), reverse=True)

    return largest[0] * largest[1] * largest[2]


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
