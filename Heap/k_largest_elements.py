"""
Given an array arr[] and an integer k, the task is to find k largest elements in the given array.
Elements in the output array should be in decreasing order.

Examples:

Input:  [1, 23, 12, 9, 30, 2, 50], k = 3
Output: [50, 30, 23]

Input:  [11, 5, 12, 9, 44, 17, 2], k = 2
Output: [44, 17]
"""


def partition(arr, low, high):
    pivot = high
    val = arr[pivot]
    i = low

    for j in range(low, high):
        if arr[j] < val:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


def find_k_largest_quick_select(arr, k):
    n = len(arr)
    low = 0
    high = n - 1

    if low < high:
        pivot = partition(arr, low, high)
        if pivot > n - k:
            find_k_largest_quick_select(arr[low: pivot - 1], k)
        elif pivot < n - k:
            find_k_largest_quick_select(arr[pivot + 1: high], k)
        else:
            return sorted(arr[n-k:], reverse=True)


import heapq


# Function to find the k largest elements in the array
def kLargest(arr, k):
    # Create a min-heap with the first k elements
    minH = arr[:k]
    heapq.heapify(minH)

    # Traverse the rest of the array
    for x in arr[k:]:
        if x > minH[0]:
            heapq.heapreplace(minH, x)

    res = []

    # Min heap will contain only k
    # largest element
    while minH:
        res.append(heapq.heappop(minH))

    # Reverse the result array, so that all
    # elements are in decreasing order
    res.reverse()

    return res