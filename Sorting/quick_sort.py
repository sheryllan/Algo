from typing import List


def partition(nums: List[int], low, high) -> int:
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = pivot, nums[i]
    return i


def quick_sort(nums: List[int]) -> None:
    def sort(low: int, high: int) -> None:
        if low < high:
            p = partition(nums, low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    sort(0, len(nums) - 1)


nums = [5, 4, 3, 2, 1]
quick_sort(nums)
print(nums)

nums = [3, 5, 0, 7, 8]
quick_sort(nums)
print(nums)

nums = [1, 1, 3, 4, 6]
quick_sort(nums)
print(nums)

nums = [3, 2, 3, 4, 0]
quick_sort(nums)
print(nums)