import copy


def expand_galaxy(map_galaxies: list[list[int]], expand_param: int) -> list[list[int]]:
    for empty_row in sorted(list(free_rows), reverse=True):
        for galaxy in map_galaxies:
            if galaxy[0] > empty_row:
                galaxy[0] += expand_param - 1

    for empty_col in sorted(list(free_cols), reverse=True):
        for galaxy in map_galaxies:
            if galaxy[1] > empty_col:
                galaxy[1] += expand_param - 1

    return map_galaxies


def get_shortest_distance(node1: list[int], node2: list[int]) -> int:
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])


if __name__ == '__main__':
    input_data = "data_challenge.in"

    map_galaxies: list[list[int]] = []
    taken_rows = set()
    taken_columns = set()

    max_row = 0
    max_col = 0

    shortest_path_part1 = 0
    shortest_path_part2 = 0

    with open(input_data, 'r') as f:
        for row_idx, line in enumerate(f.read().splitlines()):
            max_row = max(max_row, row_idx)

            for col_idx, data in enumerate(line):
                max_col = max(max_col, col_idx)

                if data == '#':
                    map_galaxies.append([row_idx, col_idx])
                    taken_rows.add(row_idx)
                    taken_columns.add(col_idx)

    free_rows = set([x for x in range(max_row)]) - taken_rows
    free_cols = set([x for x in range(max_col)]) - taken_columns

    map_part1 = expand_galaxy(copy.deepcopy(map_galaxies), 2)
    map_part2 = expand_galaxy(copy.deepcopy(map_galaxies), 1_000_000)

    for i in range(0, len(map_galaxies)):
        for j in range(i + 1, len(map_galaxies)):
            shortest_path_part1 += get_shortest_distance(map_part1[i], map_part1[j])
            shortest_path_part2 += get_shortest_distance(map_part2[i], map_part2[j])

    print("\n-- Part 1: --")
    print(shortest_path_part1)
    print("\n-- Part 2: --")
    print(shortest_path_part2)
