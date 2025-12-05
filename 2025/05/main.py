def parse_input(file_path):
    data1, data2 = open(file_path).read().strip().split("\n\n")
    fresh_ranges = [tuple(map(int, x.split("-"))) for x in data1.split("\n")]
    ids = list(map(int, data2.split("\n")))
    return fresh_ranges, ids


def part_1(data):
    fresh_ranges, ids = data
    n_fresh_ids = sum(
        any(start <= id <= end for start, end in fresh_ranges) for id in ids
    )
    return n_fresh_ids


def part_2(data):
    fresh_ranges, _ = data
    sorted_ranges = sorted(fresh_ranges)

    merged = []
    for start, end in sorted_ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    n_fresh_ids = sum(end - start + 1 for start, end in merged)
    return n_fresh_ids


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
print(part_2(data))
