import re


def parse_and_sum_selected_numbers(file_path):
    total_sum = 0
    parsed_lines = []

    with open(file_path, "r") as file:
        for line in file:
            numbers = "".join(filter(str.isdigit, line))
            selected_numbers = numbers[:1] + numbers[-1:] if numbers else ""
            parsed_lines.append(f"{line.rstrip()}: {selected_numbers}")
            if selected_numbers:
                total_sum += int(selected_numbers)

    return parsed_lines, total_sum


def text_to_int(text):
    word_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    text = text.lower()
    for word in word_to_num:
        if re.match(word, text):
            return word_to_num[word]

    return None


def parse_and_sum_selected_numbers_full(file_path):
    total_sum = 0
    parsed_lines = []

    with open(file_path, "r") as file:
        for line in file:
            line_length = len(line)
            numbers = []
            for i in range(line_length):
                if line[i].isdigit():
                    numbers.append(line[i])
                else:
                    forward_chars = line[i : i + 5]
                    number = text_to_int(forward_chars)
                    if number is not None:
                        numbers.append(number)
                    else:
                        pass
            print(numbers)
            selected_numbers = numbers[:1] + numbers[-1:] if numbers else ""
            int_selected_numbers = int(
                "".join([str(item) for item in selected_numbers])
            )
            parsed_lines.append(f"{line.rstrip()}: {int_selected_numbers}")
            if selected_numbers:
                total_sum += int(int_selected_numbers)

    return parsed_lines, total_sum


file_path = "puzzle_input.txt"
parsed_lines_part_1, total_sum_part_1 = parse_and_sum_selected_numbers(file_path)
parsed_lines_part_2, total_sum_part_2 = parse_and_sum_selected_numbers_full(file_path)
print(f"Solution part 1: {total_sum_part_1}")
print(f"Solution part 2: {total_sum_part_2}")
