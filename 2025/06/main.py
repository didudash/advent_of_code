def parse_input(file_path):
    with open(file_path, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    return {"lines": lines[:-1], "ops": lines[-1].split()}


def part_1(data):
    split_data = [line.split() for line in data["lines"]]
    ops = data["ops"]

    total = 0
    for c in range(len(split_data[0])):
        vals = [int(split_data[r][c]) for r in range(len(split_data))]
        result = vals[0]
        for num in vals[1:]:
            result = result * num if ops[c] == "*" else result + num
        total += result
    return total


def part_2(data):
    lines = data["lines"]
    ops = data["ops"]
    max_len = max(len(line) for line in lines)

    total = 0
    op_idx = len(ops) - 1
    pos = max_len - 1
    column_nums = []

    while pos >= 0:
        digits = [
            line[pos] for line in lines if pos < len(line) and line[pos].isdigit()
        ]

        if digits:
            column_nums.append(int("".join(digits)))

            next_is_space = pos == 0 or not any(
                pos - 1 < len(line) and line[pos - 1].isdigit() for line in lines
            )

            if next_is_space:
                result = column_nums[0]
                for val in column_nums[1:]:
                    result = result * val if ops[op_idx] == "*" else result + val
                total += result
                column_nums = []
                op_idx -= 1

        pos -= 1

    return total


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
print(part_2(data))
