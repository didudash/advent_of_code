import numpy as np

# filepath = "puzzle_dummy.txt"
filepath = "puzzle_input.txt"

with open(filepath, "r") as file:
    lines = file.readlines()

data = [list(line.strip()) for line in lines]
dataset = np.array(data)


# your move dependes on the char type and the direction
def map_direction(char, current_direction):
    direction_map = {
        "|": {(1, 0): (1, 0), (-1, 0): (-1, 0)},
        "-": {(0, 1): (0, 1), (0, -1): (0, -1)},
        "L": {(1, 0): (0, 1), (0, -1): (-1, 0)},
        "J": {(1, 0): (0, -1), (0, 1): (-1, 0)},
        "7": {(-1, 0): (0, -1), (0, 1): (1, 0)},
        "F": {(-1, 0): (0, 1), (0, -1): (1, 0)},
    }
    return direction_map.get(char, {}).get(current_direction, None)


ini_dirs = [(1, 0), (-1, 0), (0, 1)]  # List of initial directions

# First starts with 'S'
r_i, c_i = np.where(dataset == "S")
# with only one start
ini_pos = (r_i[0], c_i[0])

steps = 1
for d in ini_dirs:
    pos = (ini_pos[0] + d[0], ini_pos[1] + d[1])
    char = dataset[pos[0], pos[1]]
    new_dir = map_direction(char, d)
    if new_dir:  # take one road to the loop
        steps += 1
        break
new_pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
new_char = dataset[new_pos[0], new_pos[1]]
print(new_char)
while new_dir and new_char != "S":
    steps += 1
    new_dir = map_direction(new_char, new_dir)
    new_pos = (new_pos[0] + new_dir[0], new_pos[1] + new_dir[1])
    new_char = dataset[new_pos[0], new_pos[1]]
    print(new_char)

path_length = int((steps) / 2)
print(path_length)
