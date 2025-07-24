"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

 

Example 1:

      0 -> 1
      0 -> 2 -> 5
     4 -> 2
3 -> 4



Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
Example 2:

0 -> 1 -> 4
2 -> 1 
3 -> 1 

Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.
 

Constraints:

2 <= n <= 10^5
1 <= edges.length <= min(10^5, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi < n
All pairs (fromi, toi) are distinct.
"""

from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set()
        
        graph = [[] for _ in range(n)]
        for fr, to in edges:
            graph[fr].append(to)

        def dfs(i):
            if not graph[i]:
                if i in ans:
                    ans.remove(i)
                return
            
            for x in graph[i]:
                dfs(x)

            ans.add(i)
            graph[i] = []

        for i in range(n):
            dfs(i)

        return list(ans)


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n

        for fr, to in edges:
            in_degree[to] += 1

        return [i for i in range(n) if not in_degree[i]]

        

s = Solution()
print(s.findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]))
print(s.findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]))

assert s.findSmallestSetOfVertices(5, [[0,1],[0,4],[4,2],[3,0]]) == [3]
