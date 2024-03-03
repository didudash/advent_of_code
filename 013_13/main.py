import numpy as np

filepath = "puzzle_dummy.txt"
# filepath = "puzzle_input.txt"


def find_positions(group):
    positions = []
    for i, line in enumerate(group.split("\n")):
        for j, char in enumerate(line):
            if char == "#":
                positions.append((i, j))
    return positions


def find_dict_twins(d):
    twins = []
    keys_visited = set()
    for key1 in d:
        for key2 in d:
            if key1 != key2 and key1 not in keys_visited and key2 not in keys_visited:
                if sorted(d[key1]) == sorted(d[key2]):
                    twins.append((key1, key2))
                    keys_visited.add(key1)
                    keys_visited.add(key2)
    return twins


def find_twins(positions):
    rows = {}
    cols = {}
    for row, col in positions:
        rows.setdefault(row, []).append(col)
        cols.setdefault(col, []).append(row)

    row_twins = find_dict_twins(rows)
    col_twins = find_dict_twins(cols)

    return row_twins, col_twins


with open(filepath, "r") as file:
    groups = file.read().strip().split("\n\n")

for group in groups:
    rows = group.split("\n")
    num_rows = len(rows)
    num_cols = len(rows[0])
    print(f"num rows {num_rows}, num cols {num_cols}")
    pos_per_group = find_positions(group)
    row_twins, col_twins = find_twins(pos_per_group)
    print(f"row twins {row_twins}, col twins {col_twins}")


# Define symetry if columns (or rows) contiguous
# use the num_rows and num_cols

# add nummber of cols before the inflection

# add number of rows*100 before the inflection
