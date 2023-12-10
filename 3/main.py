import re
from functools import reduce

DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 1), (1, 0), (0, -1), (-1, 0)]
PATTERN_NUMBERS = r"[0-9]+"


def read_file_to_matrix(file_path):
    matrix = []
    with open(file_path, "r") as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix


def is_adjacent_to_symbol(matrix, matrix_pos, num_rows, num_cols):
    "includes even diagnoally"
    "symbol doesn't include ."
    num_adjacent = 0
    for d in DIRECTIONS:
        new_row, new_col = matrix_pos[0] + d[0], matrix_pos[1] + d[1]
        if new_row >= 0 and new_row < num_rows and new_col >= 0 and new_col < num_cols:
            element = matrix[new_row][new_col]
            if re.match(PATTERN_NUMBERS, element) or element == ".":
                pass
            else:
                num_adjacent += 1
    if num_adjacent > 0:
        return True
    else:
        return False


def is_adjacent_to_number(matrix, matrix_pos, num_rows, num_cols):
    "includes even diagnoally"
    num_adjacent = 0
    for d in DIRECTIONS:
        new_row, new_col = matrix_pos[0] + d[0], matrix_pos[1] + d[1]
        if new_row >= 0 and new_row < num_rows and new_col >= 0 and new_col < num_cols:
            element = matrix[new_row][new_col]
            if re.match(PATTERN_NUMBERS, element):
                num_adjacent += 1
            else:
                pass
    if num_adjacent > 0:
        return True
    else:
        return False


def adjacent_numbers(matrix, matrix_pos, num_rows, num_cols):
    number_list = []
    added_positions = []
    for d in DIRECTIONS:
        new_row, new_col = matrix_pos[0] + d[0], matrix_pos[1] + d[1]
        if new_row >= 0 and new_row < num_rows and new_col >= 0 and new_col < num_cols:
            element = matrix[new_row][new_col]
            if re.match(PATTERN_NUMBERS, element):
                number, positions = get_complete_number_and_positions(
                    matrix[new_row], new_col
                )
                positions_in_tuples = [(new_row, num) for num in positions]
                if not any(tup in added_positions for tup in positions_in_tuples):
                    number_list.append(number)
                    added_positions.extend(positions_in_tuples)
                else:
                    pass
    return len(number_list), number_list


def is_number(element):
    if re.match(PATTERN_NUMBERS, element):
        return True
    else:
        return False


def num_pos_to_consume(matrix_row):
    numbers_consume = {}
    for i in range(len(matrix_row)):
        if is_number:
            numbers_consume[i] = False
        else:
            pass
    return numbers_consume


def consumed_update(positions, numbers_consume):
    for pos in positions:
        consumed = numbers_consume[pos]
        if consumed:
            return True, numbers_consume
        else:
            numbers_consume[pos] = True

    return False, numbers_consume


def get_complete_number_and_positions(matrix_row, col_index):
    num_cols = len(matrix_row)
    num_and_pos = {}
    num_and_pos[col_index] = matrix_row[col_index]
    for pos in range(col_index - 1, -1, -1):
        element = matrix_row[pos]
        if is_number(element):
            num_and_pos[pos] = element
        else:
            break
    for pos in range(col_index, num_cols):
        element = matrix_row[pos]
        if is_number(element):
            num_and_pos[pos] = element
        else:
            break
    # Now reconstruct number
    number = int("".join(str(num_and_pos[key]) for key in sorted(num_and_pos.keys())))
    positions = list(num_and_pos.keys())
    return number, positions


def sum_part_numbers(file_path):
    matrix = read_file_to_matrix(file_path)
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    part_number_total = 0
    for i in range(num_rows):
        numbers_consume = num_pos_to_consume(matrix[i])
        for j in range(num_cols):
            if is_number(matrix[i][j]):
                matrix_pos = (i, j)
                if is_adjacent_to_symbol(matrix, matrix_pos, num_rows, num_cols):
                    number, positions = get_complete_number_and_positions(matrix[i], j)
                    # If index not consumed
                    has_been_consumed, numbers_consume = consumed_update(
                        positions, numbers_consume
                    )
                    if not has_been_consumed:
                        part_number_total += number

    return part_number_total


def sum_gear_ratios(file_path):
    matrix = read_file_to_matrix(file_path)
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    nums_and_pos = {}
    gear_ratios_total = 0
    for i in range(num_rows):
        # Check for asterisk
        for j in range(num_cols):
            if matrix[i][j] == "*":
                matrix_pos = (i, j)
                num_adjacent, number_list = adjacent_numbers(
                    matrix, matrix_pos, num_rows, num_cols
                )
                if num_adjacent == 2:
                    gear_ratios_total += reduce(lambda x, y: x * y, number_list)

    return gear_ratios_total


part_number_total = sum_part_numbers("puzzle_input.txt")
print(f"part number total: {part_number_total}")
gear_ratios_total = sum_gear_ratios("puzzle_input.txt")
print(f"gear_ratios_total: {gear_ratios_total}")
