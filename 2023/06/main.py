from functools import reduce
import operator


def read_as_list_num(filepath):
    with open(filepath, "r") as file:
        content = file.read()
        lines = content.strip().split("\n")
        times = []
        distances = []
        times = [int(val) for val in lines[0].split() if val.isdigit()]
        distances = [int(val) for val in lines[1].split() if val.isdigit()]
        return times, distances


def read_as_num(filepath):
    with open(filepath, "r") as file:
        content = file.read()
        lines = content.strip().split("\n")
        time = int("".join(val for val in lines[0] if val.isdigit()))
        distance = int("".join(val for val in lines[1] if val.isdigit()))
        return time, distance


def part_1(filepath):
    times, distances = read_as_list_num(filepath)
    total_ways = []
    for time, distance in zip(times, distances):
        ways = []
        df = 0
        for h in range(time + 1):
            if h == 0 or h == time:
                df = 0
            else:
                tl = time - h
                df = tl * h
                if df > distance:
                    ways.append(h)
        total_ways.append(len(set(ways)))
    mult_ways = reduce(operator.mul, total_ways)
    print(mult_ways)


def part_2(filepath):
    time, distance = read_as_num(filepath)
    ways = 0
    for h in range(time + 1):
        if h == 0 or h == time:
            df = 0
        else:
            tl = time - h
            df = tl * h
            if df > distance:
                ways += 1
    print(ways)


filepath = "puzzle_input.txt"

part_1(filepath)
part_2(filepath)
