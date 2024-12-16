import heapq


def parse_maze(file_path):
    with open(file_path, "r") as f:
        maze = f.read().splitlines()
    start, end = None, None
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)
    return maze, start, end


def is_valid(pos, maze):
    x, y = pos
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] != "#"


def part_1(maze, start, end):
    """Dijkstra-like approach"""
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # East, North, West, South
    pq = []  # Priority queue: (score, position, direction)
    heapq.heappush(pq, (0, start, directions[0]))
    visited = {}

    while pq:
        score, pos, facing = heapq.heappop(pq)

        # Avoid revisiting with the same direction if already visited with a lower score
        if (pos, facing) in visited and visited[(pos, facing)] <= score:
            continue
        visited[(pos, facing)] = score

        if pos == end:
            return score

        # Forward
        next_pos = (pos[0] + facing[0], pos[1] + facing[1])
        if is_valid(next_pos, maze):
            heapq.heappush(pq, (score + 1, next_pos, facing))

        # Clockwise
        cw_index = (directions.index(facing) + 1) % 4
        new_facing_cw = directions[cw_index]
        heapq.heappush(pq, (score + 1000, pos, new_facing_cw))

        # Counterclockwise
        ccw_index = (directions.index(facing) - 1) % 4
        new_facing_ccw = directions[ccw_index]
        heapq.heappush(pq, (score + 1000, pos, new_facing_ccw))

    return float("inf")  # No path found


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"
maze, start, end = parse_maze(file_path)
print(part_1(maze, start, end))
