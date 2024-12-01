def get_score(common_count):
    if common_count == 0:
        return 0
    else:
        return 2 ** (common_count - 1)


def points_in_scratchcards(filepath):
    with open(filepath, "r") as file:
        total_score = 0
        for line in file:
            winning_numbers = []
            your_numbers = []
            common_numbers = []

            before_pipe, after_pipe = line.split("|")

            numbers_before = [int(num) for num in before_pipe.split() if num.isdigit()]
            winning_numbers.append(numbers_before)

            numbers_after = [int(num) for num in after_pipe.split() if num.isdigit()]
            your_numbers.append(numbers_after)

            for before, after in zip(winning_numbers, your_numbers):
                common = [num for num in after if num in before]
                common_numbers.extend(common)
            common_count = len(common_numbers)
            total_score += get_score(common_count)
    return total_score


def get_matches_per_card(filepath):
    with open(filepath, "r") as file:
        matches_per_card = {}
        for line in file:
            card_label, _ = line.split(":")
            card_number = int(card_label.split()[-1])
            winning_numbers = []
            your_numbers = []
            common_numbers = []

            before_pipe, after_pipe = line.split("|")

            numbers_before = [int(num) for num in before_pipe.split() if num.isdigit()]
            winning_numbers.append(numbers_before)

            numbers_after = [int(num) for num in after_pipe.split() if num.isdigit()]
            your_numbers.append(numbers_after)

            for before, after in zip(winning_numbers, your_numbers):
                common = [num for num in after if num in before]
                common_numbers.extend(common)
            common_count = len(common_numbers)
            matches_per_card[card_number] = common_count
    return matches_per_card


def count_found_instances(filepath):
    matches_per_card = get_matches_per_card(filepath)
    cards_won = {}
    for key, value in matches_per_card.items():
        card_number = int(key)
        matches = int(value)
        cards_won_list = []
        for card in range(card_number + 1, matches + card_number + 1):
            cards_won_list.append(card)
        cards_won[card_number] = cards_won_list
    # adding all of the cards to the same matrix
    copies = []
    for key in cards_won.keys():
        copies.append(key)
    for values in cards_won.values():
        copies.extend(values)
    found_instances = 0
    for key in cards_won.keys():
        found_copies = copies.count(key)
        for _ in range(found_copies - 1):
            if cards_won[key]:
                copies.extend(cards_won[key])
        found_instances += found_copies
    return found_instances


filepath = "puzzle_input.txt"
points_part_1 = points_in_scratchcards(filepath)
print(points_part_1)
found_instances = count_found_instances(filepath)
print(found_instances)
