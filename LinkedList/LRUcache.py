"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        assert capacity > 0, 'capacity must be an integer greater than 0'
        self.capacity = capacity
        self._cache = {}
        self._head = None
        self._tail = None


    def update_linkedlist(self, node: Node):
        if self._head is None and self._tail is None:
            self._head = node
            self._tail = node

        if node is self._tail:
            return

        if node is self._head:
            self._head = self._head.next

        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        tail = self._tail
        tail.next = node
        node.prev = tail
        node.next = None
        self._tail = node

    def remove_head(self):
        if self._head is not None:
            self._cache.pop(self._head.key)
            self._head = self._head.next

    def get(self, key: int) -> int:
        if key in self._cache:
            self.update_linkedlist(self._cache[key])
            return self._cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            node.value = value
        else:
            node = Node(key, value)

        self._cache[key] = node
        self.update_linkedlist(node)

        if len(self._cache) > self.capacity:
            self.remove_head()



# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)

cache.put(2, 1)
cache.put(2, 2)
assert cache.get(2) == 2

cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(2) == -1
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
