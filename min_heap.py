import heapq

# Create an empty heap
min_heap = []

# Insert elements
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)

print(min_heap)  # Output: [1, 2, 5, 3] (Heap structure, but not necessarily sorted)

# Get the minimum element (without removing)
print(min_heap[0])  # Output: 1

# Extract the minimum element
print(heapq.heappop(min_heap))  # Output: 1
print(heapq.heappop(min_heap))  # Output: 2

# Convert a list into a heap in-place
arr = [4, 7, 1, 9, 2]
heapq.heapify(arr)  # Turns list into a min-heap
print(arr)  # Example output: [1, 2, 4, 9, 7]

# Replace the minimum element (faster than pop + push)
heapq.heapreplace(arr, 3)
print(arr)  # Example output: [2, 3, 4, 9, 7]


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None

# Example usage:
heap = MinHeap()
heap.insert(3)
heap.insert(1)
heap.insert(5)
heap.insert(2)

print(heap.get_min())  # Output: 1
print(heap.extract_min())  # Output: 1
print(heap.extract_min())  # Output: 2