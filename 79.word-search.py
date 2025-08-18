#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            tmp, board[i][j] = board[i][j], '#'
            res = (dfs(i + 1, j, k + 1) or # down
                   dfs(i - 1, j, k + 1) or # up
                   dfs(i, j + 1, k + 1) or # right
                   dfs(i, j - 1, k + 1))   # left
            board[i][j] = tmp

            return res
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
            
        return False

# @lc code=end

