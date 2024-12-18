from collections import deque


def parse_input(file_path):
    with open(file_path, "r") as f:
        byte_positions = [tuple(map(int, line.strip().split(","))) for line in f]
    return byte_positions


def simulate_memory_and_find_path(grid_size, byte_positions, start, end, num_bytes):
    """Part 1"""
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    # Simulate falling bytes
    for i in range(min(num_bytes, len(byte_positions))):
        x, y = byte_positions[i]
        grid[y][x] = "#"  # Corrupted

    def is_valid(x, y):
        return 0 <= x < grid_size and 0 <= y < grid_size and grid[y][x] == "."

    # BFS to find the shortest path
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    # If no path is found
    return -1


def find_first_blocking_byte(grid_size, byte_positions, start, end):
    """Part 2"""
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    for i, (x, y) in enumerate(byte_positions):
        grid[y][x] = "#"  # Corrupted

        # Check if the path is still reachable
        steps = simulate_memory_and_find_path(
            grid_size, byte_positions[: i + 1], start, end, i + 1
        )
        if steps == -1:
            return x, y

    return None


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"
if choose == "toy":
    grid_size = 7
    end = (6, 6)
    num_bytes = 12
else:
    grid_size = 71
    end = (70, 70)
    num_bytes = 1024

byte_positions = parse_input(file_path)
start = (0, 0)

print(simulate_memory_and_find_path(grid_size, byte_positions, start, end, num_bytes))


blocking_byte = find_first_blocking_byte(grid_size, byte_positions, start, end)
if blocking_byte:
    print(f"{blocking_byte[0]},{blocking_byte[1]}")
