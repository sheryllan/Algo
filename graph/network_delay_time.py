

from typing import List
from math import inf
class Solution:
    class Solution:
        def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
            g = [[inf for _ in range(n)] for _ in range(n)]  # 邻接矩阵
            for x, y, d in times:
                g[x - 1][y - 1] = d

            dis = [inf] * n
            ans = dis[k - 1] = 0
            done = [False] * n
            while True:
                x = -1
                for i, ok in enumerate(done):
                    if not ok and (x < 0 or dis[i] < dis[x]):
                        x = i
                if x < 0:
                    return ans  # 最后一次算出的最短路就是最大的
                if dis[x] == inf:  # 有节点无法到达
                    return -1
                ans = dis[x]  # 求出的最短路会越来越大
                done[x] = True  # 最短路长度已确定（无法变得更小）
                for y, d in enumerate(g[x]):
                    # 更新 x 的邻居的最短路
                    dis[y] = min(dis[y], dis[x] + d)

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [{} for _ in range(n)]
        for u, v, w in times:
            graph[u - 1][v - 1] = min(w, graph[u - 1].get(v - 1, inf))

        visited = {}
        def dfs(node, delay):
            if node in visited:
                visited[node] = min(delay, visited[node])
            else:
                visited[node] = delay
                for neighbour, time in graph[node].items():
                    dfs(neighbour, delay + time)

        dfs(k - 1, 0)
        return max(visited.values()) if len(visited) == n else -1


s = Solution()
print(s.networkDelayTime([
    [3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],
    [2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],
    [3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],
    [3,1,36],[2,3,59]
], 5, 5))
print(s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # expect 2
print(s.networkDelayTime([[2, 1, 3], [2, 3, 1], [3, 4, 1], [3, 1, 1]], 4, 2))  # expect 2

