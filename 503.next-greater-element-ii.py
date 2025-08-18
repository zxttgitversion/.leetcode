#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        answer = [-1] * len(nums)
        stack = []

        for i in range (2 * len(nums)):
            idx = i % len(nums)

            while stack and nums[idx] > nums[stack[-1]]:
                pre_idx = stack.pop()
                answer[pre_idx] = nums[idx]
            if i < len(nums):
                stack.append(idx)

        return answer

# @lc code=end

