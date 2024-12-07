from itertools import product

# Remenber that keys of a dict should be unique so if there are two values that
# are the same this will only include one of them


def read_and_parse_to_dict(file_path, split_char):
    with open(file_path, "r") as file:
        input_data = file.read()

    data_dict = {}
    for line in input_data.strip().split("\n"):
        key, values = line.split(split_char)
        key = int(key.strip())
        values_list = list(map(int, values.strip().split()))

        if key not in data_dict:
            data_dict[key] = []
        data_dict[key].append(
            values_list
        )  # Store each entry as a separate list of values
    return data_dict


def evaluate_left_to_right(values, target):
    if len(values) == 1:
        return values[0] == target

    num_operators = len(values) - 1
    for operators in product(["+", "*"], repeat=num_operators):
        result = values[0]
        for i, op in enumerate(operators):
            if op == "+":
                result += values[i + 1]
            elif op == "*":
                result *= values[i + 1]
        if result == target:
            return True
    return False


def part_1(data_dict):
    matching_test_values_sum = 0
    for key, all_values in data_dict.items():
        for values in all_values:
            if evaluate_left_to_right(values, key):
                matching_test_values_sum += key

    print(matching_test_values_sum)


file_path = "puzzle_input.txt"
data_dict = read_and_parse_to_dict(file_path, ":")
part_1(data_dict)
