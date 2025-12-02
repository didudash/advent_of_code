def parse_input(file_path):
    with open(file_path) as f:
        pairs = f.read().strip().split(",")
        return [tuple(map(int, p.split("-"))) for p in pairs]


def iterate_ranges(data):
    for start, end in data:
        for n in range(start, end + 1):
            s = str(n)
            if len(s) > 1 and s[0] == "0":
                continue
            yield n, s


def part_1(data):
    invalids = 0
    for n, s in iterate_ranges(data):
        if len(s) % 2 == 0:
            half = len(s) // 2
            if s[:half] == s[half:]:
                invalids += n
    return invalids


def part_2(data):
    invalids = 0
    for n, s in iterate_ranges(data):
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0 and s[:i] * (len(s) // i) == s:
                invalids += n
                break
    return invalids


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
print(part_2(data))
