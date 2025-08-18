#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1  # define [lefft, right]

        while left <= right:
            middle = left + (right - left) // 2  # prevent overflow
             
            if nums[middle] > target:
                 right = middle - 1  # narrow it to [left, middle - 1]
            elif nums[middle] < target:
                left = middle + 1  # narrow it to [middle + 1, right]
            else: 
                return middle
        return -1  # did not find target



# @lc code=end

