#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
from typing import List
import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        cum = 0
        for weight in w:
            cum += weight
            self.prefix.append(cum)
        self.total = cum

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)

        left, right = 0, len(self.prefix) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.prefix[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

