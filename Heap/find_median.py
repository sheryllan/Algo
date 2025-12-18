"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:

-10e5 <= num <= 10e5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.

"""

"""
Approach

Use two heaps:
lowerHalf: max-heap (stores smaller half)
upperHalf: min-heap (stores larger half)

When inserting a new number:
If it's smaller than or equal to the top of lowerHalf, push it into lowerHalf.
Otherwise, push it into upperHalf.

Rebalance the heaps so that:
|size(lowerHalf) - size(upperHalf)| <= 1

To find the median:
If both heaps have the same size → median = average of tops.
Otherwise → median = top of the larger heap.
"""


import heapq


class MedianFinder:

    def __init__(self):
        self._upper_half = []  # min heap
        self._lower_half = []  # max heap

    def addNum(self, num: int) -> None:
        if (not self._lower_half) and (not self._upper_half):
            self._lower_half.append(-num)
        elif self._lower_half and num > -self._lower_half[0]:
            heapq.heappush(self._upper_half, num)
        else:
            heapq.heappush(self._lower_half, -num)

        if len(self._lower_half) > len(self._upper_half) + 1:
            largest = -heapq.heappop(self._lower_half)
            heapq.heappush(self._upper_half, largest)
        elif len(self._upper_half) > len(self._lower_half) + 1:
            smallest = heapq.heappop(self._upper_half)
            heapq.heappush(self._lower_half, -smallest)

    def findMedian(self) -> float:
        n_upper, n_lower = len(self._upper_half), len(self._lower_half)

        if n_upper != n_lower:
            return self._upper_half[0] if n_upper > n_lower else -self._lower_half[0]
        return (self._upper_half[0] - self._lower_half[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()