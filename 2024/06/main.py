def parse_txt_to_dict(file_path):
    """Parse the grid into a dictionary of (y, x): symbol."""
    with open(file_path, "r") as file:
        data = file.readlines()
    height, width = len(data), len(data[0].strip())
    return {(y, x): data[y][x] for y in range(height) for x in range(width)}


def find_position_of_guard(grid):
    for position, value in grid.items():
        if value == "^":
            return position
    return None


def part_1(grid):
    start_pos = find_position_of_guard(grid)
    if not start_pos:
        return 0

    # Directions: Up, Right, Down, Left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0  # Start moving upward
    current_pos = start_pos
    unique_positions = set([current_pos])

    while True:
        next_pos = (
            current_pos[0] + directions[current_dir][0],
            current_pos[1] + directions[current_dir][1],
        )

        if next_pos not in grid:
            break

        if grid[next_pos] == "#":
            # Turn 90 degrees to the right
            current_dir = (current_dir + 1) % 4
        else:
            current_pos = next_pos
            unique_positions.add(current_pos)
            continue

    print(len(unique_positions))


# file_path = "toy_input.txt"
file_path = "puzzle_input.txt"
grid = parse_txt_to_dict(file_path)
part_1(grid)
