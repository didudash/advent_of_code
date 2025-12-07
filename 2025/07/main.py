def parse_input(file_path):
    with open(file_path, "r") as f:
        grid = [line.rstrip("\n") for line in f]

    start_col = grid[0].index("S")
    return grid, start_col


def part_1(data):
    grid, start_col = data
    rows, cols = len(grid), len(grid[0])

    beams = [(1, start_col)]
    processed = set()
    splits = 0

    while beams:
        new_beams = []
        for r, c in beams:
            if r >= rows or c < 0 or c >= cols or (r, c) in processed:
                continue

            processed.add((r, c))

            if grid[r][c] == "^":
                splits += 1
                if c > 0:
                    new_beams.append((r + 1, c - 1))
                if c < cols - 1:
                    new_beams.append((r + 1, c + 1))
            else:
                new_beams.append((r + 1, c))

        beams = new_beams

    return splits


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
