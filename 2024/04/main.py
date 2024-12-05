# Rework based in the solution of: i_have_no_biscuits
# https://www.reddit.com/r/adventofcode/comments/1h689qf/comment/m0bsh3p/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button


def parse_txt_to_dict(file_path):
    """Parse the grid into a dictionary of (y, x): c."""
    with open(file_path, "r") as file:
        data = file.readlines()
    height, width = len(data), len(data[0].strip())
    return {(y, x): data[y][x] for y in range(height) for x in range(width)}


def get_candidate_sequence(grid, y, x, dy, dx, length):
    return "".join(grid.get((y + dy * i, x + dx * i), "") for i in range(length))


def find_target(grid, target):
    """Find the occurrences of the target sequence in the grid."""
    deltas = [(dy, dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if dy != 0 or dx != 0]
    count = 0
    for y, x in grid:
        for dy, dx in deltas:
            if get_candidate_sequence(grid, y, x, dy, dx, len(target)) == target:
                count += 1
    return count


def find_mas_x(grid):
    """Find occurrences of MAS 'X' in the grid."""
    count = 0
    for (y, x), char in grid.items():
        if char == "A":
            lr = grid.get((y - 1, x - 1), "") + grid.get((y + 1, x + 1), "")
            rl = grid.get((y - 1, x + 1), "") + grid.get((y + 1, x - 1), "")
            if {lr, rl} <= {"MS", "SM"}:
                count += 1
    return count


def part_1(file_path):
    grid = parse_txt_to_dict(file_path)
    target = "XMAS"
    count = find_target(grid, target)
    print("Part 1:", count)


def part_2(file_path):
    grid = parse_txt_to_dict(file_path)
    count = find_mas_x(grid)
    print("Part 2:", count)


file_path = "puzzle_input.txt"
part_1(file_path)
part_2(file_path)
