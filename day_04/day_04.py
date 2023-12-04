def get_matching_numbers(winning_numbers_str: str, my_numbers_str: str) -> set[str]:
    winning_numbers_list = set(winning_numbers_str.split())
    my_numbers_list = set(my_numbers_str.split())
    return winning_numbers_list.intersection(my_numbers_list)


if __name__ == '__main__':
    input_data = "data_challenge.in"

    cards_points_part1 = 0
    number_of_cards_part2 = 0

    cards_copies_dict = {1: 0}

    with open(input_data, 'r') as f:
        for line in f.read().splitlines():
            all_numbers = line.split(": ")
            card_number = int(all_numbers[0].split()[1])

            if card_number not in cards_copies_dict:
                cards_copies_dict[card_number] = 0

            card_copies: int = cards_copies_dict[card_number] + 1
            winning_numbers, my_numbers = all_numbers[1].split("|")
            my_winning_numbers = get_matching_numbers(winning_numbers, my_numbers)

            if my_winning_numbers:
                cards_points_part1 += 2 ** (len(my_winning_numbers) - 1)

            for i in range(len(my_winning_numbers)):
                if not card_number + i + 1 in cards_copies_dict:
                    cards_copies_dict[card_number + i + 1] = 0
                cards_copies_dict[card_number + i + 1] += card_copies


    for value in cards_copies_dict.values():
        number_of_cards_part2 += value + 1

    print("\n-- Part 1: --")
    print(cards_points_part1)
    print("\n-- Part 2: --")
    print(number_of_cards_part2)
