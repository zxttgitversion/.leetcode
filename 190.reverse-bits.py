#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            bit = n & 1
            res = (res << 1) | bit
            n >>= 1

        return res & 0xFFFFFFFF
# @lc code=end

