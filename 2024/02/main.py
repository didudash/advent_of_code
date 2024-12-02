def parse_rows_numbers_from_txt(file_path):
    with open(file_path, "r") as file:
        return [list(map(int, line.split())) for line in file]


def is_increasing_and_valid(report):
    return all(
        report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3
        for i in range(len(report) - 1)
    )


def is_decreasing_and_valid(report):
    return all(
        report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3
        for i in range(len(report) - 1)
    )


def is_safish(report):
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if is_increasing_and_valid(new_report):
            return True
        elif is_decreasing_and_valid(new_report):
            return True


def part_1(reports):
    safe = 0
    for report in reports:
        if is_increasing_and_valid(report):
            safe += 1
        elif is_decreasing_and_valid(report):
            safe += 1
    print(safe)


def part_2(reports):
    safe = 0
    safish = 0
    for report in reports:
        if is_increasing_and_valid(report):
            safe += 1
        elif is_decreasing_and_valid(report):
            safe += 1
        else:
            if is_safish(report):
                safish += 1
    print(safe + safish)


file_path = "puzzle_input.txt"
reports = parse_rows_numbers_from_txt(file_path)
part_1(reports)
part_2(reports)
