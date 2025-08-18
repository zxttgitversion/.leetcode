#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # 初始化状态表
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty.append((r, c)) # `empty`存储所有的空格坐标
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        #  backtrack(index):我现在正在尝试填第 `index` 个空格
        def backtrack(index): 
            if index == len(empty):  # index: 还有多少个空格要填
                return True

            r, c = empty[index]
            b = (r // 3) * 3 + (c // 3)
            for d in '123456789':
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)
                    if backtrack(index + 1):
                        return True
                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)
            return False

        backtrack(0)
# @lc code=end

