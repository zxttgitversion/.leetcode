#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def dist2(a, b):
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx*dx + dy*dy
        
        # 枚举所有 6 对
        d2 = []
        for i in range(4):
            for j in range(i+1, 4):
                d2.append(dist2(timePoints[i], timePoints[j]))

# @lc code=end

