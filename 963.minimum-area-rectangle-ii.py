#
# @lc app=leetcode id=963 lang=python3
#
# [963] Minimum Area Rectangle II
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # 哈希表：键 (sumX, sumY, dist2) → 列表 of (dx, dy)
        mp = defaultdict(list)
        n = len(points)
        ans = float('inf')

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                sumX, sumY = x1 + x2, y1 + y2
                dx, dy = x2 - x1, y2 - y1
                dist2 = dx*dx + dy*dy
                key = (sumX, sumY, dist2)
                # 若已有相同对角线组，计算与每个已有向量的矩形面积
                for dx0, dy0 in mp[key]:
                    # 叉积的一半即面积
                    area = abs(dx0*dy - dy0*dx) / 2.0
                    if area < ans:
                        ans = area
                # 追加当前向量
                mp[key].append((dx, dy))

# @lc code=end

