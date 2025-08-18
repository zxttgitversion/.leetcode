#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 #[left, right]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1

        return left

# @lc code=end

