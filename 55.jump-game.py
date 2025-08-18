
#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        left, right = 0, 1
        farthest = 0

        while left < right:
            for i in range(left, right):
                farthest = max(farthest, i + nums[i])
                if farthest >= n - 1:
                    return True
                
            left = right
            right = farthest + 1
        return False

# @lc code=end

