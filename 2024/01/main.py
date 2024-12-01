def parse_two_column_file(file_path):
    with open(file_path, "r") as file:
        col1, col2 = zip(*(map(int, line.split()) for line in file))
    return list(col1), list(col2)


def sort_list_ascending(list):
    return sorted(list)


def subtract_pairs_absolute(list1, list2):
    return [abs(a - b) for a, b in zip(list1, list2)]


def part_1(list1, list2):

    sorted_list1 = sort_list_ascending(list1)
    sorted_list2 = sort_list_ascending(list2)

    distances = subtract_pairs_absolute(sorted_list1, sorted_list2)

    print(sum(distances))


def part_2(list1, list2):
    """
    Similarity Score
    """
    # See how many times each number of the list1 is in the list2
    counts = {num: list2.count(num) for num in list1}
    similarities = [num * counts[num] for num in list1]
    print(sum(similarities))


file_path = "puzzle_input.txt"
list1, list2 = parse_two_column_file(file_path)
part_1(list1, list2)
part_2(list1, list2)
