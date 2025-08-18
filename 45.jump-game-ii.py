#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        left = 0
        right = 1

        while right < n:
            jumps += 1
            farthest = 0
            for i in range(left, right):
                farthest = max(farthest, i + nums[i])
            left = right
            right = farthest + 1

        return jumps


        
# @lc code=end

