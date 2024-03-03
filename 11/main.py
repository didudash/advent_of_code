import numpy as np
from itertools import combinations

# filepath = "puzzle_dummy.txt"
filepath = "puzzle_input.txt"

with open(filepath, "r") as file:
    lines = file.readlines()

data = [list(line.strip()) for line in lines]
dataset = np.array(data)
char = "#"


def rows_cols_without_char(dataset, char):
    rows_wo_char = np.where(~np.any(dataset == char, axis=1))[0]
    cols_wo_char = np.where(~np.any(dataset == char, axis=0))[0]
    return rows_wo_char, cols_wo_char


def pos_with_char(dataset, char):
    positions = np.where(dataset == char)
    pos_pairs = list(zip(positions[0], positions[1]))
    return pos_pairs


def add_comb_paths(pos_pairs):
    sum_short_path = 0
    for pair1, pair2 in combinations(pos_pairs, 2):
        short_path = abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1])
        sum_short_path += short_path
    print(sum_short_path)


def add_cumulative_offset(rows, cols, positions, offset):
    new_positions = []
    for pos in positions:
        row, col = pos
        row_offset = sum(row > r for r in rows) * offset
        row += row_offset
        col_offset = sum(col > c for c in cols) * offset
        col += col_offset
        new_positions.append((row, col))
    return new_positions


def sum_of_paths(offset):
    rows_wo_char, cols_wo_char = rows_cols_without_char(dataset, char)
    pos_pairs = pos_with_char(dataset, char)
    new_positions = add_cumulative_offset(rows_wo_char, cols_wo_char, pos_pairs, offset)
    add_comb_paths(new_positions)


def part_1():
    sum_of_paths(1)


def part_2():
    sum_of_paths(1_000_000 - 1)


part_1()
part_2()
