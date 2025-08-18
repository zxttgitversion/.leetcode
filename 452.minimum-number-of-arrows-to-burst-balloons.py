#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 1
        arrow_pos = points[0][1]

        for point in points[1:]:
            if point[0] > arrow_pos:
                arrows += 1
                arrow_pos = point[1]
        return arrows

# @lc code=end

