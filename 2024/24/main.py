import re
from collections import deque


def parse_input(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    lines = data.strip().split("\n")
    initial_values = {
        line.split(": ")[0]: int(line.split(": ")[1]) for line in lines if ":" in line
    }
    gates = [line for line in lines if " -> " in line]
    return initial_values, gates


def simulate_gates(initial_values, gates):
    wire_values = initial_values.copy()
    pattern = re.compile(r"(\w+) (AND|OR|XOR) (\w+) -> (\w+)")

    dependencies = {gate.split(" -> ")[1]: gate for gate in gates}
    queue = deque([wire for wire in initial_values])

    while queue:
        wire = queue.popleft()
        for dependent, gate in list(dependencies.items()):
            match = pattern.match(gate)
            if not match:
                continue

            input1, operation, input2, output = match.groups()

            if input1 in wire_values and input2 in wire_values:
                val1 = wire_values[input1]
                val2 = wire_values[input2]

                if operation == "AND":
                    wire_values[output] = val1 & val2
                elif operation == "OR":
                    wire_values[output] = val1 | val2
                elif operation == "XOR":
                    wire_values[output] = val1 ^ val2

                queue.append(output)
                del dependencies[dependent]

    return wire_values


def part_1(wire_values):
    binary = "".join(
        str(wire_values[f"z{i:02}"])
        for i in range(len(wire_values))
        if f"z{i:02}" in wire_values
    )[::-1]
    return int(binary, 2)


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"
init_values, gates = parse_input(file_path)
wires = simulate_gates(init_values, gates)
print(part_1(wires))
