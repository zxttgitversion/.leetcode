#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
# matrix[m][n]
from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transpose = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                transpose[j][i] = matrix[i][j]
        
        return transpose

        

# @lc code=end

