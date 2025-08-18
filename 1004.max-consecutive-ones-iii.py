#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        zero_cnt = 0
        left, right = 0, 0

        while right < len(nums):
            if nums[right] == 0:
                zero_cnt += 1
            right += 1

            while zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1

            max_len = max(max_len, right - left)
        return max_len
# @lc code=end

