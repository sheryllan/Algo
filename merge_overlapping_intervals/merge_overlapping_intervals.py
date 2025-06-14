from typing import List

def merge_intervals(intervals):
    if not intervals:
        return intervals
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    leftmost = sorted_intervals[0][0]
    rightmost = sorted_intervals[0][1]
    merged = []
    for left, right in sorted_intervals[1:]:
        if left > rightmost:
            merged.append((leftmost, rightmost))
            leftmost = left
            rightmost = right
        else:
            rightmost = max(rightmost, right)

    merged.append((leftmost, rightmost))
    return merged

def check(start, end, interval):
    return interval[0] <= start and interval[1] >= end

def solution(P: List[int], A: List[int], B: int, E: int):
    intervals = list(map(lambda x: (x[0] - x[1], x[0] + x[1]), zip(P, A)))
    if not intervals:
        return B == E

    merged_intervals = merge_intervals(intervals)

    start = B
    end = E
    if B > E:
        start = E
        end = B

    target = start
    left = -1
    right = len(intervals)
    while left + 1 < right:
        mid = (left + right) // 2  # left + (right - left) / 2 preventing overflow in other languages
        if merged_intervals[mid][0] < target:
            left = mid
        elif merged_intervals[mid][0] > target:
            right = mid
        else:
            return check(start, end, merged_intervals[mid])

    return left > -1 and check(start, end, merged_intervals[left])  # choose left because start should >= left


# print(merge_intervals([(1, 3), (0, 4), (2, 5), (6, 9), (7, 8)]))
# print(merge_intervals([(0, 10), (5, 9), (3, 4), (4, 7)]))
# print(merge_intervals([(1, 3), (0, 4), (2, 5), (6, 9), (7, 8), (10, 11)]))


print(solution([1, 5, 0], [2, 0, 3], 2, -1))
print(solution([1, 5, 0], [2, 0, 3], 2, -4))

