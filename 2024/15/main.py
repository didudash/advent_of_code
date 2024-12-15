from collections import defaultdict


def parse_input(file_path):

    with open(file_path, "r") as f:
        lines = f.read().strip().split("\n")
    grid = defaultdict(lambda: None)
    moves = ""

    for y, line in enumerate(lines):
        if line.strip() == "":
            # Ignore line breaks to catch all of the sequence
            moves = "".join(lines[y + 1 :])
            break
        for x, char in enumerate(line):
            grid[(x, y)] = char

    return grid, moves


def part_1(grid, moves):
    directions = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
    robot_pos = next(pos for pos, char in grid.items() if char == "@")

    for move in moves:
        dx, dy = directions[move]
        next_pos = (robot_pos[0] + dx, robot_pos[1] + dy)

        if grid[next_pos] == "#":
            continue

        # Handle multiple consecutive boxes
        if grid[next_pos] == "O":
            current_pos = next_pos
            boxes_to_push = []

            while grid[current_pos] == "O":
                boxes_to_push.append(current_pos)
                current_pos = (current_pos[0] + dx, current_pos[1] + dy)

            # Check if the last box can move
            if grid[current_pos] in (None, "#", "O"):
                continue

            for pos in reversed(boxes_to_push):
                new_pos = (pos[0] + dx, pos[1] + dy)
                grid[new_pos] = "O"
                grid[pos] = "."

        grid[robot_pos] = "."
        grid[next_pos] = "@"
        robot_pos = next_pos

    gps_sum = sum(y * 100 + x for (x, y), char in grid.items() if char == "O")
    print(gps_sum)


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"
grid, moves = parse_input(file_path)
part_1(grid, moves)
