#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candi1, candi2 = None, None
        cnt1, cnt2 = 0, 0

        for x in nums:
            if candi1 == x:
                cnt1 += 1
            elif candi2 == x:
                cnt2 += 1
            elif cnt1 == 0:
                candi1 = x
                cnt1 = 1
            elif cnt2 == 0:
                candi2 = x
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        res = []
        for candi in (candi1, candi2):
            if candi is not None and nums.count(candi) > len(nums) // 3:
                res.append(candi)
        return res
# @lc code=end

