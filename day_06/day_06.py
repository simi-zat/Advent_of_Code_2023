def get_winning_strategy(max_time: int, min_distance: int) -> int:
    possible_strategies = 0

    for hold_ms in range(1, max_time):
        possible_strategies += 1 if hold_ms * (max_time - hold_ms) > min_distance else 0

    return possible_strategies


if __name__ == '__main__':
    input_data = "data_challenge.in"

    with open(input_data, 'r') as f:
        lines = f.read().splitlines()
        time_line = lines[0].split()[1:]
        distance_line = lines[1].split()[1:]

    max_times_part1 = [int(x) for x in time_line]
    min_distance_part1 = [int(x) for x in distance_line]

    number_of_ways_to_beat_record_part1 = 1
    for race in range(len(max_times_part1)):
        number_of_ways_to_beat_record_part1 *= get_winning_strategy(max_times_part1[race], min_distance_part1[race])

    max_time_part2 = int("".join(time_line))
    min_distance_part2 = int("".join(distance_line))

    print("\n-- Part 1: --")
    print(number_of_ways_to_beat_record_part1)
    print("\n-- Part 2: --")
    print(get_winning_strategy(max_time_part2, min_distance_part2))
