import re


def parse_valid_mul_from_file(file_path):
    with open(file_path, "r") as file:
        input_string = file.read()

    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input_string)
    parsed_list = [[int(num1), int(num2)] for num1, num2 in matches]

    return parsed_list


def part_1(parsed_output):
    # Sum of products of mul pairs
    print(sum([eval("*".join(map(str, sublist))) for sublist in parsed_output]))


def part_2(file_path):
    with open(file_path, "r") as file:
        input_string = file.read()
    valid = True
    parsed_output = []

    pattern = re.compile(r"mul\((\d+),(\d+)\)")

    for token in re.finditer(r"(mul\(\d+,\d+\)|don't|do\(\))", input_string):
        match = token.group(0)

        if match == "don't":
            valid = False
        elif match == "do()":
            valid = True
        elif valid and pattern.match(match):
            numbers = list(map(int, pattern.match(match).groups()))
            parsed_output.append(numbers)

    print(sum([eval("*".join(map(str, sublist))) for sublist in parsed_output]))


file_path = "puzzle_input.txt"
parsed_output = parse_valid_mul_from_file(file_path)
part_1(parsed_output)
part_2(file_path)
