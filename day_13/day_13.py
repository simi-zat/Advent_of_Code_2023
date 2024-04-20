def transpose_pattern(pattern: list[str]) -> list[str]:
    transposed_pattern = ["" for _ in range(len(pattern[0]))]
    for line in pattern:
        for idx, char in enumerate(line):
            transposed_pattern[idx] += char

    return transposed_pattern


def is_clean_mirror(part1, part2) -> bool:
    max_length = min(len(part1), len(part2))
    return part1[:max_length] == part2[:max_length]


def find_mirror_in_rows(pattern: list[str]) -> int:
    possible_mirrors = []

    for idx, line in enumerate(pattern):
        if idx + 1 < len(pattern) and line == pattern[idx + 1]:
            possible_mirrors.append(idx)

    for mirror in possible_mirrors:
        if is_clean_mirror(list(reversed(pattern[:mirror + 1])), pattern[mirror + 1:]):
            return mirror + 1

    return -1


def count_smudges(row1: str, row2: str) -> int:
    number_of_smudges = 0

    for idx in range(len(row1)):
        number_of_smudges += 1 if row1[idx] != row2[idx] else 0

    return number_of_smudges


def is_smudged_mirror(part1: list[str], part2: list[str]) -> bool:
    max_length = min(len(part1), len(part2))
    tot_num_smudges = 0

    for i in range(max_length):
        tot_num_smudges += count_smudges(part1[i], part2[i])
        if tot_num_smudges > 1: break

    return tot_num_smudges == 1


def find_mirror_with_smudges_in_rows(pattern: list[str]) -> int:
    possible_mirrors = []

    for idx, line in enumerate(pattern):
        if idx + 1 < len(pattern) and count_smudges(line, pattern[idx + 1]) <= 1:
            possible_mirrors.append(idx)

    for mirror in possible_mirrors:
        if is_smudged_mirror(list(reversed(pattern[:mirror + 1])), pattern[mirror + 1:]):
            return mirror + 1

    return -1


if __name__ == '__main__':
    input_data = "data_challenge.in"
    # input_data = "data_test.in"

    part1 = 0
    part2 = 0

    with open(input_data, 'r') as f:
        for pattern in f.read().split("\n\n"):
            transposed_pattern = transpose_pattern(pattern.split())

            found_mirror_row = find_mirror_in_rows(pattern.split())
            if found_mirror_row < 0:
                found_mirror_col = find_mirror_in_rows(transposed_pattern)
                if found_mirror_col > 0:
                    part1 += found_mirror_col
            else:
                part1 += 100 * found_mirror_row

            smudged_mirror_row = find_mirror_with_smudges_in_rows(pattern.split())
            if smudged_mirror_row < 0:
                smudged_mirror_col = find_mirror_with_smudges_in_rows(transposed_pattern)
                if smudged_mirror_col > 0:
                    part2 += smudged_mirror_col
            else:
                part2 += 100 * smudged_mirror_row

    print("\n-- Part 1: --")
    print(part1)
    print("\n-- Part 2: --")
    print(part2)
