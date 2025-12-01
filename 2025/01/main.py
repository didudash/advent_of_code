def parse_input(file_path):
    with open(file_path) as f:
        data = [int(line[1:]) * (-1 if line[0] == "L" else 1) for line in f]
        return data


def part_1(data):
    pos = 50
    psw = 0
    for n in data:
        # Circular
        pos = (pos + n) % 100
        if pos == 0:
            psw += 1
    return psw


def part_2(data):
    pos = 50
    psw = 0
    for n in data:
        dist = pos or 100 if n < 0 else 100 - pos
        steps = abs(n)
        if steps >= dist:
            # It includes first crossing
            psw += (steps - dist) // 100 + 1
        pos = (pos + n) % 100
    return psw


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
print(part_2(data))
