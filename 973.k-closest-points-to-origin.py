#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            d = x*x + y*y
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-d, x, y))
            else:
                if -max_heap[0][0] > d:
                    heapq.heapreplace(max_heap, (-d, x, y))

        return [[x, y] for _, x, y in max_heap]
# @lc code=end

