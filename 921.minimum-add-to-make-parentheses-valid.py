#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_need = 0
        right_need = 0

        for ch in s:
            if ch == '(':
                right_need += 1
            else:
                if right_need > 0:
                    right_need -= 1
                else:
                    left_need += 1

        return left_need + right_need
# @lc code=end

