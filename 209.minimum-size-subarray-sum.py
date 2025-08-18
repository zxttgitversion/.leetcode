#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start#
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        total = 0
        min_len = float('inf')

        while right < len(nums):
            total += nums[right]
            right += 1

            while total >= target:
                min_len = min(min_len, right - left)
                total -= nums[left]
                left += 1


        if min_len == float('inf'):
            return 0
        else:
            return min_len
# @lc code=end

