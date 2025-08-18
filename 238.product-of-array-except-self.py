#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
# @lc code=end

