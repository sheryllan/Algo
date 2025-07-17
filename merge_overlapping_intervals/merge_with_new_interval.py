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



assert merge([[2, 5], [6, 9], [10, 11]], [7, 8]) == [[2, 5], [6, 9], [10, 11]]
assert merge([[2, 5], [6, 9], [10, 11]], [3, 7]) == [[2, 9], [10, 11]]
assert merge([[2, 5], [6, 9], [10, 11]], [1, 12]) == [[1, 12]]
assert merge([[2, 5], [6, 9], [10, 11]], [0, 1]) == [[0, 1], [2, 5], [6, 9], [10, 11]]
assert merge([], [4, 7]) == [[4,7]]
assert merge([[2, 5], [6, 9], [10, 12]], [11, 13]) == [[2, 5], [6, 9], [10, 13]]
assert merge([[2, 5], [10, 11]], [7, 8]) == [[2, 5], [7, 8], [10, 11]]
assert merge([[2, 5], [6, 9], [10, 12]], [14, 15]) == [[2, 5], [6, 9], [10, 12], [14, 15]]








