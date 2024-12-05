def read_inputs(file_path):
    with open(file_path, "r") as file:
        content = file.read().strip()

    ordering_rules, page_updates = content.split("\n\n")

    ordering_rules = [
        tuple(map(int, pair.split("|"))) for pair in ordering_rules.split("\n")
    ]
    page_updates = [
        list(map(int, group.split(","))) for group in page_updates.split("\n")
    ]

    return ordering_rules, page_updates


def is_ordered(input_list, position_map):
    positions = [position_map.get(num, None) for num in input_list]
    positions = [pos for pos in positions if pos is not None]
    return positions == sorted(positions)


def update_position_map(pairs):
    position_map = {}
    for a, b in pairs:
        if a not in position_map and b not in position_map:
            position_map[a] = len(position_map)
            position_map[b] = len(position_map)
        elif a not in position_map:
            position_map[a] = position_map[b]
            for key in position_map:
                if position_map[key] >= position_map[a]:
                    position_map[key] += 1
        elif b not in position_map:
            position_map[b] = position_map[a] + 1
        elif position_map[a] > position_map[b]:
            for key, value in position_map.items():
                if position_map[a] <= value < position_map[b]:
                    position_map[key] += 1
            position_map[a] = position_map[b] - 1

    min_position = min(position_map.values(), default=0)
    if min_position < 0:
        for key in position_map:
            position_map[key] -= min_position

    return position_map


def find_middle(input_list):
    n = len(input_list)
    return (
        None
        if n == 0
        else (
            input_list[n // 2]
            if n % 2 == 1
            else (input_list[n // 2 - 1], input_list[n // 2])
        )
    )


def part_1(ordering_rules, page_updates):

    result = 0
    position_map = update_position_map(ordering_rules)
    print(position_map)
    for input_list in page_updates:
        if is_ordered(input_list, position_map):
            middle_number = find_middle(input_list)
            result += middle_number
    print(result)


# file_path = "toy_input.txt"
file_path = "puzzle_input.txt"
ordering_rules, page_updates = read_inputs(file_path)
part_1(ordering_rules, page_updates)
