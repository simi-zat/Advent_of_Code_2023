def hash_function(in_str: str) -> int:
    hash_sum = 0
    for char in in_str:
        hash_sum = (17 * (hash_sum + ord(char))) % 256
    return hash_sum


if __name__ == '__main__':
    input_data = "data_challenge.in"

    with open(input_data, 'r') as f:
        input_data = f.readline().split(",")

    tot_hash_sum = 0
    total_focusing_power = 0
    boxes = [[] for _ in range(256)]

    for inn in input_data:
        tot_hash_sum += hash_function(inn)

        label = inn.split("-")[0].split("=")[0]
        label_hash = hash_function(label)

        found_idx = -1
        found_val = ""

        for idx, val in enumerate(boxes[label_hash]):
            if val.startswith(label):
                found_idx = idx
                found_val = val
                break

        if "=" in inn:
            if found_idx < 0:
                boxes[label_hash].append(inn)
            else:
                boxes[label_hash][found_idx] = inn

        elif "-" in inn:
            if found_val:
                boxes[label_hash].remove(found_val)

    for idx_box, box in enumerate(boxes):
        for idx_slot, slot in enumerate(box):
            total_focusing_power += (1 + idx_box) * (1 + idx_slot) * int(slot.split("=")[1])

    print("\n-- Part 1: --")
    print(tot_hash_sum)
    print("\n-- Part 2: --")
    print(total_focusing_power)
