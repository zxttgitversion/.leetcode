#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(row):
            if row == n:
                res.append([''.join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                backtrack(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        res = []
        board = [['.'] * n for _ in range(n)]

        cols = set()
        diagonals1 = set()
        diagonals2 = set()

        backtrack(0)
        return res
# @lc code=end

