"""
a company has a list of expected revenues and payments for the upcoming year in chronological order.
the problem is that  at some moments in time the sum of previous payments can be larger than the total previous revenue.
This would put the company in debt. to avoid this problem the company takes a very simple approach.
it reschedules some expenses to the end of the year.
you are given an array of integers, where positive numbers represent revenues and negative numbers represent expenses,
all in chronological order. in one move you can relocate any expense(negative number) to the end of the array.
what is the minimum number of such relocations to make sure that the company need falls into debt?
in other words: you need to make sure that there is no consecutive sequence of elements starting from the beginning of the array,
that sums up to a negative number.
you can assume that the sum of all elements in A is non-negative.
Write a function:
def solution(A)
that, given an array oA of N integers, returns the minimum number of relocations, so that company never falls into debt.
examples:
1. given A = [10, -10, -1, -1, 10], the function should return 1. it is enough to move -10 to the end of the array.
2. Given A = [-1, -1,-1,1,1, 1,1], the function should return 3.
3. given A = [5, -2,-3,1], the function should return 0.

Write an efficient algorithm for the following assumptions:
- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [−1,000,000,000..1,000,000,000];
- sum of all elements in A is greater than or equal to 0 .
"""

import heapq

def insert(min_heap: list, x):
    min_heap.append(x)
    i = len(min_heap) - 1
    curr = min_heap[i]
    while i > 0:
        parent_i = (i - 1) // 2
        if curr >= parent_i:
            break
        min_heap[i] = min_heap[parent_i]
        min_heap[parent_i] = curr
        i = parent_i


def pop_top(min_heap: list):
    top = min_heap[0]
    rightmost = min_heap[-1]
    min_heap[0] = rightmost
    min_heap.pop()
    i = 0
    left_i = 2 * i + 1
    right_i = 2 * i + 2
    while i < left_i < right_i < len(min_heap):
        curr = min_heap[i]
        smaller_i = left_i if min_heap[left_i] < min_heap[right_i] else right_i
        smaller = min_heap[smaller_i]

        if curr <= smaller:
            break

        min_heap[i] = smaller
        min_heap[smaller_i] = curr
        i = smaller_i
        left_i = 2 * i + 1
        right_i = 2 * i + 2

    return top

def solution(A):
    min_heap = []
    running_sum = 0
    relocations = 0
    for num in A:
        running_sum += num
        if num < 0:
            insert(min_heap, num)

        if running_sum >= 0:
            continue

        while running_sum < 0 and min_heap:
            biggest_debt = pop_top(min_heap)
            running_sum -= biggest_debt
            relocations += 1

    return relocations


print(solution([10, -10, -1, -1, 10]))  # Output: 1
print(solution([-1, -1, -1, 1, 1, 1, 1]))  # Output: 3
print(solution([5, -2, -3, 1]))  # Output: 0

print(solution([5, -1, -1, -7, 3, 2]))
print(solution([10, -4, -6, 1, 6, 3]))
