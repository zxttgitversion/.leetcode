#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k:
                res.append(list(path))
                return
            
            for i in range(start, n + 1):
                if n - i + 1 < k - len(path):
                    break
                path.append(i)
                backtrack(i + 1, path)
                path.pop()


        res = []
        path = []
        backtrack(1, path)
        return res
# @lc code=end

