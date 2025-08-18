#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n =len(matrix), len(matrix[0])
        row0 = col0 = False

        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True
            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(m - 1, -1, -1): # [m - 1, 0]
            for j in range(n - 1, 0, -1): # [n - 1, 1]
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if col0:
            for i in range(m):
                matrix[i][0] = 0

        if row0:
            for j in range(n):
                matrix[0][j] = 0

        

# @lc code=end

