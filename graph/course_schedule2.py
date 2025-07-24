"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

"""
算法流程：

1、在开始排序前，扫描对应的存储空间（使用邻接表），将入度为 0 的结点放入队列。

2、只要队列非空，就从队首取出入度为 0 的结点，将这个结点输出到结果集中，并且将这个结点的所有邻接结点（它指向的结点）的入度减 1，在减 1 以后，如果这个被减 1 的结点的入度为 0 ，就继续入队。

3、当队列为空的时候，检查结果集中的顶点个数是否和课程数相等即可。

（思考这里为什么要使用队列？如果不用队列，还可以怎么做，会比用队列的效果差还是更好？）

在代码具体实现的时候，除了保存入度为 0 的队列，我们还需要两个辅助的数据结构：

1、邻接表：通过结点的索引，我们能够得到这个结点的后继结点；

2、入度数组：通过结点的索引，我们能够得到指向这个结点的结点个数。

这个两个数据结构在遍历题目给出的邻边以后就可以很方便地得到。


如果优先图中，存在环，拓扑排序不能继续得到入度值为 0 的节点，退出循环，此时图中存在没有遍历到的节点，说明图中存在环。
拓扑排序实际上应用的是贪心算法，贪心算法简而言之：每一步最优，则全局最优。

具体到拓扑排序，每一次都从图中删除没有前驱的顶点，这里并不需要真正的做删除操作，我们可以设置一个入度数组，
每一轮都输出入度为 0 的结点，并移除它、修改它指向的结点的入度（−1即可），依次得到的结点序列就是拓扑排序的结点序列。
如果图中还有结点没有被移除，则说明“不能完成所有课程的学习”。

拓扑排序保证了每个活动（在这题中是“课程”）的所有前驱活动都排在该活动的前面，并且可以完成所有活动。拓扑排序的结果不唯一。
拓扑排序还可以用于检测一个有向图是否有环。相关的概念还有 AOV 网，这里就不展开了。


"""


from collections import deque
from typing import List


# BFS - topological sorting
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            in_degree[course] += 1
            graph[pre].append(course)

        q = deque([i for i, x in enumerate(in_degree) if x == 0])
        ans = []
        while q:
            pre = q.popleft()
            ans.append(pre)
            for course in graph[pre]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    q.append(course)

        return ans if len(ans) == numCourses else []


# DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        colours = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[course].append(pre)

        ans = []

        def dfs(i):
            if colours[i] == 2:
                return True

            if colours[i] == 1:
                return False

            colours[i] = 1
            for pre in graph[i]:
                if not dfs(pre):
                    return False

            colours[i] = 2
            ans.append(i)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return ans


s = Solution()
assert s.findOrder(2, [[1,0]]) == [0,1]
assert s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,1,2,3]
assert s.findOrder(1, []) == [0]
assert s.findOrder(3, [[0,1],[1,2],[2,0]]) == []


