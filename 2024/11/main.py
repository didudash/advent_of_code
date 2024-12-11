from collections import defaultdict


def part_1(input_stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for n in input_stones:
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
        input_stones = new_stones
    print(len(input_stones))


def part_2(input_stones, blinks):
    """
    Optimized part 1 for exponential growth
    by focusing on distinct values
    """
    # Initialize stone frequency with input values
    state = defaultdict(int)
    for stone in input_stones:
        state[stone] += 1

    for _ in range(blinks):
        new_state = defaultdict(int)
        for stone, count in state.items():
            if stone == 0:
                new_state[1] += count
            else:
                str_stone = str(stone)
                if len(str_stone) % 2 == 0:
                    mid = len(str_stone) // 2
                    left = int(str_stone[:mid])
                    right = int(str_stone[mid:])
                    new_state[left] += count
                    new_state[right] += count
                else:
                    new_state[stone * 2024] += count
        state = new_state

    print(sum(state.values()))


file_path = "puzzle_input.txt"
input_stones = list(map(int, open(file_path).read().strip().split()))
part_1(input_stones, 25)
part_2(input_stones, 75)
