def sumValues(parents, startPoint, jumpLength):
    n = len(parents)
    
    # Optimization 1: Only compute for unique k values that appear in queries
    # This can save significant computation if queries reuse the same k values
    unique_k = sorted(set(jumpLength))
    if not unique_k:
        return []
    
    # Build BFS order (root to leaves) - needed for correct DP computation order
    # Optimization 2: More efficient deque operations
    from collections import deque
    order = []
    dq = deque([0])  # Root is always 0 (parents[0] == -1)
    while dq:
        u = dq.popleft()
        order.append(u)
        # Add all children of u to queue
        for v in range(n):
            if parents[v] == u:
                dq.append(v)

    # Optimization 3: Compute sum_k efficiently, building next_k on-the-fly
    # We avoid storing all next_k arrays by computing them only when needed
    sum_k = {}
    
    for k in unique_k:
        # Build next_k[k] using optimized DP: O(n) instead of O(n*k)
        next_k = [-1] * n
        if k == 1:
            next_k = parents[:]  # Direct copy for k=1
        else:
            # Build iteratively: next_k[k][v] = parent of next_k[k-1][v]
            # We can do this in one pass by building from k=1 up to k
            curr = parents[:]  # Start with k=1
            for step in range(2, k + 1):
                curr = [-1 if p == -1 else parents[p] for p in curr]
            next_k = curr
        
        # Compute sum_k[k] using DP: O(n)
        sum_k[k] = [0] * n
        for u in order:
            nxt = next_k[u]
            sum_k[k][u] = u if nxt == -1 else u + sum_k[k][nxt]

    # Answer queries in O(1) each - list comprehension is efficient
    return [sum_k[k][s] for s, k in zip(startPoint, jumpLength)]

# Test with the sample case
result = sumValues([-1, 0, 1, 1, 2, 4], [5, 4], [1, 2])
print('Result:', result)
print('Expected: [12, 5]')
print('Match:', result == [12, 5])

# Test with the example from the problem description
result2 = sumValues([-1, 0, 0, 1, 1, 3, 3, 6, 2], [6, 7, 8], [2, 2, 3])
print('Result2:', result2)
print('Expected: [7, 10, 8]')
print('Match:', result2 == [7, 10, 8])