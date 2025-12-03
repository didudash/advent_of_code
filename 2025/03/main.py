def parse_input(file_path):
    with open(file_path) as f:
        return f.read().split()


def part_1(data):
    total_joltage = 0
    for l in data:
        max_left = 0
        joltage = 0

        for char in l:
            digit = int(char)
            joltage = max(joltage, max_left * 10 + digit)
            max_left = max(max_left, digit)

        total_joltage += joltage

    return total_joltage


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
