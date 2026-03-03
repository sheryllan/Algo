"""
The core idea of the problem is Sliding window / two pointers

Efficient approach: For each right endpoint r, find the minimum valid l (call it min_l).
As r increases, min_l can only increase (monotonically). The number of valid intervals ending at r is r - min_l + 1.

Or equivalently for each left endpoint l, find its minimum valid right endpoint min_r.
The number of valid intervals starting at l ending at r is min_r - l + 1
"""


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


def get_num_intervals(n: int, allergic: list, poisonous: list):
    #  construct the dict which stores the min hazardous bacteria seen after the given bacteria
    hazards = {}
    for allergic_bacteria, poisonous_bacteria in zip(allergic, poisonous):
        smaller, bigger = allergic_bacteria, poisonous_bacteria
        if smaller > bigger:
            smaller, bigger = bigger, smaller

        if smaller not in hazards:
            hazards[smaller] = bigger
        else:
            hazards[smaller] = min(hazards[smaller], bigger)

    """
    The hazards dict only stores constraints for the smaller bacteria of each pair. 
    It doesn't account for the fact that a constraint on position j > i limits what intervals starting at i can include.
    Here is the wrong solution below:
    """
    # total = 0
    # for i in range(1, n + 1):
    #     last = hazards.get(i, n + 1) - i
    #     total += last

    # The fix requires propagating the minimum right boundary forward:
    total = 0
    limit = n + 1
    for i in range(n, 0, -1):
        if i in hazards:
            limit = min(limit, hazards[i])
        # intervals starting at i can reach at most limit-1
        total += limit - i

    return total


# AI's solution
def bioHazard(n, allergic, poisonous):
    # Build conflict pairs: for each bacteria x, list of bacteria it conflicts with
    # A conflict exists between p and a: they can't coexist
    from collections import defaultdict

    # For each value, store positions (1-indexed)
    # conflicts[x] = list of y where (x,y) or (y,x) is a poisonous pair
    conflicts = defaultdict(list)

    for a, p in zip(allergic, poisonous):
        # p is poisonous to a — they can't be in the same interval
        conflicts[p].append(a)
        conflicts[a].append(p)

    # Sliding window: for each r, maintain min valid left boundary
    # pos[bacteria] = its position (bacteria are 1-indexed, positions 1..n)
    # Here bacteria labels ARE their positions (1 to n)

    count = 0
    min_l = 1  # minimum left boundary (1-indexed)

    for r in range(1, n + 1):
        # When we include bacteria r, check all its conflict partners
        for partner in conflicts[r]:
            if partner < r:
                # partner is to the left of r, so if it's in window, push min_l
                min_l = max(min_l, partner + 1)
        count += r - min_l + 1

    return count

bioHazard(4, [3], [4])


assert get_num_intervals(3, [2, 1, 3], [3, 3, 1]) == 4
assert get_num_intervals(0, [], []) == 0
assert get_num_intervals(4, [], []) == 10
assert get_num_intervals(4, [1, 4], [2, 2]) == 6
assert get_num_intervals(4, [3], [4]) == 7