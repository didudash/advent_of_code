def parse_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip().split("\n")


def part_1(data):
    total = 0

    for line in data:
        pattern = line[line.index("[") + 1 : line.index("]")]
        target = [c == "#" for c in pattern]

        buttons = []
        rest = line[line.index("]") + 1 :]
        for part in rest.split("(")[1:]:
            if ")" in part:
                button = [int(x) for x in part[: part.index(")")].split(",")]
                buttons.append(button)

        min_presses = float("inf")

        for mask in range(1 << len(buttons)):
            lights = [False] * len(target)

            for i, button in enumerate(buttons):
                if mask & (1 << i):
                    for light_idx in button:
                        lights[light_idx] = not lights[light_idx]

            if lights == target:
                presses = bin(mask).count("1")
                min_presses = min(min_presses, presses)

        total += min_presses

    return total


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
