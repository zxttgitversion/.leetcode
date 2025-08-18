#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # without tecnique: 
        # base = sum(customers[i] for i in range(customers) if grumpy[i] == 0)
        
        base = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]

        left, right = 0, 0
        curr_num = 0 
        max_extra_num = 0

        while right < len(customers):
            if grumpy[right] == 1:
                curr_num += customers[right]
            right += 1

            if right - left > minutes:
                if grumpy[left] == 1:
                    curr_num -= customers[left]
                left += 1

            if curr_num > max_extra_num:
                max_extra_num = curr_num 

        max_satisfied = base + max_extra_num 

        return max_satisfied
                



# @lc code=end

