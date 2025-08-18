#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            digits[i] = s % 10

            carry = s // 10

            if carry == 0:
                return digits
            
        if carry:
            return [1] + digits
            
        return digits
# @lc code=end

