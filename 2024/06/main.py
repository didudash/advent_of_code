# Directions: Up, Right, Down, Left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


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

    current_dir = 0  # Start moving upward
    current_pos = start_pos
    unique_positions = set([current_pos])

    while True:
        next_pos = (
            current_pos[0] + DIRECTIONS[current_dir][0],
            current_pos[1] + DIRECTIONS[current_dir][1],
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


def part_2(grid):
    """
    Simulates movement on the grid to detect loops.
    """
    start_pos = find_position_of_guard(grid)
    if not start_pos:
        return 0

    loop_count = 0

    for cell, value in grid.items():
        if value == "#":
            continue

        current_pos = start_pos
        current_dir = 0
        visited_states = {}
        grid[cell] = "#"  # Temporarily mark the cell as an obstacle

        while current_pos in grid:
            if grid[current_pos] == "#":
                # Step back and turn 90 degrees to the right
                current_pos = (
                    current_pos[0] - DIRECTIONS[current_dir][0],
                    current_pos[1] - DIRECTIONS[current_dir][1],
                )
                current_dir = (current_dir + 1) % 4
                continue

            state = (current_pos, current_dir)
            if state in visited_states:
                loop_count += 1
                break

            visited_states[state] = True  # Mark the state as visited
            current_pos = (
                current_pos[0] + DIRECTIONS[current_dir][0],
                current_pos[1] + DIRECTIONS[current_dir][1],
            )

        grid[cell] = "."  # Restore the original cell value

    print(loop_count)


file_path = "puzzle_input.txt"
grid = parse_txt_to_dict(file_path)
part_1(grid)
part_2(grid)
