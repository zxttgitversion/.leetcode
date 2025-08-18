#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_idx = {0: -1} # {remainder: appear index}
        prefix = 0

        for idx, num in enumerate(nums):
            prefix += num
            m = prefix if k == 0 else prefix % k

            if m not in mod_idx:
                mod_idx[m] = idx
            else:
                if idx - mod_idx[m] >= 2:
                    return True
                
        return False

# @lc code=end

