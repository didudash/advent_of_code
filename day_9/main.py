# filepath = "puzzle_dummy.txt"
filepath = "puzzle_input.txt"


def last_col_with_dif(lst):
    result = [lst[-1]]
    while any(lst) and len(lst) > 1:  # Until all elements are zero
        lst = [b - a for a, b in zip(lst, lst[1:])]
        result.append(lst[-1])  # Save the last element
    return result


def rev_sum(lst):
    return sum(lst[::-1])  # In reverse order


with open(filepath, "r") as file:
    dataset = [[int(num) for num in line.split()] for line in file]


def part_1():
    sum_hist = 0
    for lst in dataset:
        last_cols = last_col_with_dif(lst)
        hist = rev_sum(last_cols)
        sum_hist += hist
    print(sum_hist)


part_1()
