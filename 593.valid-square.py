#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#

# @lc code=start
from typing import List
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 计算两点间距离的平方
        def dist2(a, b):
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx*dx + dy*dy
        
        # 枚举所有 6 对
        pts = [p1, p2, p3, p4]
        d2 = []
        for i in range(4):
            for j in range(i+1, 4):
                d2.append(dist2(pts[i], pts[j]))
        d2.sort()
        # 边长平方必须大于 0，且前 4 个相等，后 2 个相等，并且对角线 = 2 * 边长
        return (
            d2[0] > 0 and
            d2[0] == d2[1] == d2[2] == d2[3] and
            d2[4] == d2[5] and
            d2[4] == 2 * d2[0]
        )
# @lc code=end

