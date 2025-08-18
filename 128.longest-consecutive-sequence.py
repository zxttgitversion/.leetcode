#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set(nums)
        longest = 0
        for num in seen:
            if num - 1 not in seen:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in seen:
                    curr_num += 1
                    curr_streak += 1

                longest = max(longest, curr_streak)
        return longest
# @lc code=end

