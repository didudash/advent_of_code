import numpy as np

# filepath = "puzzle_dummy.txt"
filepath = "puzzle_input.txt"


# def find_positions(group):
#     positions = []
#     for i, line in enumerate(group.split("\n")):
#         for j, char in enumerate(line):
#             if char == "#":
#                 positions.append((i, j))
#     return positions


# def find_dict_twins(d):
#     twins = []
#     keys_visited = set()
#     for key1 in d:
#         for key2 in d:
#             if key1 != key2 and key1 not in keys_visited and key2 not in keys_visited:
#                 if sorted(d[key1]) == sorted(d[key2]):
#                     twins.append((key1, key2))
#                     keys_visited.add(key1)
#                     keys_visited.add(key2)
#     return twins


# def find_twins(positions):
#     rows = {}
#     cols = {}
#     for row, col in positions:
#         rows.setdefault(row, []).append(col)
#         cols.setdefault(col, []).append(row)

#     row_twins = find_dict_twins(rows)
#     col_twins = find_dict_twins(cols)

#     return row_twins, col_twins


# def check_symmetry(pairs, num):
#     # Convert list of tuples into a set for faster lookup
#     pairs_set = set(pairs)
#     first_consecutive_pair = None
#     for pair in pairs:
#         # Ensure the pair is sorted (smaller number first)
#         a, b = sorted(pair)
#         if b - a == 1 and first_consecutive_pair is None:
#             first_consecutive_pair = a
#         # Iterate outwards from each pair
#         while 0 <= a and b < num:
#             # Check for corresponding pair in the set
#             if (a, b) not in pairs_set and (b, a) not in pairs_set:
#                 return -1
#             # Move outwards
#             a -= 1
#             b += 1
#     if first_consecutive_pair is not None:
#         return first_consecutive_pair + 1
#     else:
#         return -1


# with open(filepath, "r") as file:
#     groups = file.read().strip().split("\n\n")

# pattern_notes = 0
# for group in groups:
#     rows = group.split("\n")
#     num_rows = len(rows)
#     num_cols = len(rows[0])
#     # print(f"num rows {num_rows}, num cols {num_cols}")
#     pos_per_group = find_positions(group)
#     row_twins, col_twins = find_twins(pos_per_group)
#     # print(f"row twins {row_twins}, col twins {col_twins}")
#     row_result = check_symmetry(row_twins, num_rows)
#     col_result = check_symmetry(col_twins, num_cols)
#     if col_result > 0:
#         pattern_notes += col_result
#     if row_result > 0:
#         pattern_notes += 100 * row_result
# print(pattern_notes)

with open(filepath, "r") as file:
    stream_pre = file.read().split("\n\n")
stream = [line.splitlines() for line in stream_pre]


def symmetry(arr, margin):
    """Find line of symmetry in 2D array"""
    i = 1
    while i < len(arr):
        lhs = arr[:i]
        rhs = arr[i:]
        if len(lhs) > len(rhs):
            lhs = lhs[len(lhs) - len(rhs) :]
        elif len(rhs) > len(lhs):
            rhs = rhs[: len(lhs)]
        rhs = np.flip(rhs, axis=0)
        if np.count_nonzero(lhs != rhs) == margin:
            return i
        i += 1
    return False


def iterate(margin):
    """Iterate across all puzzles and get symmetry score"""
    r = 0
    for dis in stream:
        data = np.array([list(l) for l in dis])
        transpose = data.T

        val = symmetry(transpose, margin)
        if not val:
            val = 100 * symmetry(data, margin)
        r += val
    return r


print("Part 1:", iterate(0))
print("Part 2:", iterate(1))
