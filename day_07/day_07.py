from functools import cmp_to_key
from collections import Counter

poker_rules = ["5", "14", "23", "113", "122", "1112", "11111"]
alphabet_part1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
alphabet_part2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def compare_hands_part1(hand1: list[str], hand2: list[str]) -> int:
    cards1 = hand1[0]
    cards2 = hand2[0]

    c1_key = "".join([str(x) for x in sorted(Counter(cards1).values())])
    c2_key = "".join([str(x) for x in sorted(Counter(cards2).values())])

    if poker_rules.index(c1_key) < poker_rules.index(c2_key):
        return 1
    elif poker_rules.index(c1_key) > poker_rules.index(c2_key):
        return -1

    for i in range(5):
        if alphabet_part1.index(cards1[i]) < alphabet_part1.index(cards2[i]):
            return 1
        elif alphabet_part1.index(cards1[i]) > alphabet_part1.index(cards2[i]):
            return -1
    return 0


def compare_hands_part2(hand1: list[str], hand2: list[str]) -> int:
    c1_counter = Counter(hand1[0])
    c2_counter = Counter(hand2[0])

    joker_count_c1 = c1_counter['J']
    joker_count_c2 = c2_counter['J']

    c1_counter['J'] = 0
    c2_counter['J'] = 0

    c1_sorted = sorted(c1_counter.values())
    c2_sorted = sorted(c2_counter.values())

    c1_sorted[-1] += joker_count_c1
    c2_sorted[-1] += joker_count_c2

    c1_key = "".join([str(x) for x in c1_sorted]).removeprefix("0")
    c2_key = "".join([str(x) for x in c2_sorted]).removeprefix("0")

    if poker_rules.index(c1_key) < poker_rules.index(c2_key):
        return 1
    elif poker_rules.index(c1_key) > poker_rules.index(c2_key):
        return -1

    for i in range(5):
        if alphabet_part2.index(hand1[0][i]) < alphabet_part2.index(hand2[0][i]):
            return 1
        elif alphabet_part2.index(hand1[0][i]) > alphabet_part2.index(hand2[0][i]):
            return -1
    return 0


if __name__ == '__main__':
    input_data = "data_challenge.in"

    with open(input_data, 'r') as f:
        lines = [x.split() for x in f.read().splitlines()]

    sorted_lines_part1 = sorted(lines, key=cmp_to_key(compare_hands_part1))
    sorted_lines_part2 = sorted(lines, key=cmp_to_key(compare_hands_part2))

    total_winnings_part1 = sum([(idx + 1) * int(val[1]) for idx, val in enumerate(sorted_lines_part1)])
    total_winnings_part2 = sum((idx + 1) * int(val[1]) for idx, val in enumerate(sorted_lines_part2))

    print("\n-- Part 1: --")
    print(total_winnings_part1)
    print("\n-- Part 2: --")
    print(total_winnings_part2)
