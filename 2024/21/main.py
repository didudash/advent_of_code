from functools import cache
from itertools import permutations

# Numeric keypad
num_keypad = {
    char: (x, y)
    for y, line in enumerate(["789", "456", "123", " 0A"])
    for x, char in enumerate(line)
    if char != " "
}

# Directional keypad
dir_keypad = {
    char: (x, y)
    for y, line in enumerate([" ^A", "<v>"])
    for x, char in enumerate(line)
    if char != " "
}

# Directional movement
directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


@cache
def calculate_presses(sequence, depth=2, use_dir_keypad=False, current=None):
    """Recursively calculates the minimum presses to type a sequence."""
    keypad = dir_keypad if use_dir_keypad else num_keypad
    if not sequence:
        return 0
    if not current:
        current = keypad["A"]

    cx, cy = current
    px, py = keypad[sequence[0]]
    dx, dy = px - cx, py - cy

    moves = ("<" * -dx if dx < 0 else ">" * dx) + ("^" * -dy if dy < 0 else "v" * dy)

    if depth:
        lengths = []
        for perm in set(permutations(moves)):
            test_x, test_y = current
            for step in perm:
                delta_x, delta_y = directions[step]
                test_x += delta_x
                test_y += delta_y
                if (test_x, test_y) not in keypad.values():
                    break
            else:
                lengths.append(calculate_presses(perm + ("A",), depth - 1, True))
        min_length = min(lengths)
    else:
        min_length = len(moves) + 1

    return min_length + calculate_presses(sequence[1:], depth, use_dir_keypad, (px, py))


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"
with open(file_path) as file:
    codes = file.read().splitlines()

part1, part2 = 0, 0
for code in codes:
    numeric_value = int(code[:-1])
    part1 += numeric_value * calculate_presses(code)
    part2 += numeric_value * calculate_presses(code, 25)

print(part1)
print(part2)
