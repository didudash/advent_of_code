def parse_input(file_path):
    with open(file_path) as f:
        return f.read().split()


def part_1(data):
    rolls = 0
    rows, cols = len(data), len(data[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for row in range(rows):
        for col in range(cols):
            if data[row][col] != "@":
                continue

            at_count = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and data[r][c] == "@":
                    at_count += 1

            if at_count < 4:
                rolls += 1

    return rolls


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
