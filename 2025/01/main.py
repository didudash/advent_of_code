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


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)
# print(data)
print(part_1(data))
