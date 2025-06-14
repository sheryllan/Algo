def get_interval_count(start, end):
    total = 0
    counts_at_i = list(range(end - start + 1, 0, -1))
    for moving_start in range(0, end - start + 1):
        total += counts_at_i[moving_start]

    subarray_len = end - start + 1
    counts = (1 + subarray_len) * subarray_len / 2

    assert counts == total
    return total


def get_num_intervals(n: int, allergic: list, poisonous: list):
    # a list of flags, each indicating whether the ith bacteria is a hazard(allergic or poisonous) to the next one
    hazards = [False] * (n + 1)
    for bacteria_allergic, bacteria_poisonous in zip(allergic, poisonous):
        if bacteria_allergic == bacteria_poisonous + 1:
            hazards[bacteria_poisonous] = True
        elif bacteria_poisonous == bacteria_allergic + 1:
            hazards[bacteria_allergic] = True

    intervals = 0
    i = 1
    while i < n + 1:
        hazardous = hazards[i]
        j = i
        while not hazardous:
            if j < n:
                j += 1
                hazardous = hazards[j]
            else:
                break

        if not hazards[i]:
            intervals += get_interval_count(i, j)

        i = j + 1

    return intervals


print(get_num_intervals(3, [2, 1, 3], [3, 3, 1]))
print(get_num_intervals(0, [], []))
print(get_num_intervals(4, [], []))
print(get_num_intervals(4, [1, 4], [2, 2]))