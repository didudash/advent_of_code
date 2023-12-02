import re

pattern = r"(\d+) (green|blue|red)"


def verify_games_part_1(file_path, pattern):
    max_green, max_blue, max_red = 13, 14, 12
    game_sum = 0

    with open(file_path, "r") as file:
        game_number = 0
        for game in file:
            game_number += 1
            is_higher = False
            for match in re.findall(pattern, game):
                number, color = int(match[0]), match[1]
                if color == "green":
                    if number > max_green:
                        is_higher = True
                elif color == "blue":
                    if number > max_blue:
                        is_higher = True
                elif color == "red":
                    if number > max_red:
                        is_higher = True
            if not is_higher:
                game_sum += int(game_number)
    return game_sum


def verify_games_part_2(file_path):
    game_power_sum = 0

    with open(file_path, "r") as file:
        for game in file:
            game_power = 0
            max_green_game, max_blue_game, max_red_game = 0, 0, 0
            for match in re.findall(pattern, game):
                number, color = int(match[0]), match[1]
                if color == "green":
                    if number > max_green_game:
                        max_green_game = number
                elif color == "blue":
                    if number > max_blue_game:
                        max_blue_game = number
                elif color == "red":
                    if number > max_red_game:
                        max_red_game = number
            game_power = max_green_game * max_blue_game * max_red_game
            game_power_sum += game_power
    return game_power_sum


game_sum = verify_games_part_1("puzzle_input.txt")
print(game_sum)
game_power_sum = verify_games_part_2("puzzle_input.txt")
print(game_power_sum)
