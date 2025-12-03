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


def part_2(data, batteries_n=12):
    total_joltage = 0
    for l in data:
        number = []
        remaining = batteries_n
        n = len(l)
        start = 0

        while remaining > 0:
            can_skip = n - start - remaining
            best_digit = l[start]
            best_pos = start

            for i in range(start, start + can_skip + 1):
                if l[i] > best_digit:
                    best_digit = l[i]
                    best_pos = i

            number.append(best_digit)
            start = best_pos + 1
            remaining -= 1

        joltage = int("".join(number))

        total_joltage += joltage

    return total_joltage


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
print(part_2(data))
assert part_1(data) == part_2(data, batteries_n=2)
print("The approach for part 2 can be extended to part 1")
