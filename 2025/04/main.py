def parse_input(file_path):
    with open(file_path) as f:
        return [list(row) for row in f.read().split()]


def count_neighbors(data, row, col, char):
    rows, cols = len(data), len(data[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and data[r][c] == char:
            count += 1

    return count


def part_1(data):
    rolls = 0
    rows, cols = len(data), len(data[0])

    for row in range(rows):
        for col in range(cols):
            if data[row][col] != "@":
                continue

            if count_neighbors(data, row, col, "@") < 4:
                rolls += 1

    return rolls


def part_2(data):
    total_rolls = 0
    rows, cols = len(data), len(data[0])

    while True:
        to_remove = []

        for row in range(rows):
            for col in range(cols):
                if data[row][col] != "@":
                    continue

                if count_neighbors(data, row, col, "@") < 4:
                    to_remove.append((row, col))

        if not to_remove:
            break

        for row, col in to_remove:
            data[row][col] = ""
            total_rolls += 1

    return total_rolls


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
print(part_2(data))
