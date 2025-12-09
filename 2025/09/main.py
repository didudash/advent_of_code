# Parse positions
def parse_input(file_path):
    with open(file_path, "r") as f:
        return [tuple(map(int, line.strip().split(","))) for line in f if line.strip()]


def part_1(data):
    max_area = 0

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1 = data[i]
            x2, y2 = data[j]

            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height

            if area > max_area:
                max_area = area

    return max_area


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
