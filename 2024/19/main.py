def parse_input(file_path):
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")

    towel_patterns = lines[0].split(", ")
    designs = lines[2:]
    return towel_patterns, designs


def count_possible_designs_and_arrangements(towel_patterns, designs):
    possible_count = 0  # For part 1
    total_arrangements = 0  # For part 2

    for design in designs:
        dp = [False] * (len(design) + 1)
        ways = [0] * (len(design) + 1)
        dp[0] = True
        ways[0] = 1

        for i in range(1, len(design) + 1):
            for pattern in towel_patterns:
                if i >= len(pattern) and design[i - len(pattern) : i] == pattern:
                    if dp[i - len(pattern)]:
                        dp[i] = True
                        ways[i] += ways[i - len(pattern)]

        if dp[len(design)]:
            possible_count += 1
            total_arrangements += ways[len(design)]

    return possible_count, total_arrangements


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"


towel_patterns, designs = parse_input(file_path)
possible_count, total_arrangements = count_possible_designs_and_arrangements(
    towel_patterns, designs
)
print(possible_count)
print(total_arrangements)
