import math
import numpy as np
from itertools import combinations

# filepath = "puzzle_dummy.txt"
filepath = "puzzle_input.txt"

with open(filepath, "r") as file:
    lines = file.readlines()

data = [list(line.strip()) for line in lines]
dataset = np.array(data)

char = "#"

rows_wo_char = np.where(~np.any(dataset == char, axis=1))[0]
cols_wo_char = np.where(~np.any(dataset == char, axis=0))[0]
print(rows_wo_char)
print(cols_wo_char)


# does it make sense appending them?
def part_1():
    # Appending new rows
    dataset = np.insert(dataset, rows_wo_char, ".", axis=0)
    # Appending new columns
    dataset = np.insert(dataset, cols_wo_char, ".", axis=1)

    positions = np.where(dataset == char)
    pos_pairs = list(zip(positions[0], positions[1]))

    sum_short_path = 0

    for pair1, pair2 in combinations(pos_pairs, 2):
        short_path = abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1])
        if short_path != 0:
            sum_short_path += short_path

    print(sum_short_path)
