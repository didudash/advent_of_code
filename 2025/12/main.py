import re


def parse_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return [list(map(int, re.findall(r"\d+", line))) for line in lines[30:]]


def part_1(data):
    answer = 0
    for region in data:
        w, h = region[0], region[1]
        present_counts = region[2:]

        capacity = (w // 3) * (h // 3)
        total_presents = sum(present_counts)

        if capacity >= total_presents:
            answer += 1

    return answer


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
