from itertools import product


def read_input(file_path):
    with open(file_path, "r") as f:
        data = f.read().strip().split("\n\n")
    machines = []
    for block in data:
        lines = block.split("\n")
        ax, ay = map(
            int, lines[0].replace("Button A: X+", "").replace(", Y+", ",").split(",")
        )
        bx, by = map(
            int, lines[1].replace("Button B: X+", "").replace(", Y+", ",").split(",")
        )
        px, py = map(
            int, lines[2].replace("Prize: X=", "").replace(", Y=", ",").split(",")
        )
        machines.append(((ax, ay), (bx, by), (px, py)))
    return machines


def solve_machine(a, b, prize):
    ax, ay = a
    bx, by = b
    px, py = prize

    solutions = []
    # All combinations bounded by 100 presses each
    for na, nb in product(range(101), repeat=2):
        dx = na * ax + nb * bx
        dy = na * ay + nb * by
        if dx == px and dy == py:
            cost = na * 3 + nb * 1
            solutions.append((cost, na, nb))

    if solutions:
        # Cheapest solution
        return min(solutions, key=lambda x: x[0])
    return None


def part_1(machines):
    min_total_tokens = 0
    prizes_won = 0

    for machine in machines:
        a, b, prize = machine
        result = solve_machine(a, b, prize)
        if result:
            cost, _, _ = result
            min_total_tokens += cost
            prizes_won += 1

    print(min_total_tokens)


# file_path = "toy_input.txt"
file_path = "puzzle_input.txt"

machines = read_input(file_path)
part_1(machines)
