from itertools import combinations

# Implementation based on the approach by 4HbQ
# https://www.reddit.com/r/adventofcode/comments/1hicdtb/comment/m2y56t8/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button


def parse_map(file_path):
    grid = {}
    start = None
    with open(file_path, "r") as file:
        for r, line in enumerate(file):
            line = line.strip()
            for c, char in enumerate(line):
                # Use complex numbers to represent the grid
                pos = r + c * 1j
                if char != "#":
                    grid[pos] = char
                if char == "S":
                    start = pos
    return grid, start


def bfs_distances(grid, start):
    distances = {start: 0}
    queue = [start]

    while queue:
        current = queue.pop(0)
        # Movements: up, down, left, right
        for move in [-1, 1, -1j, 1j]:
            neighbor = current + move
            if neighbor in grid and neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


def count_high_saving_cheats(file_path):
    grid, start = parse_map(file_path)
    distances = bfs_distances(grid, start)

    part_1 = 0
    part_2 = 0

    for (p1, d1), (p2, d2) in combinations(distances.items(), 2):
        # Use manhattan distance to measure difference in columns and rows
        # between two points in the grid, assuming movement only along the grid
        # lines (up, down, left, right)
        manhattan_dist = abs((p1 - p2).real) + abs((p1 - p2).imag)
        time_saved = d2 - d1 - manhattan_dist

        # Cheat can last up to 2 picoseconds
        if manhattan_dist == 2 and time_saved >= 100:
            part_1 += 1
        # Cheat can last up to 20 picoseconds
        if manhattan_dist <= 20 and time_saved >= 100:
            part_2 += 1

    return part_1, part_2


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

part_1_result, part_2_result = count_high_saving_cheats(file_path)
print(part_1_result)
print(part_2_result)
