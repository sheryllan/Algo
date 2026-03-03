from typing import List


def merge(interval_list: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    i = 0
    merged = []
    while i < len(interval_list) and interval_list[i][1] < new_interval[0]:
        merged.append(interval_list[i])
        i += 1

    leftmost = min(interval_list[i][0], new_interval[0]) if i < len(interval_list) else new_interval[0]
    rightmost = new_interval[1]
    while i < len(interval_list) and interval_list[i][0] < rightmost:
        rightmost = max(rightmost, interval_list[i][1])
        i += 1

    merged.append([leftmost, rightmost])

    while i < len(interval_list):
        merged.append(interval_list[i])
        i += 1

    return merged


def merge(interval_list: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    left_new, right_new = new_interval

    if (not interval_list) or interval_list[0][0] > right_new:
        return [new_interval, *interval_list]

    leftmost = min(interval_list[0][0], left_new)
    rightmost = interval_list[0][1]

    merged = []
    for left, right in interval_list:
        # always remember leftmost and rightmost is from last iteration, so not touched here
        if left_new <= right and right_new >= left:
            left = min(left, left_new)
            right = max(right, right_new)
        elif left_new > rightmost and right_new < left:
            merged.append([leftmost, rightmost])
            leftmost = left_new
            rightmost = right_new

        if left > rightmost:
            merged.append([leftmost, rightmost])
            leftmost = left

        rightmost = max(rightmost, right)

    merged.append([leftmost, rightmost])
    if left_new > rightmost:
        merged.append(new_interval)

    return merged


def merge(interval_list: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    left_new, right_new = new_interval
    if not interval_list or right_new < interval_list[0][0]:
        return [new_interval, *interval_list]

    merged = []
    leftmost = min(interval_list[0][0], left_new)
    rightmost = max(interval_list[0][1], right_new) \
        if right_new >= interval_list[0][0] and left_new <= interval_list[0][1] \
        else interval_list[0][1]

    for left, right in interval_list[1:]:
        if left > rightmost:
            merged.append([leftmost, rightmost])
            leftmost = left

        if rightmost < left_new <= right_new < left:
            merged.append(new_interval)
        elif left <= right_new and right >= left_new:
            leftmost = min(leftmost, left_new)
            rightmost = max(rightmost, right_new)

        rightmost = max(rightmost, right)

    merged.append([leftmost, rightmost])
    if left_new > rightmost:
        merged.append(new_interval)

    return merged




assert merge([[1,4], [5,6], [8,9]], [3, 6]) == [[1,6], [8,9]]
assert merge([[2,4], [5,7], [8,9]], [2, 6]) == [[2,7], [8,9]]
assert merge([[2, 5], [6, 9], [10, 11]], [7, 8]) == [[2, 5], [6, 9], [10, 11]]
assert merge([[2, 5], [6, 9], [10, 11]], [3, 7]) == [[2, 9], [10, 11]]
assert merge([[2, 5], [6, 9], [10, 11]], [1, 12]) == [[1, 12]]
assert merge([[2, 5], [6, 9], [10, 11]], [0, 1]) == [[0, 1], [2, 5], [6, 9], [10, 11]]
assert merge([], [4, 7]) == [[4,7]]
assert merge([[2, 5], [6, 9], [10, 12]], [11, 13]) == [[2, 5], [6, 9], [10, 13]]
assert merge([[2, 5], [10, 11]], [7, 8]) == [[2, 5], [7, 8], [10, 11]]
assert merge([[2, 5], [6, 9], [10, 12]], [14, 15]) == [[2, 5], [6, 9], [10, 12], [14, 15]]








