#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] >= target:
                    r = mid - 1

            return l


        def find_right():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            return r

        left = find_left()
        right = find_right()

        if left <= right and 0 <= left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]



# @lc code=end

