#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range((numCourses))]
        for to, pre in prerequisites:
            graph[pre].append(to)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1

            for nei in graph[course]:
                if not dfs(nei):
                    return False
                
            visited[course] = 2
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
# @lc code=end

