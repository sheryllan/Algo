# Defining a brick as: a rectangle of height = 1, and width = 2, or width = 3.
#
# You are given an infinite supply of bricks. Each brick has one of two possible lengths: 2 units or 3 units. Your task is to build a wall of a specified width and height. The wall should be built in such a way that it is made up of horizontal rows of bricks. However, the bricks must be arranged so that the right edge of a brick in one row does not align vertically with the right edge of a brick in the row directly above or below it. This is to ensure the wall's stability.
#
# Write a Python function that takes two arguments: the width and the height of the wall. The function should return the count of all possible ways to build the wall that meet the criteria.
#
# If the width is 5 and the height is 1, the function would compute that we can have 2 walls (3,2) and (2,3) that represent the two possible ways to build the wall, and would return 2, for example:


from itertools import product


def flag_widths(width):


def valid_rows(width):
    possible_rows = [[] for _ in range(width + 1)]
    possible_rows[0] = [[]]

    for i in range(2, width + 1):
        if i >= 2:
            for row in possible_rows[i - 2]:
                possible_rows[i].append(row + [2])
        if i >= 3:
            for row in possible_rows[i - 3]:
                possible_rows[i].append(row + [3])

    return possible_rows[width]

print(valid_rows(8))


def cumsum(nums):
    total = 0
    result = []
    for x in nums:
        total += x
        result.append(total)
    return result

def is_valid_wall(row1, row2):
    row1_cumsum = cumsum(row1)
    row2_cumsum = cumsum(row2)
    return all(x != y for x, y in product(row1_cumsum[:-1], row2_cumsum[:-1]))

def build(width: int, height: int) -> int:
    rows = valid_rows(width)

    wall_combinations = [{} for _ in range(height + 1)]
    wall_combinations[0] = {tuple(row): 1 for row in rows}

    for h in range(1, height):
        for row1, row2 in product(rows, rows):
            if is_valid_wall(row1, row2):
                wall_combinations[h][tuple(row2)] = wall_combinations[h].get(tuple(row2), 0) + wall_combinations[h - 1].get(tuple(row1), 0)

    return sum(wall_combinations[height - 1].values())


# Example usage:
if __name__ == "__main__":
    # width = 5
    # height = 3
    # result = build(width, height)
    # print(result)

    width = 8
    height = 2
    result = build(width, height)
    print(result)
