def parse_input(file_path):
    with open(file_path, "r") as f:
        lines = [line.split() for line in f]

    data, ops = lines[:-1], lines[-1]
    return [
        {"val": [int(data[r][c]) for r in range(len(data))], "op": ops[c]}
        for c in range(len(data[0]))
    ]


def part_1(data):
    total = 0
    for col in data:
        result = col["val"][0]
        for num in col["val"][1:]:
            if col["op"] == "*":
                result *= num
            else:
                result += num
        total += result
    return total


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
