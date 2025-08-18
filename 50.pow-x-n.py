#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp = n
        if exp < 0:
            x = 1 / x
            exp = -exp

        res = 1.0
        base = x
        while exp > 0:
            if exp & 1:  # exp 是奇数吗
                res *= base
            base *= base
            exp >>= 1
        return res


# @lc code=end

