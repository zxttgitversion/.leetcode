#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            total = x + y + carry
            res.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1

        if carry:
            res.append('1')
        return ''.join(reversed(res))
# @lc code=end

