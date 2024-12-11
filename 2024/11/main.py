def blink(stones):
    new_stones = []
    for n in stones:
        if n == 0:
            new_stones.append(1)
        elif len(str(n)) % 2 == 0:
            str_n = str(n)
            mid = len(str_n) // 2
            left = int(str_n[:mid])
            right = int(str_n[mid:])
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(n * 2024)
    return new_stones


def part_1(input_stones):
    blinks = 25
    for _ in range(blinks):
        input_stones = blink(input_stones)
    print(len(input_stones))


# file_path = "toy_input.txt"
file_path = "puzzle_input.txt"

input_stones = list(map(int, open(file_path).read().strip().split()))
part_1(input_stones)
