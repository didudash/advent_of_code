# filepath = "puzzle_dummy.txt"
filepath = "puzzle_input.txt"

with open(filepath, "r") as file:
    input_strings = file.readline().strip().split(",")
    sum_results = 0
    for input in input_strings:
        current_val = 0
        for i in range(len(input)):
            current_val = ((current_val + ord(input[i])) * 17) % 256
        sum_results += current_val
    print(sum_results)
