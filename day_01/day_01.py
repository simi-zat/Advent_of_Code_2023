import re

digits_as_string = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def part2(line: str) -> int:
    found_digits = []
    tmp_line = line

    for _ in range(len(line)):
        if tmp_line[0].isdigit():
            found_digits.append(int(tmp_line[0]))

        else:
            for index, value in enumerate(digits_as_string):
                if tmp_line.startswith(value):
                    found_digits.append(index + 1)

        tmp_line = tmp_line[1:]

    return 10 * found_digits[0] + found_digits[-1]


if __name__ == '__main__':
    input_data = "data_challenge.in"

    total_calibration_value_part1 = 0
    total_calibration_value_part2 = 0

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            found_digits = re.findall(r'\d', line)
            total_calibration_value_part1 += int(found_digits[0] + found_digits[-1])

            total_calibration_value_part2 += part2(line)

    print("\n-- Part 1: --")
    print(total_calibration_value_part1)
    print("\n-- Part 2: --")
    print(total_calibration_value_part2)
