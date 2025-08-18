#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, p = 0, len(nums) - 1, len(nums) - 1
        res = [0] * len(nums)

        while left <= right:
            l_square = nums[left] ** 2
            r_square = nums[right] ** 2

            if l_square > r_square:
                res[p] = l_square
                left += 1
            else:
                res[p] = r_square
                right -= 1
            p -= 1

        return res
# @lc code=end

