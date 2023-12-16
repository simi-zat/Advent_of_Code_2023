import re


def is_part_number(char: str) -> bool:
    return char != "." and not char.isdigit()


if __name__ == '__main__':
    input_data = "data_challenge.in"
    engine_schematic = open(input_data, 'r').read().splitlines()

    asterisk_neighbors = {}
    sum_part_numbers_part1 = 0

    for idx_line, line in enumerate(engine_schematic):
        for num in re.finditer(r'\d+', line):
            row_above_idx = max(0, idx_line - 1)
            row_below_idx = min(len(engine_schematic), idx_line + 2)
            selected_three = engine_schematic[row_above_idx:row_below_idx]

            char_min_idx = max(0, num.start() - 1)
            char_max_idx = min(len(line), num.end() + 1)

            if len(selected_three) < 3:
                selected_three = [''] + selected_three if idx_line == 0 else selected_three + ['']

            for idx_row, row_selected_three in enumerate(selected_three):

                for idx_char, char in enumerate(row_selected_three[char_min_idx:char_max_idx]):
                    if char == "*":
                        asterisk_position = (idx_line + idx_row - 1, char_min_idx + idx_char)
                        if asterisk_position not in asterisk_neighbors:
                            asterisk_neighbors[asterisk_position] = []
                        asterisk_neighbors[asterisk_position].append(num.group())

                if any([is_part_number(x) for x in row_selected_three[char_min_idx:char_max_idx]]):
                    sum_part_numbers_part1 += int(num.group())
                    break

    sum_gear_ratios_part2 = 0

    for gear in asterisk_neighbors.values():
        if len(gear) == 2:
            sum_gear_ratios_part2 += int(gear[0]) * int(gear[1])

    print("\n-- Part 1: --")
    print(sum_part_numbers_part1)
    print("\n-- Part 2: --")
    print(sum_gear_ratios_part2)
