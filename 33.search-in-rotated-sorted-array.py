#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 左边是有序的
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:  # target 在左边
                    right = mid - 1
                else:  # target 在右边
                    left = mid + 1

            # 右边是有序的
            else:
                if nums[mid] < target <= nums[right]:  # target 在右边
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# @lc code=end

