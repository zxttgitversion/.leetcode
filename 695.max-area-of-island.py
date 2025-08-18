#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            area = (1 + 
                   dfs(r + 1, c) +
                   dfs(r - 1, c) + 
                   dfs(r, c + 1) + 
                   dfs(r, c - 1))
            return area
            
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        return max_area

# @lc code=end

