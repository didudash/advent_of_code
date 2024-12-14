from collections import defaultdict


def parse_input(file_name):
    with open(file_name, "r") as file:
        robots = [
            (
                tuple(map(int, line.split()[0].split("=")[1].split(","))),
                tuple(map(int, line.split()[1].split("=")[1].split(","))),
            )
            for line in file
            if line.strip()
        ]
    return robots


def part_1(robots, seconds, width, height):

    mid_x = width // 2
    mid_y = height // 2

    # Robots in each quadrant
    quadrant_counts = defaultdict(int)

    for position, velocity in robots:
        x = (position[0] + velocity[0] * seconds) % width
        y = (position[1] + velocity[1] * seconds) % height

        # Exclude robots exactly in the middle
        if x == mid_x or y == mid_y:
            continue
        elif x < mid_x and y < mid_y:
            quadrant_counts["top_left"] += 1
        elif x >= mid_x and y < mid_y:
            quadrant_counts["top_right"] += 1
        elif x < mid_x and y >= mid_y:
            quadrant_counts["bottom_left"] += 1
        elif x >= mid_x and y >= mid_y:
            quadrant_counts["bottom_right"] += 1

    top_left = quadrant_counts["top_left"]
    top_right = quadrant_counts["top_right"]
    bottom_left = quadrant_counts["bottom_left"]
    bottom_right = quadrant_counts["bottom_right"]

    safety_factor = top_left * top_right * bottom_left * bottom_right
    print(safety_factor)


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_name = f"{choose}_input.txt"
robots = parse_input(file_name)
width = 101
height = 103
seconds = 100
part_1(robots, seconds, width, height)
