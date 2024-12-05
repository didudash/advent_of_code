# Rework based in the solution of: Fadi88
# https://raw.githubusercontent.com/Fadi88/AoC/refs/heads/master/2024/day05/code.py

from collections import defaultdict


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


def update_position_map(ordering_rules):
    position_map = defaultdict(list)
    for a, b in ordering_rules:
        position_map[a].append(b)
    return position_map


def is_ordered(input_list, position_map):
    for i, page in enumerate(input_list):
        if not all(page2 in position_map[page] for page2 in input_list[i + 1 :]):
            return False
    return True


def find_middle(input_list):
    n = len(input_list)
    return (
        input_list[n // 2]
        if n % 2 == 1
        else (input_list[n // 2 - 1] + input_list[n // 2]) // 2
    )


def part_1(file_path):
    ordering_rules, page_updates = read_inputs(file_path)
    position_map = update_position_map(ordering_rules)

    result = 0
    for input_list in page_updates:
        if is_ordered(input_list, position_map):
            result += find_middle(input_list)
    print(result)


def part_2(file_path):
    ordering_rules, page_updates = read_inputs(file_path)
    position_map = update_position_map(ordering_rules)

    result = 0
    for input_list in page_updates:
        if not is_ordered(input_list, position_map):
            to_sort = set(input_list)
            sorted_list = []
            while to_sort:
                for n in to_sort:
                    if all(n2 in position_map[n] for n2 in to_sort if n2 != n):
                        sorted_list.append(n)
                        to_sort.remove(n)
                        break
            result += find_middle(sorted_list)
    print(result)


file_path = "puzzle_input.txt"

part_1(file_path)
part_2(file_path)
