#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
"""
对于每个 heights[i]，我们想找：

左边第一个小于它的柱子的下标 left

右边第一个小于它的柱子的下标 right

max_area = (右边界 - 左边界 - 1) * heights[i]

"""
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1

                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
# @lc code=end

