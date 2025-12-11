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


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
