from collections import defaultdict
from queue import Queue
import math


def get_sum_floor(n, edges: list):
    graph = defaultdict(set)
    for edge in edges:
        a, b = edge.split()
        graph[int(a)].add(int(b))
        graph[int(b)].add(int(a))

    node_sets = bfs_find_sets(graph, n)

    return sum(math.floor(math.log(len(s), math.e)) for s in node_sets)


def bfs_find_sets(graph: dict, n):
    visited = set()
    node_sets = []

    for i in range(n):
        node = i + 1
        if node in visited:
            continue
        q = Queue()
        q.put(node)
        set_v = set()
        while not q.empty():
            v = q.get()
            if v in visited:
                continue
            visited.add(v)
            set_v.add(v)
            for connected_v in graph[v]:
                if connected_v in visited:
                    continue
                q.put(connected_v)

        node_sets.append(set_v)

    return node_sets


print(get_sum_floor(13, ['1 3', '3 4', '3 5', '4 6', '2 4', '7 8', '8 9', '10 11']))