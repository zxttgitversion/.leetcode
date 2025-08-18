#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        pre_diff = nums[1] - nums[0]
        cnt = 2 if pre_diff != 0 else 1

        for i in range(2, len(nums)):
            curr_diff = nums[i] - nums[i - 1]
            if (curr_diff > 0 and pre_diff <= 0) or (curr_diff < 0 and pre_diff >= 0):
                cnt += 1
                pre_diff = curr_diff

        return cnt
        
# @lc code=end

