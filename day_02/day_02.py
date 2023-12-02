import re
import string


def is_game_possible_part1(game_information: list[str]) -> bool:
    max_allowed_cubes = [12, 13, 14]  # RGB

    for i in range(0, len(game_information), 2):
        if game_information[i + 1] == 'red' and int(game_information[i]) > max_allowed_cubes[0]:
            return False
        elif game_information[i + 1] == 'green' and int(game_information[i]) > max_allowed_cubes[1]:
            return False
        elif game_information[i + 1] == 'blue' and int(game_information[i]) > max_allowed_cubes[2]:
            return False

    return True


def get_game_power_part2(game_information: list[str]) -> int:
    min_required_cubes = [0, 0, 0]  # RGB

    for i in range(0, len(game_information), 2):
        if game_information[i + 1] == 'red':
            min_required_cubes[0] = max(min_required_cubes[0], int(game_information[i]))
        elif game_information[i + 1] == 'green':
            min_required_cubes[1] = max(min_required_cubes[1], int(game_information[i]))
        elif game_information[i + 1] == 'blue':
            min_required_cubes[2] = max(min_required_cubes[2], int(game_information[i]))

    return min_required_cubes[0] * min_required_cubes[1] * min_required_cubes[2]


if __name__ == '__main__':
    input_data = "data_challenge.in"

    sum_possible_games_part1 = 0
    sum_game_powers_part2 = 0

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            game_information = re.sub(f"[{re.escape(string.punctuation)}]", "", line).split()

            if is_game_possible_part1(game_information[2:]):
                sum_possible_games_part1 += int(game_information[1])

            game_power = get_game_power_part2(game_information[2:])
            sum_game_powers_part2 += game_power

    print("\n-- Part 1: --")
    print(sum_possible_games_part1)
    print("\n-- Part 2: --")
    print(sum_game_powers_part2)
