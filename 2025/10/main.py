from itertools import combinations


def parse_input(file_path):
    with open(file_path, "r") as f:
        return f.read().strip().split("\n")


def part_1(data):
    total = 0

    for line in data:
        pattern = line[line.index("[") + 1 : line.index("]")]
        target = [c == "#" for c in pattern]

        buttons = []
        for part in line.split("(")[1:]:
            if ")" in part:
                button = [int(x) for x in part[: part.index(")")].split(",")]
                buttons.append(button)

        for num_presses in range(len(buttons) + 1):
            found = False

            for button_combo in combinations(range(len(buttons)), num_presses):
                lights = [False] * len(target)

                for btn_idx in button_combo:
                    for light_idx in buttons[btn_idx]:
                        lights[light_idx] = not lights[light_idx]

                if lights == target:
                    total += num_presses
                    found = True
                    break

            if found:
                break

    return total


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
