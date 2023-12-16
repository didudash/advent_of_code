# filepath = "puzzle_dummy.txt"
filepath = "puzzle_input.txt"

with open(filepath, "r") as file:
    input_strings = file.readline().strip().split(",")


def hashmap(input):
    current_val = 0
    for i in range(len(input)):
        current_val = ((current_val + ord(input[i])) * 17) % 256
    return current_val


def part_1():
    sum_results = 0
    for input in input_strings:
        current_val = hashmap(input)
        sum_results += current_val
    print(sum_results)


# focusing power
def part_2():
    boxes = {}
    j = 0
    for input in input_strings:
        j += 1
        if "=" in input:
            label = input.split("=")[0]
            f_length = input.split("=")[1]
            box_num = hashmap(label)
            if box_num in boxes:
                match_found = False
                for slot in boxes[box_num]:
                    if slot and slot[0] == label:
                        slot[1] = f_length
                        match_found = True
                if not match_found:
                    boxes[box_num].append([label, f_length])
            else:
                boxes[box_num] = [[label, f_length]]

        elif "-" in input:
            label = input.split("-")[0]
            box_num = hashmap(label)
            if box_num in boxes:
                for i, slot in enumerate(boxes[box_num]):
                    if slot and slot[0] == label:
                        boxes[box_num].pop(i)
    sum_focus_power = 0
    for box_num, slots in boxes.items():
        focus_power = 0
        for i, slot in enumerate(slots):
            focus_power = (box_num + 1) * (i + 1) * int(slot[1])
            sum_focus_power += focus_power
    print(sum_focus_power)


part_1()
part_2()
