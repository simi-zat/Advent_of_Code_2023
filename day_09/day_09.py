def get_future_step(captured_data: list[int]) -> tuple[int, int]:
    curr_level = captured_data
    all_derivations = []

    while (any(x != 0 for x in curr_level)):
        all_derivations.append(curr_level)
        curr_level = [(curr_level[idx] - curr_level[idx - 1]) for idx in range(1, len(curr_level))]

    reversed_derivations = list(reversed(all_derivations))

    for idx in range(len(reversed_derivations)):
        past_value = reversed_derivations[idx][0] - reversed_derivations[idx - 1][0] if idx > 0 else \
            reversed_derivations[idx][0]
        next_value = reversed_derivations[idx][-1] + reversed_derivations[idx - 1][-1] if idx > 0 else \
            reversed_derivations[idx][-1]

        reversed_derivations[idx] = [past_value] + reversed_derivations[idx] + [next_value]

    return reversed_derivations[-1][-1], reversed_derivations[-1][0]


if __name__ == '__main__':
    input_data = "data_challenge.in"

    sum_next_steps_part1 = 0
    sum_prev_steps_part2 = 0

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            predicted_values = get_future_step([int(x) for x in line.split()])
            sum_next_steps_part1 += predicted_values[0]
            sum_prev_steps_part2 += predicted_values[1]

    print("\n-- Part 1: --")
    print(sum_next_steps_part1)
    print("\n-- Part 2: --")
    print(sum_prev_steps_part2)
