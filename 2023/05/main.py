def extract_seeds(line):
    parts = line.split()
    seeds = [int(part) for part in parts if part.isdigit()]
    return seeds


def process_and_map(text_input, string_to_match, numbers):
    lines = text_input.split("\n")
    start_processing = False
    matrix = []

    for line in lines:
        if string_to_match in line:
            start_processing = True
            continue

        if start_processing and not line.strip():
            break

        if start_processing:
            parts = line.split()
            if len(parts) == 3 and all(part.isdigit() for part in parts):
                second_value = int(parts[0])
                first_value = int(parts[1])
                repeat_times = int(parts[2])

                for num in numbers:
                    delta = num - first_value
                    if delta in range(repeat_times):
                        matrix.append([num, first_value + delta + second_value])
                    else:
                        matrix.append([num, num])
                    # if first_value-nu
                    #     new_second_value = (num - first_value) + second_value
                    #     matrix.append([num, new_second_value])
                    # else:
                    #     matrix.append([num, num])

    return matrix


def add_missing_numbers_to_matrix(matrix, numbers):
    for number in numbers:
        if not matrix:
            matrix.append([number, number])
        else:
            first_column = [row[0] for row in matrix]
            if number not in first_column:
                matrix.append([number, number])
    return matrix


def merge_matrices(former_matrix, new_matrix):
    # Sort the former_matrix by its last column
    former_matrix_sorted = sorted(former_matrix, key=lambda row: row[-1])

    # Sort the new_matrix by its first column
    new_matrix_sorted = sorted(new_matrix, key=lambda row: row[0])

    # Merge the matrices
    merged_matrix = [
        former_row + new_row[1:]
        for former_row, new_row in zip(former_matrix_sorted, new_matrix_sorted)
    ]

    return merged_matrix


def lowest_location(filepath):
    strings_to_match = [
        "seed-to-soil map:",
        "soil-to-fertilizer map:",
        "fertilizer-to-water map:",
        "water-to-light map:",
        "light-to-temperature map:",
        "temperature-to-humidity map:",
        "humidity-to-location map:",
    ]
    with open(filepath, "r") as file:
        first_line = file.readline().strip()
        seeds = extract_seeds(first_line)
        print("length seeds, ", len(seeds))
        # print(seeds)
        file_content = file.read()
        former_mapping = []
        to_match = seeds
        for i in range(len(strings_to_match) - 1):
            # print(strings_to_match[i])
            # extract the values
            processed = process_and_map(file_content, strings_to_match[i], to_match)
            # print("length processed, ", len(processed))
            print("processed: \n", processed)
            if i == 0:
                # filtered = add_missing_numbers_to_matrix(processed, to_match)
                # print("length filtered, ", len(filtered))
                # print(filtered)
                # print("filtered", filtered)
                to_match = [row[-1] for row in processed]
                # print(to_match)
                former_mapping = processed

            else:
                # print(processed)
                # filtered = add_missing_numbers_to_matrix(
                #     processed, [row[-1] for row in former_mapping]
                # )
                # print("length filtered, ", len(filtered))
                new_mapping = merge_matrices(former_mapping, processed)
                to_match = [row[-1] for row in new_mapping]
                former_mapping = new_mapping

        # print(new_mapping)
        last_column = [row[-1] for row in new_mapping]
        # print(last_column)
        min_index = last_column.index(min(last_column))
        lowest_location_number = last_column[min_index]
        print(lowest_location_number)


# filepath = "puzzle_dummy.txt"
filepath = "puzzle_input.txt"
