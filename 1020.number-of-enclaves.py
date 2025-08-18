#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        rows, cols= len(grid), len(grid[0])
        res = 0
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res += 1

        return res
# @lc code=end

