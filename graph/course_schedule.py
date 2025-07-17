"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, course_pre in prerequisites:
            graph[course].append(course_pre)

        visited = set()

        def dfs(i, path):
            if i in path:
                return False

            if i in visited:
                return True

            path.add(i)
            for i_prerequisite in graph[i]:
                if not dfs(i_prerequisite, path):
                    return False

            path.remove(i)
            visited.add(i)
            return True

        for course in range(numCourses):
            can_do = dfs(course, set())
            if not can_do:
                return False

        return True


s = Solution()
assert s.canFinish(3, [[0,1],[0,2],[1,2]])
assert s.canFinish(2, [[1,0]])
assert not s.canFinish(2, [[1,0],[0,1]])
assert s.canFinish(5, [[1,0], [0, 3], [2,0], [1, 3], [4, 2]])
assert s.canFinish(5, [[1,0], [0, 3], [2,0], [4, 3], [4, 2], [2, 1]])
assert not s.canFinish(5, [[1,0], [0, 3], [2,0], [3, 2], [4, 2], [2, 1]])