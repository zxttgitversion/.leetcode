#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#

# @lc code=start
from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flat = [0] * (m * n)
        
        def get(index: int) -> int:
            return grid[index //n][index % n]
        
        def set(index: int, value: int) -> None:
            grid[index //n][index % n] = value

        

        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        flat = [get(i) for i in range(m * n)]
        
        k %= (m * n)
        reverse(flat, 0, m * n - 1)
        reverse(flat, 0, k - 1)
        reverse(flat, k, m * n - 1)

        for i in range(m * n):
            set(i, flat[i])

        return grid

        


        
# @lc code=end

