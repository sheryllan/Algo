

# def sumValues(parents, startPoint, jumpLength):
#     results = []
#     for i in range(len(startPoint)):
#         jump = jumpLength[i]
#         parent = startPoint[i]
#         path_sum = 0
#
#         while parent != -1:
#             if jump % jumpLength[i] == 0:
#                 path_sum += parent
#                 jump = jumpLength[i]
#
#             parent = parents[parent]
#             jump -= 1
#
#         results.append(path_sum)
#
#     return results


from collections import deque
def sumValues(parents, startPoint, jumpLength):
    n = len(parents)
    graph = [[] for _ in range(n)]
    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            graph[parent].append(i)

    paths = [[]] * n
    q = deque([(root, [])])
    while q:
        node, path = q.popleft()
        new_path = path + [node]
        paths[node] = new_path
        for child in graph[node]:
            q.append((child, new_path))

    results = []
    for start, jump in zip(startPoint, jumpLength):
        results.append(sum(paths[start][::-jump]))

    return results


# Because 1 <= jumpLength[i] <= 10, we can save the result of each jump_length and still remain O(n) complexity
def sumValues(parents, startPoint, jumpLength):
    n = len(parents)
    graph = [[] for _ in range(n)]
    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            graph[parent].append(i)

    max_jump = max(jumpLength)
    next_jumps = [[-1] * n for _ in range(max_jump + 1)]
    for k in range(1, max_jump + 1):
        for i in range(n):
            if k == 1:
                next_jumps[k][i] = parents[i]
            else:
                nxt = next_jumps[k - 1][i]
                next_jumps[k][i] = parents[nxt] if nxt != -1 else -1

    # traversing in level-by-level(BFS) order to calculate the path sum from its parent for each point
    path_sums = [[0] * n for _ in range(max_jump + 1)]
    q = deque([root])
    while q:
        i = q.popleft()
        q.extend(graph[i])
        for k in range(1, max_jump + 1):
            parent = next_jumps[k][i]
            if parent == -1:
                path_sums[k][i] = i
            else:
                path_sums[k][i] = path_sums[k][parent] + i  # the path sum of node i is only dependent on the path sum of it parent

    return [path_sums[k][i] for i, k in zip(startPoint, jumpLength)]


print(sumValues([-1, 0,0,1,1,3,3,6,2], [6, 7, 8], [2, 2, 3]))
print(sumValues([-1, 0, 1, 1, 2, 4], [5, 4], [1, 2]))

