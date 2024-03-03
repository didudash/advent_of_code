# filepath = "puzzle_dummy.txt"
filepath = "puzzle_input.txt"

import math


def match_i_one(string, column):
    # only the first index
    return next((i for i, s in enumerate(column) if s == string), -1)


def match_i_all(string, column, index=None):
    if index:
        s = s[index]
    return [i for i, s in enumerate(column) if s == string]


with open(filepath, "r") as file:
    dir = [char for char in file.readline().strip()]
    next(file)
    lines = file.readlines()
    nodes = [line.split("=")[0].strip() for line in lines]
    l, r = zip(*[line.split("=")[1].strip().strip("()").split(", ") for line in lines])


def part_1():
    node = "AAA"
    read_i = match_i_one(node, nodes)
    read = None
    s, i = 0, 0
    while read != "ZZZ":
        if dir[i] == "R":
            read = r[read_i]
        else:
            read = l[read_i]
        s += 1
        if i == len(dir) - 1:
            i = 0
        else:
            i += 1
        read_i = match_i_one(read, nodes)
    print(s)


part_1()
