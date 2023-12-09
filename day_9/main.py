# filepath = "puzzle_dummy.txt"
filepath = "puzzle_input.txt"


def col_with_dif(lst, col):
    result = [lst[col]]
    while any(lst) and len(lst) > 1:  # Until all elements are zero
        lst = [b - a for a, b in zip(lst, lst[1:])]
        result.append(lst[col])  # Save the last element
    return result


def rev_sum(lst):
    return sum(lst[::-1])  # In reverse order


def rev_sub(lst):
    for i in range(len(lst) - 1, 0, -1):
        lst[i - 1] = lst[i - 1] - lst[i]
    return lst[0] if lst else 0


with open(filepath, "r") as file:
    dataset = [[int(num) for num in line.split()] for line in file]


def part_1():
    sum_hist = 0
    for lst in dataset:
        last_cols = col_with_dif(lst, -1)
        hist = rev_sum(last_cols)
        sum_hist += hist
    print(sum_hist)


def part_2():
    sum_hist = 0
    for lst in dataset:
        last_cols = col_with_dif(lst, 0)
        hist = rev_sub(last_cols)
        sum_hist += hist
    print(sum_hist)


part_1()
part_2()
