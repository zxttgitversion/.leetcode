#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        curr = 0

        for num in nums:
            if num == 0:
                curr += 1
                ans += curr
            else:
                curr = 0
        return ans

# @lc code=end

