filepath = "puzzle_dummy.txt"
# filepath = "puzzle_input.txt"

# Approach with lists of lists

with open(filepath, "r") as file:
    lines = file.readlines()
    symbols = [[char for char in line.split(" ")[0]] for line in lines]
    values = [
        [int(num) for num in part.split(",")]
        for part in (line.split(" ", 1)[1] for line in lines)
    ]


# Check where the char '#' is (positions)
def find_char_positions(list_of_lists, character):
    return [
        [idx for idx, elem in enumerate(sublist) if elem == character]
        for sublist in list_of_lists
    ]


# how does it make sense to count the char ?


pos_char = find_char_positions(symbols, "#")

print(symbols)
print(values)
print(pos_char)
