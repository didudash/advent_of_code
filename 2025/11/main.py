def parse_input(file_path):
    graph = {}
    with open(file_path, "r") as f:
        for line in f:
            if line.strip():
                device, outputs = line.split(":")
                graph[device.strip()] = outputs.split()
    return graph


def part_1(data):
    def count_paths(current):
        if current == "out":
            return 1
        if current not in data:
            return 0

        total = 0
        for next_node in data[current]:
            total += count_paths(next_node)
        return total

    return count_paths("you")


def part_2(data):
    memo = {}

    def count_paths(current, visited_dac, visited_fft):
        key = (current, visited_dac, visited_fft)
        if key in memo:
            return memo[key]

        if current == "dac":
            visited_dac = True
        if current == "fft":
            visited_fft = True

        if current == "out":
            return 1 if (visited_dac and visited_fft) else 0

        if current not in data:
            return 0

        total = 0
        for next_node in data[current]:
            total += count_paths(next_node, visited_dac, visited_fft)

        memo[key] = total
        return total

    return count_paths("svr", False, False)


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
print(part_2(data))
