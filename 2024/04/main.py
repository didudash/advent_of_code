def parse_txt_to_grid(file_path):
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file]


def is_valid(r, c, rows, cols):
    """Is it within the grid."""
    return 0 <= r < rows and 0 <= c < cols


def check_sequence(start_r, start_c, sequence, rows, cols, directions):
    """Check for the given sequence starting from a specific position."""
    # TODO: Fix duplicates
    for dr, dc in directions:
        found = True
        for k in range(len(sequence)):
            nr, nc = start_r + dr * k, start_c + dc * k
            if not is_valid(nr, nc, rows, cols) or grid[nr][nc] != sequence[k]:
                found = False
                break
        if found:
            return True
    return False


def part_1(grid):
    word_count = 0
    rows, cols = len(grid), len(grid[0])

    directions = [
        (0, 1),  # Down
        (1, 0),  # Right
        (1, 1),  # Down-Right
        (1, -1),  # Down-Left
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1),  # Up-Right
        (-1, 1),  # Up-Left
    ]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "X" and check_sequence(
                r, c, "XMAS", rows, cols, directions
            ):
                word_count += 1
            elif grid[r][c] == "S" and check_sequence(
                r, c, "SAMX", rows, cols, directions
            ):
                word_count += 1

    print(word_count)


file_path = "toy_input.txt"
grid = parse_txt_to_grid(file_path)
part_1(grid)
