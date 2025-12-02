def parse_input(file_path):
    with open(file_path) as f:
        pairs = f.read().strip().split(",")
        return [tuple(map(int, p.split("-"))) for p in pairs]


def part_1(data):
    invalids = 0
    for start, end in data:
        for n in range(start, end + 1):
            s = str(n)
            if len(s) > 1 and s[0] == "0":
                continue
            length = len(s)
            if length % 2 == 0:
                half = length // 2
                for i in range(half):
                    if s[i] != s[i + half]:
                        break
                else:
                    invalids += n
            else:
                continue
    return invalids


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"

data = parse_input(file_path)

print(part_1(data))
